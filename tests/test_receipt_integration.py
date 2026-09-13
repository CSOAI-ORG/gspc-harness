"""Receipt interoperability proof — `inspect_receipts` (PyPI: `inspect-signed-receipt`) ↔ `gspc-harness`.

This test is OPT-IN. It runs when:

    inspect_receipts is importable (i.e. ``pip install inspect-signed-receipt``)
    AND pytest is invoked.

Without ``inspect_receipts`` installed, the module is auto-skipped.

The chain we prove:

    Inspect task → EvalLog → task receipt → run receipt → local content-id

What this test does NOT do:

    - It does NOT load or generate any signing key.
    - It does NOT call ``verify()`` against a trust anchor (the package requires
      ``--did-web`` for that and the test environment has no outbound network).
    - It does NOT claim the receipts are signed, attributable, or anchored
      to any blockchain or transparency log.

Known interaction with the receipt package (documented, worked around here):

    Inspect 0.3.263 reports ``accuracy_measured`` as ``NaN`` when every item
    is UNMEASURED (the harness's intentional behaviour — see
    ``tasks/_gspc_scoring.py``). ``inspect_receipts`` uses RFC 8785 JCS
    canonicalisation, which rejects ``NaN`` in JSON. The hook's defensive
    ``try/except: pass`` swallows the resulting ``ValueError`` silently and
    no receipt is written. This test installs a NaN-coercion shim for the
    duration of the eval so the chain can be exercised end-to-end.

    The bug is recorded in ``RECEIPTS_INTEGRATION.md`` for the receipt
    package's owner to address upstream; it is NOT fixed in this lane.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


try:
    import inspect_receipts  # noqa: F401
    HAVE_RECEIPTS = True
except ImportError:
    HAVE_RECEIPTS = False


# Inline bootstrap script that:
#   1. Coerces NaN/Inf to None in the receipt digest path (workaround)
#   2. Invokes the inspect_ai CLI on gspc_governance with mockllm/model
# The harness makes no external calls; all data is vendored.
# REPO_PATH is filled in by _run() via .replace() — we cannot use .format() here
# because the bootstrap contains Python dict literals whose braces would clash.
_BOOTSTRAP_PY = """
import sys, os, math, json

# NaN scrubber: replace non-finite floats with None so strict JCS JSON
# can encode the EvalLog. The receipt package's own canonical_bytes()
# rejects NaN (RFC 8785 has no NaN/Infinity representation).
def _scrub(o):
    if isinstance(o, float):
        if math.isnan(o) or math.isinf(o):
            return None
        return o
    if isinstance(o, dict):
        return {k: _scrub(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_scrub(v) for v in o]
    return o

# Patch inspect_receipts._hooks._digest_log so the NaN-bearing scores
# produced by the harness don't abort the JCS encoder.
import inspect_receipts._hooks as _rh

_orig_digest = _rh._digest_log

def _patched_digest_log(log):
    obj = _rh.eval_log_digest(log)
    obj = _scrub(obj)
    return {
        "eval_log": obj,
        "eval_log_sha256": _rh.sha256_hex(_rh.canonical_bytes(obj)),
        "log_location": getattr(log, "location", None),
    }

_rh._digest_log = _patched_digest_log

# Now run inspect_ai as the framework intends.
from inspect_ai._eval.eval import eval_async
sys.path.insert(0, "REPO_PATH_PLACEHOLDER")
import importlib
importlib.import_module("tasks.gspc_governance")
import tasks.gspc_governance as g
import asyncio

asyncio.run(
    eval_async(
        g.gspc_governance(),
        model="mockllm/model",
        limit=2,
        log_format="json",
    )
)
"""


@unittest.skipUnless(HAVE_RECEIPTS, "inspect_receipts not installed (optional dep)")
class ReceiptChainProof(unittest.TestCase):
    """Prove: a mockllm run on gspc_governance produces well-formed UNSIGNED receipts."""

    def setUp(self) -> None:
        self.repo = Path(__file__).resolve().parents[1]
        self.tmp = Path(tempfile.mkdtemp(prefix="gspc_receipt_"))
        self.logs = self.tmp / "logs"
        self.receipts = self.tmp / "receipts"
        self.logs.mkdir()
        self.receipts.mkdir()

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _run(self) -> tuple[int, str]:
        env = os.environ.copy()
        env.pop("INSPECT_RECEIPTS_KEY", None)  # never signed from this lane
        env.pop("PYTHONPATH", None)
        env["INSPECT_RECEIPTS"] = "1"
        env["INSPECT_RECEIPTS_DIR"] = str(self.receipts)
        env["INSPECT_LOG_DIR"] = str(self.logs)
        # Important: keep HOME set so tempfile and inspect_ai behave normally.
        bootstrap = _BOOTSTRAP_PY.replace("REPO_PATH_PLACEHOLDER", str(self.repo))
        proc = subprocess.run(
            [sys.executable, "-c", bootstrap],
            cwd=self.repo,
            env=env,
            capture_output=True,
            text=True,
            timeout=180,
        )
        return proc.returncode, proc.stdout + "\n" + proc.stderr

    def test_receipts_are_honestly_unsigned(self) -> None:
        """The hook must emit receipts; both must be UNSIGNED; no fabricated signatures."""
        code, out = self._run()
        self.assertEqual(code, 0, msg=f"inspect eval failed:\n{out}")

        # Expect exactly one task receipt and one run receipt.
        task_files = sorted(self.receipts.glob("task-*.receipt.json"))
        run_files = sorted(self.receipts.glob("run-*.receipt.json"))
        self.assertEqual(len(task_files), 1, f"expected 1 task receipt, got {task_files}")
        self.assertEqual(len(run_files), 1, f"expected 1 run receipt, got {run_files}")

        task = json.loads(task_files[0].read_text())
        run = json.loads(run_files[0].read_text())

        # Schema sanity. The package version 0.2.x emits schema "0.2";
        # source tree (post-R1 fix) emits "0.3". Accept either.
        for rcpt, name in [(task, "task"), (run, "run")]:
            self.assertRegex(
                rcpt["schema"],
                r"^csoai\.inspect-receipt/0\.[23]$",
                f"{name} receipt schema unexpected: {rcpt['schema']!r}",
            )
        self.assertEqual(task["kind"], "task")
        self.assertEqual(run["kind"], "run")

        # No fabricated signature.
        self.assertEqual(task["signature"]["status"], "UNSIGNED")
        self.assertEqual(run["signature"]["status"], "UNSIGNED")
        self.assertFalse(task["signature"].get("sig"))
        self.assertFalse(run["signature"].get("sig"))

        # Both carry a 64-hex-char content_id.
        for rcpt, name in [(task, "task"), (run, "run")]:
            cid = rcpt.get("content_id")
            self.assertTrue(cid, f"{name} receipt missing content_id")
            self.assertEqual(len(cid), 64, f"{name} content_id is not sha256 length")
            self.assertRegex(cid, r"^[0-9a-f]{64}$", f"{name} content_id is not hex")

        # Chain: task.content_id == run.prev (hash chain).
        self.assertEqual(run["prev"], task["content_id"])

        # run_id matches between the two receipts.
        self.assertEqual(task["run_id"], run["run_id"])

    def test_eval_log_sha256_is_present_and_hex(self) -> None:
        """The task receipt embeds the EvalLog sha256 — the integrity anchor for the log."""
        code, _ = self._run()
        self.assertEqual(code, 0)
        task_files = list(self.receipts.glob("task-*.receipt.json"))
        self.assertEqual(len(task_files), 1)
        task = json.loads(task_files[0].read_text())
        sha = task.get("eval_log_sha256")
        self.assertTrue(sha, "task receipt missing eval_log_sha256")
        self.assertEqual(len(sha), 64)
        self.assertRegex(sha, r"^[0-9a-f]{64}$")


if __name__ == "__main__":
    unittest.main()
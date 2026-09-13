# Receipt integration — proof chain

**Repository:** `CSOAI-ORG/gspc-harness`
**Lane:** Hermes UK Inspect adoption
**As-of date:** 2026-09-13
**Branch:** `hermes/inspect-register-readiness`

This document is the reproducible test report for the receipt-interoperability
proof in this lane. It records exact versions, commands, output paths,
content IDs, and limitations.

## What is proven

`gspc-harness` integrates with the independently published receipt package
(`inspect-signed-receipt` on PyPI / `inspect-receipts` source repo) as an
**optional** companion. With the receipt package installed and
`INSPECT_RECEIPTS=1` set, an `inspect eval` run on a CSOAI task emits:

1. one **task receipt** (`task-<eval_id>.receipt.json`) on task end, and
2. one **run receipt** (`run-<run_id>.receipt.json`) on run end.

Both receipts are content-addressed (`sha256` of RFC 8785 JCS canonical body),
both have a 64-hex-char `content_id`, and the run receipt's `prev` field
equals the task receipt's `content_id` — they are hash-chained.

A signing key was **not** configured for this report; both receipts are
honestly `UNSIGNED` with the reason text recorded in the receipt itself:

> *"no signing key configured (set INSPECT_RECEIPTS_KEY to a 32-byte Ed25519
> seed); this receipt is content-addressed but unattributed"*

This is the doctrine. No signature value appears in the receipt. A signature
is **never fabricated** when the key is absent.

## Exact versions in the proof run

| Component | Version | Source |
|---|---|---|
| `inspect-ai` | 0.3.263 | PyPI (declared as dep in `pyproject.toml`) |
| `inspect-signed-receipt` | 0.3.0 | source tree at `/Users/iokfarm/workspace_for_ai/inspect-lane/inspect-receipts`, installed `pip install -e .` |
| `csoai.inspect-receipt` schema | `/0.3` | emitted by the source tree (post-R1 fix) |
| `csoai.inspect-receipt` schema | `/0.2` | emitted by the PyPI wheel `0.2.0` |
| `cryptography` | 50.0.1 | transitive |
| `jcs` | 0.2.1 | transitive |
| Python | 3.11.15 | CPython |
| `gspc-harness` | head of `hermes/inspect-register-readiness` at `b0acfcb` + lane changes | this branch |

The PyPI release published at lane time is `0.2.0`. The source tree is `0.3.0`
(commit `5c3d8f3`, "docs: name canonical Inspect receipt package precisely").
The integration test accepts either schema version.

## Reproducible run — exact commands

The lane's `tests/test_receipt_integration.py` is the canonical reproducer
(installable as `pip install -e ".[receipts]"` and run with `pytest -v`).
The end-to-end proof recorded here used a direct subprocess invocation
matching what the test does:

```bash
TMP=$(mktemp -d -t gspc_evidence)
INSPECT_RECEIPTS=1 \
INSPECT_RECEIPTS_DIR="$TMP/receipts" \
INSPECT_LOG_DIR="$TMP/logs" \
  python3 - <<'PY'
import sys, math
sys.path.insert(0, "/Users/iokfarm/workspace_for_ai/inspect-lane/gspc-harness")
# Workaround for an upstream bug in inspect_receipts (see §"Known limitation"):
# the harness reports NaN for accuracy_measured when every item is
# UNMEASURED (its intended behaviour); inspect_receipts' RFC 8785 JCS encoder
# rejects NaN. We scrub NaN/Inf before JCS for the duration of the run.
import inspect_receipts._hooks as _rh
def _scrub(o):
    if isinstance(o, float):
        if math.isnan(o) or math.isinf(o): return None
        return o
    if isinstance(o, dict): return {k:_scrub(v) for k,v in o.items()}
    if isinstance(o,(list,tuple)): return [_scrub(v) for v in o]
    return o
_orig = _rh._digest_log
def _patched(log):
    obj = _rh.eval_log_digest(log); obj = _scrub(obj)
    return {"eval_log": obj,
            "eval_log_sha256": _rh.sha256_hex(_rh.canonical_bytes(obj)),
            "log_location": getattr(log, "location", None)}
_rh._digest_log = _patched
from inspect_ai._eval.eval import eval_async
import tasks.gspc_governance as g, asyncio
asyncio.run(eval_async(g.gspc_governance(), model="mockllm/model", limit=4, log_format="json"))
PY
```

## Output paths and content IDs (concrete evidence)

```
$TMP/receipts/
├── run-J22HQNXPMnBMm9fN4peHHt.receipt.json     (2855 bytes)
└── task-J3oW6SsDzrp4PCfbpgTobj.receipt.json    (2683 bytes)

$TMP/logs/
└── 2026-09-13T05-30-37-00-00_gspc-governance_*.json
```

### Task receipt — verbatim fields

```json
{
  "schema":             "csoai.inspect-receipt/0.3",
  "kind":               "task",
  "issued_at":          "2026-09-13T05:30:38Z",
  "eval_id":            "J3oW6SsDzrp4PCfbpgTobj",
  "run_id":             "J22HQNXPMnBMm9fN4peHHt",
  "content_id":         "f578064c520a3a0ddf2b69a2644bbd4c3e1663b449b50c27e3738a8e514a8436",
  "prev":               null,
  "eval_log_sha256":    "7f6de22fa637d71cde1be70f59c79b8632b2530f17f2c09a2f42874d7ad3cc03",
  "signature": {
    "status": "UNSIGNED",
    "alg":    null,
    "kid":    null,
    "reason": "no signing key configured (set INSPECT_RECEIPTS_KEY to a 32-byte Ed25519 seed); this receipt is content-addressed but unattributed"
  }
}
```

### Run receipt — verbatim fields

```json
{
  "schema":             "csoai.inspect-receipt/0.3",
  "kind":               "run",
  "issued_at":          "2026-09-13T05:30:38Z",
  "run_id":             "J22HQNXPMnBMm9fN4peHHt",
  "content_id":         "0f50ba74ad282854283a9607cd3a7ad35f6ce5b4f5d28a195199908468fdfb83",
  "prev":               "f578064c520a3a0ddf2b69a2644bbd4c3e1663b449b50c27e3738a8e514a8436",
  "exception":          null,
  "signature": {
    "status": "UNSIGNED",
    "alg":    null,
    "kid":    null,
    "reason": "no signing key configured (set INSPECT_RECEIPTS_KEY to a 32-byte Ed25519 seed); this receipt is content-addressed but unattributed"
  }
}
```

### Chain proof

```
task.content_id = f578064c520a3a0ddf2b69a2644bbd4c3e1663b449b50c27e3738a8e514a8436
run.prev        = f578064c520a3a0ddf2b69a2644bbd4c3e1663b449b50c27e3738a8e514a8436
match: True
```

The run receipt chains back to the task receipt's content_id by SHA-256.

## Test results (CI gate)

`tests/test_receipt_integration.py` runs the same proof as a `pytest` suite.
It is the canonical reproducer and is invoked in `.github/workflows/ci.yml`.

```
tests/test_receipt_integration.py::ReceiptChainProof::test_eval_log_sha256_is_present_and_hex PASSED
tests/test_receipt_integration.py::ReceiptChainProof::test_receipts_are_honestly_unsigned PASSED
============================== 2 passed in 3.92s ===============================
```

The test installs the package, runs a bounded `mockllm/model --limit 2` eval
on `gspc_governance`, and asserts:

- exactly one `task-*.receipt.json` and one `run-*.receipt.json` are written,
- both receipts have `schema: csoai.inspect-receipt/0.[23]` (accepts either),
- both have `signature.status == "UNSIGNED"` and no `signature.sig` value,
- both have a 64-hex-char `content_id`,
- `run["prev"] == task["content_id"]` (hash chain),
- `task["run_id"] == run["run_id"]` (eval/run pairing),
- `task["eval_log_sha256"]` is a 64-hex-char SHA-256 (integrity anchor).

## Known limitation (worked around in this lane, not fixed upstream)

`inspect_receipts@0.3.0` rejects NaN in the EvalLog it canonicalises with
RFC 8785 JCS. The harness (`gspc-harness`) intentionally reports
`accuracy_measured = NaN` when every item is UNMEASURED — that is rule 2 of
its honesty register (see `tasks/_gspc_scoring.py` and `README.md §"The
honesty register"`). When the EvalLog's `results.scores[].metrics.accuracy_measured.value`
is NaN, `_digest_log → canonical_bytes` raises `ValueError: Invalid JSON
number: nan`, the hook's defensive `try/except: pass` swallows it, and **no
receipt is written**.

The lane does NOT fix this in `inspect-receipts`. The receipt package is
maintained by the receipts lane; the fix belongs there. The lane works
around it for the proof by replacing `inspect_receipts._hooks._digest_log`
with a NaN-scrubbing variant. The workaround is documented inline in
`tests/test_receipt_integration.py` and reproduced at the top of this file.

**Bug report suggestion** for the receipt lane: change
`canonical_bytes` / `jcs_bytes` (or the `_digest_log` caller) to coerce
non-finite floats to `None` (RFC 8785 §3.2.2.4: JSON `null` IS in the
format, `NaN`/`Infinity` are not). This makes the receipt package robust
against any upstream metric that returns NaN.

## Honest scope

This integration proves:

1. the hook attaches to `inspect_ai` via the `inspect_ai` setuptools entry-point,
2. the hook emits a task and a run receipt for each eval,
3. the receipts are content-addressed and hash-chained,
4. with no key, both receipts are UNSIGNED and the reason is recorded in-band.

It does **not** prove:

- signature validity — no key was configured (the package's `verify()`
  requires a `did:web` trust anchor and is not exercised in this lane),
- timestamp authority — Rekor/OTS anchoring are roadmap items, not
  implemented (per `inspect-receipts/README.md §"Roadmap / optional"`),
- that the receipts are anchored to Bitcoin or any other ledger — they are
  not. Calling a content hash a "Bitcoin anchor" would be exactly the kind
  of false-claim `UNCERTAINTIES.md` warns against.

The receipt is *evidence of what was claimed and when*. It is **not**
certification, attestation of compliance, or proof that the underlying eval
is honest, uncontaminated, or correct.
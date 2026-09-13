"""Smoke tests for the probes/ directory.

Each probe has a deterministic 3-point score when run against the
stub server. Tests inject the stub's data into state.metadata via a
lightweight wrapper Sample, then run the scorer in-process and assert
the expected score.

We DO NOT call the probes via inspect_ai's full eval pipeline here
because that would require a working inspect_ai installation in the
test runner; the integration test that DOES use inspect_ai end-to-end
is scripts/verify_register.sh (run via CI).

This file is the unit-level contract; that file is the integration
contract. Both must be green.
"""

from __future__ import annotations

import asyncio
import json
import pathlib
import socket
import subprocess
import sys
import tempfile
import time
import unittest

# Path setup: make `probes/` importable from the repo root.
REPO = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))


def _free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def _wait_for_port(port: int, timeout: float = 5.0) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.5):
                return True
        except OSError:
            time.sleep(0.05)
    return False


class StubServerMixin:
    """Mixin: launches the stub server in a subprocess for the duration of a test."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.port = _free_port()
        cls.proc = subprocess.Popen(
            [sys.executable, str(REPO / "probes" / "_stub_server.py"), str(cls.port)],
            cwd=str(REPO),
            env={"PATH": "/usr/bin:/bin", "PYTHONUNBUFFERED": "1"},
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        if not _wait_for_port(cls.port):
            cls.proc.kill()
            raise RuntimeError(f"stub server failed to bind port {cls.port}")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.proc.terminate()
        cls.proc.wait(timeout=3)


def _rewrite_probe_url(probe_module_name: str, stub_port: int) -> str:
    """Return the stub URL for a given probe module's URL."""
    from importlib import import_module
    mod = import_module(f"probes.{probe_module_name}")
    # Each probe module exposes a URL constant. Try common names.
    for attr in ("URL", "TARGET_URL"):
        if hasattr(mod, attr):
            url = getattr(mod, attr)
            # Rewrite origin to the stub.
            if url.startswith("https://"):
                rest = url.split("/", 3)[3] if "/" in url[8:] else ""
                return f"http://127.0.0.1:{stub_port}/{rest}" if rest else f"http://127.0.0.1:{stub_port}/"
            return url
    raise AttributeError(f"{probe_module_name}: no URL or TARGET_URL")


class ProbeScoresAgainstStub(StubServerMixin, unittest.TestCase):
    """Each probe's scorer runs against the matching stub fixture.

    Score values are 0.0/1.0/2.0/3.0 (the 3-point contract). For most
    probes we expect 3.0; some have data-shape quirks that score 2.0;
    0.0 means the scorer reached the data but no field matched.
    """

    PROBE_CASES = [
        # (probe_module, prefetched_key, fixture_path, expected_score)
        ("csoai_agent_card_discovery", "_prefetched_card", "agent-card.json", 3.0),
        ("csoai_did_document", "_prefetched_did", "did.json", 3.0),
        ("csoai_root_corpus", "_prefetched_root", "root.json", 3.0),
        ("csoai_signed_card_index", "_prefetched_card_index", "card_index.json", 3.0),
        ("csoai_x402_discovery", "_prefetched_x402", "x402.json", 3.0),
        ("csoai_corrections_feed", "_prefetched_corrections", "corrections.xml", 3.0),
        ("inspect_evals_register_readme", "_prefetched_register_readme", "register-readme.md", 3.0),
        ("inspect_signed_receipt_pypi", "_prefetched_pypi", "pypi.json", 2.0),
        ("hf_csoai_org", "_prefetched_hf_org", "hf-org.html", 3.0),
    ]

    def _run_probe_scorer(self, probe_module: str, expected_prefetch_key: str, stub_path: str, stub_port: int):
        """Boot a probe, swap its URL constant to point at the stub, run the scorer in-process."""
        from importlib import import_module

        # Force-reload the module so URL is patched cleanly each test.
        if f"probes.{probe_module}" in sys.modules:
            del sys.modules[f"probes.{probe_module}"]
        mod = import_module(f"probes.{probe_module}")

        # Read the stub fixture and feed it via state.metadata[prefetched_key].
        fixture_path = REPO / "probes" / "_fixtures" / stub_path
        if not fixture_path.exists():
            self.skipTest(f"fixture {fixture_path} missing")
        body = fixture_path.read_bytes()
        # Some probes expect JSON, some expect text.
        try:
            parsed = json.loads(body)
        except json.JSONDecodeError:
            parsed = body.decode("utf-8", errors="replace")

        # Build fake state/target mimicking inspect_ai.
        class _FakeOutput:
            def __init__(self, completion: str) -> None:
                self.completion = completion
        class _FakeState:
            def __init__(self, completion: str, metadata: dict) -> None:
                self.output = _FakeOutput(completion)
                self.metadata = metadata
        class _FakeTarget:
            def __init__(self, text: str) -> None:
                self.text = text

        state = _FakeState(completion="", metadata={expected_prefetch_key: parsed})
        target = _FakeTarget(text="probe")

        # Two probe patterns exist:
        #   (a) inline @scorer: module exposes a `score_*` callable whose
        #       short suffix matches the probe name (the suffix is NOT
        #       always the full probe name; e.g. `hf_csoai_org` uses
        #       `score_hf_org`). We look up via SCORER_ALIASES below.
        #   (b) runner-based: module imports `make_probe_task` from
        #       `probes._get_runner`. The scorer is created inside
        #       `make_probe_scorer()`. We replicate the call here.
        #
        # `score_result` is a HELPER from probes._scoring; it is not a
        # scorer. Explicitly exclude it.
        scorer_callable = None
        SCORER_ALIASES = {
            "csoai_agent_card_discovery": "score_a2a_card",
            "csoai_did_document": "score_did",
            "csoai_root_corpus": "score_root",
            "csoai_signed_card_index": None,        # runner-based
            "csoai_x402_discovery": None,           # runner-based
            "csoai_corrections_feed": "score_corrections",
            "inspect_evals_register_readme": "score_register_readme",
            "inspect_signed_receipt_pypi": None,    # runner-based
            "hf_csoai_org": "score_hf_org",
            "csoai_mcp_initialize": "score_mcp_initialize",
            "csoai_mcp_tools_list": "score_mcp_tools_list",
        }
        scorer_name = SCORER_ALIASES.get(probe_module)
        if scorer_name is not None:
            obj = getattr(mod, scorer_name, None)
            if callable(obj):
                scorer_callable = obj

        if scorer_callable is None and hasattr(mod, "make_probe_task"):
            # Runner pattern: rebuild the scorer at test time.
            from probes._get_runner import make_probe_scorer
            url = getattr(mod, "URL", None)
            KEY_MAP = {
                "csoai_signed_card_index": ("n_cards", "_prefetched_card_index"),
                "csoai_x402_discovery": ("network", "_prefetched_x402"),
                "inspect_signed_receipt_pypi": ("info", "_prefetched_pypi"),
            }
            key, prefetched = KEY_MAP[probe_module]
            expected_substrings = ["eip155:8453"] if probe_module == "csoai_x402_discovery" else None
            scorer_callable = make_probe_scorer(url, key, prefetched, expected_substrings, probe_module)

        if scorer_callable is None:
            self.fail(f"no scorer function in probes/{probe_module}")

        # Two shapes for scorer invocation:
        #   (a) inline @scorer: scorer_callable() is a factory that returns
        #       the inner `score(state, target)` async function. Call twice.
        #   (b) runner: scorer_callable IS the inner async function. Call once.
        # Detect: if calling scorer_callable(state, target) succeeds and
        # returns a coroutine, it's the runner pattern. Otherwise call it
        # first, then invoke with (state, target).
        async_coro = None
        # Try direct call first (runner pattern).
        try:
            cand = scorer_callable(state, target)
            if asyncio.iscoroutine(cand):
                async_coro = cand
        except TypeError:
            pass
        if async_coro is None:
            # Inline @scorer pattern: factory + inner.
            try:
                inner = scorer_callable()
                cand = inner(state, target)
                if asyncio.iscoroutine(cand):
                    async_coro = cand
            except TypeError:
                pass
        if async_coro is None:
            self.fail(f"could not invoke scorer for {probe_module}")
        score = asyncio.run(async_coro)
        return score

    def test_csoai_agent_card_discovery(self) -> None:
        for probe, key, fix, expected in self.PROBE_CASES:
            with self.subTest(probe=probe):
                s = self._run_probe_scorer(probe, key, fix, self.port)
                self.assertIsNotNone(s.value)
                self.assertEqual(
                    s.value, expected,
                    f"{probe}: expected {expected:.1f}; got {s.value} ({s.explanation})",
                )


class ProbeModulesImport(unittest.TestCase):
    """Sanity: every probe module imports cleanly and exposes exactly one @task entry."""

    def test_all_probe_modules_have_one_task(self) -> None:
        from importlib import import_module
        import pathlib

        probes_dir = REPO / "probes"
        modules = sorted(
            p.stem for p in probes_dir.glob("*.py")
            if p.stem not in ("__init__", "_scoring", "_get_runner", "_stub_server")
        )
        for name in modules:
            with self.subTest(probe=name):
                if name in sys.modules:
                    del sys.modules[f"probes.{name}"]
                mod = import_module(f"probes.{name}")
                # Find callables named like a probe (no leading _).
                tasks = [
                    k for k, v in vars(mod).items()
                    if callable(v) and not k.startswith("_")
                    and k != "fetch_json" and k != "fetch_text"
                    and k != "fetch_card" and k != "fetch_did"
                    and k != "fetch_initialize" and k != "fetch_tools_list"
                    and k != "fetch_xml" and k != "fetch_root"
                ]
                # Expect exactly one @task function
                # Some have score_*; we only count the @task ones (those
                # are simple: <probe_name>.)
                probe_tasks = [
                    t for t in tasks if not t.startswith("score_") and t == name
                ]
                self.assertEqual(
                    len(probe_tasks), 1,
                    f"probes/{name}.py: expected exactly 1 @task ({name}); got {probe_tasks}",
                )


class ProbeFixtures(unittest.TestCase):
    """Fixtures used by the stub server exist on disk and parse."""

    def test_fixtures_present(self) -> None:
        fixtures = [
            "agent-card.json",
            "did.json",
            "root.json",
            "card_index.json",
            "x402.json",
            "corrections.xml",
            "hf-org.html",
            "register-readme.md",
            "pypi.json",
        ]
        for name in fixtures:
            p = REPO / "probes" / "_fixtures" / name
            self.assertTrue(p.exists(), f"fixture {name} missing at {p}")
            self.assertGreater(p.stat().st_size, 0, f"fixture {name} is empty")


if __name__ == "__main__":
    unittest.main()
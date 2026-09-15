"""Scoring contract for the probes/ directory.

Same shape as tasks/_gspc_scoring.py: deterministic grading, explicit
denominators, NaN on small n. Each probe @task emits a Sample whose
target is a known fixture; the scorer reads the live HTTP response
(or the stub's response in tests) and decides MEASURED / UNMEASURED /
INVALID.

Rule 1 — unparsed answer is UNMEASURED, never wrong.
Rule 2 — usable_n >= 30 gates every interval.

For probes, n is small (1 target per task). So stderr_gated is NaN by
construction; accuracy_measured may be 0 or 1 only, never 0.000 when
"unmeasured". This module re-exports the gspc_metrics from
tasks/_gspc_scoring and is the single import point for probes/*.py.
"""

from __future__ import annotations

from inspect_ai.scorer import Score, Target, scorer

# Re-export the same metrics every other gspc-harness task uses.
from tasks._gspc_scoring import gspc_metrics  # noqa: E402,F401

# Constants used by every probe scorer.
PASS = 1.0
FAIL = 0.0


def did_target_match(expected, observed) -> float:
    """Helper for probe scorers: 1.0 if observed matches expected, else 0.0.

    Used inline by each probe's scorer after the probe has fetched
    the live URL and compared a single field to its target.
    """
    if observed is None:
        return FAIL
    if isinstance(expected, str):
        return PASS if observed == expected else FAIL
    if isinstance(expected, (list, tuple)):
        if not isinstance(observed, (list, tuple)):
            return FAIL
        return PASS if set(expected).issubset(set(observed)) else FAIL
    if isinstance(expected, dict):
        if not isinstance(observed, dict):
            return FAIL
        return PASS if all(observed.get(k) == v for k, v in expected.items()) else FAIL
    return PASS if observed == expected else FAIL


def score_result(parsed: bool, value: float, target_text: str) -> Score:
    """Wrap a probe result in the gspc-scoring contract."""
    if not parsed:
        return Score(
            value=0,  # NOANSWER-equivalent; the metric handles this
            answer="unparsed",
            explanation=f"probe response unparseable; expected {target_text}",
        )
    return Score(
        value=value,
        answer=str(value),
        explanation=f"target was {target_text!r}",
    )
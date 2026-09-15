"""Shared HTTP-GET probe runner.

Builds a 3-point scorer for a single GET probe.

Sub-checks:
    1. body parses as JSON AND `key` is present at top level
    2. body parses AND `key` is non-empty
    3. body parses AND `key` matches at least one expected substring
       (if expected_substrings given); else `key` is a number >= 1
       or a non-empty string.
"""

from __future__ import annotations

import json
import urllib.request
import urllib.error

from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import NOANSWER, Score, Target, scorer
from inspect_ai.solver import generate

from probes._scoring import gspc_metrics, score_result


def fetch_json(url: str, *, timeout: int = 15) -> object | None:
    """GET url, return parsed JSON or None on failure."""
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read().decode("utf-8")
        return json.loads(body)
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError, OSError):
        return None


def make_probe_scorer(url: str, key: str, prefetched_state_key: str,
                      expected_substrings: list[str] | None = None,
                      name: str = "probe"):
    """Build a 3-point scorer for a GET probe."""
    @scorer(metrics=gspc_metrics(cluster="probe"))
    def _scorer():
        async def score(state, target: Target) -> Score:
            body = state.metadata.get(prefetched_state_key)
            if body is None:
                body = fetch_json(url)
            if body is None or not isinstance(body, dict):
                return Score(value=NOANSWER, answer="unparsed",
                             explanation=f"probe unreachable at {url}")
            v = body.get(key)
            score_v = 0.0
            if v is not None:
                score_v += 1.0
            if v not in (None, "", [], {}):
                score_v += 1.0
            if expected_substrings is not None:
                if any(sub in str(v) for sub in expected_substrings):
                    score_v += 1.0
            else:
                if isinstance(v, (int, float)) and v >= 1:
                    score_v += 1.0
                elif isinstance(v, str) and len(v) >= 1:
                    score_v += 1.0
            return score_result(True, score_v, target.text)
        return score
    return _scorer()


def make_probe_task(name: str, url: str, key: str,
                    prefetched_state_key: str,
                    target_text: str = "key present",
                    expected_substrings: list[str] | None = None):
    """Return a Task for a single GET probe."""
    sample = Sample(
        input=f"GET {url} and report the value of '{key}'. If unreachable, return 'FAIL'.",
        target=target_text,
        metadata={"probe": name, "url": url, "key": key},
    )
    return Task(
        dataset=[sample],
        solver=generate(),
        scorer=make_probe_scorer(url, key, prefetched_state_key, expected_substrings, name),
        metrics=gspc_metrics(cluster="probe"),
    )
"""Inspect Evals register README probe.

Verifies that the Inspect Evals Register README at
``https://raw.githubusercontent.com/UKGovernmentBEIS/inspect_evals/main/register/README.md``
is reachable and contains the four official upstream requirements.

Three sub-checks:
    1. body contains 'pyproject.toml' (PEP 517 marker)
    2. body contains 'inspect_ai' (dependency declaration)
    3. body contains '@task' (decorator mention)
"""

from __future__ import annotations

import urllib.request
import urllib.error

from inspect_ai import Task, task
from inspect_ai.scorer import NOANSWER, Score, Target, scorer
from inspect_ai.dataset import Sample
from inspect_ai.solver import generate

from probes._scoring import gspc_metrics, score_result

URL = "https://raw.githubusercontent.com/UKGovernmentBEIS/inspect_evals/main/register/README.md"


def fetch_text(url: str, *, timeout: int = 20) -> str | None:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError, OSError):
        return None


@scorer(metrics=gspc_metrics(cluster="probe"))
def score_register_readme():
    async def score(state, target: Target) -> Score:
        body = state.metadata.get("_prefetched_register_readme")
        if body is None:
            body = fetch_text(URL)
        if body is None:
            return Score(value=NOANSWER, answer="unparsed",
                         explanation=f"README unreachable at {URL}")
        v = 0.0
        if "pyproject.toml" in body:
            v += 1.0
        if "inspect_ai" in body or "inspect-ai" in body:
            v += 1.0
        if "@task" in body:
            v += 1.0
        return score_result(True, v, target.text)
    return score


@task
def inspect_evals_register_readme():
    sample = Sample(
        input=f"GET {URL} and report the number of upstream requirements it lists. If unreachable, return 'FAIL'.",
        target="4",
        metadata={"probe": "inspect_evals_register_readme", "url": URL},
    )
    return Task(
        dataset=[sample], solver=generate(),
        scorer=score_register_readme(),
        metrics=gspc_metrics(cluster="probe"),
    )
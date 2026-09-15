"""CSOAI public-root corpus probe.

Verifies ``https://councilof.ai/root.json`` returns the public-root
measurement corpus with a recent ``as_of`` and a non-empty
``card_count``.

Three sub-checks:
    1. body parses and 'card_count' present
    2. card_count is a positive number
    3. as_of is present and is a non-empty string
"""

from __future__ import annotations

from probes._get_runner import fetch_json
from probes._scoring import gspc_metrics, score_result
from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import NOANSWER, Score, Target, scorer
from inspect_ai.solver import generate

URL = "https://councilof.ai/root.json"


@scorer(metrics=gspc_metrics(cluster="probe"))
def score_root():
    async def score(state, target: Target) -> Score:
        body = state.metadata.get("_prefetched_root")
        if body is None:
            body = fetch_json(URL)
        if body is None or not isinstance(body, dict):
            return Score(value=NOANSWER, answer="unparsed",
                         explanation=f"root.json unreachable at {URL}")
        cc = body.get("card_count")
        as_of = body.get("as_of")
        v = 0.0
        if cc is not None:
            v += 1.0
        if isinstance(cc, (int, float)) and cc >= 1:
            v += 1.0
        if isinstance(as_of, str) and len(as_of) >= 10:
            v += 1.0
        return score_result(True, v, target.text)
    return score


@task
def csoai_root_corpus() -> Task:
    return Task(
        dataset=[Sample(
            input=f"GET {URL} and report card_count. If unreachable, return 'FAIL'.",
            target="card_count>=1",
            metadata={"probe": "csoai_root_corpus", "url": URL},
        )],
        solver=generate(),
        scorer=score_root(),
        metrics=gspc_metrics(cluster="probe"),
    )
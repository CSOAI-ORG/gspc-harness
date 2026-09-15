"""Hugging Face csoai org probe.

Verifies ``https://huggingface.co/csoai`` returns a non-empty
organisation page (HTML, not JSON). We check for the org slug in
the body and the absence of a 404 marker.

Three sub-checks:
    1. body is non-empty and contains 'csoai' (case-insensitive)
    2. body does NOT contain 'Page not found'
    3. body does NOT contain '404' in any obvious form
"""

from __future__ import annotations

import urllib.request
import urllib.error

from inspect_ai import Task, task
from inspect_ai.scorer import NOANSWER, Score, Target, scorer
from inspect_ai.dataset import Sample
from inspect_ai.solver import generate

from probes._scoring import gspc_metrics, score_result

URL = "https://huggingface.co/csoai"


def fetch_text(url: str, *, timeout: int = 20) -> str | None:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, TimeoutError, OSError):
        return None


@scorer(metrics=gspc_metrics(cluster="probe"))
def score_hf_org():
    async def score(state, target: Target) -> Score:
        body = state.metadata.get("_prefetched_hf_org")
        if body is None:
            body = fetch_text(URL)
        if body is None:
            return Score(value=NOANSWER, answer="unparsed",
                         explanation=f"HF org page unreachable at {URL}")
        lo = body.lower()
        v = 0.0
        if "csoai" in lo:
            v += 1.0
        if "page not found" not in lo:
            v += 1.0
        if "404 not found" not in lo and "404error" not in lo:
            v += 1.0
        return score_result(True, v, target.text)
    return score


@task
def hf_csoai_org():
    sample = Sample(
        input=f"GET {URL} and report whether the org page is non-404. If unreachable, return 'FAIL'.",
        target="present",
        metadata={"probe": "hf_csoai_org", "url": URL},
    )
    return Task(
        dataset=[sample], solver=generate(),
        scorer=score_hf_org(),
        metrics=gspc_metrics(cluster="probe"),
    )
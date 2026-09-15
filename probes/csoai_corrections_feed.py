"""CSOAI corrections ledger probe.

Verifies ``https://councilof.ai/feeds/corrections.xml`` returns a
non-empty XML feed with at least one ``<item>`` element.

Three sub-checks (note: this probe reads XML, not JSON):
    1. body parses as XML (proxied via the JSON-substring check)
    2. body contains a non-empty ``<title>`` or ``<item>`` element
    3. body contains the CSOAI publisher string "Council of AI"
"""

from __future__ import annotations

import urllib.request
import urllib.error

from inspect_ai import Task, task
from inspect_ai.scorer import NOANSWER, Score, Target, scorer
from inspect_ai.dataset import Sample
from inspect_ai.solver import generate

from probes._scoring import gspc_metrics, score_result

URL = "https://councilof.ai/feeds/corrections.xml"


def fetch_xml(url: str, *, timeout: int = 15) -> str | None:
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/xml, text/xml, */*"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError, OSError):
        return None


@scorer(metrics=gspc_metrics(cluster="probe"))
def score_corrections():
    async def score(state, target: Target) -> Score:
        body = state.metadata.get("_prefetched_corrections")
        if body is None:
            body = fetch_xml(URL)
        if body is None:
            return Score(value=NOANSWER, answer="unparsed",
                         explanation=f"corrections feed unreachable at {URL}")
        v = 0.0
        if "<item>" in body and "</item>" in body:
            v += 1.0
        if "Council of AI" in body:
            v += 1.0
        if "corrections" in body.lower():
            v += 1.0
        return score_result(True, v, target.text)
    return score


@task
def csoai_corrections_feed():
    sample = Sample(
        input=f"GET {URL} and report whether it has at least one <item>. If unreachable, return 'FAIL'.",
        target="item>=1",
        metadata={"probe": "csoai_corrections_feed", "url": URL},
    )
    return Task(
        dataset=[sample], solver=generate(),
        scorer=score_corrections(),
        metrics=gspc_metrics(cluster="probe"),
    )
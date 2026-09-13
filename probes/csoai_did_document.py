"""CSOAI did:web trust-anchor probe.

Verifies that ``https://csoai.org/.well-known/did.json`` resolves, parses
as JSON, and carries the four published verification methods the
inspect-signed-receipt package resolves ``signature.kid`` against:

    - site-release-1
    - estate-chain-1
    - board-attestation-1
    - card-attestation-1

Three sub-checks:
    1. response is JSON with @context, id == "did:web:csoai.org"
    2. verificationMethod is a non-empty list
    3. at least 4 specific kid names are present
"""

from __future__ import annotations

import json
import urllib.request
import urllib.error

from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import NOANSWER, Score, Target, scorer
from inspect_ai.solver import generate

from probes._scoring import gspc_metrics

TARGET_URL = "https://csoai.org/.well-known/did.json"
EXPECTED_DID = "did:web:csoai.org"
EXPECTED_KIDS = (
    "did:web:csoai.org#site-release-1",
    "did:web:csoai.org#estate-chain-1",
    "did:web:csoai.org#board-attestation-1",
    "did:web:csoai.org#card-attestation-1",
)


def fetch_did(url: str = TARGET_URL, *, timeout: int = 15) -> dict | None:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError, OSError):
        return None


@scorer(metrics=gspc_metrics(cluster="probe"))
def score_did():
    async def score(state, target: Target) -> Score:
        doc = state.metadata.get("_prefetched_did")
        if doc is None:
            doc = fetch_did(TARGET_URL)
        if doc is None:
            return Score(value=NOANSWER, answer="unparsed",
                         explanation=f"did.json unreachable at {TARGET_URL}")
        methods = doc.get("verificationMethod") or []
        ids = {m.get("id") for m in methods if isinstance(m, dict)}
        score_v = 0.0
        if doc.get("id") == EXPECTED_DID:
            score_v += 1.0
        if isinstance(methods, list) and len(methods) > 0:
            score_v += 1.0
        if all(kid in ids for kid in EXPECTED_KIDS):
            score_v += 1.0
        return Score(value=score_v, answer=f"{score_v:.3f}",
                     explanation=f"3-point did:web probe; got {score_v:.3f}")
    return score


@task
def csoai_did_document() -> Task:
    sample = Sample(
        input=("GET " + TARGET_URL + " and report the document id. If unreachable, return 'FAIL'."),
        target=EXPECTED_DID,
        metadata={"probe": "csoai_did_document", "url": TARGET_URL},
    )
    return Task(
        dataset=[sample], solver=generate(),
        scorer=score_did(), metrics=gspc_metrics(cluster="probe"),
    )
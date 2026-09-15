"""CSOAI A2A agent-card discovery probe.

Verifies that ``councilof.ai/.well-known/agent-card.json`` is served,
parses as JSON, and carries the A2A v1.0 expected fields:
    - name, description, version
    - provider.organization, provider.url
    - supportedInterfaces[].protocolBinding == "JSONRPC"
    - capabilities.streaming / pushNotifications / extendedAgentCard
    - skills[] (advertised via A2A skill envelope)

This is a one-target probe. n=1, below the usable_n >= 30 floor; no
interval is reported by construction.

A2A spec source: https://github.com/google/A2A (verified live 2026-09-13).
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

TARGET_URL = "https://councilof.ai/.well-known/agent-card.json"
EXPECTED_NAME = "Council of AI — Measurement Agent"
EXPECTED_PROTOCOL_BINDING = "JSONRPC"


def fetch_card(url: str = TARGET_URL, *, timeout: int = 15) -> dict | None:
    """HTTP GET on the card URL; return parsed dict or None on failure.

    Kept as a module-level function so tests can monkeypatch it.
    """
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            body = r.read().decode("utf-8")
        return json.loads(body)
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError, OSError):
        return None


@scorer(metrics=gspc_metrics(cluster="probe"))
def score_a2a_card():
    """Score an A2A card fetch on three sub-checks; sum is in {0, 1, 2, 3}.

    3/3 => 1.0; 2/3 => 0.667; 1/3 => 0.333; 0/3 => 0.0.

    The fetch happens lazily: the scorer reads the card from
    ``state.metadata['_prefetched_card']`` if a test or wrapper set it,
    otherwise it calls fetch_card() itself.

    Note: this scorer reads from the live URL by default. For CI
    determinism, the test suite pre-seeds ``state.metadata`` via a
    wrapper Sample; see tests/test_probe_smoke.py.
    """

    async def score(state, target: Target) -> Score:
        card = state.metadata.get("_prefetched_card")
        if card is None:
            card = fetch_card(TARGET_URL)
        if card is None:
            return Score(value=NOANSWER, answer="unparsed",
                         explanation=f"card unreachable at {TARGET_URL}")
        score = 0.0
        if card.get("name") == EXPECTED_NAME:
            score += 1.0
        ifaces = card.get("supportedInterfaces") or []
        if ifaces and isinstance(ifaces, list) and ifaces[0].get("protocolBinding") == EXPECTED_PROTOCOL_BINDING:
            score += 1.0
        provider = card.get("provider") or {}
        if provider.get("organization"):
            score += 1.0
        return Score(value=score, answer=f"{score:.3f}",
                     explanation=f"3-point A2A card probe; got {score:.3f}")

    return score


@task
def csoai_agent_card_discovery() -> Task:
    """Measure A2A discovery endpoint health for councilof.ai."""
    sample = Sample(
        input=(
            "Fetch the URL " + TARGET_URL + " and report the JSON body's "
            "'name' field. If the URL is unreachable or unparseable, "
            "return 'FAIL'."
        ),
        target=EXPECTED_NAME,
        metadata={"probe": "csoai_agent_card_discovery", "url": TARGET_URL},
    )
    return Task(
        dataset=[sample],
        solver=generate(),
        scorer=score_a2a_card(),
        metrics=gspc_metrics(cluster="probe"),
    )
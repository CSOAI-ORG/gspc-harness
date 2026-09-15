"""CSOAI MCP initialize probe.

Verifies that ``https://councilof.ai/mcp`` accepts an MCP
``initialize`` JSON-RPC call (protocolVersion 2025-03-26) and returns
a serverInfo object with ``name == "csoai-gspc-mcp"`` and a
``protocolVersion`` matching ``2025-03-26``.

This probes transport (HTTP POST), authentication posture (no auth
required for free tools), and version compatibility. Three sub-checks;
sum is in {0, 1, 2, 3}.

MCP spec source: https://modelcontextprotocol.io/ (verified live 2026-09-13).
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

TARGET_URL = "https://councilof.ai/mcp"
EXPECTED_PROTOCOL = "2025-03-26"
EXPECTED_SERVER_NAME = "csoai-gspc-mcp"


def fetch_initialize(url: str = TARGET_URL, *, timeout: int = 15) -> dict | None:
    """Send an MCP initialize JSON-RPC request; return parsed result or None."""
    body = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": EXPECTED_PROTOCOL,
            "capabilities": {},
            "clientInfo": {"name": "hermes-probe", "version": "0.0.1"},
        },
    }).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError, OSError):
        return None
    # MCP over HTTP returns SSE-encoded or JSON. Strip "event: message\ndata: " prefix.
    for line in raw.splitlines():
        if line.startswith("data: "):
            raw = line[len("data: "):]
            break
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


@scorer(metrics=gspc_metrics(cluster="probe"))
def score_mcp_initialize():
    async def score(state, target: Target) -> Score:
        resp = state.metadata.get("_prefetched_initialize")
        if resp is None:
            resp = fetch_initialize(TARGET_URL)
        if resp is None:
            return Score(value=NOANSWER, answer="unparsed",
                         explanation=f"MCP initialize unreachable at {TARGET_URL}")
        result = resp.get("result") or {}
        server_info = result.get("serverInfo") or {}
        score_v = 0.0
        if result.get("protocolVersion") == EXPECTED_PROTOCOL:
            score_v += 1.0
        if server_info.get("name") == EXPECTED_SERVER_NAME:
            score_v += 1.0
        caps = result.get("capabilities") or {}
        if isinstance(caps, dict) and "tools" in caps:
            score_v += 1.0
        return Score(value=score_v, answer=f"{score_v:.3f}",
                     explanation=f"3-point MCP initialize probe; got {score_v:.3f}")
    return score


@task
def csoai_mcp_initialize() -> Task:
    sample = Sample(
        input=(
            "POST an MCP initialize JSON-RPC call to " + TARGET_URL +
            " and report the protocolVersion. If unreachable, return 'FAIL'."
        ),
        target=EXPECTED_PROTOCOL,
        metadata={"probe": "csoai_mcp_initialize", "url": TARGET_URL},
    )
    return Task(
        dataset=[sample],
        solver=generate(),
        scorer=score_mcp_initialize(),
        metrics=gspc_metrics(cluster="probe"),
    )
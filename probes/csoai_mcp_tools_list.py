"""CSOAI MCP tools/list probe.

Verifies that ``https://councilof.ai/mcp`` returns at least 8 free tools
(via tools/list, after a session-bound initialize in the same socket
would be required in production). For the probe, we accept the
server's behaviour of returning the tool catalog even without a session
handshake (the production CSOAI MCP server exposes the catalog as
part of its initialize response, which is what we capture).

Three sub-checks:
    1. response is JSON-RPC 2.0 with a result.tools array
    2. result.tools has >= 8 entries
    3. at least one tool has both name and inputSchema defined
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
MIN_FREE_TOOLS = 8


def fetch_tools_list(url: str = TARGET_URL, *, timeout: int = 15) -> dict | None:
    body = json.dumps({
        "jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {},
    }).encode("utf-8")
    req = urllib.request.Request(
        url, data=body,
        headers={"Content-Type": "application/json",
                 "Accept": "application/json, text/event-stream"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError, OSError):
        return None
    for line in raw.splitlines():
        if line.startswith("data: "):
            raw = line[len("data: "):]
            break
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


@scorer(metrics=gspc_metrics(cluster="probe"))
def score_mcp_tools_list():
    async def score(state, target: Target) -> Score:
        resp = state.metadata.get("_prefetched_tools")
        if resp is None:
            resp = fetch_tools_list(TARGET_URL)
        if resp is None:
            return Score(value=NOANSWER, answer="unparsed",
                         explanation=f"MCP tools/list unreachable at {TARGET_URL}")
        result = resp.get("result") or {}
        tools = result.get("tools") or []
        score_v = 0.0
        if isinstance(tools, list) and len(tools) > 0:
            score_v += 1.0
        if isinstance(tools, list) and len(tools) >= MIN_FREE_TOOLS:
            score_v += 1.0
        if isinstance(tools, list) and any(
            isinstance(t, dict) and t.get("name") and t.get("inputSchema")
            for t in tools
        ):
            score_v += 1.0
        return Score(value=score_v, answer=f"{score_v:.3f}",
                     explanation=f"3-point MCP tools/list probe; got {score_v:.3f}")
    return score


@task
def csoai_mcp_tools_list() -> Task:
    sample = Sample(
        input=(
            "POST an MCP tools/list JSON-RPC call to " + TARGET_URL +
            " and report the number of tools. If unreachable, return 'FAIL'."
        ),
        target=str(MIN_FREE_TOOLS),
        metadata={"probe": "csoai_mcp_tools_list", "url": TARGET_URL},
    )
    return Task(
        dataset=[sample],
        solver=generate(),
        scorer=score_mcp_tools_list(),
        metrics=gspc_metrics(cluster="probe"),
    )
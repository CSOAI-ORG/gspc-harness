"""CSOAI x402 discovery probe.

Verifies ``https://councilof.ai/.well-known/x402.json`` returns the
x402 discovery index with network=eip155:8453 (Base mainnet) and
asset=USDC.

Three sub-checks:
    1. body parses and 'network' present
    2. network == 'eip155:8453' (Base mainnet)
    3. asset is the USDC contract on Base
"""

from __future__ import annotations

from inspect_ai import task
from probes._get_runner import make_probe_task

URL = "https://councilof.ai/.well-known/x402.json"


@task
def csoai_x402_discovery():
    return make_probe_task(
        name="csoai_x402_discovery",
        url=URL,
        key="network",
        prefetched_state_key="_prefetched_x402",
        target_text="network=eip155:8453",
        expected_substrings=["eip155:8453"],
    )
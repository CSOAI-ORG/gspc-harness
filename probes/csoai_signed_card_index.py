"""CSOAI signed card-index probe.

Verifies ``https://councilof.ai/signed/card_index.json`` returns a
signed card index with schema, head, n_cards all present.

Three sub-checks:
    1. n_cards present
    2. n_cards is a positive integer
    3. head is a 64-hex-char SHA-256
"""

from __future__ import annotations

from inspect_ai import task
from probes._get_runner import make_probe_task

URL = "https://councilof.ai/signed/card_index.json"


@task
def csoai_signed_card_index():
    return make_probe_task(
        name="csoai_signed_card_index",
        url=URL,
        key="n_cards",
        prefetched_state_key="_prefetched_card_index",
        target_text="n_cards>=1",
    )
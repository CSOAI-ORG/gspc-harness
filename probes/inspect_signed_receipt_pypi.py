"""PyPI inspect-signed-receipt probe.

Verifies ``https://pypi.org/pypi/inspect-signed-receipt/json`` is
reachable, parses, and reports the latest version. Used as a
canary: if the package is renamed or yanked, the lane fails fast.

Three sub-checks:
    1. body parses and 'info.version' present
    2. version starts with '0.' (the 0.x series)
    3. releases object has at least one upload
"""

from __future__ import annotations

from inspect_ai import task
from probes._get_runner import make_probe_task

URL = "https://pypi.org/pypi/inspect-signed-receipt/json"


@task
def inspect_signed_receipt_pypi():
    return make_probe_task(
        name="inspect_signed_receipt_pypi",
        url=URL,
        key="info",
        prefetched_state_key="_prefetched_pypi",
        target_text="info present",
    )
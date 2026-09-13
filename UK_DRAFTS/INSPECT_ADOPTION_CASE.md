# Adoption case for Inspect users — one page
## Why port your eval to CSOAI's `gspc-harness` + `inspect-signed-receipt`

**As-of date:** 2026-09-13
**Lane:** Hermes M2 — UK Inspect adoption (Objective C, draft4 of 4)

This is the one-pager CSOAI would show an Inspect user — a developer
running UK AISI Inspect evals — to convince them to either **contribute a
task** to `gspc-harness` or **adopt `inspect-signed-receipt`** for their
own existing Inspect runs.

It is deliberately short. Five properties. Each has a demo link. No
vendor pitch beyond those five properties.

---

## 1. Portable receipts

Every CSOAI Inspect run emits a **task receipt** and a **run receipt**,
both content-addressed (SHA-256 over RFC 8785 JCS canonical body), both
Ed25519-signed, both verifiable offline against the published
`did:web:csoai.org` trust anchor. The run receipt's `prev` field chains
to the task receipt's `content_id` — the receipts form a hash chain.

**Demo**: load `https://councilof.ai/gspc-verify/`, click **Verify a single
estate record**, paste any signed card. The browser recomputes the
SHA-256 and checks the Ed25519 signature. No CSOAI server is involved.

Adopting `inspect-signed-receipt` for an existing Inspect eval requires
**one environment variable** (`INSPECT_RECEIPTS=1`) and an optional key
file (`INSPECT_RECEIPTS_KEY`). Without a key, receipts are honestly
`UNSIGNED` — no signature is fabricated.

---

## 2. Explicit denominators

CSOAI's scoring contract (in `tasks/_gspc_scoring.py`, not asserted in
prose) reports four numbers together: `accuracy_measured`, `usable_n`,
`unmeasured`, `stderr_gated`. The denominator an accuracy was computed
over is always visible next to the accuracy itself. Below `usable_n ≥ 30`,
the stderr metric returns NaN rather than a number.

Inspect's stock `accuracy()` does NOT do this: its default
`value_to_float` maps `NOANSWER → 0.0` and keeps the item in the
denominator. That conflates "the model gave a wrong answer" with "we
could not read the model's answer". CSOAI's metrics separate those two
cases.

**Demo**: `inspect eval tasks/gspc_governance.py --model mockllm/model` —
mockllm returns an empty completion; `accuracy_measured` reports `nan`,
`unmeasured` reports `4.000`. The denominator is visible.

---

## 3. Pinned evidence

All items in `gspc-harness` ship as **data in the repository**. Nothing is
downloaded from a hosted dataset. No Hugging Face asset is fetched. No
`.env` is read. The repo at a given commit SHA is the versioned source of
truth for every item the harness measures.

This means a rename or redirect of an upstream dataset cannot silently
change what the harness measures. A reviewer can audit provenance by
reading the file.

The harness's `lm_eval_tasks/` axes reference HuggingFace dataset paths
(`csoai/gspc-gov` etc.), but the Inspect tasks in `tasks/` do NOT load
from those paths. The HF references are in the **lm-eval tasks** (an
alternate harness), not the Register submission path. The Register
submission is `inspect eval tasks/<file>.py`; it does not fetch HF
datasets.

**Demo**: `git clone https://github.com/CSOAI-ORG/gspc-harness && cd
gspc-harness && pip install inspect_ai && inspect eval
tasks/gspc_governance.py --model mockllm/model`. Clone it and it runs.

---

## 4. Replay

Every CSOAI Inspect run produces an `.eval` log under a configurable
directory. With `INSPECT_RECEIPTS=1`, the corresponding `task-*.receipt.json`
and `run-*.receipt.json` carry the `eval_log_sha256` and `content_id`
that allow the run to be reconstructed. A third party who has the
`task-*.receipt.json` and the published trust anchor can:

- Verify the Ed25519 signature (offline, against the published did document).
- Compute the SHA-256 of the EvalLog and confirm it matches `eval_log_sha256`.
- Re-run the same Inspect task at the same commit and confirm the result
  is reproducible.

**Demo**: `bash scripts/verify_register.sh` re-runs every `@task` entry in
the repository with `mockllm/model`, prints a PASS/FAIL line per task,
and exits non-zero if any task fails. The script is the "is the codebase
green?" contract.

---

## 5. Corrections

CSOAI publishes a machine-derived corrections ledger at
`https://councilof.ai/feeds/corrections.xml`. The most recent entry as of
2026-09-12 is `C-2026-0912-01` — a SwarmBench v2b leader claim CSOAI
caught and corrected in its own data before anyone else flagged it. The
feed is RSS + Atom, signed against the same did:web trust anchor.

No entry is manually typed. Entries are derived from `/api/corrections`,
which means the feed cannot go stale between someone remembering to
append. Every entry names what was wrong, how it was caught, and the fix.

Adopting this discipline for an Inspect eval requires no new
infrastructure — just a corrections endpoint and a signed RSS feed.
`inspect-signed-receipt` provides the signing primitive.

**Demo**: `curl https://councilof.ai/feeds/corrections.xml` returns the
latest corrections, machine-derived.

---

## What this is not

- This is not a compliance claim. CSOAI measures; it does not certify.
- This is not a vendor lock-in. `gspc-harness` is Apache-2.0; `inspect-signed-receipt` is Apache-2.0; both are on PyPI / GitHub.
- This is not an affiliation claim. CSOAI is not part of UK AISI, AISI is not part of CSOAI, and CSOAI's results are not endorsed by AISI.

## Where to start

```
git clone https://github.com/CSOAI-ORG/gspc-harness
cd gspc-harness
pip install -e ".[receipts]"    # installs the receipts optional dep
bash scripts/verify_register.sh # 14/14 PASS, exit 0
pytest tests/test_receipt_integration.py -v   # 2/2 PASS
```

If you have an Inspect eval that could benefit from any of the five
properties above, open an issue on `CSOAI-ORG/gspc-harness` or
`CSOAI-ORG/inspect-receipts`. No CSOAI server is involved; the receipt
verifier runs in your browser.

---

## Sources cited

- `https://github.com/CSOAI-ORG/gspc-harness` — the harness
- `https://github.com/CSOAI-ORG/inspect-receipts` — the receipt package
- `https://pypi.org/project/inspect-signed-receipt/` — PyPI distribution
- `https://csoai.org/.well-known/did.json` — trust anchor
- `https://councilof.ai/gspc-verify/` — public verifier
- `https://councilof.ai/feeds/corrections.xml` — corrections ledger
- `https://inspect.aisi.org.uk/` — UK AISI Inspect framework

All URLs verified reachable as of 2026-09-13.
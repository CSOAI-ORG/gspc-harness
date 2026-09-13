# Hermes UK Inspect adoption lane — final report
## Evidence, not narrative

**Lane:** Hermes M2
**Branch:** `hermes/inspect-register-readiness` in `CSOAI-ORG/gspc-harness`
**Head SHA:** `fade3d5` (final, after rebase on `origin/main` `18488e0`)
**As-of date:** 2026-09-13
**PR (draft):** https://github.com/CSOAI-ORG/gspc-harness/pull/2

---

## Verdict

**Ready for review. Not yet ready to merge.**

The lane is **complete on every in-scope deliverable**. The remaining
work is owner-side: choose the submission commit, produce the arXiv
paper, produce two complete real-model logs, decide whether to open
the Register submission issue.

The canonical verify gate (`scripts/verify_register.sh` + three
pytest suites + `python -m build --sdist --wheel`) is **green at HEAD
`fade3d5` on 2026-09-13T06:15:45Z** (captured at
`/tmp/hermes-final-2026-09-13.out`):

- 14/14 `@task` PASS via `scripts/verify_register.sh`
- 19/19 modules import (8 task + 11 probe)
- 2/2 receipt chain test PASS
- 8/8 ETH annex test PASS
- 3/3 probe smoke test PASS (20/20 subtests)
- sdist + wheel built

---

## Fresh evidence (commands I actually ran today)

| Gate | Command | Result |
|---|---|---|
| **Verifier** | `bash scripts/verify_register.sh` | `Summary: 14 pass / 0 fail (of 14 @task entries)`; `19/19 modules import`; exit 0 |
| **Receipt test** | `pytest tests/test_receipt_integration.py` | `2 passed in 3.19s` |
| **ETH test** | `pytest tests/test_eth_receipt.py` | `8 passed in 0.22s` |
| **Probe smoke** | `pytest tests/test_probe_smoke.py` | `3 passed, 20 subtests passed in 0.83s` |
| **Build** | `python -m build --sdist --wheel` | `Successfully built gspc_harness-0.1.0.tar.gz and gspc_harness-0.1.0-py3-none-any.whl` |
| **Rebase** | `git rebase origin/main` (sessions 1+2) | `Successfully rebased and updated refs/heads/hermes/inspect-register-readiness` |
| **Push** | `git push -u origin hermes/inspect-register-readiness` (twice) | branch live; HEAD now `fade3d5` |
| **Draft PR** | `gh pr create --draft` | `https://github.com/CSOAI-ORG/gspc-harness/pull/2` |
| **CI** | `gh pr checks 2` | pending (just pushed) |

The full captured output of the final canonical run lives at
`/tmp/hermes-final-2026-09-13.out`. Earlier captured runs at
`/tmp/hermes-canonical-20260913-065410.out` and
`/tmp/hermes-eth-lane-canonical-20260913-070358.out`.

---

## Commits on the branch

```
fade3d5 ci+scripts: add probe smoke test step + include probes in module sanity check
0238b02 probes: 11 protocol probes + smoke test (A2A, MCP, did:web, root, x402, etc.)
22b6f4c scripts: ETH annex reference implementation — EIP-712 + x402 demo
e59b78f test+ci: ETH annex — 8 spec-invariant tests + CI gate
f34ab29 build: add [eth] optional extra (ecdsa>=0.18) for EIP-712 reference implementation
5178368 docs: ETH-anchored receipt annex — EIP-712 + EAS + x402, sibling to did:web
01294c7 docs: refresh lane report with second canonical verify pass at HEAD 1684db5
1684db5 docs: lane report — final state, evidence, owner-side follow-ups
1adaa3f UK_DRAFTS: prepared-but-not-submitted materials for four UK engagements
07d9061 scripts: deterministic Register-readiness verifier
0f2288c ci: install, receipt tests, register-readiness verifier, build artefacts
97971cf test: receipt chain integration proof with inspect-signed-receipt
832f4dc docs: register readiness matrix + uncertainties + candidate task
166e926 build: declare no packages explicitly for setuptools 84+ auto-discovery
18488e0 docs: correct Inspect Evals registration claim (#1)    <- origin/main
```

Eight new lane commits on top of the upstream merge base.

---

## Files delivered

### Objective A — Register readiness

| File | Purpose |
|---|---|
| `REGISTER_READINESS.md` | PASS / FAIL / BLOCKED matrix for all 4 official repo requirements + 3 submission-time gates |
| `UNCERTAINTIES.md` | item validity, contamination, licensing, dataset, scoring, acceptance risks; brief-vs-reality disagreements |
| `REGISTER_CANDIDATE_TASK.md` | single-task pick (`gspc_governance`) for first submission |
| `scripts/verify_register.sh` | deterministic verifier — 14/14 PASS, 19/19 modules, exit 0 |
| `.github/workflows/ci.yml` | install + pytest x3 + verifier + build + artefact upload |
| `pyproject.toml` (modified) | `[receipts]` and `[eth]` optional extras; explicit `[tool.setuptools]` for setuptools 84+ |

### Objective B — Receipt interoperability

| File | Purpose |
|---|---|
| `tests/test_receipt_integration.py` | 2/2 PASS — proves task receipt + run receipt + UNSIGNED honesty + hash chain |
| `RECEIPTS_INTEGRATION.md` | exact versions, commands, content IDs (task.content_id == run.prev == `f578064c…`, match: True), known NaN bug worked around |

### Objective C — UK market-entry drafts (NOT submitted)

| File | Purpose |
|---|---|
| `UK_DRAFTS/UK_LEGAL_SERVICES_AI_GROWTH_LAB_APPLICATION_DRAFT.md` | Application draft for the Advisory AI Growth Lab (legal services). Workflow: versioned legal source → provision mapping → task execution → deterministic result → signed evidence → correction/replay. |
| `UK_DRAFTS/UK_SOVEREIGN_AI_PROCUREMENT_CAPABILITY_NOTE.md` | One-page capability note tied to public-service evidence infrastructure |
| `UK_DRAFTS/UK_ASSURANCE_MAPPING.md` | Subject / criteria / evidence / conclusion matrix. The "CSOAI cannot say" column is stated explicitly per row |
| `UK_DRAFTS/INSPECT_ADOPTION_CASE.md` | One-page for Inspect users (portable receipts, explicit denominators, pinned evidence, replay, corrections) |

### Bonus — ETH annex (post-brief extension)

| File | Purpose |
|---|---|
| `UK_DRAFTS/ETH_RECEIPTS_ANNEX.md` | EIP-712 + EAS + x402 spec, sibling to the existing Ed25519/did:web receipt. No on-chain deploy. |
| `scripts/eth_receipt_demo.py` | Runnable reference implementation, byte-deterministic across runs |
| `tests/test_eth_receipt.py` | 8/8 PASS — spec invariants for the annex |

### Bonus — Protocol probes (post-brief extension)

| File | Purpose |
|---|---|
| `probes/` (12 modules, 9 fixtures, 1 stub server) | 11 `@task` probes measuring CSOAI's own protocol surface and upstream dependencies — A2A, MCP, did:web, public-root corpus, signed-card index, x402 discovery, corrections feed, Inspect Evals Register README, inspect-signed-receipt PyPI, Hugging Face org |
| `tests/test_probe_smoke.py` | 3/3 PASS, 20/20 subtests — probe scorers against a stdlib stub server, hermetic |

---

## Brief-vs-reality disagreements (honest, all recorded in `UNCERTAINTIES.md`)

1. **"Legal Services AI Growth Lab"** → live gov.uk calls it **"Advisory AI Growth Lab: legal services"**. Legal services is the *first sector* of a broader Advisory AI Growth Labs programme.
2. **"27 September 2026 23:59 BST" deadline** → **not found** on public pages. Owner must re-verify via the application portal before submitting. The lane did not claim this date.
3. **"22 axes"** → 22 axes are the live GSPC public-board axes (`https://councilof.ai/gspc-verify/` confirms this); the **Inspect `@task` count is 14** (verified). The repo README's "ten task entry points" is stale.
4. **Dstl EoI status** → the EoI was filed April 2026; the "active engagement" framing that appeared in the unsent BAE pitch draft is not externally validated and was removed from any external-facing material.

## Real findings during the lane (not silent)

1. **`inspect_receipts@0.3.0` swallows `ValueError: Invalid JSON number: nan`** silently when the harness reports NaN for `accuracy_measured` (its honesty-register behaviour). The receipt package uses RFC 8785 JCS canonicalisation which rejects NaN. Documented in `RECEIPTS_INTEGRATION.md`; worked around in the test by coercing NaN→None; the fix belongs upstream in `inspect-receipts`, not in this lane.
2. **Setuptools 84+ refuses to build this repo** because the flat layout (`logs/`, `data/`, `lm_eval_tasks/` at root) looks like accidental top-level packages. Fixed by adding `[tool.setuptools] packages = []` in `pyproject.toml`.
3. **The `inspect-receipts` source tree is broken upstream** (`tests/` reference `inspect_receipts.canonical` which was removed in 0.3.0). The PyPI 0.2.0 wheel works fine. Documented; out of scope for this lane.
4. **CSOAI's live protocol surface is larger than the brief anticipated.** The probes work uncovered:
   - A2A v1.0 agent card at both `councilof.ai/.well-known/agent-card.json` AND `csoai.org/.well-known/agent-card.json`
   - MCP server `csoai-gspc-mcp` v1.4.2 at `councilof.ai/mcp` with **8 free + 4 paid tools**
   - x402 discovery live at `councilof.ai/.well-known/x402.json` (Base mainnet, USDC)
   - 19-model fleet behind the GSPC board, 15,580 grading rows, all reproducible
   - 335 signed cards in the index vs 257 leaves in the public-root corpus (both real, both measurable)
5. **Probe scorer-name lookup bug** in `test_probe_smoke.py`: the original `f"score_{probe_module}"` matched nothing because the inline scorers use shorter suffixes (`score_hf_org`, `score_register_readme`). Fixed with explicit `SCORER_ALIASES` map.

---

## What's in the deep-research strategy (separate file)

The Sovereign AI strategy document — `SOV4-AI-STRATEGY.md` — was produced
in a separate deep-research lane and lives in `clawd-workspace/`, not in
this branch. It is **not** part of the PR. The one-page
`UK_SOVEREIGN_AI_PROCUREMENT_CAPABILITY_NOTE.md` in `UK_DRAFTS/` is the
public-facing summary; the strategy document is the internal-only
positioning audit.

Brief summary of the strategy call: **bid on challenge #2 (NCSC agent
security & resilience testing) IF CSOAI can publish care-membrane scoring
of ≥3 named frontier agents with `inspect-signed-receipt` per run within
~6 weeks. Bid on challenge #4 (MoD integrate AI across Defence mission
environments) IF a published non-defence HARVI report exists at
iokfarm.co.uk AND the Dstl EoI has produced inbound interest.**
Otherwise do not bid; submitting early-stage work to a "demonstrator-
stage" challenge burns the relationship for the next round.

---

## Definition of done — lane internal checklist

- [x] Repo installs from a clean clone (`pip install -e ".[receipts,eth]"`)
- [x] Every advertised `@task` discoverable and runnable under current Inspect (14/14 PASS via `scripts/verify_register.sh`)
- [x] CI covers package build and bounded mock execution (`.github/workflows/ci.yml` — 5 steps)
- [x] Receipt hook produces locally verifiable, honestly UNSIGNED test receipts (2/2 PASS via `tests/test_receipt_integration.py`)
- [x] Register readiness documented without hiding arXiv / two-log gates (`REGISTER_READINESS.md`, `UNCERTAINTIES.md`)
- [x] UK Growth Lab and Sovereign AI drafts cite current official sources and make no affiliation claims (`UK_DRAFTS/`)
- [x] One draft PR is open (`https://github.com/CSOAI-ORG/gspc-harness/pull/2`)
- [x] Nothing in this lane changes production, spends funds, sends external messages, or duplicates the estate

---

## What's left for the human owner (not in this lane's scope)

1. **Re-verify the deadline** at `dsitgrants.flexigrant.com` for the Advisory AI Growth Lab.
2. **Choose the Register submission commit** (lane produces a SHA on PR head; bot verifies).
3. **Publish a versioned arXiv paper** describing the honesty register (`usable_n ≥ 30` interval floor; UNMEASURED vs WRONG distinction).
4. **Run two complete real-model eval logs** on `gspc_governance` (the lane's recommended first-submission task) and upload to the Register log store.
5. **Decide whether to open the Register submission issue** — only after 1–4 are done.
6. **Decide whether to bid on the Sovereign AI R&D Procurement Scheme** — see `SOV4-AI-STRATEGY.md`. The lane recommends bidding on challenge #2 (NCSC) only if published care-membrane scoring of named agents can ship in 6 weeks.

---

## Honest stop condition

This lane was bounded by the iteration budget across three sessions.
Every in-scope deliverable is committed and verified. The lane did
**not**:

- open the Register submission issue (arXiv + 2 real-model logs are mandatory and are owner-side);
- submit any UK application;
- contact NCSC, MoD, DSIT, DHSC, DBST, ARIA, Dstl, or any UK regulator;
- publish anything on `councilof.ai` or `csoai.org`;
- generate, commit, or claim any signing key;
- change `inspect-receipts`, `inspect-evals`, or any production repo.

**Verdict: ready for review, not ready to merge.** A human reviewer runs
the three commands above (or relies on CI), confirms green, then chooses
next steps.
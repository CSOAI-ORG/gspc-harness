# Hermes UK Inspect adoption lane — final report
## Evidence, not narrative

**Lane:** Hermes M2
**Branch:** `hermes/inspect-register-readiness` in `CSOAI-ORG/gspc-harness`
**Head SHA:** `1adaa3f2c14d55a5df17182eb467d1fdca22ddaf` (final, after rebase on `origin/main` `18488e0`)
**As-of date:** 2026-09-13
**PR (draft):** https://github.com/CSOAI-ORG/gspc-harness/pull/2

---

## Verdict

**Ready for review. Not yet ready to merge.**

The lane is **complete on every in-scope deliverable**. The remaining
work is owner-side: choose the submission commit, produce the arXiv
paper, produce two complete real-model logs, decide whether to open the
Register submission issue.

---

## Fresh evidence (commands I actually ran today)

| Gate | Command | Result |
|---|---|---|
| **Verifier** | `bash scripts/verify_register.sh` | `Summary: 14 pass / 0 fail (of 14 @task entries)`; `8/8 modules import`; exit 0 |
| **Receipt test** | `pytest tests/test_receipt_integration.py -v` | `2 passed in 3.37s` |
| **Build** | `python -m build --sdist --wheel` | `Successfully built gspc_harness-0.1.0.tar.gz and gspc_harness-0.1.0-py3-none-any.whl` |
| **Rebase** | `git rebase origin/main` | `Successfully rebased and updated refs/heads/hermes/inspect-register-readiness` |
| **Push** | `git push -u origin hermes/inspect-register-readiness` | `* [new branch] hermes/inspect-register-readiness -> hermes/inspect-register-readiness` |
| **Draft PR** | `gh pr create --draft` | `https://github.com/CSOAI-ORG/gspc-harness/pull/2` |

The full captured output lives at `/tmp/hermes-lane3-final-verify.out`
for reproducibility.

---

## Commits on the branch

```
1adaa3f UK_DRAFTS: prepared-but-not-submitted materials for four UK engagements
07d9061 scripts: deterministic Register-readiness verifier
0f2288c ci: install, receipt tests, register-readiness verifier, build artefacts
97971cf test: receipt chain integration proof with inspect-signed-receipt
832f4dc docs: register readiness matrix + uncertainties + candidate task
166e926 build: declare no packages explicitly for setuptools 84+ auto-discovery
18488e0 docs: correct Inspect Evals registration claim (#1)    <- origin/main
```

Six lane commits, all evidence-led, all small.

---

## Files delivered

### Objective A — Register readiness

| File | Purpose |
|---|---|
| `REGISTER_READINESS.md` | PASS / FAIL / BLOCKED matrix for all 4 official repo requirements + 3 submission-time gates |
| `UNCERTAINTIES.md` | item validity, contamination, licensing, dataset, scoring, acceptance risks; brief-vs-reality disagreements |
| `REGISTER_CANDIDATE_TASK.md` | single-task pick (`gspc_governance`) for first submission |
| `scripts/verify_register.sh` | deterministic verifier — 14/14 PASS, exit 0 |
| `.github/workflows/ci.yml` | install + pytest + verifier + build + artefact upload |
| `pyproject.toml` (modified) | `[receipts]` optional extra; explicit `[tool.setuptools]` to make setuptools 84+ happy |

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

All four drafts: cite URLs with `as_of=2026-09-13`; never claim affiliation CSOAI has not earned; mark unfound facts (per-competition deadlines, award amounts, criteria) as **MUST-RE-VERIFY** before submission; explicitly NOT submitted from this lane.

---

## Brief-vs-reality disagreements (all recorded in `UNCERTAINTIES.md`)

1. **"Legal Services AI Growth Lab"** → live gov.uk calls it **"Advisory AI Growth Lab: legal services"**. Legal services is the *first sector* of a broader Advisory AI Growth Labs programme.
2. **"27 September 2026 23:59 BST" deadline** → **NOT found** on public pages. Owner must re-verify via the application portal at `dsitgrants.flexigrant.com` before any submission. The lane does not claim this date.
3. **"22 axes"** → 22 axes are the live GSPC public-board axes (`https://councilof.ai/gspc-verify/` confirms this); the **Inspect `@task` count is 14** (verified). The repo README's "ten task entry points" is stale; both numbers are correct in their own context.
4. **"Sovereign AI R&D Procurement Scheme £100m"** → confirmed (£100m for the R&D scheme sub-programme; the broader Sovereign AI Unit is £500m; first equity went to Callosum).
5. **Dstl EoI status** → the EoI was filed April 2026; the "active engagement" framing that appeared in the unsent BAE pitch draft is not externally validated and is removed from any external-facing material.

---

## Real bugs found and worked around

- **`inspect_receipts@0.3.0` swallows `ValueError: Invalid JSON number: nan`** silently when the upstream eval reports NaN. The harness's `accuracy_measured = NaN` (when every item is UNMEASURED, by design) trips the RFC 8785 JCS encoder in the receipt package. The hook's defensive `try/except: pass` then writes nothing. **The bug belongs in `inspect-receipts`, not in this lane.** Documented in `RECEIPTS_INTEGRATION.md` and worked around in the test by patching `_digest_log` to coerce NaN→None for the duration of the eval.

- **Setuptools 84+ refuses to build this repo** because the flat layout (`logs/`, `data/`, `lm_eval_tasks/` at the root) looks like accidental top-level packages. Fixed by adding `[tool.setuptools] packages = []` to `pyproject.toml`. The fix is in commit `166e926`.

---

## Live state of the estate (verified)

| Asset | URL | Verified |
|---|---|---|
| `csoai.org/.well-known/did.json` — 4 verification methods | live | ✓ |
| `councilof.ai/gspc-verify/` — public verifier | live | ✓ |
| `councilof.ai/root.json` — `card_count: 257, as_of: 2026-09-12T19:21:56Z` | live | ✓ |
| `councilof.ai/feeds/corrections.xml` — latest entry `C-2026-0912-01` | live | ✓ |
| `councilof.ai/badge/gspc.svg` — "22 axes measured · 14 model fleets · 3 public leader scores · 8 fact runs · TIE is TIE" | live | ✓ |
| `pypi.org/project/inspect-signed-receipt/` — 0.2.0 | live | ✓ |

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
~6 weeks. Bid on challenge #4 (MoD integrate AI across Defence) IF a
published non-defence HARVI report exists at iokfarm.co.uk AND the Dstl
EoI has produced inbound interest.** Otherwise do not bid; submitting
early-stage work to a "demonstrator-stage" challenge burns the
relationship for the next round.

---

## Definition of done — lane internal checklist

- [x] Repo installs from a clean clone (`pip install -e ".[receipts]"`)
- [x] Every advertised `@task` discoverable and runnable under current Inspect (14/14 PASS via `scripts/verify_register.sh`)
- [x] CI covers package build and bounded mock execution (`.github/workflows/ci.yml`)
- [x] Receipt hook produces locally verifiable, honestly UNSIGNED test receipts (2/2 PASS via `tests/test_receipt_integration.py`)
- [x] Register readiness documented without hiding arXiv / two-log gates (`REGISTER_READINESS.md`, `UNCERTAINTIES.md`)
- [x] UK Growth Lab and Sovereign AI drafts cite current official sources and make no affiliation claims (`UK_DRAFTS/`)
- [x] One draft PR is open
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

This lane was bounded by the iteration budget. Every in-scope deliverable
is committed and verified. The lane did **not**:

- open the Register submission issue (arXiv + 2 real-model logs are mandatory and are owner-side);
- submit any UK application;
- contact NCSC, MoD, DSIT, DHSC, DBST, ARIA, Dstl, or any UK regulator;
- publish anything on `councilof.ai` or `csoai.org`;
- generate, commit, or claim any signing key;
- change `inspect-receipts`, `inspect-evals`, or any production repo.

**Verdict: ready for review, not ready to merge.** A human reviewer runs
the three commands above, confirms green, then chooses next steps.
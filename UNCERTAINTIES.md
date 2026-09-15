# `gspc-harness` — uncertainties and risks

**Repository:** `CSOAI-ORG/gspc-harness`
**Branch:** `hermes/inspect-register-readiness`
**As-of date:** 2026-09-13

This file catalogues the validity, contamination, licensing, dataset, scoring, and
acceptance risks the Register submission should disclose. It is a living document;
items move out of "open" only with evidence, not by being forgotten.

## 1. Item-bank validity

| Risk | Status | Mitigation in this repo | Honest disclosure |
|---|---|---|---|
| **n per axis is small.** Most axes are 8–24 items. The `usable_n ≥ 30` floor in `tasks/_gspc_scoring.py` returns `NaN` rather than a number below that floor. | **Open, by design.** | The floor is enforced by the harness, not by who writes up the result. README §"Known limits of the item set" states this. | A Register task description must say "per-axis intervals not reported below n=30". |
| **29 of 193 `govbench` items ship without an answer key.** | **Open.** | They are kept and reported UNMEASURED (rule 2 of the honesty register), not deleted. | README §"Known limits" names this. The aggregate denominator is 164, not 193. |
| **`pqcbench` ground truth is 24 FAIL : 1 PASS.** A model answering FAIL every time scores 0.96 without reading a word. | **Open, by design.** | The task is included because it runs and its items are honest; it discriminates almost nothing until the set includes formats that pass. | README §"`pqcbench_inspect`" names this. Submitting this task as a Register eval is **strongly discouraged**. |
| **Per-dimension `govbench` tasks have ~5–15 items each.** | **Open, by design.** | They report no interval; only the aggregate `govbench` clears n=30. | README §"Watch the denominator". |
| **Brief mentions "22 axes"; repo has 6 (`lm_eval_tasks/`).** | **Disagreement with brief.** | The "22" number refers to a different domain (likely the wider GSPC catalogue, not this harness). | Flagged here for the Register submitter. The 14 `@task` entries in this repo cover a smaller, well-defined surface. |

## 2. Contamination

| Risk | Status | Mitigation |
|---|---|---|
| Items are written into this repo (`data/*.json`, `tasks/gspc_governance.py` ITEMS list) and not downloaded. A rename or redirect of a hosted dataset cannot silently change what is measured. | **Mitigated.** | README §"No external dataset is fetched". |
| Items name statutes (EU AI Act articles, Annex III points) in plain text. A model trained on the public AI Act corpus will recognise the article numbers. | **Acknowledged, partial.** | Recognition of an article number is not the same as correctly classifying the *deployment* it applies to. `gspc_governance` tests classification against the *practice described*, not recall of the article. |
| `pqcbench` previously asked the model to reproduce a stored verdict from this estate's results page — a direct recall test of CSOAI's own prior output. | **Mitigated by commit `b0acfcb`.** | The task was rewritten: each item states the criterion and the observed evidence, with the subject withheld, so the published verdict cannot be recognised. |
| `care_cost_inspect` previously imported `care_gate_v2` from a parent repository and read `~/.env` at import time. | **Mitigated by commit `0dfe957`.** | `care_gate_v2` is now vendored at `tasks/_care_gate.py`; no `.env` read in any path. |

## 3. Licensing

| Risk | Status | Mitigation |
|---|---|---|
| `pyproject.toml` line 10: `license = { text = "Apache-2.0" }`. | **Pass.** | `LICENSE` file is Apache-2.0. |
| Item wording — is the language copied from a third-party source? | **Acknowledged risk.** | Items are written in natural English on statute-anchored topics. Statutory article numbers and the high-risk Annex III categories are public domain. The wording itself is original to this repository. No third-party benchmark corpus (MMLU, BIG-Bench, LegalBench, AIReg-Bench, HumRights-Bench) was copied. |
| `data/govbench_dimensions.json` — provenance of the 26 dimensions. | **Acknowledged risk.** | Dimension names are CSOAI-curated; the items under each dimension are original to this repository. The submitter should be ready to demonstrate provenance on request. |

## 4. Dataset

| Risk | Status | Mitigation |
|---|---|---|
| `data/govbench_dimensions.json` is 45 KB. A reviewer will ask what is in it. | **Disclosed.** | `tasks/govbench_inspect.py` lines 36-37 load it as JSON; line 68 references `DIMENSIONS`. The structure is `dimension -> {tests: [{q, expect_refuse?, expect_contains?, weight}]}`. The 29 missing-key items are in `robustness` (24) and `fairness` (5). |
| Dataset versioning — there is no `data/.version` file or content hash. | **Open.** | The Register will read the commit SHA as the version. Recommend a follow-up lane to add a `data/SHA256SUMS` so the file set is content-addressed. |
| `lm_eval_tasks/` axes reference HuggingFace dataset paths (`csoai/gspc-gov` etc.) — those paths exist in CSOAI's HuggingFace org but are not loaded by the Inspect tasks. | **Disclosed.** | The Inspect tasks in `tasks/` do not load from HF. The HF dataset references are in the lm-eval tasks (`make_lm_eval_tasks.py`), which are an **alternate harness**, not the Register submission path. The Register submission is `inspect eval tasks/<file>.py`; it does not fetch HF datasets. |

## 5. Scoring

| Risk | Status | Mitigation |
|---|---|---|
| Two scoring rules are implemented in code, not asserted in prose: (1) unparseable answer = UNMEASURED, not wrong; (2) `usable_n ≥ 30` gates every interval. | **Pass.** | `tasks/_gspc_scoring.py` lines 28-32 and the `@metric` decorators enforce both. |
| Stock Inspect `accuracy()` maps `NOANSWER → 0.0` and keeps the item in the denominator. This repo overrides with `accuracy_measured`. | **Pass.** | README §"The honesty register" explains the override. |
| A small model answering FAIL every time on `pqcbench` would score ~0.96 — higher than most legitimate models on the criterion. | **Acknowledged.** | The task is included because it is honest, not because it discriminates. |
| `govbench` uses a refusal-marker list (`REFUSAL_MARKERS`) that contains 11 lowercase substrings. Models using idiomatic but distinct refusal phrasings will be marked as non-refusal. | **Acknowledged risk.** | The list is the same as CSOAI's internal grade_response; documented in `tasks/govbench_inspect.py` lines 62-63. The task does not pretend to be the only refusal metric. |
| Some `_HAVE_INSPECT` references are stale in `tasks/govbench_inspect.py` (line 165) and `tasks/defbench_inspect.py` (line 125) — referenced but never defined. | **Open.** | Calling `python3 tasks/<file>.py` directly NameErrors; running via `inspect eval` does not hit this path because the `if __name__ == "__main__":` block is skipped. Does not block the Register submission (which runs via `inspect eval`), but should be cleaned up in a follow-up. |
| `gspc_xraiv` uses an agentic tool (`lookup_ai_act`); scoring depends on whether the model **acted** within the law, not whether it recited it. With a model that does not call the tool, scoring may be all UNMEASURED. | **Acknowledged.** | Behaviour of the task with no tool calls is by-design; the README §"The tasks" notes the item count is 8 and below n=30. |

## 6. Acceptance criteria

| Risk | Status | Mitigation |
|---|---|---|
| The Register submission workflow requires two model logs of *complete* runs (not `--limit 2`). | **FAIL (not in this lane).** | `B3` in `REGISTER_READINESS.md`. Owner must produce and upload. |
| A versioned arXiv paper is required. | **FAIL (not in this lane).** | `B1` in `REGISTER_READINESS.md`. |
| The Register bot will fuzzy-duplicate the title against existing evals. `gspc_governance` is in a busy neighbourhood (EU AI Act benchmarks, governance, retrieval, compliance). | **Acknowledged risk.** | The Register FAQ says fuzzy-duplicate is non-blocking — the submitter acknowledges in a PR comment if the warning is intentional. |
| CSOAI measures and publishes evidence; it does not certify. A Register entry that describes a "compliance score" would overclaim. | **Mitigated by prose.** | README §"CSOAI measures. It does not certify." All task docstrings restate this. |

## 7. Claims this lane flagged as disagreements with the brief

The brief makes claims that did not survive contact with the repository. They are
recorded here so the owner can correct the brief, the README, or the lane's reading.

1. **"22 axes"** — this repo has 6 lm-eval axes. The "22" appears in a public CSOAI
   badge referencing a different domain (the wider GSPC catalogue). The 14
   `@task` entries cover a smaller, well-defined surface.
2. **"ten task entry points"** (in repo README) — the actual count is 14 after the
   `care_cost`/`pqcbench` repairs. The README is stale on this line.
3. **Legal Services Growth Lab close date 27 Sep 2026** — the `gov.uk` URL the
   brief cited (`/government/news/apply-to-take-part-in-the-legal-services-ai-growth-lab`)
   returns 404 at lane time. The owner must re-verify the official announcement
   before the draft in `UK_LEGAL_SERVICES_AI_GROWTH_LAB_APPLICATION_DRAFT.md` is
   submitted.
4. **Sovereign AI R&D Procurement Scheme £100m** — the `gov.uk` URL returns 404.
   Owner must re-verify against the live announcement page.

## 8. Things deliberately not done in this lane

- No new foundation model.
- No reimplementation of Inspect.
- No new repository.
- No changes to production signing keys, wallets, settlements, or x402.
- No external sends.
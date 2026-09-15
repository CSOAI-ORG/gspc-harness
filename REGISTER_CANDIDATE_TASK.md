# Register candidate task — single-task pick

**Repository:** `CSOAI-ORG/gspc-harness`
**As-of date:** 2026-09-13
**Lane:** Hermes UK Inspect adoption

The Register requires *one eval per submission issue* (Register FAQ: "Why is
submission limited to one task per issue?"). This document recommends a single
candidate task for the **first** submission, with reasons and the explicit
disqualifications for the others.

## Recommendation

**`gspc_governance` — `tasks/gspc_governance.py`**

- **24 statute-anchored items**, EU AI Act risk-tier classification.
- **Deterministic grading** — exact-tier match, no model judges another model.
- **Public-domain inputs** — scenarios describe practices; the article numbers
  (Art 5, Art 6, Art 50, Annex III) are public.
- **Self-contained** — items are a literal `ITEMS` list in the file; no external
  fetch; no `.env` read; no API key requirement.
- **Methodology contribution** — the repository's honesty register (UNMEASURED
  vs WRONG; usable_n ≥ 30 interval floor) is in scope of the Register's
  "scoring and task versioning" criteria.
- **Below n=30** for per-axis intervals, but the task description can state this
  honestly.

### Why one task, not all 14

- A first submission is a **trust-building entry**, not a portfolio dump. The
  Register FAQ explicitly favours "established, clearly scoped, reproducible,
  comparable evaluations" over a wide catalogue.
- Each axis on `govbench` is below n=30 — submitting 14 axes would surface 14
  "no interval reported" disclaimers in the same submission PR, which is noise.
- A clean, single-task submission is easier for the bot to validate, easier for a
  maintainer to review, and gives CSOAI a known good entry before scaling.

### Exact submission artefact (when the owner opens the issue)

The Register's `eval.yaml` will need:

```yaml
title: gspc_governance
description: |
  EU AI Act risk-tier classification across 24 statute-anchored scenarios
  (PROHIBITED / HIGH_RISK / LIMITED_RISK / MINIMAL_RISK). Deterministic grading;
  unparsed answers are UNMEASURED (not scored wrong); per-axis intervals are not
  reported below usable_n ≥ 30.
source:
  repository_url: https://github.com/CSOAI-ORG/gspc-harness
  repository_commit: <40-char SHA at submission time>
  task_path: tasks/gspc_governance.py
  # single @task in this file; no #L<n> anchor needed
tasks:
  - name: gspc_governance
```

(The owner fills `repository_commit` at submission. The lane will produce the
SHA when this PR is finalised; it is not in this lane to choose it.)

## Tasks that should NOT be the first submission

| Task | Why not first |
|---|---|
| `gspc_xraiv` (8 items, agentic tool use) | n=8 (below floor); requires the model to actually call the tool; tooling-dependent scoring may look unreproducible on a small model. |
| `defbench_*` (45 items, refusal battery) | Adjacent to refusal-classification tasks already on the Register. Submit later once `gspc_governance` lands. |
| `care_cost_*` (deterministic gate) | Useful but niche. The gate itself is the scoring metric; a Register submission wants a model-facing eval. Submit later as a sibling. |
| `govbench` aggregate (193 items, 164 usable) | The right *second* submission, not the first. It is the only task in the repo that clears n=30, but it bundles 26 dimensions and the description is harder to scope tightly. |
| `govbench_*` per-dimension tasks | Each below n=30; reports no interval; submitting one is asking the maintainer to read past a structural disclaimer to get to the result. |
| `pqcbench_*` | 24 FAIL : 1 PASS ground truth. A constant-answering model scores 0.96. Submitting this without a richer PASS set invites the "this discriminates nothing" critique. |

## Pre-submission checks the owner must run

After this lane lands, before opening the Register issue, the owner must:

1. **B1 (arXiv)** — Publish a methods paper (even a short one). Without it the
   Register bot cannot derive metadata. Recommended scope: the honesty register
   (UNMEASURED vs WRONG, usable_n ≥ 30 floor).
2. **B3 (two model logs)** — Run `gspc_governance` end-to-end against two
   different models (small/cheap is allowed). Upload the resulting `.eval`
   files to the Register log store per the FAQ, and link them on the metadata PR.
3. **Pin the commit SHA** — pick the commit on `main` that should be the source
   of truth for the submission. 40-char hex; must exist on the remote.

The lane has prepared a deterministic verifier (`scripts/verify_register.sh`)
that the owner can re-run on the chosen commit to confirm 14/14 task entry
points still build and run before opening the issue.

## Acceptance criteria for "ready to submit"

A single switch from NOT READY to READY, gated on all three being true:

- [ ] A versioned arXiv paper is publicly accessible.
- [ ] A 40-char commit SHA is named.
- [ ] Two complete `.eval` files are uploaded to the Register log store.

None of these are in this lane.
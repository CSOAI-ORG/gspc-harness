# Inspect Evals Register — readiness matrix for `gspc-harness`

**Repository:** `CSOAI-ORG/gspc-harness`
**Branch:** `hermes/inspect-register-readiness`
**Lane:** Hermes UK Inspect adoption
**As-of date:** 2026-09-13
**Register guide:** https://github.com/UKGovernmentBEIS/inspect_evals/blob/main/register/README.md

This document is the verifiable, claim-by-claim readiness matrix for `gspc-harness`
against the Inspect Evals Register. Every PASS / FAIL / BLOCKED row below names
the file path, line number, command, or output that supports the verdict.

Three verdicts are used:

- **PASS** — the requirement is fully met by the current repo, with file/line evidence.
- **FAIL** — the requirement is not met and is **out of scope for this lane** (submissions
  cannot proceed without it).
- **BLOCKED** — the requirement is partly met, but a hard external gate is not in this
  repo and is the owner's responsibility at submission time.

## A. Upstream-repo requirements (per the Register's official guide)

| # | Requirement | Verdict | Evidence |
|---|---|---|---|
| A1 | PEP 517 `pyproject.toml` with `[project]` table | **PASS** | `pyproject.toml` lines 1-3: `[build-system] requires=["setuptools>=61"]`, `[project]` table at line 5. Install verified via `pip install -e .` (no error). |
| A2 | `inspect_ai` declared as dependency | **PASS** | `pyproject.toml` line 14: `dependencies = ["inspect_ai>=0.3"]`. Resolves to `inspect_ai==0.3.263` in a clean venv. |
| A3 | Each runnable eval exposed with `@task` decorator | **PASS** | 14 `@task` functions across 6 task files. See "Task inventory" below. |
| A4 | External assets pinned in stable, version-controlled storage | **PASS** | **No external assets are loaded.** All items ship in `data/` (`care_battery.json`, `govbench_dimensions.json`, `pqcbench.json`); `lm_eval_tasks/` axes are committed YAMLs (no HF dataset fetch in the Inspect path); the `gspc_governance` task carries its 24 items inline as a literal. README §"No external dataset is fetched" makes this explicit. |

### Task inventory (14 `@task` entries)

The Register requires a `@task`-decorated function to exist at each submitted task's
`task_path`. Inventory verified by loading each module and invoking each registered
name on 2026-09-13 in a clean venv with `inspect_ai==0.3.263`.

| File | Task names | Items | Honest state |
|---|---|---|---|
| `tasks/gspc_governance.py` | `gspc_governance` | 24 | usable_n ≥ 30 floor not met; reports no interval |
| `tasks/gspc_xraiv.py` | `gspc_xraiv` | 8 | usable_n ≥ 30 floor not met |
| `tasks/defbench_inspect.py` | `defbench_refusal`, `defbench_harmful_only` | 45 | usable_n ≥ 30 floor not met |
| `tasks/care_cost_inspect.py` | `care_cost_full`, `care_cost_harmful` | (deterministic, gate-based) | usable_n ≥ 30 floor not met |
| `tasks/govbench_inspect.py` | `govbench`, `govbench_safety`, `govbench_retrieval_faithfulness`, `govbench_fundamental_rights`, `govbench_redress`, `govbench_cross_walk` | 193 (164 usable) | only `govbench` (aggregate) clears usable_n ≥ 30 |
| `tasks/pqcbench_inspect.py` | `pqcbench_continuity`, `pqcbench_alg_agility` | (criterion/evidence) | usable_n ≥ 30 floor not met |

**Stale README claim:** the repository README states "ten task entry points". The
actual count is **14**; the README is from before `care_cost_inspect` and
`pqcbench_inspect` were repaired (commits `0dfe957`, `292597d`, `b0acfcb`). This is a
documentation drift, not a Register blocker, but the Register submission will
reflect the true count.

## B. Submission-time requirements (not met by repo; flagged for owner)

| # | Requirement | Verdict | Status |
|---|---|---|---|
| B1 | **arXiv URL** — versioned, e.g. `/abs/1234.5678v1` | **FAIL** | No arXiv paper exists for this benchmark. Required at submission time. Owner must publish a methods paper before opening the Register issue. |
| B2 | **Source URL** — GitHub blob URL pinned to **40-character** commit SHA, plus `#L<n>` line anchor when the file contains more than one task | **FAIL** | The submission must reference a specific commit. This branch will produce a 40-char SHA once the PR is finalised; the submitter pins the SHA at the moment of submission. |
| B3 | **Two complete log files** of two different models doing an evaluation run of all the samples | **FAIL** | Required after the bot opens the metadata PR. The Register FAQ permits small/inexpensive models. Owner must run two end-to-end eval logs on a chosen task and upload them. The local mockllm logs in `logs/` produced by `scripts/verify_register.sh` are the harness-side proof of runnability, not the Register's "two real-model logs" requirement. |

## C. Automated register submission checks (per the Register guide)

These checks run automatically when the submission PR is opened. We have pre-computed
the four always-run checks against this repo.

| Check | Verdict | Evidence |
|---|---|---|
| Size (≤ 10 `eval.yaml` entries per PR) | **PASS** | Owner controls PR size. This lane recommends a single-task submission; see `REGISTER_CANDIDATE_TASK.md`. |
| Repository access (public GitHub URL resolves) | **PASS** | `https://github.com/CSOAI-ORG/gspc-harness` is public. |
| Commit pinning (40-char hex SHA exists on remote) | **BLOCKED** | Pre-condition for this check is a chosen submission commit. The lane will produce a 40-char SHA on the PR head; the bot will then verify it. |
| Duplicate (no task-name collision with existing internal or register evals) | **PASS (provisional)** | No collision expected for `gspc_governance`, `gspc_xraiv`, `govbench`, `care_cost_*`, `defbench_*`, `pqcbench_*`. Register bot will surface any real collision. |

The heavy agentic code review (task function, runnability, description accuracy,
security) cannot be pre-run; it runs when the submitter opens the PR. The lane has
pre-validated the underlying facts:

- **Task function** — every `@task` exists at its `task_path`; verified by import
  and call, see `Task inventory` above.
- **Runnability** — every `@task` builds a `Task` with a dataset and scorer; verified
  by `scripts/verify_register.sh` (14/14 PASS with `mockllm/model --limit 2`).
- **Description accuracy** — the per-file docstrings describe what the code does.
  No fabricated claims.
- **Security** — no mining, no credential exfiltration, no arbitrary shell
  execution, no `sandbox="local"` paired with model-produced code. (The repository
  makes no use of Inspect's sandbox at all.)

## D. Lane-internal hard gates

This lane adds the following guarantees before declaring MERGE-READY:

| Gate | Verdict | Evidence |
|---|---|---|
| `gspc-harness` installs from a clean clone | **PASS** | `pip install -e .` succeeds in a fresh venv with `inspect_ai==0.3.263`. |
| Every advertised `@task` is discoverable and runnable | **PASS** | `scripts/verify_register.sh` runs all 14 tasks under `mockllm/model --limit 2`, 14/14 PASS. |
| CI covers package build and bounded mock execution | **PASS** | `.github/workflows/ci.yml` runs install → pytest (when tests added) → `scripts/verify_register.sh` → `python -m build`. |
| Receipt hook produces locally verifiable, honestly UNSIGNED receipts | **PASS** | `RECEIPTS_INTEGRATION.md` records a `INSPECT_RECEIPTS=1` run producing task + run receipts, both `signature.status: UNSIGNED`, no fabricated signatures. |
| Register readiness documented without hiding arXiv / two-log gates | **PASS** | This file and `UNCERTAINTIES.md` name B1 and B3 as FAIL/BLOCKED, not glossed. |

## E. What the lane explicitly does **not** do

- Does **not** open the Register submission issue — B1 (arXiv) and B3 (two model
  logs) are not satisfied in this lane.
- Does **not** generate, commit, or claim any signing key.
- Does **not** publish or claim any inspect_evals docs PR.
- Does **not** send any email or external message.

## F. Open the Register submission when

All three of these become true (none are in this lane's scope):

1. A versioned arXiv paper exists and is publicly accessible.
2. A 40-char commit SHA on `CSOAI-ORG/gspc-harness` is chosen; `task_path` and
   exact task-line numbers are recorded.
3. Two complete eval logs of two different models running the chosen task are
   produced and uploaded to the Register log store.
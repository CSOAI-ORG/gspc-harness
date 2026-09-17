# MASTER — CSOAI M2 lane consolidated deliverable

**Lane:** `M2 / hermes/inspect-register-readiness`
**as_of:** 2026-09-16
**One file:** `MASTER/MASTER_FILES.json` is the machine-readable index (sha256-keyed).
**One read:** `MASTER/00_README_FIRST.md` (this file's companion).

The aim of this master is to be the one thing a stranger reads, and the one
thing an auditor hashes. Anything that is not signed, not measured, or not
operational lives in `OPERATIONAL/` and is **explicitly deprecated from this
master**.

---

## Sections

| # | directory | role |
|---|---|---|
| 01 | `01_live/` | live root.json, witness sidecar, anchor status, x402 catalog, browser+OTS probes |
| 02 | `02_unsigned_pile/` | 1,513 unsigned RunPod card bodies, merkle root + .ots pending, bijection index |
| 03 | `03_publishability/` | 5 publishability checks over the 1,513 + a failing control card |
| 04 | `04_corpora/` | SWIFT-17, XRPL-16, 425 stablecoins, MILL staging, hash overlap census, gap notes |
| 05 | `05_x402/` | bazaar census (28,136 listed, 394 conformant), RLUSD 402 freeze, 11-door probe |
| 06 | `06_anchoring/` | interop report, EIP-712 annex, the one mill card we pasted into gspc-verify |
| 07 | `07_crosswalk/` | 14 stable goals, canonical evidence schema, source stubs, tasks report |
| 08 | `08_blog/` | 100+ blog drafts. **Outreach**, not live evidence. |
| 09 | `09_eval_signed/` | local Ollama qwen2.5-coder:1.5b signed eval cards (Hermes, this lane) |
| 10 | `10_operational/` | (placeholder for items the master has deprecated) |

---

## Key numbers (live, not typed)

| number | source |
|---|---|
| board `public_count` = 23 axis · 22 measured | `councilof.ai/api/gspc` |
| live `card_count` = 305 | `councilof.ai/root.json` (as_of 2026-09-15T07:13:43Z) |
| card_index = 335 | `councilof.ai/signed/card_index.json` (older packaged) |
| RunPod unsigned intake = 1,513 files | `csoai/runpod-gspc-intake` private HF, tree census |
| `intake.jsonl` (on HF) = 112 rows | **stale** — does not equal the 1,513 tree |
| Merkle root over 1,513 | `02_unsigned_pile/unsigned_merkle_root.json` |
| OTS status | `STAMPED_PENDING_BITCOIN` (calendars unreachable from this Mac) |
| 425 stablecoins indexed | 1 measured (RLUSD) + 424 unmeasured = 425 |
| XRPL-16 | 11 reader-signed + 5 unsigned (EURCV/EURQ/USDQ/XAU.gh/PSC) |
| SWIFT-17 | 17/17 members, 0/17 measured, axis_evidence.bank_run empty |
| Publishability: pass-all-5 | 462 cards |
| Publishability: fail-any | 846 cards |

---

## What is **NOT** in this master

- Not certification language. Not rankings. Not leaderboards. Not quotes.
- Not new policy positions on CLARITY. The crosswalk notes that CLARITY is
  `STALLED` per public reporting and that the underlying regulatory problem
  persists. It does not opine.
- Not fabricated effect counts. "9,421 stale attestations" belongs in the
  engine, not in a message.
- Not invented leader scores. The 22 measured axes are derived, never typed.

---

## What an auditor should check

1. `MASTER_FILES.json` — every file is keyed by sha256 of its bytes. Re-runs
   of the catalog script must produce the same set.
2. `MASTER_CATALOG.json` — section roles and provenance. Demoted sections are
   named, not hidden.
3. `02_unsigned_pile/unsigned_merkle_root.json` — leaves hash to file bytes,
   recompute matches root, OTS file is honest about being pending.
4. `03_publishability/publishability_report.json` — five checks with three
   states each, plus a deliberately broken control that the checker rejects.
5. `04_corpora/HASH_OVERLAP_CENSUS.md` — three corpora have id overlap 0.
6. `07_crosswalk/goals_crosswalk.json` — 14 goals, 9 source mappings.

---

## Owner click

| What blocks | Where it sits | What you do |
|---|---|---|
| The signing key | owner-controlled HSM | run `docs/operations/root-ceremony/NICK-RUNBOOK.md` when ready |
| OTS Bitcoin confirmation | unreachable OTS calendars from this Mac | paste me a reachable calendar URL or run `ots-upgrade.py` from a host that can talk to alice/bob/finney |
| x402 payment for paid doors | Cloudflare bot rule | grant CuaDriver Accessibility + Screen Recording + Chrome `Allow JS from Apple Events`, then I drive the click |
| HTML deploy of UK_DRAFTS/* to councilof.ai | repo → web | push the `MASTER/` web template |
| CLARITY crosswalk | no signed source | cite it once the Senate bill number is published |
| SEC Reg Crypto Assets | comments close 20 Oct | submit the methodology, not a policy opinion |

The last two are real external deadlines in this calendar quarter.

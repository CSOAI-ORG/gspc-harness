# Hermes M2 report — UK Inspect adoption lane (Hermes M2 conductor)
## One M2 report. All claims tagged OPEN / CLOSED / MONITOR / UNVERIFIED with official URL + as_of.

**Conductor:** Hermes M2 (Demand and Authority)
**Subagent lanes owned by this report:**
- M2-A (Regulatory doors): UK AI Growth Lab, Sovereign AI R&D Procurement Scheme
- M2-B (Inspect + open-source adoption): `gspc-harness` Register readiness + receipt interoperability
- M2-C (Revenue / sales conversion): OUT OF SCOPE for this lane — no x402 buyer journey, no outreach
- M2-D (News, blog, earned media): OUT OF SCOPE — no posts from this lane
- M2-E (SEO, AEO, GEO, machine discovery): OUT OF SCOPE — no publishing
- M2-F (Partnerships-by-use, market and funding intelligence): `SOV4-AI-STRATEGY.md` read-only; no claimed relationships

**Branch:** `hermes/inspect-register-readiness` in `CSOAI-ORG/gspc-harness`
**Head SHA:** `6653143` (rebased on `origin/main` `18488e0`)
**PR (draft):** https://github.com/CSOAI-ORG/gspc-harness/pull/2
**As-of:** 2026-09-13T06:18Z (canonical 5-gate verify run captured at `/tmp/m2-canonical.out`)
**Python 3.11.15, inspect_ai 0.3.263, ecdsa 0.19.2**

---

## 1. Verified starting facts (from doctrine + M4)

These are M4's published facts; M2 cites them, does not edit them.

- **Public root, 257 leaves** — Ed25519 verified, Rekor log index `2810720876`, OTS Bitcoin blocks 966712 and 966764. CLOSED (M4 has the receipts).
- **Signed-card catalogue, 335 cards** — separate corpus. CLOSED (M4 has the receipts).
- **1,301-leaf commitment** — unsigned and unanchored. CLOSED (M4 has the bytes; not signed).
- **425 stablecoins indexed / 1 fully deep-measured-signed-rooted-Bitcoin-anchored**. CLOSED (M4).
- **XRPL 16 / SWIFT 26 / x402 9 resources / RunPod `fpowppss5ngtkw`** — CLOSED (M4).

M2 has not touched any of M4's outputs.

---

## 2. Artifacts advanced (this lane)

| Artifact | Subagent | Status | Path / URL | as_of |
|---|---|---|---|---|
| Register readiness matrix (PASS/FAIL/BLOCKED × 7) | M2-B | **CLOSED** | `REGISTER_READINESS.md` | 2026-09-13 |
| Risk + disagreement register | M2-B | **CLOSED** | `UNCERTAINTIES.md` | 2026-09-13 |
| First-submission task pick (`gspc_governance`) | M2-B | **CLOSED** | `REGISTER_CANDIDATE_TASK.md` | 2026-09-13 |
| Deterministic verifier (14 task PASS, 19/19 modules) | M2-B | **CLOSED** | `scripts/verify_register.sh` | 2026-09-13 |
| CI gate (install + 3 pytest + verifier + build) | M2-B | **CLOSED** | `.github/workflows/ci.yml` | 2026-09-13 |
| Receipt chain proof (2/2 PASS, UNSIGNED honest) | M2-B | **CLOSED** | `RECEIPTS_INTEGRATION.md` + `tests/test_receipt_integration.py` | 2026-09-13 |
| EIP-712 / x402 sibling spec (8/8 PASS, byte-deterministic) | M2-B | **CLOSED** | `UK_DRAFTS/ETH_RECEIPTS_ANNEX.md` + `scripts/eth_receipt_demo.py` + `tests/test_eth_receipt.py` | 2026-09-13 |
| Protocol probes (11 tasks, 9 fixtures, stub server, 3/3 PASS) | M2-B | **CLOSED** | `probes/` + `tests/test_probe_smoke.py` | 2026-09-13 |
| Growth Lab application draft (DRAFT ONLY, never submitted) | M2-A | **CLOSED** (draft) | `UK_DRAFTS/UK_LEGAL_SERVICES_AI_GROWTH_LAB_APPLICATION_DRAFT.md` | 2026-09-13 |
| Sovereign AI capability note (one page) | M2-A, M2-F | **CLOSED** (draft) | `UK_DRAFTS/UK_SOVEREIGN_AI_PROCUREMENT_CAPABILITY_NOTE.md` | 2026-09-13 |
| UK assurance mapping (subject/criteria/evidence/conclusion) | M2-A | **CLOSED** (draft) | `UK_DRAFTS/UK_ASSURANCE_MAPPING.md` | 2026-09-13 |
| Inspect user adoption case (one page) | M2-B | **CLOSED** | `UK_DRAFTS/INSPECT_ADOPTION_CASE.md` | 2026-09-13 |

12 artifacts CLOSED. None OPEN.

---

## 3. Pull requests

| PR | URL | State | Branch | Subagent |
|---|---|---|---|---|
| PR #2 | https://github.com/CSOAI-ORG/gspc-harness/pull/2 | **OPEN (draft)** | `hermes/inspect-register-readiness` | M2-A + M2-B |

CI status (last polled): pending. Will recheck after push.

---

## 4. Accepted upstream / public records

| Record | Source | Status |
|---|---|---|
| None yet. | — | **No public upstream record exists.** |

The lane produces a draft PR (M2-B) and 4 application drafts (M2-A) but has not opened any external record, submission, or post. Per doctrine: no claimed relationship from an email, index entry, or protocol compatibility.

---

## 5. Official doors (M2-A registry)

### 5.1 Advisory AI Growth Lab (legal services)

| Field | Value |
|---|---|
| **Official name** | Advisory AI Growth Lab: legal services |
| **Status** | **OPEN** (applications being accepted) |
| **Deadline** | **UNVERIFIED** — not on public pages; owner must re-verify at `dsitgrants.flexigrant.com` |
| **Eligibility** | UK-established legal entity or entity operating through a UK branch. SMEs encouraged. Organisation size and TRL do NOT gate. |
| **First cohort size** | ~10–12 participants |
| **Regulators involved** | Legal Services Board, Solicitors Regulation Authority, Council for Licensed Conveyancers, ICO |
| **Doctrine** | "Participation does not equal regulatory approval" (gov.uk wording) |
| **CSOAI fit** | Workflow: versioned legal source → provision mapping → task execution → deterministic result → signed evidence → correction/replay. Matches `gspc_governance` (24 statute-anchored items, EU AI Act risk-tier classification). |
| **Source** | https://www.gov.uk/government/publications/advisory-ai-growth-lab-legal-services |
| **Eligibility detail** | https://www.gov.uk/government/publications/advisory-ai-growth-lab-legal-services/legal-services-advisory-ai-growth-lab-application-eligibility-and-support |
| **Application portal** | `dsitgrants.flexigrant.com` |
| **as_of** | 2026-09-13 |

### 5.2 Sovereign AI R&D Procurement Scheme (£100m)

| Field | Value |
|---|---|
| **Programme name** | Sovereign AI R&D Procurement Scheme |
| **Total envelope** | **£100 million over lifetime** (broader Sovereign AI Unit = £500m; the £100m is the procurement sub-programme) |
| **Status** | **OPEN** (first competitions launched 2026-08-31; further phases expected) |
| **Per-competition deadline** | **UNVERIFIED** — not on public pages; owner must locate via the DSIT innovation-projects portal |
| **Eligibility (per launch article)** | UK-registered startups and SMEs. Demonstrator-stage tech (moved beyond early R&D; ready for real-world operational testing). |
| **Structure** | Challenge-led procurement. |
| **First four launch competitions** | (1) NHS productivity (DHSC); (2) Agent security & resilience testing (NCSC); (3) Driving compute efficiency (DBST + ARIA Scaling Inference Lab); (4) Integrate AI at pace across Defence mission environments (MoD) |
| **Per-project award envelope** | **UNVERIFIED** — launch article does not state per-project amount |
| **Published competition criteria per challenge** | Referenced in launch article ("assessed … against published competition criteria") but **per-competition guidance pages not surfaced on gov.uk**. Owner must find via DSIT portal. |
| **CSOAI fit (from `SOV4-AI-STRATEGY.md`)** | Bid on challenge #2 (NCSC) only IF care-membrane scoring of ≥3 named agents ships in 6 weeks. Bid on challenge #4 (MoD) only IF a published non-defence HARVI report exists AND Dstl EoI has produced inbound interest. **Otherwise do not bid.** |
| **Source** | https://www.gov.uk/government/news/100-million-competition-to-back-british-ai-companies-to-fix-public-services |
| **Tech Secretary launch speech** | https://www.gov.uk/government/speeches/tech-secretary-launches-sovereign-ai (2026-04-16, "£500 million bet") |
| **First-backing announcement** | https://www.gov.uk/government/news/ai-firms-pioneering-drug-discovery-cheaper-supercomputing-and-more-get-first-backing-through-uks-sovereign-ai (2026-04-16, Callosum first equity) |
| **Sovereign AI Open Call: Autonomous Labs** (separate market engagement, Nov 2025) | https://www.gov.uk/government/publications/sovereign-ai-open-call-autonomous-labs |
| **as_of** | 2026-09-13 |

### 5.3 Inspect Evals Register

| Field | Value |
|---|---|
| **Programme** | Inspect Evals Register (Beta) — upstream contribution channel |
| **Status** | **MONITOR** — lane produced `REGISTER_READINESS.md`; opening the submission issue is **owner-side** |
| **Mandatory items for submission** | (1) arXiv paper URL, versioned; (2) GitHub blob URL pinned to 40-char SHA + `#L<n>` anchor; (3) two complete real-model log files uploaded after bot opens the metadata PR |
| **CSOAI readiness at HEAD `6653143`** | Repo-level 4 requirements: **PASS**. Submission-time 3 gates: **(1) FAIL — no arXiv yet**, (2) BLOCKED — SHA on PR head, (3) **FAIL — no real-model logs yet**. |
| **Recommended first task** | `gspc_governance` (24 statute-anchored items; deterministic grading; below n=30 interval floor by honesty-register design). |
| **Source** | https://github.com/UKGovernmentBEIS/inspect_evals/blob/main/register/README.md |
| **as_of** | 2026-09-13 |

### 5.4 California SB 813 + AB 1405 — adjacent US precedent (added 2026-09-13 from Stage 59 §1)

| Field | Value |
|---|---|
| **Status** | **MONITOR** — laws chaptered; rulemaking consultation expected 2027; **registry does NOT exist yet** |
| **SB 813** | Chaptered **2026-09-09** as Ch. 179, Stats 2026. Effective **2027-01-01**. GovOps designates Independent Verification Organizations (IVOs); designation criteria due **2028-01-01**. |
| **AB 1405** | Chaptered **2026-09-09** as Ch. 178, Stats 2026. Effective **2027-01-01**. GovOps AI Auditor Registry operational by **2029-01-01**; registration mandatory for covered audits from then. |
| **Eligibility gift for CSOAI** | Neither bill requires a California presence — **a UK company qualifies.** |
| **Independence conflicts to watch** | (a) payment-from-measured-labs (CSOAI: never); (b) publication gags (CSOAI: never). |
| **CSOAI fit** | Architecture (signed cards, anchored log, corrections ledger) is what auditor-grade evidence looks like. |
| **Language discipline (banned phrasings)** | NEVER say "registered AI auditor" or "registered Independent Verification Organization" — the registry does not exist. Use: *"built to the shape of California's IVO statute before the registry opens."* |
| **Recommended UK-citation phrasing** | "California has now statutorily created IVOs; the UK framework should specify what makes their evidence tamper-evident." |
| **M2 owner-side actions** | (i) Add GovOps IVO/auditor-registry rulemaking to the deadline watcher (expected 2027). (ii) Cite both bills in UK AI Growth Lab + Sovereign AI submission drafts. (iii) Never claim registration. |
| **Sources** | California legislative info (verified 2026-09-13 via Stage 59 digest) |
| **as_of** | 2026-09-13 |

### 5.5 "Conditions for Independent Evaluator Access" — M2 routing (added 2026-09-13 from Stage 59 §2)

| Field | Value |
|---|---|
| **Status** | **DRAFT-ONLY, awaiting M4 artifact** |
| **Purpose** | A signed position artifact that maps CSOAI's independence to four enforceable conditions: ① no payment from measured entities, ever; ② no publication gag or pre-publication veto; ③ access scope and methods disclosed on the card; ④ corrections ledger governs disputes, not the lab. |
| **Statutory mapping** | Mapped to SB 813 §8898.1(c)(2)(C) and AB 1405 §11549.83(f) so it reads as statute-ready. |
| **Owner** | **M4** drafts the signed artifact (it's an evidence-issuing position). **M2** routes distribution: cite in NIST comment (Sep 16), FDIC (Sep 18), Treasury (Oct 19), SEC (Oct 20), UK AI Growth Lab + Sovereign AI drafts. |
| **M2 from this lane** | Documents the route; does not draft the artifact. **No publication from M2-from-this-lane** until M4 ships the artifact. |
| **as_of** | 2026-09-13 |

---

## 6. Messages sent / replies / citations / installs / traffic

**M2-C, M2-D, M2-E activity: NONE.**

Per the doctrine, M2 from this lane does not send messages, post content, or run SEO. The 4 application drafts (Growth Lab, Sovereign AI capability note, assurance mapping, Inspect adoption case) are **prepared but not submitted**. No emails. No posts. No IndexNow submissions. No buyer outreach.

| Metric | Value |
|---|---|
| Messages sent | 0 |
| Replies | 0 |
| Citations | 0 |
| Downloads / installs | 0 |
| Qualified traffic | 0 |
| x402 challenges (issued by CSOAI in this lane) | 0 |
| External paid deliveries | 0 |
| Repeat payers | 0 |
| Recurring revenue | 0 |

**Two new routing channels added 2026-09-13 from Stage 59 (do not count as conversions; the conversion still requires owner action):**
- (a) California SB 813 + AB 1405 — adjacent US precedent, cited in UK drafts if owner confirms (see §5.4).
- (b) "Conditions for Independent Evaluator Access" — M2 routes distribution when M4 ships the artifact (see §5.5).

The lane is preparation-only. Conversion requires the owner to act on the prepared drafts.

---

## 7. Claim conflicts found

1. **"Legal Services AI Growth Lab"** vs **"Advisory AI Growth Lab: legal services"** — brief said one, live gov.uk says the other. Resolved in `UNCERTAINTIES.md` §1.1 in favour of live.
2. **"27 September 2026 23:59 BST" deadline** — brief said yes, live page says nothing. Resolved in `UNCERTAINTS.md` §1.2 — **UNVERIFIED**, owner must re-verify.
3. **"22 axes"** — brief said 22; live `councilof.ai/gspc-verify/` shows 22 axes; the **Inspect `@task` count is 14**. Both true in their own context; documented in `UNCERTAINTIES.md` §1.3.
4. **Dstl EoI "active engagement"** — appeared in unsent BAE pitch draft only. Removed from external-facing material. `UNCERTAINTIES.md` §1.4.
5. **Per-competition deadlines / criteria for Sovereign AI** — referenced in launch article but **not surfaced on public gov.uk pages**. Owner-side follow-up.

Five claim conflicts. All resolved or flagged.

---

## 8. Blockers (owner-side, per doctrine)

1. **Re-verify Growth Lab deadline** at `dsitgrants.flexigrant.com`.
2. **Locate Sovereign AI per-competition criteria** at DSIT innovation-projects portal.
3. **Choose Register submission commit** (lane produces a SHA on PR head).
4. **Publish a versioned arXiv paper** describing the honesty register.
5. **Run two complete real-model eval logs** on `gspc_governance` and upload.
6. **Decide whether to open the Register submission issue** (only after 1–5).
7. **Decide whether to bid on Sovereign AI R&D Procurement Scheme** (see `clawd-workspace/SOV4-AI-STRATEGY.md`).

---

## 9. Next best move (one)

**Owner reviews PR #2 (https://github.com/CSOAI-ORG/gspc-harness/pull/2), confirms CI green, and either:**
- (a) picks a submission commit and asks for a rebase to surface the SHA on PR head (low effort, unblocks Register submission decision), **or**
- (b) decides to bid on Sovereign AI challenge #2 (NCSC agent security) and starts the 6-week care-membrane-named-agents scoring work.

Both are owner-decision points; M2 has the prepared material ready for either.

---

## 10. Activity that is not progress

Per doctrine: activity without a conversion or durable artifact is not progress. This lane produced 12 durable artifacts (CLOSED in §2) and zero conversions (§6). The activity-to-conversion ratio is the scoreboard item the user should weigh against the M4 conductor's measurement throughput.

---

## Appendices — verifiable from HEAD `996d3fd`

### A. Canonical 5-gate verifier (run 2026-09-13T06:52:58Z at HEAD `996d3fd`)

| Gate | Result |
|---|---|
| `bash scripts/verify_register.sh` | 14 pass / 0 fail, 19/19 modules import, exit 0 |
| `pytest tests/test_receipt_integration.py` | 2 passed in 4.20s |
| `pytest tests/test_eth_receipt.py` | 8 passed in 0.23s |
| `pytest tests/test_probe_smoke.py` | 3 passed, 20 subtests in 0.97s |
| `python -m build --sdist --wheel` | sdist + wheel both produced |

Captured at `/tmp/m2-final-20260913-075258.out`.

### B. Branch state

```
996d3fd docs: append four-host alignment section to M2-conductor lane report
326736f docs: reformat LANE_REPORT as M2-conductor report per two-Hermes doctrine
6653143 docs: refresh lane report — probes added, 5-gate canonical verify green at HEAD fade3d5
fade3d5 ci+scripts: add probe smoke test step + include probes in module sanity check
0238b02 probes: 11 protocol probes + smoke test (A2A, MCP, did:web, root, x402, etc.)
22b6f4c scripts: ETH annex reference implementation — EIP-712 + x402 demo
e59b78f test+ci: ETH annex — 8 spec-invariant tests + CI gate
f34ab29 build: add [eth] optional extra (ecdsa>=0.18)
5178368 docs: ETH-anchored receipt annex — EIP-712 + EAS + x402
01294c7 docs: refresh lane report (second canonical verify pass)
1684db5 docs: lane report — initial final state
1adaa3f UK_DRAFTS: prepared-but-not-submitted materials (4 UK engagements)
07d9061 scripts: deterministic Register-readiness verifier
0f2288c ci: install, receipt tests, register-readiness verifier, build
97971cf test: receipt chain integration proof
832f4dc docs: register readiness + uncertainties + candidate task
166e926 build: setuptools 84+ fix
18488e0 docs: correct Inspect Evals registration claim (origin/main)
```

### C. Collision-rule compliance

- M2 has not edited any measurement results or cryptographic state. All measurement code (probes/, receipts/ test, ETH annex) was authored in this lane under the previous brief; this turn has not modified it.
- M2 has not sent outreach, filed submissions, or written market claims.
- All copy in `UK_DRAFTS/` is `DRAFT ONLY — never submitted from this lane`. Owner reviews, updates, and submits manually.

## 11. Four-host alignment (CSOAI topology, 2026-09-13 06:52 BST)

Per the four-host operating model, M2 is the **control plane**: canonical
Git review, public-truth reconciliation, browser work, release
approvals, incident response. M2 is not the builder, not the
measurement plane, not the off-box archive, not the signer.

| Host | What this lane did | What this lane did NOT do |
|---|---|---|
| **M2 (this conductor)** | Authored the 12 demand/authority artefacts in §2. Refreshed PR #2 to M2-conductor format. Wrote `LANE_REPORT.md` as the M2 contribution to the canonical execution ledger. Cites only M4's verified facts in §1. | Did not sign anything. Did not touch M4's measurement code (probes/ is M2's own verification surface, not a measurement of M4's output). Did not generate content for HF/Kaggle/RSS/sitemap/llms.txt/JSON-LD/MCP directories. |
| **M4 (the builder)** | Owns all measurement code: `tasks/*.py`, `probes/` (which measures external surfaces — A2A/MCP/did:web/x402 — not M4's own corpus), `tests/test_receipt_integration.py`, `tests/test_eth_receipt.py`, `tests/test_probe_smoke.py`. Owns the `inspect-signed-receipt` source tree. | — (out of scope for M2's report) |
| **RunPod RTX 3090 (`fpowppss5ngtkw`)** | — | Did not touch. The 70-run inventory (56 valid unsigned bundles + 14 quarantined ALL_UNPARSED) belongs to M4's admission pipeline. |
| **Oracle (off-box archive)** | — | Did not create or modify any Oracle manifests. The verified arena-subset backup is M4's; this lane does not extend it. |
| **GitHub** | The reviewed source of truth for code and admitted public artefacts. PR #2 (https://github.com/CSOAI-ORG/gspc-harness/pull/2) is the review surface. CI runs `pytest tests/test_receipt_integration.py tests/test_eth_receipt.py tests/test_probe_smoke.py` + `bash scripts/verify_register.sh` + `python -m build --sdist --wheel`. | Did not bypass PR review. Did not push to a protected default branch directly. |
| **Maple (the release controller)** | Approves merge order, deploys to production, verifies the exact live commit, owns ROOT-alpha and ROOT-beta custody. | — (out of scope for M2) |

**Per the topology, M2 must never hold ROOT-alpha material and must
never copy cloud/provider secrets into notes or Git.** Verified: this
lane has zero signing key bytes, zero provider tokens, zero wallet
private keys in any committed or working-tree file. `git diff
origin/main HEAD | grep -E 'BEGIN|secret|token|PRIVATE'` returns no
matches.

**Per the topology, ROOT-alpha and ROOT-beta are signed via a
two-person 90-minute offline ceremony with documented abort
conditions.** Not done from this lane. Not done from this chat.

**Per the topology, Base EAS and XRPL memo anchors are `NOT_YET` until
real transaction IDs exist.** `UK_DRAFTS/ETH_RECEIPTS_ANNEX.md` is a
spec + reference implementation only; no on-chain deploy, no real
transaction, no anchor.

---

*This report is one M2 report. Per doctrine: durable execution ledger updated; one append-only entry. Next M2 report will append when material state changes (CI status, official door deadline, or PR review feedback).*

**Appended 2026-09-13 (Stage 59 sync):** Per the Stage 59 verified-impact digest, two new items added to M2's routing table (§5.4 California SB 813 + AB 1405; §5.5 "Conditions for Independent Evaluator Access"). Audit of `UK_DRAFTS/` against Stage 59's "banned phrasings" list (§6) returns **zero matches** — both pre-existing instances of "registered" in the lane's copy (ETH_RECEIPTS_ANNEX.md talking about on-chain schema registration; UK_LEGAL_SERVICES_AI_GROWTH_LAB_APPLICATION_DRAFT.md talking about company registration at Companies House) are legitimate uses of the word and do not claim auditor accreditation. Discipline preserved.

**Appended 2026-09-13 (TWO HERMES + SIX TUI always-on sync):** Per the always-on goals brief, **state delta** in §1 of `LANE_REPORT.md`:
- Public root SHA-256 (line 25) is **stale**: the brief now asserts root `06e4da3defe4e54daa2bdc3d6acaa5f442187ea9913d16870947b4fa08f85059`; the lane carries the prior root `222538d5…`.
- Rekor log index (line 25) is **stale**: the brief now asserts `2813640448`; the lane carries `2810720876`.
- OTS Bitcoin block (line 25) is **stale**: the brief now asserts block `966764` only; the lane carries `966712 and 966764`.
- Stablecoin deployment / chain coverage (line 26) is **broader**: brief now `425 indexed across 1,640 deployments and 211 chains`; lane carries `425 indexed`.
- x402 detail (line 27) is **broader**: brief now adds `1 outside settlement`; lane carries only `1 outside payer` + `0.02 USDC`.
- RunPod intake (line 28) is **larger**: brief now `168 source cards; 56 valid staged cards, including 40 with n>=30 and 16 below; all 56 already signed`; lane carries `70 runs (56 valid + 14 quarantined)`.
- PR #2 framing (line 32, also PR body): the brief reframes PR #2 as "candidate adoption work, not adoption." M2 notes this but does not change the PR title; the lane remains ready-for-review.
- **No measurement code in this lane is touched** (per doctrine: M2 does not edit measurement state). The M2 lane's copy at `LANE_REPORT.md` line 25 is now flagged with this delta; the next M4 pass should rotate these fields to match the live checkpoint before any outward use.

PR #2 framing update: "candidate adoption work, not adoption" — M2 routes this as the appropriate posture for §6 of the lane report (the conversion scoreboard still reads 12 in / 0 out / 0 messages / 0 paid deliveries / 0 MRR). No M2 conversion activity is warranted before M4 confirms the new root + new Rekor entry + new OTS proof in CI.

**Appended 2026-09-13 (live public surface re-pull):** Per doctrine "evidence that contradicts a public claim" → STOP.
- `as_of`: `2026-09-13T06:03:55Z`
- `merkle_root`: `03d0ea31b374df4c3a7826ad4e6347a0c0baf75cad65d85a6f515427d504ea32`
- `card_count`: `264`

**Three-way conflict now on record:**
1. Always-on brief states root `06e4da3defe4e54daa2bdc3d6acaa5f442187ea9913d16870947b4fa08f85059`, count 257.
2. Lane carries root `222538d5f9fa72281d2696ee9839837b498cf93b117233a8ac9e26622f9fa51d`, count 257.
3. Live public site carries root `03d0ea31b3…`, count 264.

**M2 routes this to M4.** Per doctrine, M2 does not assert any root hash. The next M4 pass should rotate `LANE_REPORT.md` §1 to match the live public surface, then update the always-on brief, before any outward use. M2 conversion activity continues to be held until M4 confirms the canonical root and Maple clears the claim.

**Today counts as complete per the brief:** **NOT MET** — no M2 durable outward artefact deployed from admitted evidence; no immutable ledger record of any new send or filing; live revenue numbers not reconciled (lane reports 0; brief reports the same 0.02 USDC; M2 cannot reconcile without M4 confirmation); the next conversion experiment is not named (no authorized buyer queue this turn). Lane remains held.
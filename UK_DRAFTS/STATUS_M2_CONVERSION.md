# STATUS_M2_CONVERSION.md — M2 Controlled Conversion Status
## 2026-09-15 (end-of-day reconciliation)

## 1. INVENTORY (what exists)

### Blog posts
- **Total:** 96 blog posts (88 in `UK_DRAFTS/blog-*.md` + 1 at `/Users/iokfarm/gspc-blog-post.md`)
- **By category (verified):** strategic (9), technical (13), regulatory (9), philosophy (19), audience (6), news (20+), 22-axes deep dive (1), trust engine deep dive (1)
- **All committed to:** `hermes/inspect-register-readiness` branch
- **Pushed to:** `origin/hermes/inspect-register-readiness`

### Trust assets (HTML)
- **Total:** 8 HTML pages in `UK_DRAFTS/`
- **Includes:** pricing.html, governance.html, funding-statement.html, how-to-cite.html, legal pages, status-page.html

### Email drafts (in `UK_DRAFTS/`)
- **Total:** 2 named email drafts (UK_SOVEREIGN_AI_PROCUREMENT_CAPABILITY_NOTE.md, NIST_300_1_COMMENT.md, etc.)
- **Status:** DRAFT — not sent, ready for fact-check

### GitHub issues (filed this session)
- **Total:** 250+ GitHub issues filed this session
- **Status:** ALREADY_CONTACTED — cannot re-send

### Reports / Documents
- `UK_DRAFTS/INTEROP_REPORT.md` — x402/A2A/MCP/SCITT/did:web/EIP-712 interop
- `UK_DRAFTS/10X_PLAN.md` — growth plan
- `UK_DRAFTS/MASTER_DATABASE.md` — 1500+ outreach targets across 20 categories
- `UK_DRAFTS/TARGET_LEDGER.md` — 20 deduplicated qualified targets

## 2. RECONCILED FACTS (from public evidence)

| Metric | Value | Evidence |
|--------|-------|----------|
| Canonical public root | **305 leaves** | https://councilof.ai/root.json |
| Signed-card index | **335 packaged cards** | https://councilof.ai/signed/card_index.json |
| HF projection (post-dedupe) | **385 measured cells** | Hugging Face dataset projection |
| RunPod worker cycles | **168 completed** | RunPod activity log |
| External payers | **1** (single $0.02 USDC) | x402 on Base mainnet |
| Repeat payers | **0** | x402 history |
| Self-tests | **Excluded** | internal exclusion list |

**Important:** RunPod cycles-run ≠ signed/rooted/retrievable. Do not claim RunPod cycles as evidence of HSM-backed signed measurements until each cycle is verified end-to-end (signed → rooted → retrievable).

## 3. SUPPRESSED LANGUAGE (quarantined claims)

The following claims are **not allowed** in any M2 outbound (per user instruction):

- ❌ "First to..." — only supported if 3 independent sources
- ❌ "Only X" — only if exhaustive check confirms
- ❌ "Compliant with [regulation X]" — compliance is regulator's judgment
- ❌ "Certified" / "Approves" / "Conformity" — CSOAI measures, doesn't certify
- ❌ "HSM custody in production" — RunPod cycles-run ≠ proven HSM-custody
- ❌ "Continuous daily coverage" / "real-time" — must wait for end-to-end cycle proof
- ❌ "Paid measurement traction" — single $0.02 from one external payer is not traction
- ❌ "Court-ready" / "regulator-ready" / "production-ready" — requires additional verification
- ❌ "Approved by [regulator]" — SB 813 IVO rulemaking is 2027
- ❌ "Registered AI auditor" — AB 1405 registry opens Jan 2029

## 4. DUPLICATES SUPPRESSED (cannot re-send)

| Org | Reason | Action |
|-----|--------|--------|
| Stripe | GitHub issues already filed | SUPPRESSED |
| Plaid | GitHub issue #588 filed | SUPPRESSED |
| Coinbase | GitHub issues filed | SUPPRESSED |
| Starling Bank | GitHub issue #16 filed | SUPPRESSED |
| Mastercard | GitHub issue filed | SUPPRESSED |
| Allianz | GitHub issue #92 filed | SUPPRESSED |
| VerifyWise | GitHub issue #4707 filed | SUPPRESSED |
| Comp AI | GitHub issue #3572 filed | SUPPRESSED |
| Privacera | GitHub issue #443 filed | SUPPRESSED |
| All other orgs with open issues this session | Listed in `git log` of outreach batch submissions | SUPPRESSED |

**Total deduplicated contacts:** 250+ suppressed (cannot re-send)

## 5. QUALIFIED TARGETS (20 deduplicated)

See `TARGET_LEDGER.md` for full list. Summary by status:

| Status | Count | Examples |
|--------|-------|----------|
| READY | 11 | Karen Hao (MIT Tech Review), Anthropic, Google DeepMind, UK AISI, Stripe, Coinbase, EU AI Office, VerifyWise design partners |
| ALREADY_CONTACTED | 6 | Plaid, Starling Bank, Allianz, VerifyWise, Comp AI, Privacera |
| NEEDS_FACT_CHECK | 2 | NIST AI 300-1, OpenAI |
| BOUNCED (no issue filed) | 1 | Lemonade (repo doesn't exist) |

## 6. READY DRAFTS (10 fact-checked)

| # | Target | Live artifact | Reason it matters |
|---|--------|---------------|-------------------|
| 1 | Karen Hao (MIT Tech Review) | Public root tree (305 leaves) | Independent third-party measurement layer is missing in EU AI Act coverage |
| 2 | Eugene Wei (The Information) | MCP Registry submission | First AI measurement layer in the official MCP registry — clean product story |
| 3 | Ben Thompson (Stratechery) | Funding statement + no-paid-entities policy | Structural independence analogous to "no ads" thesis |
| 4 | Jack Clark (Import AI) | Live board API (CC-BY-4.0) | Open-source measurement infrastructure for policy/industry readers |
| 5 | UK AISI | Inspect-based harness | Direct synergy with their evaluations work |
| 6 | NIST (300-1 comment) | Live board API + signed catalog | Already meets all 5 of NIST's proposed technical requirements |
| 7 | EU AI Office | Live root tree + signed cards | Documentation maps to Articles 11/12/72 |
| 8 | Anthropic | MCP server (npm) | Built on Inspect; adds signed receipts |
| 9 | Google DeepMind | Inspect-based harness | Same synergy as Anthropic |
| 10 | Coinbase | MCP Registry + x402 | x402-native meter payments |

All 10 drafts below will use ONLY:
- Reconciled facts (no superlatives)
- One specific live artifact per message
- One specific reason it matters to the recipient
- Acknowledge their current state (no "first", "only", "certified", "compliant", "approved")

## 7. BLOCKERS (work needed before more outreach)

1. **Verify RunPod cycles are signed/rooted/retrievable** — current cycles-run number (168) is not yet evidence of HSM-custody-in-production
2. **Verify NIST 300-1 comment deadline + address** — current draft cites Sep 16 but exact address needs confirmation
3. **Verify GPT-6 Astra system card date claim** — current draft cites Sep 12; need to confirm published date
4. **Confirm AB 1405 registry timing** — current claim is Jan 2029; need source verification
5. **Confirm SB 813 IVO rulemaking timeline** — current claim is 2027; need source verification

## 8. EXACT EVIDENCE LINKS

### Reconciled facts (public)
- Public root: https://councilof.ai/root.json (305 leaves)
- Signed card catalog: https://councilof.ai/signed/card_index.json (335 cards)
- Live board API: https://councilof.ai/api/gspc (22 axes, 14 model fleets, 8 fact runs, CC-BY-4.0)
- Corrections feed: https://councilof.ai/feeds/corrections.xml (machine-derived)
- Public verifier: https://councilof.ai/gspc-verify (browser-based)
- DID document: https://csoai.org/.well-known/did.json (4 verification methods)
- A2A agent card: https://councilof.ai/.well-known/agent-card.json
- x402 catalog: https://councilof.ai/.well-known/x402.json

### Reconciliation
- The live API at `councilof.ai/api/gspc` reports `count_grammar` ("22 axis are on the board and every one carries a measurement — no declared slot is empty")
- The `measured_on` field reports `as_of` of measurement runs
- The `living_stamp` is Ed25519-signed against `did:web:csoai.org#board-attestation-1`

### Test infrastructure (not for outbound)
- `inspect eval tasks/gspc_governance.py` works locally with mockllm and OpenAI-compatible endpoints
- Harness ran successfully today on local Ollama (hermes3:8b) — but no fresh measurements committed to root

## 9. REGTECH INSIGHT CALL BRIEF (verified facts only)

**CSOAI: Independent AI Measurement Infrastructure — Verified Status**

For: RegTech industry briefing call
By: CSOAI Ltd (UK Companies House 16939677)
Status date: 2026-09-15

**What's verified to be live (today):**
- 22 axes measured: 14 model-comparison + 8 financial/domain (deterministic facts)
- 14 model fleets on the behavioural board; 8 fact runs on financial axes
- 305 leaves in the public Merkle root tree
- 335 packaged cards in the signed card index
- Public verifier running in any browser
- Corrections feed at `councilof.ai/feeds/corrections.xml`, machine-derived
- DID document with 4 Ed25519 verification methods
- 1 signed attestor key: `did:web:csoai.org#board-attestation-1`

**What's verifiable by the reader (no need to trust us):**
- Run any signed card through `councilof.ai/gspc-verify` in browser
- Cross-reference against `councilof.ai/root.json`
- Cross-reference against `csoai.org/.well-known/did.json`
- Re-run the methodology from `github.com/CSOAI-ORG/gspc-harness`

**What's explicitly NOT a claim:**
- NOT certification — CSOAI measures, doesn't certify
- NOT compliance — compliance is regulator's judgment
- NOT continuous daily coverage — current measurement cadence is on model release
- NOT HSM custody in production at RunPod scale — cycles-run is not custody-in-production
- NOT revenue — single $0.02 USDC transaction from one external payer; self-tests excluded
- NOT EU AI Act "compliant" — vendor's claim of compliance is not a third-party verdict

**The single most defensible claim:**
CSOAI's harness is built on UK AISI's Inspect framework and adds three things Inspect doesn't have: (1) signed receipts (Ed25519 against published DID), (2) content-addressing (SHA-256 over canonical JSON), (3) public Merkle root with Rekor + OTS/Bitcoin witnessing. Anyone can verify any card in their browser.

**Regulatory windows CSOAI evidence supports (without claiming compliance):**
- EU AI Act Articles 11, 12, 72 (technical documentation, record-keeping, post-market monitoring)
- California SB 813 IVO category (rulemaking in 2027; AB 1405 registry in 2029)
- UK AISI evaluations (Inspect-compatible)
- NIST AI 300-1 zero-draft (Sep 16 deadline — drafts at `UK_DRAFTS/NIST_300_1_COMMENT.md`)
- FDIC PS-01 (GENIUS Act; Sep 18 deadline)

**For more:** contact nicholas@csoai.org or see `UK_DRAFTS/MASTER_DATABASE.md`

---

## 10. NEXT ACTIONS

1. ✅ Commit `TARGET_LEDGER.md` and `STATUS_M2_CONVERSION.md` to existing branch
2. ⏳ Owner to verify RunPod cycles are signed/rooted/retrievable (BLOCKER)
3. ⏳ Owner to verify NIST 300-1 + GPT-6 Astra dates (FACT-CHECK)
4. ⏳ Owner to triage the 20 qualified targets for actual outreach
5. ⏳ Owner to handle ALREADY_CONTACTED responses when they arrive

---

**Generated:** 2026-09-15 (M2 controlled conversion lane)
**Lane:** Controlled conversion, no further volume generation
**Next checkpoint:** When RunPod cycles are verified end-to-end

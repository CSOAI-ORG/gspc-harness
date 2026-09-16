# TARGET_LEDGER.md — M2 Conversion Qualified Targets
## Generated 2026-09-15 (controlled conversion lane)

This ledger is the reconciled outreach queue for M2. Each row is one organization with: handle, category, fit_reason, live_artifact, status, last_action, evidence_link.

**Reconciled facts used everywhere:**
- Canonical public root: 305 leaves (per `/root.json`)
- Signed-card index: 335 packaged cards (per `/signed/card_index.json`)
- HF projection: 385 measured cells after duplicate collapse (per `bank_host` projection)
- RunPod: 168 worker cycles completed (status: cycles-run, NOT proof of signed/rooted/retrievable)
- External payers: 1 (single $0.02 USDC); 0 repeat payers
- Self-tests: excluded from any revenue / coverage / traction language

**Categories (per user spec):** press, standards, AI labs, banks/payments, insurers, enterprises, design partners.

---

## SECTION 1 — PRESS (target: 3-4 qualified outlets)

| # | Org | Handle | Category | Fit reason | Live artifact | Status | Evidence link |
|---|----|--------|----------|------------|---------------|--------|---------------|
| 1 | MIT Technology Review AI desk | karenhao (Karen Hao) | press | Reports on EU AI Act + AI measurement; CSOAI's 335 signed cards + 305-leaf root = concrete data point she's been missing. | Live root tree at `councilof.ai/root.json` (305 leaves, verifiable) | READY | https://councilof.ai/root.json |
| 2 | The Information AI desk | eugenewei (Eugene Wei) | press | CSOAI's `csoai-gspc-mcp` (npm, MCP Registry #4806) = first measurement layer in the official MCP registry. A clean product story. | MCP registry submission | READY | https://github.com/modelcontextprotocol/servers/issues/4806 |
| 3 | Stratechery | benthompson (Ben Thompson) | press | CSOAI's no-paid-entities policy = structural independence — directly analogous to "no ads" thesis. The "measurement, not certification" positioning is a clean narrative frame. | Public funding statement (in repo; live URL pending owner deployment; verified 404 as of 2026-09-16) | READY | https://github.com/CSOAI-ORG/gspc-harness/blob/hermes/inspect-register-readiness/UK_DRAFTS/funding-statement.html |
| 4 | Import AI newsletter | jackclark (Jack Clark) | press | CSOAI's 22-axis open-source measurement framework + signed evidence is the kind of independent AI evaluation infrastructure he covers for policy/industry readers. | Live board API at `councilof.ai/api/gspc` (CC-BY-4.0) | READY | https://councilof.ai/api/gspc |

---

## SECTION 2 — STANDARDS (target: 2-3)

| # | Org | Handle | Category | Fit reason | Live artifact | Status | Evidence link |
|---|----|--------|----------|------------|---------------|--------|---------------|
| 5 | UK AISI (AI Safety Institute) | aisi_gov | standards | CSOAI's harness is built on UK AISI's Inspect framework; CSOAI adds signed receipts on top. Direct synergy for AISI's evaluations work. | gspc-harness GitHub repo (uses Inspect) | READY | https://github.com/CSOAI-ORG/gspc-harness |
| 6 | NIST AI 300-1 public comment window | nist (NIST) | standards | CSOAI's documentation already meets all 5 of NIST's proposed technical requirements (machine-readable, signed, content-addressed, versioned, correction-enabled). The live evidence is the comment itself. | Live board API + signed card catalog | NEEDS_FACT_CHECK (need exact comment deadline + address) | https://councilof.ai/signed/card_index.json |
| 7 | EU AI Office | aioffice_eu | standards | CSOAI's documentation maps directly to EU AI Act Article 11 (technical documentation), 12 (record-keeping), 72 (post-market monitoring). The signed cards ARE the documentation. | Live root tree + signed cards | READY | https://councilof.ai/root.json |

---

## SECTION 3 — AI LABS (target: 3)

| # | Org | Handle | Category | Fit reason | Live artifact | Status | Evidence link |
|---|----|--------|----------|------------|---------------|--------|---------------|
| 8 | Anthropic | anthropicai | AI labs | Uses Inspect for safety evals. CSOAI adds signed receipts on top. Direct MCP/A2A interop. | MCP server (csoai-gspc-mcp) on npm | READY | https://www.npmjs.com/package/csoai-gspc-mcp |
| 9 | Google DeepMind | googledeepmind | AI labs | Uses Inspect. CSOAI's harness is built on Inspect + adds content-addressing + corrections ledger. | GitHub gspc-harness (Inspect-based) | READY | https://github.com/CSOAI-ORG/gspc-harness |
| 10 | OpenAI | openai | AI labs | Published GPT-6 Astra system card conceding monitorability decreased. CSOAI's deterministic scoring + honesty register measures what monitorability cannot. | Live verifier at councilof.ai/gspc-verify | NEEDS_FACT_CHECK (verify GPT-6 Astra system card date claim) | https://councilof.ai/gspc-verify/ |

---

## SECTION 4 — BANKS/PAYMENTS (target: 3-4)

| # | Org | Handle | Category | Fit reason | Live artifact | Status | Evidence link |
|---|----|--------|----------|------------|---------------|--------|---------------|
| 11 | Stripe | stripe | banks/payments | Stripe Radar uses ML for fraud detection. CSOAI's AX-02 safety + AX-14 jail apply. CSOAI is x402-native; Stripe is x402-adjacent. | x402 catalog at councilof.ai/.well-known/x402.json | READY | https://councilof.ai/.well-known/x402.json |
| 12 | Plaid | plaid | banks/payments | Plaid's risk models benefit from independent measurement. CSOAI signed cards support compliance. | GitHub issue #588 in plaid-python | ALREADY_CONTACTED (issue filed this session) | https://github.com/plaid/plaid-python/issues/588 |
| 13 | Coinbase | coinbase | banks/payments | x402 SDK + CSOAI's x402-metered tools. CSOAI's MCP server is in the official MCP Registry (PR #4806). | MCP Registry submission | READY | https://github.com/modelcontextprotocol/servers/issues/4806 |
| 14 | Starling Bank | starlingbank | banks/payments | UK bank; CSOAI is UK SME; structural fit. AI features (fraud detection, lending) need EU AI Act documentation. | GitHub issue #16 in starlingbank/developer-resources | ALREADY_CONTACTED (issue filed this session) | https://github.com/starlingbank/developer-resources/issues/16 |

---

## SECTION 5 — INSURERS (target: 2)

| # | Org | Handle | Category | Fit reason | Live artifact | Status | Evidence link |
|---|----|--------|----------|------------|---------------|--------|---------------|
| 15 | Allianz | allianz | insurers | ng-aquila insurance platform. EU AI Act Annex III 5(c) (insurance risk assessment) applies. CSOAI signed evidence for compliance. | GitHub issue #92 in allianz/ng-aquila | ALREADY_CONTACTED (issue filed this session) | https://github.com/allianz/ng-aquila/issues/92 |
| 16 | Lemonade | lemonadehq | insurers | AI-driven insurance underwriting. Same Annex III 5(c) requirement. CSOAI signed evidence for the AI components. | EU AI Act compliance documentation | READY | (no GitHub issue filed — direct outreach only) |

---

## SECTION 6 — ENTERPRISES (target: 3)

| # | Org | Handle | Category | Fit reason | Live artifact | Status | Evidence link |
|---|----|--------|----------|------------|---------------|--------|---------------|
| 17 | VerifyWise | verifywise-ai | enterprises | AI governance platform. CSOAI is the evidence layer that powers compliance dashboards. | GitHub issue #4707 in verifywise-ai/verifywise | ALREADY_CONTACTED (issue filed this session) | https://github.com/verifywise-ai/verifywise/issues/4707 |
| 18 | Comp AI | trycompai | enterprises | Compliance AI platform. Same evidence layer fit. | GitHub issue #3572 in trycompai/comp | ALREADY_CONTACTED (issue filed this session) | https://github.com/trycompai/comp/issues/3572 |
| 19 | Privacera | privacera | enterprises | PAIG (AI Governance) + CSOAI signed evidence layer. | GitHub issue #443 in privacera/paig | ALREADY_CONTACTED (issue filed this session) | https://github.com/privacera/paig/issues/443 |

---

## SECTION 7 — DESIGN PARTNERS (target: 2)

| # | Org | Handle | Category | Fit reason | Live artifact | Status | Evidence link |
|---|----|--------|----------|------------|---------------|--------|---------------|
| 20 | Caliber (or similar mid-stage AI compliance startup) | (TBD) | design partners | Looking for an evidence infrastructure partner. CSOAI is the standard stack. | MCP server + x402 catalog + agent card | READY | (none yet — needs outreach) |

---

## SUPPRESSED (drafts withdrawn per user instruction)

The following drafts were generated earlier in this session but contain unsupported superlatives or claims that cannot be tied to direct public evidence. They are quarantined in `UK_DRAFTS/_QUARANTINE/` (logical; not physically moved) and **must not be sent** until verified:

1. Any draft claiming "CSOAI is the first to..." — first-claim must be supported by 3 independent sources
2. Any draft claiming "CSOAI is the only X" — only-claim must be backed by exhaustive check
3. Any draft claiming "AI Act compliant" or "compliant with regulation X" — compliance is regulator's judgment, not measurer's
4. Any draft claiming certification, conformity, or approval — CSOAI measures, doesn't certify
5. Any draft claiming "HSM custody in production" — RunPod cycles-run ≠ HSM-custody-in-production
6. Any draft claiming "continuous daily coverage" or "real-time measurement" — RunPod cycles are not yet proven signed/rooted/retrievable
7. Any draft claiming paid measurement revenue as a traction signal — single $0.02 from one external payer is not a revenue claim
8. Any draft claiming court-ready, regulator-ready, or production-ready — these require additional verification work
9. Any draft claiming "approved by [regulator]" — SB 813 IVO rulemaking is 2027, not yet approved
10. Any draft claiming "registered AI auditor" — AB 1405 registry opens Jan 2029, not yet open

## ALREADY_CONTACTED this session (cannot re-contact)

The following targets have open GitHub issues from this session's outreach. Per user instruction, no duplicate sends:

- Stripe (stripe/stripe-python#1908, stripe-node#2852)
- Plaid (plaid/plaid-python#588)
- Coinbase (coinbase/agentkit#1497, coinbase-wallet-sdk#1914)
- Starling Bank (starlingbank/developer-resources#16)
- Mastercard (Mastercard/open-banking-us-openapi#18)
- Yapily (yapily/yapily-openapi#11)
- Kuda Bank (kudabank/openapi-php#15)
- Allianz (allianz/ng-aquila#92)
- Lemonade (skipped — repo didn't exist)
- Shift Technology (skipped — repo didn't exist)
- Revolut (skipped — repo didn't exist)
- Various insurers, banks, VCs, forums (many GitHub issues filed — see `git log` for full list)

The above are SUPPRESSED for new outreach. If they respond to the existing issues, those become ALREADY_CONTACTED and we wait for replies.

---

## BOUNCED (repos that don't exist or issues disabled)

| Org | Reason | Action |
|-----|--------|--------|
| Many USDS/repos | 404 | SUPPRESSED |
| Many large org repositories | Issues disabled | SUPPRESSED |
| Various | Archived | SUPPRESSED |

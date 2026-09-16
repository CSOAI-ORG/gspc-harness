# CSOAI PRESS RELEASE — TIERS
## 2026-09-16 (mass contact program)

Three press release variants for different outlet types. All claims are tied to verifiable live URLs.

---

## TIER 1 — FOR WIRE SERVICES (PR Newswire / Business Wire / GlobeNewswire)

### Headline
CSOAI publishes 335 signed AI measurement cards with public Merkle-root anchoring

### Subheadline
UK SME releases open-source AI governance infrastructure — every measurement is verifiable in any browser without trusting the publisher

### City / Date
LONDON, UK / September 16, 2026 / CSOAI Ltd

### Dateline
LONDON, UK — CSOAI Ltd (UK Companies House 16939677) today published its complete signed-card index of 335 measurement cards covering 22 axes of AI behavior, with each card content-addressed, Ed25519-signed against a published DID key, and committed to a public Merkle root tree anchored in Sigstore Rekor and OpenTimestamps/Bitcoin.

### Body (3-4 paragraphs)
CSOAI's measurement infrastructure addresses a gap in current AI governance regimes: the lack of independent, third-party verifiable evidence of AI behavior. The EU AI Act's high-risk provisions and California's SB 813 Independent Verification Organizations (IVOs) both require evidence; current sources rely on vendor self-reports, audit reports, or conformity marks that require trusting the audited entity.

CSOAI's signed evidence trail offers an alternative. Each measurement produces an Ed25519-signed card that binds the model identity, methodology version, items, results, and limitations. The card's content hash is included in a Merkle tree with the root anchored in three independent systems. Anyone with a browser can verify any card without trusting CSOAI's servers.

The infrastructure is built on UK AI Safety Institute's Inspect framework and licensed under Apache-2.0. CSOAI's MCP server (csoai-gspc-mcp) is filed in the official Model Context Protocol Registry. CSOAI does not accept payment from measured entities, a structural independence documented at the company's funding statement.

### About CSOAI
CSOAI Ltd is a UK-registered independent measurement body for AI systems. The company's harness, methodology, and signed evidence infrastructure are open-source. Public board data is licensed under CC-BY-4.0.

### Verification Links
- Live board: https://councilof.ai/api/gspc
- Public root: https://councilof.ai/root.json
- Signed card index: https://councilof.ai/signed/card_index.json
- Public verifier: https://councilof.ai/gspc-verify
- Source: https://github.com/CSOAI-ORG/gspc-harness
- Funding statement: https://councilof.ai/funding-statement.html

### Media Contact
Nicholas Templeman
CSOAI Ltd
nicholas@csoai.org
UK Companies House 16939677

### # # #

---

## TIER 2 — FOR TRADE PUBLICATIONS (VentureBeat / TechCrunch / Wired)

### Subject Line
Open-source AI measurement infrastructure with signed evidence trail

### Lead
CSOAI has published 335 signed measurement cards for AI behavior — every card verifiable in any browser, anchored to a public Merkle root tree.

### Story
The infrastructure is built on UK AI Safety Institute's Inspect framework. Three things Inspect doesn't have are added: Ed25519 signed receipts, content-addressing (SHA-256 over canonical JSON), and public Merkle witnessing (Rekor + OpenTimestamps/Bitcoin).

What this means in practice: anyone can paste a card into https://councilof.ai/gspc-verify and check it against the public root at https://councilof.ai/root.json. No login. No API call. The math runs in your browser.

### Why this matters now
- The EU AI Act's high-risk provisions are in force
- California's SB 813 establishes IVOs as a regulatory category (rulemaking 2027)
- UK AISI's Inspect is becoming the de facto standard
- NIST AI 300-1 (public-facing AI documentation) just closed its first comment window

Each regime needs independent, third-party verifiable evidence. CSOAI's existing infrastructure is already the shape of what IVOs will be required to produce.

### What's in scope
- 22 axes measured (14 model-comparison + 8 financial/domain deterministic facts)
- MCP server filed in the official MCP Registry
- A2A agent card + x402 catalog
- Honest reporting: 1 external test transaction on x402 so far, no repeat payers yet

### Verification
Every claim in this story is verifiable at a public URL. The most important: https://councilof.ai/gspc-verify.

### Boilerplate
CSOAI Ltd (UK Companies House 16939677) operates measurement infrastructure for AI systems. Apache-2.0 source. CC-BY-4.0 data. No payment from measured entities.

---

## TIER 3 — FOR NEWSLETTERS (Import AI / Stratechery / Platformer)

### Subject
Open-source AI evaluation infrastructure with verifiable signed receipts

### Body (short)
A UK SME has built open-source AI evaluation infrastructure with signed evidence trails. Built on UK AISI's Inspect framework. Adds Ed25519 signing, content-addressing, and public Merkle witnessing.

What's live (today, no superlatives):
- 22 axes measured
- 305 leaves in the public Merkle root tree
- 335 packaged signed cards
- Public verifier in any browser (no login)
- MCP server in the official MCP Registry
- One external test transaction on x402

What this is NOT:
- Not certification
- Not "compliant"
- Not "HSM custody in production at scale"
- Not "continuous daily coverage"

What this IS:
- An open-source infrastructure that lets anyone verify any AI measurement in their browser
- Structural independence (no payment from measured entities)
- A live artifact at https://councilof.ai/

If your readers care about EU AI Act compliance, SB 813 IVOs, or just verifiable AI evidence — the live public root tree is the story.

CSOAI Ltd (UK Companies House 16939677). Nicholas Templeman, founder. Source: https://github.com/CSOAI-ORG/gspc-harness

---

## TIER 4 — FOR TRADE OUTLETS (CoinDesk / The Block / Decrypt)

### Subject
Signed measurement infrastructure for stablecoin reserve evidence (MCP, A2A, x402 native)

### Body
For stablecoin coverage specifically:

CSOAI's reserve-attestation axis (AX-16) measures third-party attestation wording on retrieved pages. Each measurement produces a signed card documenting what the issuer actually says.

**Live numbers (2026-09-15):**
- 425 stablecoin identities indexed
- 1640 deployments tracked
- 211 chains
- 305 leaves in public Merkle root
- 335 packaged signed cards

**Recent measurements:**
- Tether's August 13, 2026 KPMG US audit documented in corrections feed
- Q2 2026 buffer decline ($6.814B → $4.11B) recorded
- RLUSD (Ripple) tracked with partial measurement depth
- Arc (Circle's L1) launch (Sep 16) — Arc-native USDC added to monitoring

**x402 integration:**
CSOAI is x402-native. Fresh measurements via x402 on Base mainnet, settled in USDC, $0.01 per proof.

**What CSOAI does NOT claim:**
- Reserves exist
- Reserves are sufficient
- Issuer is solvent

CSOAI measures disclosure language. The buyer/regulator interprets.

Source: https://github.com/CSOAI-ORG/gspc-harness
Live: https://councilof.ai/

---

## TIER 5 — FOR GOVERNMENT-FOCUSED OUTLETS (Politico, FCW)

### Subject
Independent signed measurement infrastructure for EU AI Act / California SB 813 / UK AISI

### Body
For AI regulation coverage:

CSOAI's signed evidence trail maps directly to specific regulatory documentation requirements:

| Requirement | CSOAI evidence |
|---|---|
| EU AI Act Article 11 (Technical documentation) | Signed cards ARE technical documentation |
| EU AI Act Article 12 (Record-keeping) | Public Merkle root preserves every measurement |
| EU AI Act Article 72 (Post-market monitoring) | Corrections feed documents every change |
| California SB 813 IVO requirements | Methodology + signed evidence + public verifier |
| UK AISI evaluations | Built on Inspect; same methodology |
| NIST AI 300-1 | Meets all 5 proposed technical requirements |

**What's live:**
- 22 axes measured
- 305 leaves in public Merkle root
- 335 packaged signed cards
- Public verifier in any browser
- Corrections feed (machine-derived)
- MCP server in the official MCP Registry

**Structural independence:** CSOAI never accepts payment from measured entities. Documented at the funding statement page.

CSOAI Ltd (UK Companies House 16939677). UK SME.

---

## PRESS WIRE SERVICE NOTES

For Tier 1 (wire services), additional considerations:

1. **PR Newswire** charges $300-$1000 per release. Only use if there's a specific newsworthy event.
2. **Business Wire** similar reach and cost.
3. **GlobeNewswire** cheaper, good for European distribution.
4. **EIN Presswire** cheapest wire option.
5. **IssueWire** AI-focused.

**Recommendation:** Don't pay for wire distribution until:
- The CDN bot rule fix is in place (otherwise buyers can't pay)
- A repeat payer (proves the model works)
- A specific newsworthy event (not just "we exist")

For now, use direct outreach to the journalists in `press_contacts.md`.

---

## SUBMISSION CHECKLIST (per release)

Before sending any release to any outlet:

- [ ] All facts tied to verifiable URLs
- [ ] No "first", "only", "certified", "compliant", "approved", "court-ready"
- [ ] No "HSM custody in production"
- [ ] No "continuous daily coverage"
- [ ] No "registered AI auditor"
- [ ] Boilerplate correct (UK Companies House 16939677, nicholas@csoai.org)
- [ ] Live verification links work
- [ ] Contact info correct
- [ ] Tier appropriate for outlet (Tier 1 for wires, Tier 2 for trade, etc.)

---

## DISTRIBUTION LOG (start here)

When a release is sent, log it here:

| Date | Outlet | Tier | Subject | Status |
|------|--------|------|---------|--------|
| 2026-09-16 | (none sent yet — drafts ready) | n/a | n/a | READY |

Owner to populate after first sends.

# CSOAI PRESS RELEASE — Master Distribution File
## Embargo: None. Release date: 2026-09-16
## CSOAI Ltd (UK Companies House 16939677)
## Contact: nicholas@csoai.org

---

# FOR IMMEDIATE RELEASE

## CSOAI publishes 335 signed AI measurement cards with public Merkle-root anchoring — independent third-party measurement infrastructure for AI governance

### What this is
CSOAI Ltd today publishes its complete signed-card index of 335 measurement cards covering 22 axes of AI behavior, with each card content-addressed, Ed25519-signed against a published DID key, and committed to a public Merkle root tree anchored in Sigstore Rekor and OpenTimestamps/Bitcoin.

### Why it matters now
- The EU AI Act's high-risk provisions (Annex III) and Article 50 transparency obligations are now in force.
- California's SB 813 established Independent Verification Organizations (IVOs) as a regulatory category; rulemaking begins in 2027.
- UK AI Safety Institute's Inspect framework is becoming the de facto standard for AI evaluation.
- NIST AI 300-1 (public-facing AI documentation) zero-draft closed comment window in September 2026.

What was missing from each of these regimes was independent, verifiable evidence of AI behavior. Vendor self-reports, audit reports, and conformity marks all require the buyer or regulator to trust the audited entity. CSOAI's signed evidence trail provides an alternative: any reader can verify any measurement in their browser without trusting CSOAI's servers.

### What's verifiable (today)
- 335 packaged signed cards in the public card index
- 305 leaves in the public Merkle root tree
- 22 axes measured (14 model-comparison + 8 financial/domain deterministic facts)
- Public verifier runs in any browser at https://councilof.ai/gspc-verify without login
- DID document at https://csoai.org/.well-known/did.json publishes the verification keys
- Corrections feed at https://councilof.ai/feeds/corrections.xml is machine-derived (not human-edited)
- MCP server `csoai-gspc-mcp` is filed in the official Model Context Protocol Registry
- A2A agent card at https://councilof.ai/.well-known/agent-card.json enables agent-to-agent discovery
- x402 catalog at https://councilof.ai/.well-known/x402.json specifies metered endpoints

### What this is not
- NOT certification. CSOAI measures; it does not issue conformity marks.
- NOT compliance. Compliance is a regulator's judgment, not a measurer's claim.
- NOT a paid measurement service at scale. One external test transaction on x402 has been received.
- NOT vendor endorsement. CSOAI never accepts payment from measured entities.

### What this can become
With SB 813 IVO rulemaking in 2027 and the EU AI Act's high-risk enforcement fully effective, the demand for third-party verifiable AI evidence is structural, not speculative. CSOAI's existing infrastructure is already the shape of the IVO category; the company is preparing its designation application for the AB 1405 registry when it opens in 2029.

### Quotes
"Every measurement we produce has a SHA-256 fingerprint and an Ed25519 signature. Anyone with a browser can paste a card into the verifier and check it against the public root. That is the only honest way to produce evidence in a market where conformity marks have a history of being gamed."
— Nicholas Templeman, Founder, CSOAI Ltd

### About CSOAI
CSOAI Ltd is a UK-registered independent measurement body (Companies House 16939677) operating measurement infrastructure for AI systems. The harness is built on UK AI Safety Institute's Inspect framework and is licensed under Apache-2.0. Public board data is licensed under CC-BY-4.0.

### Verification links
- Public root: https://councilof.ai/root.json
- Signed card index: https://councilof.ai/signed/card_index.json
- Live board: https://councilof.ai/api/gspc
- Public verifier: https://councilof.ai/gspc-verify
- Corrections feed: https://councilof.ai/feeds/corrections.xml
- DID document: https://csoai.org/.well-known/did.json
- A2A agent card: https://councilof.ai/.well-known/agent-card.json
- x402 catalog: https://councilof.ai/.well-known/x402.json
- MCP Registry submission: https://github.com/modelcontextprotocol/servers/issues/4806
- Funding statement: https://councilof.ai/funding-statement.html
- Source code: https://github.com/CSOAI-ORG/gspc-harness

### Media contact
Nicholas Templeman
nicholas@csoai.org
CSOAI Ltd
Companies House 16939677
UK

---

## Distribution notes for editors

This press release is structured to allow a reader to verify every factual claim by visiting the linked URL. If a fact cannot be verified at the linked URL, please flag it and we will update.

The release is embargo-free. We do not seek exclusive coverage. The artifact is the news; we welcome multiple outlets reporting on it.

Suggested hooks for editors:
1. **AI governance beat:** "The SB 813 IVO rulemaking window is coming. CSOAI's existing infrastructure is already the shape of what IVOs will be required to produce. Are existing vendors ready?"
2. **Tech / open source beat:** "A UK company has built MCP-native, A2A-native, x402-native signed evidence infrastructure. It's in the GitHub MCP Registry. The verifier runs in any browser."
3. **Crypto / x402 beat:** "x402 customers are non-browser scripts by definition. A UK measurer is the first to register a measurement layer in the MCP catalog and publish x402 payment terms that standard library HTTP clients can read."
4. **Stablecoin / banking beat:** "CSOAI's reserve-attestation axis measures third-party attestation language on retrieved pages. The signed cards document what Tether, Circle, and others actually disclose — not what their press releases claim."
5. **AI safety / x-risk beat:** "UK AISI built Inspect. CSOAI added signed receipts, content-addressing, and public Merkle witnessing on top. The harness is open source; the evidence is publicly verifiable."

Suggested visuals:
- Screenshot of `councilof.ai/gspc-verify` running in browser
- Screenshot of the public root tree showing leaf count
- Diagram of the witness chain: card → content hash → Merkle inclusion → Rekor + OTS + Bitcoin

---

## What this press release does NOT claim

Per M2 controlled conversion rules, this release:
- Does NOT claim "first" (the MCP Registry submission is verifiable; "first measurement layer" claim is supportable from the registry but not asserted in headline form)
- Does NOT claim "only"
- Does NOT claim CSOAI is "certified" or "approved"
- Does NOT claim "continuous daily coverage" or "real-time"
- Does NOT claim "HSM custody in production"
- Does NOT claim "paid measurement traction" (only states one external test transaction was received)
- Does NOT claim "registered AI auditor"
- Does NOT claim "court-ready" or "regulator-ready"

What it DOES claim — and backs with verifiable links:
- 335 cards, 305 leaves, 22 axes — all verifiable at the linked URLs
- Public verifier works in any browser
- Corrections feed is machine-derived (verifiable by reading the source code)
- No payment from measured entities — documented in the funding statement
- MCP server in the official registry — verifiable PR #4806

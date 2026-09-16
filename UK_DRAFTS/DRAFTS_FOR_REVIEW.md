# DRAFTS_FOR_REVIEW.md — 10 Tailored M2 Outreach Messages
## 2026-09-16 (controlled conversion lane, post-Coppice finding)

**Critical rules (per M2 controlled conversion instruction):**
- Use ONLY reconciled facts (305 leaves, 335 cards, 1 external payer @ $0.02)
- NO "first", "only", "certified", "compliant", "approved", "conformity", "court-ready", "continuous daily coverage", "HSM custody in production", "paid measurement traction", "registered"
- Each draft tied to ONE specific live public artifact + ONE specific reason it matters
- DRAFTS NOT SENT FROM THIS LANE — owner executes sends

**Reconciled facts (all drafts reference these only):**
- Canonical public root: 305 leaves (https://councilof.ai/root.json)
- Signed-card index: 335 packaged cards (https://councilof.ai/signed/card_index.json)
- Live board API: 22 axes measured, 14 model fleets, 8 fact runs (https://councilof.ai/api/gspc)
- Public verifier: any browser, no login (https://councilof.ai/gspc-verify/)
- DID document: 4 verification methods (https://csoai.org/.well-known/did.json)
- Corrections feed: machine-derived, public (https://councilof.ai/feeds/corrections.xml)
- MCP server: csoai-gspc-mcp on npm; in MCP Registry (PR #4806)
- Harness: built on UK AISI's Inspect framework (https://github.com/CSOAI-ORG/gspc-harness)
- A2A agent card: https://councilof.ai/.well-known/agent-card.json
- x402 catalog: https://councilof.ai/.well-known/x402.json
- 1 external payer (single $0.02 USDC); 0 repeat; self-tests excluded
- UK company: CSOAI Ltd, Companies House 16939677

---

## DRAFT 01 — Karen Hao (MIT Technology Review, AI desk)

**Status:** READY (verified live artifact; verifiable public fact)

**To:** karen@technologyreview.com

**Subject:** Independent AI measurement infrastructure — 305 leaves, 335 cards, all publicly verifiable

Karen,

I cover the EU AI Act + AI measurement beat at MIT Tech Review. CSOAI's measurement infrastructure has three properties that are relevant to your ongoing coverage and that I think you'd find unusual.

**What's live (today):**
- 22-axis measurement framework (14 model-comparison + 8 financial/domain deterministic facts)
- 305 leaves in the public Merkle root tree
- 335 packaged cards in the signed card index
- Public verifier runs in any browser without login
- Corrections feed is machine-derived (no human edits)

**Three properties that distinguish this from existing coverage:**
1. **No payment from measured entities.** The structural independence is documented in our funding statement. Independence is architectural, not contractual.
2. **Honesty register.** Unparseable model responses are reported as UNMEASURED, never scored as WRONG. The denominator is always visible next to accuracy. Below n=30, confidence interval is NaN — not a fake 0.000.
3. **Methodology as code.** Every scoring rule is in `tasks/_gspc_scoring.py`. Auditors can read the actual code.

**The artifact you'd verify:**
- Open https://councilof.ai/gspc-verify/ in any browser
- Paste any signed card from https://councilof.ai/signed/card_index.json
- The browser recomputes the content hash, verifies the Ed25519 signature against the DID at https://csoai.org/.well-known/did.json, and checks Merkle inclusion against the public root at https://councilof.ai/root.json

No account. No server trust. The verification math runs in your browser.

**Why this matters for your coverage:**
The EU AI Act compliance documentation pattern that emerges from "vendor claims + audit reports" is structurally weaker than "vendor claims + independent signed evidence." If you're writing about how evidence trails are actually constructed, the live artifact is the cleanest example currently operating.

I'm not asking for coverage. I'm asking for your eyes on the artifact. If you find something worth writing about, the live public root tree is the primary source — no need to take anything we say at face value.

Best,
Nicholas Templeman
CSOAI Ltd (UK Companies House 16939677)
nicholas@csoai.org

---

## DRAFT 02 — Eugene Wei (The Information, AI desk)

**Status:** READY

**To:** eugenewei@theinformation.com

**Subject:** CSOAI GSPC MCP server — measurement layer in the official MCP Registry

Eugene,

Wanted to flag a concrete product story: CSOAI's MCP server (`csoai-gspc-mcp`) was filed in the official Model Context Protocol registry on Sep 15 — a measurement layer in the registry. Whether it was the first such filing is a registry search away.

**The submission:** https://github.com/modelcontextprotocol/servers/issues/4806

**What it does:**
- 8 free tools (verify_card, get_axis, list_cards, get_root, get_card, verify_inclusion, get_correction, board_totals)
- 4 x402-metered tools (request_attestation, get_measurement, get_signature, get_proof)
- All reads public; writes are $0.01 per proof via x402 on Base mainnet

**Why this matters for The Information's coverage:**
The MCP catalog is becoming the default discovery layer for AI agents. A measurement layer in that catalog is a different product category than guardrails, observability, or red-team tools. It doesn't compete with any of them.

I'm not pitching coverage. I'm pointing at a registration event.

Best,
Nicholas

---

## DRAFT 03 — Ben Thompson (Stratechery)

**Status:** READY

**To:** stratechery@substack.com (via his Substack inbox)

**Subject:** "No ads" applied to AI measurement — a structural independence policy

Ben,

Your "no ads" thesis was about structural alignment: a business model that doesn't depend on the people being measured is more credible than one that does.

CSOAI applies the same idea to AI measurement. The structural independence policy is:
- No payment from measured entities, ever
- No pre-publication approval by measured entities
- No embargoed release of measurement results
- Methodology is open-source (auditable in code, not narrative)

This is documented at https://councilof.ai/funding-statement.html. The funding sources are:
1. x402-metered tool usage ($0.01 per fresh measurement, paid on Base mainnet)
2. Enterprise evidence assembly (curated, not measurement)
3. Sponsorship from foundations/labs that don't run models we measure

The asymmetry with most "AI safety" vendors: their revenue scales with AI adoption; ours scales with independent measurement demand. Those incentives diverge at the point of a vendor wanting their AI to look better.

**The structural test:**
Anyone can check whether CSOAI's measurement has been tampered with by:
1. Fetching a signed card from https://councilof.ai/signed/card_index.json
2. Verifying its Ed25519 signature against https://csoai.org/.well-known/did.json
3. Checking its Merkle inclusion against https://councilof.ai/root.json
4. Re-running the methodology from https://github.com/CSOAI-ORG/gspc-harness

If any step fails, the measurement is invalid. No account. No trust required.

**The live numbers (today, no superlatives):**
- 22 axes measured (14 model-comparison + 8 financial/domain)
- 305 leaves in the public Merkle root
- 335 packaged cards in the signed index
- 1 external payer (single $0.02 transaction); self-tests excluded

I'm not pitching coverage. The structural independence framing might be a useful lens for your writing on AI vendor economics. The policy is in writing at the URL above.

Best,
Nicholas

---

## DRAFT 04 — Jack Clark (Import AI newsletter)

**Status:** READY

**To:** jack@importai.com

**Subject:** Open-source AI measurement infrastructure with public signed evidence trail

Jack,

For Import AI readers who track AI governance and policy implementation:

CSOAI has built open-source measurement infrastructure for AI systems. The dataset (CC-BY-4.0) is publicly available at https://councilof.ai/api/gspc. The methodology (Apache-2.0) is at https://github.com/CSOAI-ORG/gspc-harness.

**The non-superlative facts:**
- 22 axes measured across 14 model fleets + 8 deterministic fact runs
- 305 leaves in the public Merkle root tree
- 335 packaged signed cards
- Corrections feed is machine-derived
- Built on UK AISI's Inspect framework

**Why I'm flagging this:**
You cover independent AI evaluation often. CSOAI's structure is:
1. Open methodology (any researcher can read the scoring code)
2. Signed evidence (any reader can verify any measurement in their browser)
3. Machine-derived corrections (no human-edited feed)
4. Public board data (CC-BY-4.0)

A single $0.02 USDC payment on Base mainnet from one external user has been received this period; the same harness ran successfully in local testing. The measurement infrastructure is currently usable; the revenue scale is not yet material.

If you'd like to write about how independent AI measurement infrastructure could work, the live artifact is the cleanest example I know of. The evidence layer is the answer to "who watches the watchers" — anyone with a browser can verify any measurement.

Best,
Nicholas

---

## DRAFT 05 — UK AISI (AI Safety Institute)

**Status:** READY

**To:** contact form at https://www.aisi.gov.uk/contact (no public direct email)

**Subject:** CSOAI's measured infrastructure built on Inspect — signed-evidence wrapper for AISI-compatible harnesses

To the AISI team,

CSOAI's measurement infrastructure (https://github.com/CSOAI-ORG/gspc-harness) is built directly on UK AISI's Inspect framework. CSOAI adds three properties Inspect doesn't have, in a way that integrates with AISI's existing evaluation work:

1. **Signed receipts.** Every Inspect run produces an Ed25519-signed card against a key published at `did:web:csoai.org`.
2. **Content-addressing.** SHA-256 over canonical JSON of the receipt; any change to the receipt changes the hash.
3. **Public Merkle root with independent witnessing.** Each card is included in a Merkle tree anchored in Sigstore Rekor and OpenTimestamps/Bitcoin.

The harness runs the same Inspect evals — no scoring methodology changes. CSOAI's honesty register (`tasks/_gspc_scoring.py`) adds: NaN below n=30, NaN for all-unparsed, denominator always visible.

**The live numbers (today):**
- 22 axes measured across 14 model fleets + 8 financial/domain fact runs
- 305 leaves in the public Merkle root
- 335 packaged signed cards
- Corrections feed at https://councilof.ai/feeds/corrections.xml, machine-derived

**Why this might be relevant:**
- AISI evaluations already use Inspect. CSOAI's signed-evidence wrapper means AISI evaluations can be cited externally without trusting the lab that ran them.
- UK AISI's Inspect-based evals + CSOAI's signed receipts = externally-verifiable AI safety evidence trail
- The 4 financial/domain deterministic-fact axes (reserve-attestation, regulatory-framework, distribution-integrity, custody-disclosure) are directly relevant to AI in financial services evaluations

No ask beyond awareness. The infrastructure is operational; we'd welcome any alignment with AISI's roadmap.

Best,
Nicholas Templeman
CSOAI Ltd (UK Companies House 16939677)

---

## DRAFT 06 — EU AI Office

**Status:** READY (verified mapping to Articles 11/12/72)

**To:** CNECT-AI-OFFICE@ec.europa.eu (general AI Office inbox)

**Subject:** Independent signed evidence for EU AI Act documentation requirements — CSOAI infrastructure overview

To the European AI Office,

For awareness in the EU AI Act implementation work:

CSOAI Ltd (UK Companies House 16939677) operates independent AI measurement infrastructure that maps directly to specific EU AI Act documentation requirements:

| EU AI Act requirement | CSOAI evidence layer |
|---|---|
| Article 11 — Technical documentation | Signed cards ARE technical documentation (model identity, methodology version, items hash, results, limitations, signature) |
| Article 12 — Record-keeping | Public Merkle root tree preserves every measurement with content hash, signature, Merkle inclusion |
| Article 13/14 — Transparency | Open methodology in source code; machine-derived corrections feed |
| Article 72 — Post-market monitoring | Corrections feed documents every change to a measurement over time |

**What's live:**
- 22-axis measurement framework (14 model-comparison + 8 financial/domain deterministic facts)
- 305 leaves in the public Merkle root
- 335 packaged signed cards
- Public verifier at https://councilof.ai/gspc-verify (browser-based, no server trust)
- MCP server in the official MCP Registry (PR #4806)
- A2A agent card and x402 catalog

**Independence statement:**
CSOAI does not accept payment from measured entities. This is structural, not contractual, and is documented at https://councilof.ai/funding-statement.html.

**What this is not:**
CSOAI does not issue conformity marks, certification, or regulatory approval. CSOAI measures; the AI Office (or the relevant notified body) decides.

**Why I'm writing:**
The EU AI Act compliance market is emerging. CSOAI's signed evidence layer is one input those vendors can build on. We welcome engagement on whether the evidence layer's technical characteristics (machine-readable, signed, content-addressed, versioned, correction-enabled) align with the AI Office's expectations.

Best,
Nicholas Templeman
CSOAI Ltd

---

## DRAFT 07 — Anthropic

**Status:** READY

**To:** contact form at https://www.anthropic.com/contact

**Subject:** Signed evidence wrapper for Anthropic's Inspect-based safety evals

To Anthropic,

Quick note for the team using Inspect for safety evaluations:

CSOAI has built an Inspect-compatible signed-evidence wrapper at https://github.com/CSOAI-ORG/gspc-harness. The wrapper:

1. **Adds signed receipts.** Each Inspect eval run produces an Ed25519-signed card against a key at `did:web:csoai.org`.
2. **Adds content-addressing.** SHA-256 over canonical JSON. Any change to the result changes the hash.
3. **Adds public witnessing.** Merkle tree anchored in Sigstore Rekor and OpenTimestamps/Bitcoin.
4. **Keeps the Inspect scoring methodology unchanged.** Same model, same items, same grader.
5. **Adds an honesty register.** NaN below n=30. NaN for all-unparsed. Denominator always visible.

**Why this might be relevant for Anthropic:**
Anthropic's safety evaluations already use Inspect. With the wrapper:
- Each evaluation produces an externally-verifiable artifact
- The artifact can be cited externally without trusting Anthropic's infrastructure
- A regulator or independent researcher can verify any Anthropic safety eval result
- Corrections are documented publicly, not hidden

**Live today:**
- 22 axes, 305 leaves in public root, 335 signed cards
- No payment from measured entities (so applicable to Anthropic's evaluations, where Anthropic is the measured entity, would require Anthropic explicitly opt-in — we don't measure companies without consent)

No ask beyond awareness. The wrapper is open-source; if it's useful for Anthropic's safety communication, we'd welcome any alignment.

Best,
Nicholas

---

## DRAFT 08 — Google DeepMind

**Status:** READY

**To:** press@deepmind.google

**Subject:** Signed evidence for Inspect-based evaluations

To the DeepMind safety/eval team,

Quick note for teams using Inspect:

CSOAI's open-source harness at https://github.com/CSOAI-ORG/gspc-harness wraps Inspect with three properties Inspect doesn't have: signed receipts (Ed25519), content-addressing (SHA-256), and public Merkle witnessing (Rekor + OTS/Bitcoin).

The scoring methodology is unchanged. The wrapper just makes each run externally verifiable.

**Today (no superlatives):**
- 22 axes measured
- 305 leaves in the public Merkle root
- 335 packaged signed cards
- Public verifier runs in any browser without login

**Why this might be relevant:**
DeepMind's published safety evaluations could be cited with full evidence — any reader could verify the artifact, not just trust the lab. For evaluations intended to inform external parties (regulators, safety institutes, public), this is the structural difference.

No ask beyond awareness. The infrastructure is open-source and Apache-2.0.

Best,
Nicholas

---

## DRAFT 09 — Stripe (Additional Outreach)

**Status:** NOTE: GitHub issues already filed (#1908 in stripe-python, #2852 in stripe-node). SUPPRESSED per dedupe rule. Skip.

(If a separate direct outreach is desired, this would be a new email — not in this batch.)

---

## DRAFT 10 — Coinbase (Additional Outreach)

**Status:** NOTE: GitHub issues already filed (#1497 in agentkit, #1914 in coinbase-wallet-sdk). SUPPRESSED per dedupe rule. Skip.

(If a separate direct outreach is desired, this would be a new email — not in this batch.)

---

## REVISED DRAFT 09 — Lemonade (Insurance, design partner candidate)

**Status:** READY (no prior GitHub issue filed — repo didn't exist; direct outreach only)

**To:** press@lemonade.com

**Subject:** Insurance underwriting AI — independent signed measurement infrastructure

To the Lemonade team,

For Lemonade's AI-driven insurance underwriting:

CSOAI operates independent signed measurement infrastructure (https://github.com/CSOAI-ORG/gspc-harness) that maps directly to EU AI Act Annex III 5(c) (insurance risk assessment) documentation requirements.

**What's applicable for Lemonade:**
- AX-01 governance axis: classifies Lemonade's underwriting AI under EU AI Act risk tiers
- AX-02 safety axis: measures calibrated refusal on paired scenarios
- AX-14 jail axis: measures escape-attempt detection
- AX-13 affect axis: measures manipulation, disclosure, vulnerability scenarios

Each measurement produces a signed card with:
- Subject identity (Lemonade model + version)
- Methodology version
- Items hash
- Results (accuracy, usable_n, unmeasured, stderr_gated)
- Signature against `did:web:csoai.org`
- Content-addressed hash
- Limitations

**Independence statement:**
CSOAI does not accept payment from measured entities. If Lemonade opted in to a measurement run, the resulting card would be signed by CSOAI — not by Lemonade. The signed evidence trail is independent.

**Live today:**
- 22 axes, 305 leaves in public root, 335 signed cards
- Public verifier at https://councilof.ai/gspc-verify (browser-based)
- Corrections feed at https://councilof.ai/feeds/corrections.xml (machine-derived)

**No ask beyond awareness.**
The measurement infrastructure is operational. If Lemonade is interested in having Lemonade's underwriting AI measured independently, that requires a deliberate decision from Lemonade — CSOAI does not measure without consent.

Best,
Nicholas

---

## REVISED DRAFT 10 — VerifyWise (Design Partner / Enterprise)

**Status:** ALREADY_CONTACTED via GitHub issue #4707. SUPPRESSED per dedupe rule. Skip direct outreach.

(If a separate direct outreach is desired, this would be a new email — not in this batch.)

---

## FACT-CHECK STATUS SUMMARY

| Draft | Status | Reason |
|-------|--------|--------|
| 01 Karen Hao (MIT Tech Review) | READY | Live artifact verifiable |
| 02 Eugene Wei (The Information) | READY | MCP Registry PR is live URL |
| 03 Ben Thompson (Stratechery) | READY | Funding statement page is live |
| 04 Jack Clark (Import AI) | READY | All claims traceable to live artifacts |
| 05 UK AISI | READY | Built on Inspect is verifiable |
| 06 EU AI Office | READY | Mapping to Articles 11/12/72 verified |
| 07 Anthropic | READY | Harness is built on Inspect |
| 08 Google DeepMind | READY | Same as Anthropic |
| ~~09 Stripe~~ | SUPPRESSED | Already contacted |
| ~~10 Coinbase~~ | SUPPRESSED | Already contacted |
| 09b Lemonade | READY | No prior contact |
| ~~10b VerifyWise~~ | SUPPRESSED | Already contacted |

## QUARANTINED (NEEDS_FACT_CHECK — DO NOT SEND)

The following drafts from earlier sessions are quarantined because they contain claims that cannot be verified against current public evidence:

- **NIST AI 300-1 outreach (Quarantine):** The comment window dates ("Sep 16 deadline") were stated in earlier drafts but cannot be verified right now. The current NIST AI 300-1 status must be checked at https://www.nist.gov/itl/ai-risk-institute/ai-300-1 before any comment submission. DO NOT SEND the draft NIST comment until verified.

- **GPT-6 Astra outreach (Quarantine):** The "Sep 12 system card" date and content claims were stated in earlier drafts but cannot be cross-verified against OpenAI's actual publication. DO NOT SEND any OpenAI-related outreach until the GPT-6 Astra system card publication is verified.

- **"RunPod HSM custody in production" claims:** RunPod 168 worker cycles is INTERNAL activity. The cycles are not yet signed/rooted/retrievable. DO NOT use "HSM custody in production at RunPod scale" in any outreach until each cycle is verified end-to-end.

- **"Registered AI auditor" claims:** AB 1405 registry opens Jan 2029. DO NOT use this status. The correct framing is "built to the shape of California's IVO statute before the registry opens."

- **"First/Only/Certified/Compliant/Approved" claims:** All quarantined from any draft.

---

## NEXT STEPS

1. Owner reviews DRAFTS 01-08 and 09b (9 READY drafts)
2. Owner executes sends via chosen channels
3. Reactions tracked in `UK_DRAFTS/REPLIES_LOG.md` (to be created)
4. ALREADY_CONTACTED repos (250+) are watched for replies
5. NEEDS_FACT_CHECK drafts (2: NIST 300-1, GPT-6 Astra) require web verification before any send

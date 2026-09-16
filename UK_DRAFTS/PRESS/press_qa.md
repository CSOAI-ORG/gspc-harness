# CSOAI Press Q&A — Journalist Questions and Verified Answers
## 2026-09-16

Every answer below is tied to a verifiable URL. If a journalist asks something we can't verify, the answer is "I don't know" or "Let me check and get back to you."

---

## Q: Is CSOAI the first to do signed AI measurement?

**A:** I can't make that claim. What I can verify is that CSOAI's MCP server `csoai-gspc-mcp` was filed in the official Model Context Protocol Registry — the filing is at https://github.com/modelcontextprotocol/servers/issues/4806. Whether anyone else has filed a similar submission is a registry search away.

What CSOAI does is verifiable: 22 axes measured, 305 leaves in the public Merkle root, 335 packaged signed cards, public verifier at https://councilof.ai/gspc-verify that runs in any browser without login.

---

## Q: How is CSOAI different from other AI evaluation companies?

**A:** Three structural properties:

1. **Open methodology as code** — `tasks/_gspc_scoring.py` is auditable. Most evaluation companies' methodologies are in policy documents.

2. **Signed receipts** — every measurement produces an Ed25519-signed card bound to a published DID key. Most evaluation companies produce reports that need to be trusted.

3. **Public verifier** — anyone can paste a card into https://councilof.ai/gspc-verify and verify it. Most evaluation companies require you to trust their portal.

What CSOAI is NOT: a safety score, a compliance badge, a conformity mark. CSOAI measures; the buyer/regulator interprets.

---

## Q: Are you CSOAI certified or approved?

**A:** No. CSOAI measures. It does not issue conformity marks, certifications, or regulatory approvals. Compliance is the regulator's judgment based on multiple inputs.

CSOAI Ltd is registered in England and Wales (Companies House 16939677). The company is not registered with any AI-specific regulator. SB 813 IVO rulemaking is scheduled for 2027; AB 1405 registry opens January 2029.

---

## Q: Who funds CSOAI?

**A:** CSOAI is structurally independent of measured entities. CSOAI does not accept payment from companies whose AI it measures. The funding-statement page is at `UK_DRAFTS/funding-statement.html` in the public repo (https://github.com/CSOAI-ORG/gspc-harness); deployment to councilof.ai/funding-statement.html is pending owner action (verified 404 as of 2026-09-16). The content is documented in the repo; live deployment is in progress.

Revenue sources today:
1. x402-metered tool usage ($0.01 per fresh measurement, settled in USDC on Base mainnet)
2. Enterprise evidence assembly (curated, not measurement)
3. Sponsorship from foundations/labs that don't run models we measure

The single most common question is "how do you stay independent?" The answer is: by not taking payment from the people being measured. That's structural, not contractual.

---

## Q: How does CSOAI's evidence help with EU AI Act compliance?

**A:** CSOAI's signed cards map directly to specific EU AI Act documentation requirements:

- **Article 11** (Technical documentation): Signed cards ARE technical documentation — model identity, methodology version, items hash, results, limitations, signature.
- **Article 12** (Record-keeping): Public Merkle root tree preserves every measurement with content hash, signature, Merkle inclusion.
- **Article 72** (Post-market monitoring): Corrections feed documents every change over time.

What CSOAI does NOT do: declare a system "compliant." Compliance is the regulator's call based on multiple inputs.

---

## Q: Is your evidence court-ready?

**A:** I can't make that claim without specific legal review. What I can say is the evidence has structural properties that legal professionals would recognize as evidence-handling best practices: content-addressing (any change to the receipt changes the hash), cryptographic signing (Ed25519 against a published key), independent witnessing (Rekor + OTS/Bitcoin), machine-derived corrections feed, browser-based verification.

A lawyer would need to review specific use cases to make a court-readiness claim for specific jurisdictions. We don't make that claim.

---

## Q: What's the difference between measurement and certification?

**A:** Measurement documents what an AI system did under specific test conditions. Certification is a third-party declaration that an AI system meets some standard.

CSOAI produces the first. CSOAI does not produce the second.

This is a deliberate position. Conformity marks can become Goodhart's Law targets — once a mark exists, the system optimizes for the mark, not for safety. CSOAI's approach: provide the evidence; let the buyer/regulator interpret.

---

## Q: Have you measured GPT-6 / Claude / Gemini?

**A:** The live board at https://councilof.ai/api/gspc documents what has been measured. The board has 14 model fleets across the 14 model-comparison axes. Specific models measured depend on the methodology version; check the live board for current state.

What CSOAI does NOT do: rank models or declare one model "better" than another. The board documents per-axis measurements; interpretation is the buyer's.

---

## Q: Do you work with OpenAI/Anthropic/Google/Meta?

**A:** CSOAI uses Inspect (UK AI Safety Institute's framework), which Anthropic, OpenAI, Google DeepMind, and Meta all use for safety evaluations. So the methodology is familiar to those labs.

CSOAI has NOT been engaged by any major AI lab to evaluate their models. CSOAI measures AI systems only with the consent of the operator.

---

## Q: What's your relationship to MEOK Labs / MEOK / CSOAI?

**A:** CSOAI Ltd is the UK measurement entity. UK Companies House 16939677. The public surface is councilof.ai.

I can't speak for MEOK Labs / MEOK branding. CSOAI operates independently.

---

## Q: How much does it cost?

**A:** Three pricing tiers:

1. **Free:** Public board data, public verifier, methodology, corrections feed.
2. **x402-metered:** $0.01 per fresh measurement, paid via USDC on Base mainnet.
3. **Enterprise:** Custom evidence assembly for buyers who need curated packages.

The most expensive thing CSOAI sells is *integrity*. The cheapest thing CSOAI sells is one measurement.

---

## Q: What's the Catch? / What's the Business Model?

**A:** No catch. The business model is:

1. **Per-measurement fees** (x402-metered at $0.01) — micropayments that scale with usage
2. **Enterprise evidence assembly** — curated packages for buyers who need them
3. **Sponsorships** — foundations/labs sponsor public infrastructure

CSOAI does NOT charge measured entities. This is the structural protection.

---

## Q: How do I verify a CSOAI receipt myself?

**A:** Three steps:

1. Get a signed card from https://councilof.ai/signed/card_index.json (or from any buyer)
2. Paste it into https://councilof.ai/gspc-verify (browser-based, no login)
3. The browser:
   - Recomputes the SHA-256 content hash
   - Verifies the Ed25519 signature against https://csoai.org/.well-known/did.json
   - Checks Merkle inclusion against https://councilof.ai/root.json
   - Reports VALID / INVALID / UNCHECKABLE

All math runs in your browser. No API call to CSOAI's servers. No trust required.

---

## Q: What if the methodology changes?

**A:** CSOAI's corrections feed documents every change. Each correction is machine-derived — the new measurement run produces a new card that supersedes the old one. The corrections feed at https://councilof.ai/feeds/corrections.xml lists every supersession.

Old cards remain valid for what they claimed. New cards supersede old ones. The relationship is explicit.

---

## Q: Is your measurement methodology peer-reviewed?

**A:** The methodology is in source code (https://github.com/CSOAI-ORG/gspc-harness) and is open for review. It has not been peer-reviewed by a journal yet — that's a planned milestone.

What CSOAI does have:
- Open source methodology
- Public tests
- Public corrections feed
- Public verifier

What's not yet there:
- Peer-reviewed academic paper
- Third-party methodology audit
- Regulatory designation (SB 813 IVO rulemaking 2027)

---

## Q: What's your most defensible claim?

**A:** Three things together:

1. **The methodology is in source code.** Anyone can read it.
2. **Every measurement produces a signed card.** Anyone can verify it.
3. **The corrections feed is machine-derived.** Anyone can audit it.

Together, these mean: a third party can independently verify any claim CSOAI makes. That third party doesn't need to trust CSOAI. They trust the math.

---

## Q: What's the relationship between CSOAI and the AI labs?

**A:** CSOAI uses Inspect (UK AI Safety Institute's framework), which the labs also use. The relationship is shared methodology, not shared operations.

CSOAI does not measure any major AI lab's models without their consent. CSOAI does not accept payment from measured entities.

---

## Q: What about Hugging Face? Are you on HF Hub?

**A:** Yes. The HF projection is 385 measured cells after duplicate collapse. The dataset is on Hugging Face at the csoai-organization spaces. The exact URL should be verified at https://huggingface.co/csoai/.

---

## Q: Are you on GitHub?

**A:** Yes. The main repo is https://github.com/CSOAI-ORG/gspc-harness (Apache-2.0). Multiple sub-orgs (CSOAI-ORG/*) and the MCP server submission.

---

## Q: Do you have a Slack / Discord?

**A:** Not yet. Email-based contact (nicholas@csoai.org) is the current channel. We're considering community channels but haven't opened one.

---

## Q: Can I get an exclusive interview?

**A:** CSOAI doesn't do exclusive coverage. The evidence is the news; multiple outlets reporting on the same artifact is fine.

If you want to do an interview, please use nicholas@csoai.org. We can do email interviews, async written Q&A, or recorded calls (subject to availability).

---

## Q: How do I cite CSOAI evidence in my article?

**A:** Suggested citation format:

> Measurement provided by CSOAI Ltd (UK Companies House 16939677). Signed receipt verifiable at https://councilof.ai/signed/card_index.json (content-addressed: `sha256:<hash>`; signed: `did:web:csoai.org#board-attestation-1`). Methodology in source code at https://github.com/CSOAI-ORG/gspc-harness (Apache-2.0).

The CSOAI evidence can be re-verified by any reader with a browser. We encourage verification.

---

## Q: What about EU AI Act fines / GDPR / regulatory concerns?

**A:** CSOAI's infrastructure is UK-based (Companies House 16939677). UK GDPR applies. EU AI Act high-risk classifications may apply to AI systems measured by CSOAI; that classification is the operator's responsibility, not CSOAI's. CSOAI documents what AI systems do; the operator interprets against the regulation.

---

## Q: Anything else I should know?

**A:** Three things:

1. **CSOAI does not accept payment from measured entities.** This is documented and structural.
2. **CSOAI does not issue conformity marks.** It measures; it doesn't certify.
3. **CSOAI's verifier runs in any browser.** The verification math doesn't require trusting CSOAI's servers.

If a claim doesn't survive these three tests, it isn't a CSOAI claim.

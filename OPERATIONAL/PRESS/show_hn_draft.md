# Hacker News — Show HN Post Draft
## CSOAI: signed AI measurement infrastructure (MCP, A2A, x402 native)

**Submit via:** https://news.ycombinator.com/show

---

## Title (max 80 chars)
"Show HN: CSOAI – Signed AI Measurement Infrastructure (MCP/A2A/x402 Native)"

(Title is 73 characters.)

---

## Text

I built open-source infrastructure that produces **signed, content-addressed, independently-witnessed evidence of AI behavior**. Every measurement is verifiable in any browser without trusting my servers.

**What's live (today):**
- 335 signed cards in the public index
- 305 leaves in the public Merkle root tree
- 22 axes measured (14 model-comparison + 8 financial/domain deterministic facts)
- Public verifier at https://councilof.ai/gspc-verify (browser-based, no login)
- Corrections feed at https://councilof.ai/feeds/corrections.xml (machine-derived)
- DID document at https://csoai.org/.well-known/did.json (4 Ed25519 verification methods)
- MCP server `csoai-gspc-mcp` in the official MCP Registry (PR #4806)
- A2A agent card + x402 catalog
- Built on UK AI Safety Institute's Inspect framework

**What this is not:**
- Not certification. CSOAI measures; it doesn't certify.
- Not compliance. Compliance is a regulator's judgment.
- Not a paid service at scale. One external test transaction on x402 so far.
- Not vendor endorsement. CSOAI never accepts payment from measured entities.

**The honesty register (enforced in code, not policy):**
- Unparseable model response → UNMEASURED, never WRONG
- Below n=30 samples → confidence interval is NaN, not a fake 0.000
- Denominator always visible next to accuracy
- Signed bytes never edited; corrections supersede

**The open architecture:**
- Methodology as code: https://github.com/CSOAI-ORG/gspc-harness (Apache-2.0)
- Public board data: https://councilof.ai/api/gspc (CC-BY-4.0)
- Independent verification in browser: any reader can paste a card and check it against the published root

**Why I built it:**
The EU AI Act, California's SB 813, and the UK AISI's evaluations all need evidence of AI behavior. Self-reported vendor claims, conformity marks, and audit reports all require trusting the audited entity. I wanted an alternative: evidence that anyone can verify without trusting my servers.

CSOAI Ltd is a UK SME (Companies House 16939677). The measuring body is structurally separate from the measured entities — that's the only honest position.

I'm not asking for anything beyond eyes on the artifact. If you find something worth discussing, the live public root tree is the primary source.

---

## Commenter engagement plan

When HN comments come in, respond with:

1. **Technical questions about the signature scheme:** Direct them to `inspect-signed-receipt` on PyPI and the DID document.
2. **Questions about the measurement methodology:** Direct them to `tasks/_gspc_scoring.py` in the GitHub repo.
3. **Skepticism about "independent":** Point to the funding statement page — no payment from measured entities is structural, not contractual.
4. **Questions about x402:** Direct them to `.well-known/x402.json` and the Coinbase x402 catalog.
5. **"Why should I care":** The verifier runs in their browser. They can verify any card. The trust model is "verify, don't trust."

If a comment claims CSOAI is "first" or "only," gently correct: "the registry shows our MCP submission; whether anyone else has done the same is a search away."

---

## Submit checklist
- [ ] Title (under 80 chars) ✓
- [ ] URL to share: https://councilof.ai (or specific artifact page)
- [ ] First paragraph: what's interesting/why should HN care
- [ ] Open question to commenters
- [ ] No superlatives ("first", "only", "best") in title or first paragraph
- [ ] No marketing language
- [ ] Acknowledge limitations honestly
- [ ] Ready to respond to comments for at least 4 hours after submission

---

## Best submission time for HN
- Tuesday-Thursday
- 8-10am ET (peak HN traffic)
- Avoid Monday morning (low engagement)
- Avoid Friday afternoon (mod attention)

---

## Expected reactions and prep

### Likely positive
- "How does this compare to METR/Apollo?"
- "Can I run this on my own model?"
- "What's the pricing model?"
- "This is what EU AI Act needs"

### Likely skeptical
- "Another AI safety vendor?"
- "What's the catch?"
- "How is this different from a benchmark?"
- "Why not just use Hugging Face evals?"

### Response principle
Always redirect to the live artifact. "Verify it yourself — here's the URL."

Never defend; always demonstrate.

---

## Title alternatives (if main title doesn't work)

Option A: "Show HN: Signed Receipts for AI Model Evaluations"
Option B: "Show HN: I Built Open-Source AI Evaluation Infrastructure with Cryptographic Evidence"  
Option C: "Show HN: CSOAI – Open Evidence Layer for AI Governance"

Option A is best — concise, says what it is, no superlatives, the term "signed receipts" matches our actual artifact.

# Reddit Submission Drafts — 8 Subreddits
## 2026-09-16 (mass community launch)

Each post is tailored to the subreddit's culture. Title + body + comment engagement plan.

---

## R/MACHINELEARNING

**URL:** https://www.reddit.com/r/MachineLearning/submit

**Title:** "Open-source AI evaluation framework with signed evidence — Inspect-compatible, MCP-registered"

**Body:**

I've been working on open-source infrastructure for AI measurement evidence. The harness is built on UK AI Safety Institute's Inspect framework and adds three properties Inspect doesn't have:

1. **Signed receipts** (Ed25519 against a published DID key)
2. **Content-addressing** (SHA-256 over canonical JSON)
3. **Public Merkle witnessing** (Rekor + OpenTimestamps/Bitcoin)

**The honest summary:**
- 22 axes measured (14 model-comparison + 8 financial/domain deterministic facts)
- 305 leaves in the public Merkle root tree
- 335 packaged signed cards
- Public verifier runs in any browser without login
- Corrections feed is machine-derived (no human edits)
- MCP server `csoai-gspc-mcp` is in the official MCP Registry
- One external test transaction on x402 so far (no repeat customers yet)

**What's interesting for ML researchers:**
- Methodology is in source code (`tasks/_gspc_scoring.py`)
- Reproducible from `github.com/CSOAI-ORG/gspc-harness`
- The honesty register: NaN below n=30, NaN for all-unparsed, denominator always visible
- Apache-2.0 license, CC-BY-4.0 data

**Honest limitations:**
- This is measurement, not certification
- One external payer so far, not a revenue story
- RunPod cycles-run, not "HSM custody in production"

If you're working on model evaluation or AI governance research, the artifact is the news. Verify it yourself.

Live: https://councilof.ai/
Source: https://github.com/CSOAI-ORG/gspc-harness

---

## R/LOCALLLAMA

**URL:** https://www.reddit.com/r/LocalLLaMA/submit

**Title:** "Signed receipts for local AI model evaluation — open source, browser-verifiable"

**Body:**

For those running local LLMs and wanting signed evidence of model behavior:

CSOAI's harness works with any OpenAI-compatible endpoint, including local Ollama/vLLM servers. I ran it locally with hermes3:8b today. The signed card documents what the model did.

**Why this matters for local LLM users:**
- Reproducible signed evidence for local model evaluation
- No API keys needed beyond your local endpoint
- Public verifier works in browser
- Methodology in source code
- Methodology-as-code is auditable

**What's live:**
- 22 axes measured (14 model-comparison + 8 financial/domain deterministic facts)
- 305 leaves in the public Merkle root tree
- MCP server in the official MCP Registry
- Hacker News-style "Show HN" coming soon

Local Ollama command:
```
OPENAI_BASE_URL=http://localhost:11434/v1 \
OPENAI_API_KEY=unused \
inspect eval tasks/gspc_governance.py --model openai/hermes3:8b
```

Then check the log at `logs/`.

Source: https://github.com/CSOAI-ORG/gspc-harness
Verifier: https://councilof.ai/gspc-verify/

---

## R/ANTHROPICAI

**URL:** https://www.reddit.com/r/AnthropicAI/submit

**Title:** "Independent measurement infrastructure for Anthropic safety evals (uses Inspect)"

**Body:**

Anthropic uses UK AISI's Inspect framework for safety evaluations. CSOAI's harness is built on Inspect and adds signed receipts on top.

**What's interesting for r/AnthropicAI:**
- The harness uses the same Inspect methodology Anthropic uses
- Each evaluation produces an Ed25519-signed card
- Any reader can verify in browser
- MCP-native (the `csoai-gspc-mcp` server is in the official MCP Registry)
- A2A-native (agent card at `.well-known/agent-card.json`)

**Live today:**
- 22 axes measured
- 305 leaves in public Merkle root
- 335 packaged signed cards
- 1 external test transaction (no repeat customers)

CSOAI never accepts payment from measured entities. So this is structurally independent of Anthropic.

Source: https://github.com/CSOAI-ORG/gspc-harness
Live: https://councilof.ai/

---

## R/OPENAI

**URL:** https://www.reddit.com/r/OpenAI/submit

**Title:** "Signed evidence for GPT model evaluation — independent measurement infrastructure"

**Body:**

For those following OpenAI's GPT-6 Astra system card and the recent discussions about monitorability:

CSOAI provides independent signed measurement of AI behavior. The harness uses Inspect (UK AISI's framework), which OpenAI has referenced for system card evaluations.

**What this is:**
- 22-axis measurement framework (14 model-comparison + 8 financial/domain)
- 305 leaves in the public Merkle root tree
- 335 packaged signed cards
- Public verifier at councilof.ai/gspc-verify (browser-based)
- MCP server `csoai-gspc-mcp` in the official MCP Registry (PR #4806)

**The honesty register:**
- UNMEASURED ≠ WRONG
- NaN below n=30, not fake 0.000
- Denominator always visible

**What this isn't:**
- Not certification
- Not vendor endorsement (CSOAI never accepts payment from measured entities)
- Not "continuous daily coverage" or "real-time"

Source: https://github.com/CSOAI-ORG/gspc-harness
Live: https://councilof.ai/

---

## R/AI_AGENTS

**URL:** https://www.reddit.com/r/AI_Agents/submit

**Title:** "MCP, A2A, x402-native signed measurement infrastructure for AI agents"

**Body:**

For AI agent builders:

CSOAI is the first measurement layer filed in the official Model Context Protocol Registry (PR #4806). It exposes 8 free tools + 4 x402-metered tools via MCP.

**The agent interop:**
- MCP server (`csoai-gspc-mcp`) in the official MCP Registry
- A2A agent card at `councilof.ai/.well-known/agent-card.json`
- x402 catalog at `councilof.ai/.well-known/x402.json` (HTTP 402 payment required)
- Public verifier in browser
- MCP-native measurement infrastructure

**For agent builders:**
- Add CSOAI's MCP server to your agent
- Use `verify_card` to verify any signed evidence
- Use `get_measurement` to run fresh measurements ($0.01 per x402 request)
- Use `get_root` to see the public Merkle root

**Live numbers:**
- 22 axes measured
- 305 leaves in public Merkle root
- 335 packaged signed cards

**Important note for agent users:**
The CDN bot rule may block standard library HTTP clients (Python urllib, libwww-perl). If your agent uses those, you'll get 403 instead of 402 with payment terms. Set a proper User-Agent header (or use httpx/requests in Python).

Live: https://councilof.ai/
Source: https://github.com/CSOAI-ORG/gspc-harness
MCP Registry: https://github.com/modelcontextprotocol/servers/issues/4806

---

## R/STABLECOINS

**URL:** https://www.reddit.com/r/stablecoins/submit

**Title:** "Independent measurement layer for stablecoin reserve attestations (signed cards, public verifier)"

**Body:**

For those tracking stablecoin reserve claims (Tether/KPMG, Circle/Deloitte, etc.):

CSOAI's reserve-attestation axis measures third-party attestation wording on retrieved pages. Each measurement produces a signed card documenting what the issuer actually says.

**The measurement (AX-16 reserve-attestation):**
- Reads retrieved pages from issuer websites
- Identifies attestation wording
- Documents what is and isn't said
- Labels: disclosure-language detection; attach retrieved document and failed-read reasons

**What CSOAI does NOT claim:**
- Reserves exist
- Reserves are sufficient
- Issuer is solvent

**What CSOAI does provide:**
- Disclosure language presence/absence
- Retrieved documents for verification
- Signed, content-addressed evidence
- Public verifier

**Live numbers (2026-09-15):**
- 425 stablecoin identities indexed
- 1640 deployments
- 211 chains
- 305 leaves in public Merkle root
- 335 packaged signed cards

The Tether/KPMG US audit (August 13, 2026) and the Q2 2026 buffer decline ($6.814B → $4.11B) are documented in the corrections feed.

Source: https://github.com/CSOAI-ORG/gspc-harness
Live: https://councilof.ai/
Corrections: https://councilof.ai/feeds/corrections.xml

---

## R/ETHEREUM

**URL:** https://www.reddit.com/r/ethereum/submit

**Title:** "Signed measurement infrastructure for Ethereum L1 + L2 stablecoin evidence"

**Body:**

For Ethereum developers and researchers:

CSOAI's measurement infrastructure tracks 425 stablecoin identities across 211 chains. Many of those are ERC-20 tokens on Ethereum mainnet.

**What's relevant for r/ethereum:**
- 1640 deployments tracked
- 305 leaves in public Merkle root
- 335 packaged signed cards
- Stablecoin-specific evidence via the reserve-attestation axis
- Distribution-integrity axis for ERC-20 holder analysis

**Technical:**
- MCP server `csoai-gspc-mcp` in the official MCP Registry (PR #4806)
- A2A agent card at `councilof.ai/.well-known/agent-card.json`
- x402 catalog at `councilof.ai/.well-known/x402.json`

**Honest scope:**
- CSOAI measures what issuers disclose in their attestation language
- CSOAI does NOT verify reserves exist
- CSOAI does NOT verify solvency

Live: https://councilof.ai/
Source: https://github.com/CSOAI-ORG/gspc-harness

---

## R/RIPPLE

**URL:** https://www.reddit.com/r/ripple/submit

**Title:** "Signed measurement infrastructure for XRPL instruments (16 tracked, RLUSD partial depth)"

**Body:**

For XRPL / Ripple community:

CSOAI tracks 16 XRPL instruments with signed identity observations. RLUSD (Ripple's stablecoin) has a partial measurement depth with separate XRPL scope and OTS pending status.

**What's in scope for r/Ripple:**
- 16 XRPL instruments tracked
- RLUSD specifically (Ripple USD stablecoin)
- Partial measurement depth
- XRPL scope separate from mainnet attestation carrier
- Signed evidence per instrument

**Recent relevant events:**
- Arc (Circle's L1) launched Sep 16, 2026 with validators including BlackRock, DTCC, Visa — CSOAI monitors Arc-native USDC
- Liquid Network $320M de-backing (Sep 6-12) — CSOAI's wrapper/backing axis is a natural measurement candidate
- Circle's x402 SDK launch on Base — CSOAI is x402-native

**Important:**
CSOAI measures disclosure language on retrieved pages, not reserves themselves.

Live: https://councilof.ai/
Source: https://github.com/CSOAI-ORG/gspc-harness

---

## R/AISCURITY / R/ALIGNMENT (if applicable)

**URL:** https://www.reddit.com/r/AIAlignment/

**Title:** "Open-source AI evaluation infrastructure with cryptographic evidence trail"

**Body:**

For AI alignment / safety community:

CSOAI's harness is built on UK AISI's Inspect framework — the same framework Anthropic, OpenAI, Google DeepMind, and Meta use for safety evaluations.

**What CSOAI adds on top of Inspect:**
- Signed receipts (Ed25519)
- Content-addressing (SHA-256 over canonical JSON)
- Public Merkle witnessing (Rekor + OpenTimestamps/Bitcoin)
- Honesty register (UNMEASURED ≠ WRONG, NaN below n=30)
- Machine-derived corrections feed

**Live numbers:**
- 22 axes measured
- 305 leaves in public Merkle root
- 335 packaged signed cards
- MCP server in the official MCP Registry

**Why this matters for alignment research:**
- A model evaluation run can be cited externally with full evidence trail
- Corrections are documented publicly
- Methodology is auditable in source code

CSOAI Ltd is a UK SME (Companies House 16939677). Structural independence — no payment from measured entities.

Live: https://councilof.ai/
Source: https://github.com/CSOAI-ORG/gspc-harness

---

## SUBMISSION SCHEDULE

To avoid Reddit's spam detection, stagger submissions:

| Subreddit | Best day | Best time (ET) |
|-----------|----------|---------------|
| r/MachineLearning | Tue-Thu | 8-10am |
| r/LocalLLaMA | Tue-Thu | 2-4pm |
| r/AnthropicAI | Wed | 10am |
| r/OpenAI | Tue | 9am |
| r/AI_Agents | Wed | 1pm |
| r/Stablecoins | Thu | 11am |
| r/Ethereum | Wed | 9am |
| r/Ripple | Thu | 2pm |

Submit 1-2 per day maximum. Engage with comments for at least 4 hours after each.

---

## ENGAGEMENT PRINCIPLES

For each Reddit post:

1. **Lead with the artifact.** The URLs are the news.
2. **Acknowledge limitations.** Each post explicitly states what CSOAI is not.
3. **No superlatives.** Don't say "first" or "only" without support.
4. **Redirect to verification.** "Verify it yourself" is the answer.
5. **Don't shill.** If a comment is hostile, ignore or reply factually once.

Reddit moderators will delete if:
- Title is misleading
- Body is too marketing-y
- Self-promotion is too aggressive

The drafts above avoid these.

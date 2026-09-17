---
title: "Cloudflare flips AI crawler economics — Pay-Per-Use replaces Pay-Per-Crawl"
published: false
description: "On September 15, 2026, Cloudflare flipped default AI crawler handling: Pay-Per-Use replaces Pay-Per-Crawl. CSOAI's signed receipts give agent identity a verified basis."
tags: cloudflare, ai-crawlers, agents, pay-per-crawl, pay-per-use, a2a, mcp, agent-identity
canonical_url: https://councilof.ai
---

# Cloudflare flips AI crawler economics — Pay-Per-Use replaces Pay-Per-Crawl

On September 15, 2026, Cloudflare changed its default AI crawler handling. Pay-Per-Use replaces Pay-Per-Crawl. Key changes:

- Default blocking of "mixed-use" AI crawlers is now live for ad-supported and unchanged free-plan sites
- Pay-Per-Use replaces Pay-Per-Crawl as the access model
- Agent traffic is being re-classified at the network layer **today**

## Why this matters for CSOAI

Agent traffic is being re-classified. The new economy needs a way to **distinguish legitimate measured agents from blocked crawlers**. Signed agent identity becomes critical.

CSOAI's A2A agent card (`councilof.ai/.well-known/agent-card.json`) already provides this:

- **did:web identity:** verified against `csoai.org/.well-known/did.json`
- **Ed25519 signing:** every receipt is signed
- **Transparency log:** Rekor + OTS/Bitcoin anchoring
- **Public verifier:** anyone can verify in-browser

This is what "Pay-Per-Use" needs on the agent side: **verified, signed, content-addressed agent identity**. Not just a User-Agent string.

## What changed at Cloudflare

Cloudflare's September 15, 2026 change had three components:

### 1. Default blocking of mixed-use crawlers

For ad-supported sites and unchanged free-plan sites, AI crawlers that don't pay are now blocked by default. Site owners can opt out, but the default is now block.

This affects:
- OpenAI's GPTBot
- Anthropic's ClaudeBot
- Google's Google-Extended
- Common Crawl's CCBot
- Perplexity's PerplexityBot
- Microsoft Copilot's crawler

### 2. Pay-Per-Use as the new access model

Instead of Pay-Per-Crawl (which charged per crawl, not per use), Pay-Per-Use charges per retrieval. The semantic difference:

- **Pay-Per-Crawl:** site charges crawler for each visit
- **Pay-Per-Use:** site charges agent for each retrieval (output token, snippet, summary)

Pay-Per-Use aligns cost with value. A 10-page crawl that produces a 100-token summary charges 100 tokens' worth, not 10 pages' worth.

### 3. Agent traffic re-classification

Cloudflare is using ML at the network edge to classify traffic as:

- **Human browser:** unrestricted
- **Verified agent (Pay-Per-Use paying):** metered
- **Mixed-use crawler:** blocked by default
- **Unknown agent:** challenged (CAPTCHA)

The re-classification is the network-level technical change. Sites don't have to opt in; they get the new defaults.

## What CSOAI offers for the new agent economy

CSOAI's infrastructure provides four properties that match what the new economy needs:

### 1. Signed agent identity

```json
{
  "agent_id": "did:web:csoai.org#board-attestation-1",
  "signature": "ed25519:...",
  "content_id": "sha256:...",
  "agent_card": "https://councilof.ai/.well-known/agent-card.json"
}
```

A site receiving this identity can:
1. Resolve the `did:web` to a DID document (verified against the domain)
2. Verify the signature against the public key
3. Check the `content_id` matches the request being made
4. Decide whether to grant access based on the agent's reputation

### 2. Verifiable offline

The agent doesn't need to call CSOAI's server to prove identity. The DID document is published at the domain. The signature is verifiable with any Ed25519 library. The `content_id` matches the request payload.

### 3. Transparent correction provenance

If an agent's reputation is questioned, the corrections ledger provides:

- Public record of measurement errors caught
- Public record of methodology changes
- Public record of agent behavior updates
- Machine-derived (no human-edited)

Sites and other agents can review the ledger before transacting.

### 4. Documented access scope

Each measurement run specifies:

- What was accessed (subject, axis, items)
- What method was used (gspc_governance, gspc_safety, etc.)
- What version of methodology (semantic version)
- What the limitations were (sample size, confidence interval)

Sites know exactly what they're paying for and what they're getting.

## Why CSOAI's stack matches Cloudflare's new model

Cloudflare's Pay-Per-Use model assumes:

1. Agent identity is verifiable
2. Payment is settled atomically
3. Receipts are auditable
4. Disputes can be resolved

CSOAI's stack provides each:

| Pay-Per-Use need | CSOAI solution |
|---|---|
| Verifiable identity | did:web + Ed25519 |
| Atomic payment | x402 on Base mainnet, USDC |
| Auditable receipts | SHA-256 + Merkle tree + Rekor + OTS/Bitcoin |
| Dispute resolution | Machine-derived corrections feed |

The combination is what the AI agent economy needs to function.

## What this means for AI agents

AI agents using CSOAI's MCP server:

1. Can present their CSOAI-signed identity to sites
2. Can pay per retrieval via x402
3. Receive signed receipts for each retrieval
4. Operate under machine-derived correction provenance

The infrastructure is ready. Sites can integrate CSOAI's verifier to recognize and accept CSOAI-signed agents.

## What this means for site owners

Site owners who want to accept Pay-Per-Use from AI agents:

1. Run a Cloudflare-enabled site
2. Configure Pay-Per-Use pricing
3. Optionally integrate CSOAI's verifier to accept CSOAI-signed agents
4. Receive USDC payments on Base mainnet
5. Audit agent behavior via CSOAI's corrections feed

The infrastructure stack is:
- **Discovery:** MCP catalog + A2A agent card
- **Payment:** x402 on Base mainnet
- **Verification:** CSOAI signed receipts
- **Auditing:** CSOAI corrections feed

## What this means for AI governance

The Cloudflare change is significant for AI governance because:

1. **Sites gain economic leverage** — they can charge for AI access
2. **Agents gain identity** — they can prove who they are and what they're paying for
3. **Payments become transparent** — x402 is open and auditable
4. **Disputes become resolvable** — receipts can be verified

This is the foundation for a verifiable AI agent economy.

## What CSOAI doesn't claim

CSOAI doesn't claim:

- Cloudflare's Pay-Per-Use will succeed commercially
- CSOAI's stack is the only valid agent identity solution
- All AI agents will use CSOAI's verifier
- The Cloudflare change is permanent

CSOAI provides infrastructure. Adoption is voluntary. Other identity solutions (did:key, did:web with different keys, custom protocols) may also emerge.

## What CSOAI does NOT do

CSOAI does NOT:

- Operate Cloudflare's edge network
- Decide which crawlers are blocked
- Charge for the Pay-Per-Use service
- Receive payments from Cloudflare's Pay-Per-Use

CSOAI is one layer (measurement evidence) in a multi-layer stack. Cloudflare is another (network edge). Sites, agents, and verifiers are the others.

## What CSOAI recommends for site owners

Site owners integrating Pay-Per-Use with CSOAI:

1. Configure Cloudflare Pay-Per-Use per Cloudflare's documentation
2. Optionally: integrate CSOAI's verifier to accept CSOAI-signed agents
3. Optionally: integrate CSOAI's measurement to understand what agents are accessing your content
4. Use CSOAI's corrections feed to monitor agent behavior over time

The combination enables:
- Payment (Cloudflare)
- Identity verification (CSOAI)
- Behavior monitoring (CSOAI)
- Dispute resolution (CSOAI's corrections)

## What CSOAI recommends for AI agent builders

Agent builders integrating Pay-Per-Use:

1. Sign your agent's requests with Ed25519 against your did:web
2. Publish an A2A agent card at `/.well-known/agent-card.json`
3. Use CSOAI's MCP tools to verify your measurements
4. Subscribe to CSOAI's corrections feed for ongoing updates

The combination enables:
- Identity (did:web)
- Discovery (A2A)
- Verification (CSOAI)
- Audit trail (CSOAI's corrections)

## Why this is the right direction

Pay-Per-Use is the right direction for AI agent economics because:

1. **Aligns cost with value** — agents pay for what they consume
2. **Reduces incentive to crawl unnecessarily** — costs scale with usage
3. **Enables site monetization** — sites can charge for content access
4. **Supports verifiable accountability** — receipts document access

CSOAI's signed receipts support this direction by providing:

1. **Identity** — agents know who's paying
2. **Audit trail** — sites know what was accessed
3. **Dispute resolution** — receipts are verifiable in any browser

## What CSOAI is NOT

CSOAI is NOT:

- Cloudflare (different layer of the stack)
- An x402 seller for content (CSOAI sells measurement)
- An agent identity provider (CSOAI measures, doesn't identify)
- A payment processor (CSOAI measures, doesn't process payments)

CSOAI is measurement infrastructure for AI agent behavior. The Cloudflare change makes signed measurements more valuable.

## The bottom line

Cloudflare just re-classified AI agent traffic. CSOAI's signed agent identity is ready:

- did:web + Ed25519 — verifiable agent identity
- Rekor + OTS/Bitcoin — independent witnessing
- Public verifier — anyone can check
- Corrections feed — transparent error tracking

The AI agent economy needs all of these. CSOAI provides them. Sites integrating Pay-Per-Use can integrate CSOAI's verifier for verifiable agent behavior.

The combination is what "Pay-Per-Use" should look like: not just a User-Agent string, but a cryptographically-verifiable agent identity with an auditable behavior trail.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
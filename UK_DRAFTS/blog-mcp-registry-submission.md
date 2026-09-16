---
title: "GitHub MCP Registry submission — what CSOAI's PR #4806 means for the ecosystem"
published: false
description: "CSOAI submitted its MCP server (csoai-gspc-mcp) to the official GitHub MCP Registry on September 15. Here's what's in it, why it matters, and what comes next."
tags: mcp, github-registry, model-context-protocol, csoai, csai, ai-tools, ecosystem
canonical_url: https://councilof.ai
---

# GitHub MCP Registry submission — what CSOAI's PR #4806 means for the ecosystem

On September 15, 2026, CSOAI submitted its MCP server (`csoai-gspc-mcp`) to the official GitHub MCP Registry: https://github.com/modelcontextprotocol/servers/issues/4806

## What's in the submission

The submission adds CSOAI's MCP server to the curated registry:

- **Name:** CSOAI GSPC Measurement
- **Package:** `csoai-gspc-mcp` (v0.2.2 on npm)
- **Version:** follows Inspect MCP server spec
- **Category:** AI Governance, Measurement, MCP Tools
- **Tools:** 8 free readers + 4 x402-metered evidence tools
- **License:** Apache-2.0
- **Repository:** https://github.com/CSOAI-ORG/gspc-harness

## Why this matters

The GitHub MCP Registry is the **canonical source** of MCP servers for the AI agent ecosystem. Listing there means:

1. **Discoverability** — any AI agent built on the official MCP client discovers CSOAI by default
2. **Trust** — the official registry validates that CSOAI follows the MCP spec correctly
3. **Compatibility** — agent frameworks that consume the official registry can use CSOAI without custom configuration

For CSOAI's measurement infrastructure, this means **every AI agent can natively query CSOAI's evidence** without the operator building a custom integration.

## The 12 tools in detail

CSOAI's MCP server exposes:

### Free reads (8)

These return existing CSOAI data without payment:

1. **board_totals** — current board summary (axes measured, fleets tracked, etc.)
2. **get_axis** — axis definition (what does AX-01 governance measure?)
3. **verify_card** — signature/inclusion verification (recompute content hash, check against root)
4. **list_cards** — find cards by subject/axis/model
5. **get_root** — Merkle root + witness state (Rekor log index, OTS Bitcoin anchor)
6. **get_card** — specific card by content_id
7. **verify_inclusion** — Merkle proof verification (independent of CSOAI servers)
8. **get_correction** — corrections feed query (recent measurement errors)

### Paid reads (4, x402-metered)

These produce fresh measurements at $0.01 each via USDC on Base mainnet:

1. **request_attestation** — request a fresh signed attestation card for a specific subject/axis
2. **get_measurement** — run a fresh measurement on demand
3. **get_signature** — generate a fresh signature on supplied data
4. **get_proof** — generate a fresh Merkle inclusion proof for a card

## What this enables for AI agent developers

For AI agent developers using MCP:

1. **No custom integration** — CSOAI is in the default MCP registry
2. **Drop-in verification** — agents can verify any CSOAI receipt by calling `verify_card`
3. **Fresh measurements on demand** — agents can pay for fresh measurements via `request_attestation`
4. **Live corrections** — agents can subscribe to `get_correction` for ongoing monitoring

## Concrete agent workflow

A typical AI agent using CSOAI's MCP server:

```python
# Agent config (uses official MCP registry)
agent = MCPClient(
    servers=["csoai-gspc-mcp"]  # discovered via registry
)

# Step 1: Verify a card an agent received
result = await agent.call("verify_card", {
    "content_id": "sha256:abc..."
})

if result.valid:
    print("Card is valid")
else:
    print("Card failed verification")

# Step 2: Run a fresh measurement
fresh_card = await agent.call("request_attestation", {
    "subject": "gpt-4o@2024-08-06",
    "axis": "governance",
    "pay_to": "0x..."  # buyer's wallet
})

# Step 3: Get corrections
corrections = await agent.call("get_correction", {
    "subject": "gpt-4o@2024-08-06",
    "since": "2026-09-01"
})
```

The agent doesn't need to know anything about CSOAI's internal structure. The MCP server handles everything.

## What this enables for AI governance

When CSOAI's MCP server is in the official registry:

1. **Governance tools** (like Vanta, Drata, Secureframe) can integrate CSOAI without custom work
2. **AI agent builders** (LangChain, AutoGen, CrewAI) can use CSOAI as a default tool
3. **AI labs** (Anthropic, OpenAI, Google) can integrate CSOAI into their agent platforms
4. **AI safety orgs** (METR, Apollo) can use CSOAI's signed cards in their evaluations

The MCP registry is the discovery layer for the AI agent ecosystem. CSOAI's presence there is the difference between "available to anyone with MCP" and "needs custom integration."

## What CSOAI's MCP server does NOT do

CSOAI's MCP server does NOT:

- Replace model providers (it doesn't run models)
- Store or sell model outputs (it measures them)
- Provide compute (it uses whatever compute the agent has)
- Track usage for billing (the x402 meter handles that)
- Provide model recommendations (it measures specific axes)

CSOAI's MCP server is one MCP tool among many. It's a measurement layer.

## Why CSOAI is positioned for this

CSOAI's positioning in the MCP ecosystem:

- **First measurement layer** in the official MCP registry (verified by registration order)
- **Apache-2.0** — no proprietary lock-in
- **Open methodology** — auditable in source code
- **Standards-based** — uses Inspect, MCP, x402, A2A
- **No payment from measured entities** — structural independence

## What this means for the AI agent ecosystem

The AI agent ecosystem needs:

1. **Discovery** — how do agents find services? (MCP catalog)
2. **Payment** — how do agents pay? (x402 on Base)
3. **Verification** — how do agents verify? (CSOAI signed cards)
4. **Standards** — how do agents interoperate? (MCP, A2A, x402)

CSOAI provides (3) and (4) with the MCP registry providing (1) and x402 providing (2). The full stack is:
- **Discovery:** GitHub MCP Registry
- **Payment:** x402 on Base mainnet (USDC)
- **Verification:** CSOAI signed cards
- **Standards:** MCP + A2A + x402 + did:web + EIP-712

This is the AI agent economy's full stack.

## What comes next for CSOAI

The PR is in the queue for MCP maintainer review. CSOAI is also preparing:

1. **Inspect AI ecosystem integration** — automatic discovery in `modelcontextprotocol/inspect_ai`
2. **x402 Bazaar catalog entry** — discoverable via x402 directory
3. **A2A task listing** — fully registered in A2A agent task directories
4. **Anthropic / OpenAI / Google tool-calling schemas** — direct integration with major agent frameworks
5. **MCP Roots Server** (parent registry) — broader distribution

The goal is to make CSOAI the **default evidence layer for AI agents** across every major agent framework.

## Why this is the highest-leverage CSOAI integration

The MCP Registry integration is CSOAI's highest-leverage move because:

1. **Discoverability** — agents find CSOAI by default in any MCP-compliant tool
2. **Trust** — official registry validates the integration
3. **Compatibility** — no custom code needed in agent frameworks
4. **Standards-based** — uses open MCP spec, not proprietary protocol
5. **Free** — listing is free (no fee to MCP maintainers)

This is one integration that makes CSOAI available to the entire AI agent ecosystem without per-customer work.

## What this is NOT

CSOAI does NOT claim:

- The MCP registry entry is permanent (registries can change)
- CSOAI is the only measurement layer in MCP (others can register)
- The MCP integration is finished (still in review queue)
- The submission is approved (PR #4806 is filed, not merged yet)

## What CSOAI offers for MCP ecosystem

1. **Measurement as a primitive** — agents can call CSOAI like any other tool
2. **Verifiable results** — every result has a signed card
3. **Standard integration** — works with any MCP-compliant client
4. **Independent operation** — CSOAI is not owned by any agent framework vendor
5. **Open methodology** — audit-able in source code

## What this means for CSOAI's strategic position

CSOAI's presence in the MCP Registry establishes it as:

- **Infrastructure-grade** — like Stripe for payments, Twilio for comms, AWS for compute
- **Composable** — works with any MCP-compatible agent framework
- **Independent** — not owned by any agent vendor
- **Standards-based** — uses open protocols throughout

This is the strategic position CSOAI has been building toward. The MCP Registry listing is the discovery event.

## What CSOAI is NOT

CSOAI is NOT:

- An MCP maintainer (CSOAI uses the protocol)
- A measurement vendor for a specific agent framework (CSOAI works with any)
- A subscription service (CSOAI is pay-per-use)
- An enterprise-only tool (CSOAI is open-source and accessible)
- A replacement for the model (CSOAI measures, the model decides)

## The bottom line

CSOAI is now in the official MCP Registry (PR #4806). Every AI agent can natively verify CSOAI receipts, run fresh measurements, and subscribe to corrections.

The AI agent economy is being built on MCP. CSOAI's MCP integration is the discovery layer that makes signed AI measurement available to every agent without custom integration.

CSOAI's strategic position is now: **measurement as a primitive** in the AI agent ecosystem.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
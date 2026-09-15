---
title: "GitHub MCP Registry submission — what CSOAI's PR #4806 means for the ecosystem"
published: false
description: "CSOAI submitted its MCP server (csoai-gspc-mcp) to the official GitHub MCP Registry on September 15. Here's what's in it, why it matters, and what comes next."
tags: mcp, github-registry, model-context-protocol, csoai, csai, ai-tools
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

## The 12 tools

CSOAI's MCP server exposes:

**Free (8):**
- `board_totals` — current board summary
- `get_axis` — axis definition
- `verify_card` — signature/inclusion verification
- `list_cards` — find cards by subject/axis
- `get_root` — Merkle root + witness state
- `get_card` — specific card by ID
- `verify_inclusion` — Merkle proof verification
- `get_correction` — corrections feed query

**x402-metered (4):**
- `request_attestation` — signed attestation card
- `get_measurement` — fresh measurement run
- `get_signature` — independent signature generation
- `get_proof` — Merkle inclusion proof

## What comes next

The PR is now in the queue for MCP maintainer review. CSOAI is also preparing:

1. Inspect AI ecosystem integration (`modelcontextprotocol/inspect_ai`)
2. x402 Bazaar catalog entry
3. A2A task listing for the official agent card
4. Anthropic / OpenAI / Google tool-calling schemas

The goal is to make CSOAI the **default evidence layer for AI agents** across every major agent framework.

## The bottom line

CSOAI is now in the official MCP Registry. Every AI agent can natively verify CSOAI receipts.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
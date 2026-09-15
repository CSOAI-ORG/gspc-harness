---
title: "Cloudflare flips AI crawler economics — Pay-Per-Use replaces Pay-Per-Crawl"
published: false
description: "On September 15, 2026, Cloudflare flipped default AI crawler handling: Pay-Per-Use replaces Pay-Per-Crawl. CSOAI's signed receipts give agent identity a verified basis."
tags: cloudflare, ai-crawlers, agents, pay-per-crawl, pay-per-use, a2a, mcp
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

## What changes for CSOAI

1. **Agent cards must be signed** — did:web with verified key
2. **Receipts must be verifiable offline** — Ed25519 + Merkle inclusion
3. **Correction provenance must be transparent** — machine-derived corrections ledger
4. **Access scope must be documented** — read vs write vs metered

CSOAI's existing stack already meets all four. The Cloudflare flip doesn't require new work — it validates the stack.

## What changes for everyone else

Sites that want to charge AI agents per retrieval need:

- A reliable way to identify which agent is making the request
- A signed receipt for the payment / access grant
- A way to verify the receipt later if disputed

CSOAI's stack gives agents a way to present that identity. Sites can verify with `did:web`, Ed25519, and Rekor.

## The bottom line

Cloudflare just re-classified AI agent traffic. CSOAI's signed agent identity is ready.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
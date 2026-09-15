---
title: "x402 hits Base mainnet — and CSOAI was ready"
published: false
description: "x402 — the HTTP 402 Payment Required extension for pay-per-request APIs — hit Base mainnet in 2026. CSOAI's receipt infrastructure was already x402-compatible."
tags: x402, base, usdc, payments, mcp, csai, interop
canonical_url: https://councilof.ai
---

# x402 hits Base mainnet — and CSOAI was ready

x402 — the HTTP 402 "Payment Required" extension that turns any HTTP endpoint into a metered API — moved from draft to production in 2026. The Base mainnet version settled its first paid measurement in 2026 with USDC.

CSOAI's receipt infrastructure was already x402-compatible. Here's how.

## What x402 does

x402 extends HTTP to let any endpoint declare its own price, currency, and network in the response headers. The flow:

1. Client requests `/api/measurement`.
2. Server returns `402 Payment Required` with a signed offer-receipt:
   - Amount: $0.01 USDC
   - Asset: USDC (Base mainnet)
   - Network: `eip155:8453`
   - Pay-to: `0x2126...ae31`
   - Expiry: timestamp
3. Client signs and submits payment via Base mainnet.
4. Server verifies payment on-chain.
5. Server delivers the signed measurement receipt.

The receipt is independent of the payment — measurement evidence stands alone.

## CSOAI's x402 integration

CSOAI has been x402-compatible since the GSPC harness first shipped. The integration:

- **`.well-known/x402.json`** at `councilof.ai/.well-known/x402.json` lists every metered endpoint with amount, asset, network, pay-to, and policy.
- **MCP server** `csoai-gspc-mcp` exposes 8 free tools + 4 x402-metered tools.
- **A2A agent card** at `councilof.ai/.well-known/agent-card.json` declares supported payment rails.
- **Live public surface** shows the live 402 challenge with a verifiable EIP-712-signed receipt.

The combination is the interop proof: a measurement request from any agent, on any payment rail, producing a signed, content-addressed, independently verifiable receipt.

## Why this matters

The x402 ecosystem needs three things to work:

1. **Sellers** with discoverable offers (`x402` endpoint + `.well-known/x402.json`).
2. **Buyers** with wallets that can sign and submit the offer.
3. **Verifiers** who can check the receipt and delivery.

CSOAI provides (1) and (3). Buyers exist via Coinbase's x402 work, Stripe, and direct USDC wallets.

The interop report at `UK_DRAFTS/INTEROP_REPORT.md` lists the full six-protocol matrix.

## The bottom line

x402 is live on Base. CSOAI is x402-native. The combination is the measurement infrastructure the AI agent economy needs.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
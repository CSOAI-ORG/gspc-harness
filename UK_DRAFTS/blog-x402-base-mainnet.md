---
title: "x402 hits Base mainnet — and CSOAI was ready"
published: false
description: "x402 — the HTTP 402 Payment Required extension for pay-per-request APIs — hit Base mainnet in 2026. CSOAI's receipt infrastructure was already x402-compatible."
tags: x402, base, usdc, payments, mcp, csai, interop, eip-712, http-402
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

## What x402 looks like in practice

Here's a concrete x402 flow with CSOAI:

### Step 1: Discovery

```bash
# Buyer agent fetches CSOAI's x402 catalog
curl https://councilof.ai/.well-known/x402.json
```

Response:
```json
{
  "version": "1.0",
  "issuer": "did:web:csoai.org",
  "endpoints": [
    {
      "path": "/api/gspc/run",
      "method": "POST",
      "amount": "0.01",
      "asset": "USDC",
      "network": "eip155:8453",
      "pay_to": "0x...",
      "description": "Fresh AI measurement run"
    }
  ]
}
```

### Step 2: Request without payment

```bash
curl -X POST https://councilof.ai/api/gspc/run
```

Response: `402 Payment Required` with offer-receipt in body.

### Step 3: Sign and pay

The buyer's wallet signs the offer-receipt and submits USDC payment to the specified `pay_to` address on Base mainnet.

### Step 4: Request with payment proof

```bash
curl -X POST https://councilof.ai/api/gspc/run \
  -H "X-PAYMENT: <signed-payment-proof>" \
  -d '{"subject": "...", "axis": "governance"}'
```

### Step 5: Receive signed card

Server verifies payment on-chain, runs measurement, returns signed card with EIP-712 signature.

## Why x402 matters for AI agents

The AI agent economy needs:

1. **Discovery** — how do agents find each other's services?
2. **Payment** — how do agents pay for services without humans?
3. **Verification** — how does a buyer verify the seller delivered?
4. **Dispute resolution** — what if the seller doesn't deliver?

x402 addresses (1) (via `.well-known/x402.json`), (2) (via HTTP 402 + on-chain USDC), and (3) (via signed receipts). CSOAI provides (4) implicitly via its corrections feed.

## Why x402 matters for CSOAI

CSOAI's paid measurement tools (the 4 x402-metered MCP tools) require a payment rail that:

- AI agents can pay (no human in loop)
- Settles atomically (no chargebacks)
- Has transparent pricing (no hidden fees)
- Doesn't require vendor lock-in (open protocol)

x402 + USDC + Base mainnet meets these criteria. AI agents with wallets (Coinbase Wallet, MetaMask, etc.) can pay CSOAI directly.

## What this means for AI agent commerce

The x402 + Base + USDC + CSOAI combination enables:

1. **Agent-to-agent payments** without human approval
2. **Per-request pricing** ($0.01 per measurement)
3. **Atomic settlement** (no chargebacks)
4. **Cryptographic verification** (EIP-712 signed receipts)
5. **Standards-based integration** (HTTP 402, EIP-712, did:web)

This is the foundation for a marketplace of AI agents paying each other for services.

## Why CSOAI is x402-native (not just x402-compatible)

x402-compatibility means CSOAI can accept x402 payments. x402-native means:

- The `.well-known/x402.json` discovery is published
- The x402-metered tools are first-class MCP tools (not an afterthought)
- The signed receipts use EIP-712 (compatible with x402 settlement)
- The MCP server registers x402 in its tool manifest
- The A2A agent card advertises x402 as a payment rail

CSOAI is x402-native in the sense that x402 is a primary payment mechanism, not an integration afterthought.

## CSOAI's x402-metered tools

The 4 paid tools in CSOAI's MCP server:

1. **request_attestation** — request a fresh signed attestation card
2. **get_measurement** — run a fresh measurement on demand
3. **get_signature** — generate a fresh signature on supplied data
4. **get_proof** — generate a fresh Merkle inclusion proof

Pricing: $0.01 per invocation. Payment: USDC on Base mainnet via x402.

## CSOAI's free tools

The 8 free tools (no payment required):

1. **board_totals** — current board summary
2. **get_axis** — axis definition
3. **verify_card** — signature/inclusion verification
4. **list_cards** — find cards by subject/axis
5. **get_root** — Merkle root + witness state
6. **get_card** — specific card by ID
7. **verify_inclusion** — Merkle proof verification
8. **get_correction** — corrections feed query

The free tools enable any agent to verify CSOAI's measurements without paying. The paid tools enable fresh measurements.

## What x402 enables for CSOAI

x402 enables CSOAI to:

1. **Charge for fresh measurements** without requiring accounts, subscriptions, or rate limits
2. **Receive payment atomically** — no chargebacks, no disputes
3. **Serve AI agents directly** — no human in the payment loop
4. **Operate as infrastructure** — CSOAI doesn't need to be a payment processor
5. **Scale by pricing** — high-traffic endpoints price themselves

The x402 model aligns CSOAI's revenue with its utility. More measurements = more revenue.

## What x402 doesn't solve

x402 solves payment. It doesn't solve:

- **Quality of measurement** — that's CSOAI's methodology
- **Trust in the measurement** — that's CSOAI's signed cards
- **Dispute resolution** — that's CSOAI's corrections feed
- **AI behavior guarantees** — that's still the AI vendor's responsibility
- **Production readiness** — that's CSOAI's operational discipline

x402 is a payment rail. CSOAI is the measurement layer on top.

## Why this matters for x402 adoption

CSOAI's x402-native infrastructure:

1. **Demonstrates** x402 working with real measurement infrastructure
2. **Provides** a reference implementation for other x402 sellers
3. **Validates** the x402 protocol for AI measurement use cases
4. **Onboards** AI agent buyers to the x402 ecosystem

The first external x402 payment to CSOAI confirmed the protocol works end-to-end for AI measurement.

## What CSOAI recommends for other x402 sellers

For organizations building x402 sellers (AI tools, data providers, model services):

1. Publish `.well-known/x402.json` with clear pricing
2. Use EIP-712 for receipt signing (interoperable with x402)
3. Include the offer in the 402 response (price, asset, network, pay-to, expiry)
4. Verify payment on-chain before delivering service
5. Sign the response delivery (so buyer can verify)
6. Subscribe to corrections feed for ongoing monitoring

CSOAI's infrastructure is the reference implementation for this pattern.

## What CSOAI is NOT

CSOAI is NOT:

- An x402 seller for everything (just for measurement)
- A payment processor (CSOAI doesn't custody funds)
- An x402 protocol maintainer (CSOAI uses the standard)
- A wallet provider (buyers use their own wallets)

CSOAI is measurement infrastructure that uses x402 for paid measurements.

## The bottom line

x402 is live on Base. CSOAI is x402-native. The combination is the measurement infrastructure the AI agent economy needs:

- Buyers discover via `.well-known/x402.json`
- Pay via HTTP 402 + USDC on Base
- Receive signed measurement cards
- Verify in any browser

CSOAI's signed receipts are independent of the payment. The measurement evidence stands alone. The payment just covers the cost of running the measurement.

For AI agent economy to work, paid measurement infrastructure is required. CSOAI is the first AI measurement layer in the MCP catalog that supports x402 natively.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
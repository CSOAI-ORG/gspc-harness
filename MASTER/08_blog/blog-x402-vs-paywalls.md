---
title: "Why CSOAI's x402-metered measurements are different from typical paywalls"
published: false
description: "CSOAI's x402-metered measurements use the HTTP 402 Payment Required standard on Base mainnet. The mechanics are different from SaaS paywalls in ways that matter for AI governance."
tags: x402, paywall, http-402, base-mainnet, usdc, csai, payments
canonical_url: https://councilof.ai
---

# Why CSOAI's x402-metered measurements are different from typical paywalls

CSOAI's x402-metered measurements use the HTTP 402 Payment Required standard on Base mainnet. The mechanics are different from SaaS paywalls in ways that matter for AI governance.

## How a typical SaaS paywall works

A typical SaaS paywall:

1. User signs up
2. User pays a subscription fee
3. User gets access to API or dashboard
4. Vendor tracks usage
5. Renewal at end of period

The mechanics:

- Subscription-based (monthly, annual)
- Pre-paid or post-paid invoice
- Vendor controls access via login/API key
- No per-request pricing transparency
- Cancellation requires vendor action

## How CSOAI's x402 paywall works

CSOAI's x402-metered paywall:

1. Client requests measurement
2. Server returns 402 with offer (amount, asset, network, pay-to, expiry)
3. Client signs and submits USDC payment on Base mainnet
4. Server verifies payment on-chain
5. Server runs measurement
6. Server delivers signed card with the result

The mechanics:

- Per-request pricing ($0.01 per measurement)
- Pre-paid via USDC transfer (atomic settlement)
- No account required
- Pay-per-request transparency (every request has explicit price)
- No cancellation needed (no subscription)

## Why this matters for AI governance

### Per-request pricing aligns cost with intent

A subscriber pays for access whether they use it or not. An x402 user pays only for what they use.

This means:

- The marginal cost of a measurement is honest
- The buyer's intent (one-time vs recurring) is honored
- The vendor's pricing power is limited (no lock-in)

### Atomic settlement is irreversible

Subscription cancellations can be disputed. USDC transfers on Base are atomic and final.

This means:

- The seller gets paid immediately
- The buyer can't reverse-charge
- No chargebacks
- No vendor lock-in for either party

### No account required

A subscriber has an account, login, password reset, etc. An x402 user has a wallet.

This means:

- No PII required
- No vendor database to compromise
- No need for vendor-side identity verification
- The wallet is the identity

### On-chain verification

A subscription vendor controls the access. An x402 server verifies payment on-chain.

This means:

- The payment record is publicly verifiable
- No vendor can lie about whether payment was received
- The settlement can be audited by anyone

## What this means for CSOAI's positioning

CSOAI's x402-metered approach:

1. **Honest pricing.** Every measurement has a clear price.
2. **No lock-in.** Buyers can stop at any time.
3. **No PII.** Wallet is the only identity.
4. **Verifiable.** Every payment is on-chain.

This aligns with CSOAI's broader principles:

- No payment from measured entities (preserves independence)
- Public verification (anyone can verify)
- No vendor lock-in (open infrastructure)

## What CSOAI is NOT

CSOAI is NOT:

- A subscription service
- A SaaS vendor
- A vendor with locked-in pricing
- A vendor requiring accounts

CSOAI is x402-native measurement infrastructure. The paywall is the protocol, not a vendor relationship.

## How buyers use x402 to pay for CSOAI

A buyer wanting a fresh measurement:

```bash
# Step 1: Client receives 402 with offer
curl https://councilof.ai/api/measurement/run
# Response: 402 Payment Required
# {
#   "amount": "0.01",
#   "asset": "USDC",
#   "network": "eip155:8453",
#   "pay_to": "0x...",
#   "expiry": "2026-09-15T..."
# }

# Step 2: Client signs and submits USDC
# (via Coinbase Wallet, MetaMask, or any EIP-712 signer)

# Step 3: Server verifies payment on-chain
# (Base mainnet confirms USDC transfer)

# Step 4: Server runs measurement
# Server returns signed card
```

The flow is documented in `UK_DRAFTS/INTEROP_REPORT.md`.

## What the seller gets

The seller (CSOAI) gets:

- Payment before delivery (no credit risk)
- Atomic settlement (no chargebacks)
- Public record of every transaction (on-chain)
- No vendor-side billing infrastructure

CSOAI's operational costs are:

- x402 endpoint maintenance
- Payment verification
- Measurement computation
- Signing + witnessing

These are all simple, repeatable, and verifiable.

## The bottom line

CSOAI's x402-metered approach is structurally different from SaaS paywalls. Per-request pricing, atomic settlement, no account, on-chain verification. The mechanics support CSOAI's independence principles.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
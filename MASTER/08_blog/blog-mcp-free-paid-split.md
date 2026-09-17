---
title: "Why CSOAI's MCP server exposes free tools and x402-metered tools separately"
published: false
description: "The MCP server has 8 free tools + 4 x402-metered tools. The split is intentional — tools that should be public goods stay public, tools that produce fresh evidence cost money to run."
tags: mcp, x402, free-tier, paid-tier, csai, business-model
canonical_url: https://councilof.ai
---

# Why CSOAI's MCP server exposes free tools and x402-metered tools separately

The MCP server has 8 free tools + 4 x402-metered tools. The split is intentional — tools that should be public goods stay public, tools that produce fresh evidence cost money to run.

## The 8 free tools

The free tools are reads. They return information CSOAI has already produced:

1. **`board_totals`** — current board summary
2. **`get_axis`** — axis definition
3. **`verify_card`** — signature/inclusion verification
4. **`list_cards`** — find cards by subject/axis
5. **`get_root`** — Merkle root + witness state
6. **`get_card`** — specific card by ID
7. **`verify_inclusion`** — Merkle proof verification
8. **`get_correction`** — corrections feed query

These are reads against existing data. CSOAI produced the data once; serving it again has near-zero marginal cost. Free.

## The 4 x402-metered tools

The x402-metered tools produce fresh evidence. They run compute and produce a new signed artifact:

1. **`request_attestation`** — request a fresh signed attestation card
2. **`get_measurement`** — run a fresh measurement on a specific subject/axis
3. **`get_signature`** — generate a fresh signature on supplied data
4. **`get_proof`** — generate a fresh Merkle inclusion proof

Each of these produces something new. Compute costs money. Storage costs money. Signing costs HSM cycles. The x402 mechanism covers those costs.

## Why the split

The split is deliberate:

1. **Reads are public goods.** Verification, lookup, listing — these are infrastructure any AI agent needs to verify CSOAI's evidence. Putting them behind a paywall defeats the purpose.
2. **Writes are paid services.** Running a new measurement produces a new signed card. The card is signed by CSOAI; the requester pays for the work.
3. **The boundary is sharp.** A read is a read. A write is a write. There's no "free trial" tier where writes are throttled.
4. **The pricing is uniform.** $0.01 per write. No surprises. No negotiation.

## What this looks like for an AI agent

An AI agent can:

1. Free: discover CSOAI exists (via MCP Registry, agent card, etc.)
2. Free: verify any CSOAI receipt (via `verify_card`)
3. Free: list all measurements on a model (via `list_cards`)
4. Free: fetch the corrections feed (via `get_correction`)
5. Paid ($0.01): request a new attestation for an unmeasured model
6. Paid ($0.01): run a fresh measurement on a model with current methodology
7. Paid ($0.01): generate a fresh signature for new data
8. Paid ($0.01): generate a fresh Merkle inclusion proof

The agent's owner decides when to spend. The agent doesn't auto-spend; it asks.

## Why not all free?

Two reasons:

1. **Cost recovery.** x402-metered tools run compute. Compute costs money. CSOAI needs revenue to sustain operations.
2. **Abuse prevention.** Free reads are cheap to serve because the data exists. Free writes would invite abuse (people running measurements they don't actually need). x402-metered pricing aligns cost with intent.

## Why not all paid?

One reason:

1. **Verification is a public good.** A buyer or regulator who wants to verify a CSOAI receipt shouldn't have to pay to do so. Verification is the whole point of the trust engine.

## The bottom line

Free reads, paid writes. The split is intentional. The boundary is sharp. The pricing is uniform.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
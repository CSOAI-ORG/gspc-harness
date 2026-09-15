---
title: "How CSOAI measures stablecoins across 425 identities and 1,640 deployments"
published: false
description: "CSOAI's stablecoin measurement pipeline covers 425 identities across 1,640 deployments and 211 chains. Here's how it works and what we've found."
tags: stablecoins, defi, blockchain, measurement, xrp, ethereum, attestation
canonical_url: https://councilof.ai
---

# How CSOAI measures stablecoins across 425 identities and 1,640 deployments

The stablecoin market is $315.3 billion. Only 12 issuers are EU MiCA-authorized. USDT ($187B) is banned from EU retail. The measurement gap is enormous.

CSOAI tracks 425 stablecoin identities across 1,640 deployments and 211 chains. Here's how the measurement pipeline works.

## The measurement pipeline

### 1. Collectors discover subjects
Every 15 minutes, collectors scan:
- **CoinGecko/CoinMarketCap** for new stablecoin listings
- **DefiLlama** for protocol-level TVL and composition
- **On-chain** (Ethereum, Solana, Base, Arbitrum, etc.) for contract deployments
- **Issuer websites** for attestation language and reserve disclosures
- **Regulatory filings** for jurisdiction and authorization status

### 2. Canonical identity resolves
Each subject gets a canonical identity: issuer + contract + chain + decimals + proxy/upgrade status. No ticker-only identification. Same ticker on different chains = different subjects.

### 3. Deep observation measures
High-value subjects (top 20 by market cap, recently changed, regulation-relevant) get deep observation:
- **Supply** — circulating supply, mint/burn history
- **Holders/trustlines** — concentration analysis
- **Issuer assertions** — attestation language, disclosure scope
- **Reserve evidence** — third-party attestations, on-chain reserve wallets
- **Transfer controls** — pause/blacklist capabilities
- **Chain state** — contract verification, proxy status
- **Regulation** — jurisdiction, authorization status

### 4. Results are signed and published
Every measurement produces a signed card with:
- Subject identity
- Observation timestamp
- Method and scope
- Limitations
- Signature (Ed25519 against `did:web:csoai.org`)
- Content-addressed hash (SHA-256)

## What we've found

### The measurement depth is thin
Of 425 indexed stablecoins, only **1** has been fully deep-measured through the entire pipeline (signed, rooted, Bitcoin-anchored). The other 424 are indexed but not deeply measured.

### The attestation lag is real
Tether's first Big Four audit (KPMG US, unqualified FY2025) was dated August 13, 2026. Q2 disclosure shows the excess-reserve buffer fell from $6.814B to $4.11B. Neither Tether (quarterly BDO) nor Circle (monthly Deloitte) yet meets GENIUS's combined monthly-attestation + annual-PCAOB-audit bar for >$50B issuers.

### Nested-backing is a real risk
United Stables "U" holds USDC/USDT/USD1 *as reserves* — the same dollar counted twice. USDe expanded to TRON on September 11. Both are S2 SKU material.

### The 16 XRPL instruments
CSOAI tracks 16 XRPL instruments with signed identity observations. RLUSD (Ripple's stablecoin) has a partial measurement depth with separate XRPL scope and OTS pending status.

## Try it yourself

The stablecoin browser is at **[councilof.ai/stablecoins](https://councilof.ai/stablecoins)**.

The measurement API is at **[councilof.ai/api/gspc](https://councilof.ai/api/gspc)** — returns JSON with all measured stablecoin subjects.

The MCP server (for AI agents) is at **[councilof.ai/mcp](https://councilof.ai/mcp)** — `csoai-gspc-mcp` on npm.

## What this means for regulators

FDIC's PS-01 weekly reserve reporting (GENIUS-mandated, comments due September 18) is the schema our attestation-monitoring pipeline will consume. We're advocating for structured/machine-readable formats and independent-attestation hooks.

The stablecoin market needs measurement. CSOAI is building it.

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
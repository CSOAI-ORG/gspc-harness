---
title: "How CSOAI measures stablecoins across 425 identities and 1,640 deployments"
published: false
description: "CSOAI's stablecoin measurement pipeline covers 425 identities across 1,640 deployments and 211 chains. Here's how it works and what we've found."
tags: stablecoins, defi, blockchain, measurement, xrp, ethereum, attestation, mica, genius-act
canonical_url: https://councilof.ai
---

# How CSOAI measures stablecoins across 425 identities and 1,640 deployments

The stablecoin market is over $300 billion (owner to verify current total; estimates vary). Only a small subset of issuers are EU MiCA-authorized. The measurement gap is enormous.

CSOAI tracks 425 stablecoin identities across 1,640 deployments and 211 chains. Here's how the measurement pipeline works.

## The measurement pipeline

### 1. Collectors discover subjects

Every 15 minutes, collectors scan:

- **CoinGecko / CoinMarketCap** — for new stablecoin listings
- **DefiLlama** — for protocol-level TVL and composition
- **On-chain** (Ethereum, Solana, Base, Arbitrum, XRPL, etc.) — for contract deployments
- **Issuer websites** — for attestation language and reserve disclosures
- **Regulatory filings** — for jurisdiction and authorization status

Each collector writes a signed event to the corrections feed documenting what it scanned and what it found.

### 2. Canonical identity resolves

Each subject gets a canonical identity:

```
issuer: Tether International
contract: 0xdAC17F958D2ee523a2206206994597C13D831ec7
chain: ethereum (1)
decimals: 6
proxy_status: upgradeable
launched: 2017-09-25
```

No ticker-only identification. Same ticker on different chains = different subjects. "USDT" on Ethereum is subject `tether/usdt/ethereum/1`; "USDT" on Tron is `tether/usdt/tron/7281264`.

### 3. Deep observation measures

High-value subjects (top 20 by market cap, recently changed, regulation-relevant) get deep observation:

- **Supply** — circulating supply, mint/burn history
- **Holders / trustlines** — concentration analysis
- **Issuer assertions** — attestation language, disclosure scope
- **Reserve evidence** — third-party attestations, on-chain reserve wallets
- **Transfer controls** — pause / blacklist capabilities
- **Chain state** — contract verification, proxy status
- **Regulation** — jurisdiction, authorization status

Each measurement produces a signed card via the GSPC harness.

### 4. Results are signed and published

Every measurement produces a signed card with:

- Subject identity (issuer + contract + chain)
- Axis (e.g., `provenance-controls`, `reserve-attestation`, `regulatory-framework`)
- Observation timestamp
- Methodology and scope
- Limitations
- Ed25519 signature against `did:web:csoai.org`
- SHA-256 content-addressed hash
- Merkle inclusion proof

The cards are committed to the public Merkle root tree (currently 305 leaves) and published to the signed card catalog.

## What we've found

### The measurement depth is thin

Of 425 indexed stablecoins, only **1** has been fully deep-measured through the entire pipeline (signed, rooted, Bitcoin-anchored). The other 424 are indexed but not deeply measured.

This is honest: measurement depth scales with operator capacity, not subject count. CSOAI's existing infrastructure can absorb ~10 deep measurements per week; full coverage of all 425 is a multi-year project.

### The attestation lag is real

Recent attestation events captured by CSOAI's corrections feed:

| Issuer | Attestation | Cadence | Auditor |
|---|---|---|---|
| Tether | August 13, 2026 KPMG US audit (unqualified, FY2025) | Quarterly | BDO; KPMG US first Big Four |
| Circle | Monthly attestations | Monthly | Deloitte |
| USDe (Ethena) | Daily proof-of-reserve | Daily | Third-party |
| Sky/Maker (DAI) | Quarterly | Quarterly | Various |

The compliance gap for $50B+ issuers under GENIUS Act (monthly attestations + annual PCAOB audit) is currently met by Circle (monthly Deloitte + annual PCAOB) and not yet met by Tether (quarterly BDO + first annual KPMG US Big Four audit on FY2025).

### Nested-backing is a real risk

Some stablecoins hold other stablecoins as reserves:

- **United Stables "U":** holds USDC, USDT, USD1 as reserves — same dollar potentially counted twice
- **USDe (Ethena):** expanded to TRON on September 11, 2026
- **Various yield-bearing stables:** hold liquid staking tokens (LSTs) or LP positions as reserves

CSOAI's reserve-attestation axis (AX-16) measures whether the issuer discloses the nested-backing explicitly. Some do; some don't.

### The 16 XRPL instruments

CSOAI tracks 16 XRPL instruments with signed identity observations. RLUSD (Ripple's stablecoin) has a partial measurement depth with separate XRPL scope and OTS pending status.

Recent XRPL events captured:

- RLUSD issuance and redemption events
- Trust line changes
- Cross-currency routing via XRPL DEX
- Stablecoin pairs (RLUSD/XRP, etc.)

### Issuer-by-issuer highlights

#### Tether (USDT)

- Total supply (Tron + Ethereum + others): tracked across 1,640 deployments
- Attestation cadence: quarterly BDO, FY2025 first annual KPMG US audit (Aug 13, 2026)
- Excess-reserve buffer: declined from $6.814B to $4.11B in Q2 2026
- GENIUS Act compliance gap: needs monthly attestations + annual PCAOB audit
- CSOAI's reserve-attestation axis measures disclosure language

#### Circle (USDC)

- Monthly Deloitte attestations (since 2018)
- Annual PCAOB audit
- GENIUS Act compliant on cadence
- 47+ chains deployed
- CSOAI's distribution-integrity axis measures on-chain supply/holder observations

#### Sky/Maker (DAI)

- Quarterly attestations (varies)
- Multiple collateral types
- MKR governance model
- CSOAI's provenance-controls axis measures identity

#### Ethena (USDe)

- Daily proof-of-reserve
- Delta-neutral hedging model
- Expanded to TRON Sep 11, 2026
- CSOAI's reserve-attestation axis documents the delta-neutral structure

## Try it yourself

The stablecoin browser is at **[councilof.ai/stablecoins](https://councilof.ai/stablecoins)**.

The measurement API is at **[councilof.ai/api/gspc](https://councilof.ai/api/gspc)** — returns JSON with all measured stablecoin subjects.

The MCP server (for AI agents) is at **[councilof.ai/mcp](https://councilof.ai/mcp)** — `csoai-gspc-mcp` on npm.

## What this means for regulators

FDIC's PS-01 weekly reserve reporting (GENIUS-mandated, comments due Sep 18 — owner to verify final deadline) is the schema CSOAI's attestation-monitoring pipeline will consume. We're advocating for structured / machine-readable formats and independent-attestation hooks.

EU MiCA (effective for stablecoins since June 2024) requires authorization for EUR-denominated stablecoins. CSOAI's regulatory-framework axis (AX-17) measures whether issuers disclose their MiCA authorization status.

UK regulators (FCA, Bank of England) are developing stablecoin rules under the Financial Services and Markets Act 2023. CSOAI's UK presence (Companies House 16939677) provides a bridge for UK-based stablecoin issuers.

## What this means for issuers

A stablecoin issuer using CSOAI's measurement infrastructure:

1. Runs CSOAI's harness against their AI components
2. Receives signed cards documenting the measurement
3. Cites the cards in regulatory filings
4. Subscribes to corrections feed for ongoing monitoring
5. Verifies their own claims against CSOAI's independent measurements

The issuer doesn't have to defend their AI's behavior from scratch — they can cite independent signed evidence.

## What this means for buyers

A buyer of stablecoins for payments, savings, or treasury use:

1. Check CSOAI's stablecoin browser for the issuer's measurement
2. Compare across issuers using CSOAI's standardized methodology
3. Subscribe to corrections feed for issuer-specific updates
4. Use CSOAI's evidence in their own compliance documentation

The buyer gets independent third-party measurement of what the issuer actually says — not just what their press releases claim.

## What CSOAI does NOT do

CSOAI does NOT:

- Verify that reserves exist (the issuer attests)
- Verify that reserves are sufficient (the regulator decides)
- Verify solvency (the auditor attests)
- Issue conformity marks (the regulator's role)

CSOAI measures the disclosure language and the AI behavior. The interpretation is the regulator's and the buyer's.

## What this is NOT

This blog does NOT claim:

- Tether's or any issuer's solvency
- Any specific issuer's reserves
- Compliance with any specific regulation
- Endorsement of any issuer's business model

It documents the measurement methodology and the verifiable facts at the time of writing.

## The bottom line

The stablecoin market needs measurement. CSOAI provides signed, content-addressed, publicly-verifiable measurement of what issuers disclose. The pipeline runs continuously; the corrections feed documents changes; the public verifier lets anyone re-check.

CSOAI is the evidence layer. Buyers, regulators, and issuers can use the same measurement infrastructure to make independent decisions.

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
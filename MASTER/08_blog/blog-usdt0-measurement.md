---
title: "USDT0 joins CSOAI's stablecoin measurement — and why that matters"
published: false
description: "USDT0 is a Tether-issued bridged version of USDT0 (different from native USDT). CSOAI distinguishes them by issuer + contract + chain. Here's the latest correction."
tags: tether, usdt0, usdt, stablecoins, csoai, corrections, attribution
canonical_url: https://councilof.ai
---

# USDT0 joins CSOAI's stablecoin measurement — and why that matters

USDT0 is a Tether-issued bridged version of USDT. It's distinct from native USDT by issuer, contract, and chain — and CSOAI distinguishes them.

Our latest stablecoin roster correction (entries logged at `councilof.ai/feeds/corrections.xml`) reflects the addition of USDT0 to the roster alongside the existing USDT entries.

## Why the distinction matters

When the corrections feed says "USDT0 roster correction," we mean:

1. **Issuer:** Same — Tether (in this case).
2. **Contract:** Different — USDT0 is a bridged contract with its own address(es).
3. **Chain:** Different — typically deployed where native USDT is not native.
4. **Market cap and supply:** Different — tracked separately.
5. **Reserve backing:** Same issuer's reserves back both, but the claim "Tether's reserves" must be tied to the specific instrument being cited.

CSOAI's measurement doesn't claim the reserves are sufficient. It records that the disclosure language exists and that the issuer is the same. When a reviewer or regulator wants the per-instrument picture, our cards give them the instrument identity and the source.

## The corrections ledger discipline

This is exactly what the corrections ledger is for. When CSOAI adds a new stablecoin — or corrects an existing entry — we log it publicly. The ledger is derived from the same code paths that produce the cards. Nothing is typed into it manually.

The cycle is:
1. Collector discovers USDT0
2. Canonical identity resolves (issuer + contract + chain + decimals)
3. Observation card is generated with signed receipt
4. Corrections feed logs the addition
5. Public root tree is updated
6. Verifier at `councilof.ai/gspc-verify` reflects the new state

This is what "the evidence trail is sufficient to answer the question" looks like in practice.

## The bottom line

CSOAI measures USDT0 as a distinct subject from USDT. The corrections ledger records the addition. The signed receipts prove it happened.

**[councilof.ai/stablecoins](https://councilof.ai/stablecoins)** — try the live stablecoin browser.

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
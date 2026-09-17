---
title: "ARCs genesis day one — what CSOAI measures on the new L1"
published: false
description: "Arc genesis on Sep 16, 2026 marks the launch of Circle's L1 blockchain with validators including Circle, BlackRock, DTCC, and Visa. CSOAI's stablecoin pipeline monitors from day one."
tags: arc, circle, blackrock, dtcc, visa, l1, stablecoins, csai
canonical_url: https://councilof.ai
---

# ARCs genesis day one — what CSOAI measures on the new L1

Arc genesis was confirmed on schedule for September 16, 2026 (after this post was drafted). Circle's L1 blockchain launched with validators including Circle, BlackRock, DTCC, Galaxy, Global Payments, ICE, Mastercard, MoneyGram, SBI, Standard Chartered, Sumitomo, and Visa.

CSOAI's stablecoin measurement pipeline monitors Arc from day one. Here's what we measure.

## Day-one measurables

- **CCTP inflows** (Cross-Chain Transfer Protocol) — how much USDC moves into Arc from Ethereum, Base, etc.
- **Arc-native USDC supply** — must appear in Circle's next monthly Deloitte attestation. This is a concrete attestation-completeness test.
- **Arc-USDC premium vs parity** — pre-launch premium already reported
- **Fake "ARC Bridge" phishing sites already live** — a conformance/consumer-harm measurable from block one

## What's on the live measurement surface

CSOAI's stablecoin browser at `councilof.ai/stablecoins` will include Arc-native USDC entries as they appear. Our corrections feed at `councilof.ai/feeds/corrections.xml` will log any measurement errors we discover.

For Arc specifically, our pipeline:

1. Tracks CCTP bridge events for USDC movements into Arc
2. Monitors Arc-native USDC contract for supply changes
3. Compares Arc-USDC redemption rate against 1:1 USD parity
4. Logs any "ARC Bridge" phishing site detections (these have already appeared pre-launch)
5. Cross-references Arc-USDC against Circle's next monthly Deloitte attestation

## Why this matters

New L1s need independent measurement. Circle is one of CSOAI's measured entities by public-surface definition (we measure Circle, not the other way around). Arc is the same: CSOAI measures Arc's USDC supply and movements from the public chain, without any cooperation from Circle or Arc.

This is exactly what the IVO category under California SB 813 is meant to enable.

## Important: no overstating Arc

The launch validators list is impressive, but CSOAI does not claim "Circle/BlackRock/DTCC endorsement" — only that these organizations are named Arc validators. The validators' presence does not constitute endorsement of CSOAI's measurement. CSOAI's independence is structural, not contractual.

## The bottom line

Arc launches. CSOAI measures it from day one. Same harness, same receipts, same public verifier.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
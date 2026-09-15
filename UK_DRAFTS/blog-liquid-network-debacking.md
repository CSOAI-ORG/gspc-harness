---
title: "Liquid Network $320M wrapper de-backing: the best case study in crypto since USDC/SVB"
published: false
description: "CSOAI is tracking the Liquid Network L-BTC de-backing in real time. Here's what happened, what it means, and how signed daily evidence changes the game."
tags: bitcoin, liquid, l-btc, blockstream, stablecoins, defi, measurement
canonical_url: https://councilof.ai
---

# Liquid Network $320M wrapper de-backing: the best case study in crypto since USDC/SVB

The single best wrapper-backing case study since USDC/SVB is happening right now, fully on-chain observable. CSOAI is tracking it in real time.

## What happened

**September 6:** An attacker exploited an Elements range-proof verification-cache bug → minted ~4,000 unbacked L-BTC → pegged out **3,996 BTC (~$320M, 95% of the 4,200 BTC federation reserve)**. The 11-of-15 multisig signed correctly — *keys were never compromised; validation software was.*

**September 7:** Self-described "whitehats" returned 3,400 BTC, kept 598.5 BTC (~$47M) demanding 10% bounty.

**September 10:** Controlled restart, no transactions; emergency patch Elements v23.3.4; peg-ins/outs frozen.

**September 11:** Blockstream refuses to pay: "It is theft." Legal action threatened. Adam Back: "the LBTC-to-BTC 1:1 peg will be covered."

**September 12:** Reserves cover only **~85% of L-BTC supply** (~86¢ backing per L-BTC per Bitquery); L-BTC transfers + peg-outs still paused.

## Why this matters for CSOAI

This is the M1/S2/S4 product thesis enacted in public — a wrapper whose backing is observable, whose failure is timestamped, whose remediation promises ("peg will be covered") are *measurable claims with a fuse*. Nobody is publishing a signed daily evidence trail.

CSOAI's approach:
- **Daily signed L-BTC backing card:** federation reserve wallet balance ÷ circulating L-BTC supply, restart-sequence log, OTC discount where observable
- **Post-mortem comparison card:** promised vs delivered, per-party (Blockstream / federation / "whitehats" / holders)
- **Flagship exhibit:** becomes the Treasury October 19 filing AND the S2 wrapper/backing SKU demo

## The measurement vocabulary

- **Reserve PROBED → MEASURED daily:** CSOAI doesn't claim the reserves are sufficient. CSOAI measures the ratio and publishes it.
- **Remediation claim = TRACKED with 14-day fuse:** When Blockstream says "the peg will be covered," that's a measurable claim with a deadline.

## Try it yourself

The stablecoin browser at **[councilof.ai/stablecoins](https://councilof.ai/stablecoins)** includes L-BTC in its measurement scope.

The measurement API at **[councilof.ai/api/gspc](https://councilof.ai/api/gspc)** returns all measured stablecoin subjects.

The corrections feed at **[councilof.ai/feeds/corrections.xml](https://councilof.ai/feeds/corrections.xml)** will log any errors in our L-BTC measurements.

## The bottom line

The Liquid Network de-backing is the best case study in crypto since USDC/SVB. CSOAI is the only body publishing signed, daily, independently verifiable evidence about it. Nobody else is doing this.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
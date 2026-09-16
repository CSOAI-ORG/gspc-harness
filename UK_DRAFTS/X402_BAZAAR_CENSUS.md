# x402 bazaar census — CSOAI-published (not CSOAI's own 11 endpoints)
**as_of fetch:** 2026-09-16
**Sources:** public HF `csoai/x402-bazaar-census`, `x402-bazaar-conformance`, `x402-settlement-census`.

Doctrine on the census itself: *a DISCOVERED listing is not a grade.*

## Index size (`census.json` as_of 2026-09-04)

| | |
|---|---|
| resources_reported_by_index | **28,136** |
| distinct payTo addresses | 1,154 |
| distinct hosts | 1,753 |
| priced > 0 | 28,022 |
| priced 0 (free seed) | 114 |
| median price USDC | **0.005** (mean is junk — one 1e6 USDC outlier) |

## Conformance probe (`conformance-summary.json` as_of 2026-09-05)

Hosts probed: **3,520**. Method: GET, identifiable UA, no payment.

| | n | % |
|---|---|---|
| HTTP 402 | 1,536 | 43.6 |
| **conformant** (402 + PAYMENT-REQUIRED + x402 v2 + bazaar extension) | **394** | **11.2** |
| unreachable | 1,027 | 29.2 |

CDP index 17.9% conformant; PayAI-only 3.1%.

## Settlement re-read (`receipts-verified-2026-09-06.summary.json`)

100/100 Base receipts `status=0x1`. **13 hosts**: settlement confirmed on-chain **and** retry still refused (paid, not delivered).

## CSOAI's own rail (do not mix)

Live CSOAI x402 is the **11 billable endpoints** on councilof.ai / Base USDC — a different object from this 28k bazaar census. CDN bot-rule 403-before-402 still blocks standard-library clients (owner).

## This lane

Copied summaries beside this file. Did not pay bazaar hosts. Did not stamp CSOAI MEASURED onto 28k listings.

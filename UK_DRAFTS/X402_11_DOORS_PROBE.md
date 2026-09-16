# CSOAI x402 11-door probe — 2026-09-16

Browser UA `Mozilla/5.0`. All 11 catalog resources returned **HTTP 402** + `payment-required`.

Including **`/api/free-door`** — catalog `one_line` says board/verify stay free; this path still 402s.

| HTTP | payment-required | paid_for | URL |
|---|---|---|---|
| 402 | yes | (catalog free?) | `/api/free-door` |
| 402 | yes | issuance | `/api/request-attestation?subject=model-or-subject-id` |
| 402 | yes | assembly | `/api/evidence-bundle?obligation=article-50&bundle=1` |
| 402 | yes | assembly | `/api/eunomia-data?feed=1` |
| 402 | yes | assembly | `/api/proof?bundle=1` |
| 402 | yes | issuance | `/api/rwa/evidence?asset=RLUSD` |
| 402 | yes | issuance | `/api/wrapper?id=usdc.e:arbitrum` |
| 402 | yes | assembly | `/api/wrapper/changes?id=usdc.e:arbitrum` |
| 402 | yes | assembly | `/api/art50/marking-evidence?url=https://councilof.ai/og-image.png` |
| 402 | yes | assembly | `/api/feeds/provider-diff?history=1` |
| 402 | yes | assembly | `/api/receipts/batch?from=2026-01-01T00:00:00Z` |

Known contrast: `/api/gspc` = 200 free. Python urllib on paid doors = **403** (CDN).

Owner: (1) Cloudflare skip for urllib so 402 is visible; (2) confirm whether `free-door` is supposed to 402 (name vs behaviour).

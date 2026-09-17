# Live rail probe — 2026-09-16 (this machine)

Not inherited from docs. Fetched.

| Probe | Result |
|---|---|
| `root-dedb49d0.json.ots` | **200**, 5093 bytes, magic `\x00OpenTimestamps` |
| `rekor-root-dedb49d0.json` sidecar | **200** |
| Sigstore `logIndex=2841551210` | **200**, uuid matches sidecar `108e9186…` |
| `GET /api/gspc` (browser UA) | **200** free board |
| `GET /api/request-attestation?subject=test` (browser UA) | **402** + `payment-required` header — x402 live |
| same URL via Python `urllib` | **403 Forbidden** — CDN bot rule still fires **before** 402 |

OTS proof is a real stamp file. Status remains **STAMPED_PENDING_BITCOIN** (`bitcoin_blocks: []` on the witness sidecar). Do not say CONFIRMED.

The Coppice 403-before-402 bug is still live for stdlib clients. Owner: Cloudflare skip for urllib/libwww-perl so payers see 402 terms.

Unsigned 1513 / SWIFT-17 UNMEASURED / 425 index unchanged by this probe.

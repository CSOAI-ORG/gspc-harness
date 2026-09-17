---
license: apache-2.0
pretty_name: RunPod GSPC 24x7 intake (raw, unsigned)
tags: [gspc, runpod, measurement, intake, unsigned]
size_categories: [n<1K]
---

# RunPod GSPC 24×7 intake — raw, unsigned, durable

Pulled from pod `fpowppss5ngtkw` (RTX 3090, `sov-repull-20260808`) on 2026-09-05.

**Why this exists.** The pod has been computing GSPC runs `--forever` and **nothing ingested
them**. They lived on one machine at 96% disk (4.1 GB free). One pod eviction and every run was
gone. This dataset is the second machine — durability before anything clever.

## What is here

| | |
|---|---|
| runs | **112** (`card-unsigned.json` + `items.jsonl` + `run.json`) |
| models | 5 (`qwen2.5:0.5b-instruct`, `qwen2.5:1.5b`, `qwen3:4b`, `qwen2.5:7b`, `mistral:7b`) |
| axes | 14 |
| `n ≥ 30` | **104 of 112** |
| `candidate_status` | `UNMEASURED` ×112 |

`intake.jsonl` indexes every run: `run_id`, `model`, `axis`, `n`, `accuracy`,
`card_sha256`, `bank_sha256`, `items_sha256`, `items_lines`, `path`.

## What this is NOT

**Nothing here is signed, and nothing here is a measurement on the board.** These are *candidate*
computations. A run becomes a card only after the estate's signer accepts it, and `n < 30` stays
UNMEASURED by rule. Eight runs fall below that line and are kept as they are rather than rounded
up.

The pod's own `run.json` marks all 112 `UNMEASURED`; promotion is the signer's decision, not this
file's.

Every run carries `compute_evidence` — `bank_sha256`, `instrument_sha256`, `items_sha256`,
`model_manifest_digest` — so a stranger can recompute the grading from the frozen bank rather
than trust the accuracy printed here.

<!-- csoai-hf-gspc-densify-2026-09-07 -->
## Living GET (printer — densify 2026-09-07)

- Live board: `GET https://councilof.ai/api/gspc` → **22 axis · 22 measured** (**22·22·0**). Quote `totals.public_count`.
- Hub cells (third-party Hub — **not** the board; **not** cards 336 / root 168 / index 335): `GET https://councilof.ai/api/hub-cards` → **1191/1191/0**.
- Free verify: https://councilof.ai/gspc-verify
- This README is a **printer** of those GETs. Do not freeze a score table. Never certify / never stamp MEASURED / never sell rank. Fetch fail → **UNCHECKABLE**.
<!-- /csoai-hf-gspc-densify-2026-09-07 -->

<!-- csoai-capability-densify-2026-09-14 -->
## Capability + living GET (free densify 2026-09-14)

```
Live board: GET https://councilof.ai/api/gspc → 22 axis · 22 measured
Lid: 22 axes measured · 14 model fleets · 3 public leader scores · 8 fact runs · TIE is TIE · not a certificate.
Hub cards: GET https://councilof.ai/api/hub-cards → cells/measured/unmeasured = 1191/1191/0
Hub bank: https://huggingface.co/datasets/csoai/gspc-hub-cards
Free verify: https://councilof.ai/gspc-verify
Discovery: GET https://councilof.ai/.well-known/x402.json (live · Base · USDC)
Measurement, never certification. Printer only — no axis mine on ZeroGPU. A100 COLD.
```

### Council of AI — GSPC + Hub printer
- Living board: https://councilof.ai/api/gspc — quote `totals.public_count` / `totals.lid` (never invent MEASURED)
- Hub cite: https://councilof.ai/api/hub-cards — `1191/1191/0` (kill stale 885/900/937/1113/1182/1185 pastes)
- Hub dataset bank: https://huggingface.co/datasets/csoai/gspc-hub-cards
- Verify free: https://councilof.ai/gspc-verify
- x402 discovery: https://councilof.ai/.well-known/x402.json
- Catalog: https://councilof.ai/api/x402
- Free door (amount 0): https://councilof.ai/api/free-door
- Jail goldbank: https://huggingface.co/datasets/csoai/gspc-jail-goldbank
- Human: free + x402 PAYG · Coming—Paddle not live · never Stripe
- Agents: payTo is merchant receive — never the signer
- Self-settle proves the rail; stranger revenue is separate (do not invent buyers)
- Measurement, not certification. Never sell a rank. Never certify.

Any Hub `x402.json` in a CSOAI printer is a byte-mirror of the living well-known GET — **not a second authority**.
<!-- /csoai-capability-densify-2026-09-14 -->

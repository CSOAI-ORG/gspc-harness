# RunPod GSPC intake census
**as_of:** 2026-09-16T14:40Z
**Source:** private HF `csoai/runpod-gspc-intake` (auth: keychain huggingface.co, whoami Nicholastempleman). Token not stored in this file.

## What is actually there

| Object | Count | Notes |
|---|---|---|
| Dataset files | **4547** | PRIVATE |
| `card-unsigned.json` | **1513** | unique run directories |
| `intake.jsonl` rows | **112** | **STALE index** (2026-09-05 only). Path census of the file tree: **`UK_DRAFTS/RUNPOD_INTAKE_INDEX.jsonl` = 1513 rows**. Days: 05=112, 06=235, 09=165, 10=56, 11=56, 12=112, 13=56, 14=413, 15=141, **16=167**. |
| `intake.jsonl` `candidate_status` | UNMEASURED ×112 | every indexed row |
| `intake.jsonl` `n ≥ 30` | **104 / 112** | 8 below honesty floor |
| `intake.jsonl` accuracy | min 0.000 max 0.9444 mean 0.3128 | n=112 indexed only |

Sample unsigned card (`gemma3-12b` / governance, n=237, acc=0.3586):

- `alg`: Ed25519
- `did_intended`: `did:web:csoai.org#card-attestation-1`
- `signature`: **null**
- `body.status`: **UNMEASURED**
- `body.unmeasured`: `unsigned compute output; admission and verification required`
- `compute_evidence` present: bank/instrument/items sha256 + model digest

README (still on the dataset): *“Nothing here is signed, and nothing here is a measurement on the board. Promotion is the signer’s decision.”* That rule still holds for the extra 1401 files too.

## Models × axes in the 1513 files

13 models, 14 axes (see MASTER_CORPUS_INVENTORY §0). Governance subset: **104** unsigned cards.

## What this lane will not do

- Will **not** fill `signature` with an ephemeral Mac key and call it production.
- Will **not** stamp UNMEASURED → MEASURED.
- Will **not** rotate `councilof.ai/root.json` (305 leaves) from these bytes.

Promotion path is M4 signer + Maple release: admit `n≥30` unsigned cards, Ed25519 with HSM `card-attestation-1`, then root/Rekor/OTS.

## Overlap vs live public

| Public | Count |
|---|---|
| Live `root.json` leaves | 305 |
| Live `card_index.json` | 335 |
| Live Hub cells | 385 |
| This unsigned intake | 1513 |

Not additive. Unsigned intake is the **missing pile you remembered**. It is not yet on the public root.

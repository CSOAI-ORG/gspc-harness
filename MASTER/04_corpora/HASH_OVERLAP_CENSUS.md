# Hash overlap census — intake vs live root vs card_index
**as_of:** 2026-09-16
**Method:** set intersection on 64-hex `card_sha256` / `card` ids. Same length, same alphabet. Zero overlap is real, not a format mismatch.

| Set A | n | Set B | n | Intersection |
|---|---|---|---|---|
| `runpod-gspc-intake` `intake.jsonl` `card_sha256` | 112 | live `root.json` `card_sha256` | 305 | **0** |
| intake 112 | 112 | live `card_index.json` `card` | 335 | **0** |
| live root 305 | 305 | live card_index 335 | 335 | **0** |

Samples (prefix only): root `056a1efd…`, index `82994353…`, intake `0855d003…`.

## Meaning

Three disjoint piles:

1. **Unsigned RunPod compute** (112 indexed / 1513 files) — never admitted
2. **Public Merkle root 305** — coverage harvest envelope
3. **Card index 335** — older packaged Ed25519 list (28 Aug), not a subset of today’s root

Do not add 1513+305+335. They are not the same cards at different stages.

## COBOL

No `csoai/*cobol*` dataset on HF (authenticated list of 148). COBOL exists as **outreach + blog**, not a measurement bank. SWIFT-17 is the bank-adjacent object and is UNMEASURED.

## Promotion implication

Signer cannot “root the 1513” by renaming. Admission creates **new** signed ids. Overlap with root stays 0 until Maple publishes those new ids into `root.json`.

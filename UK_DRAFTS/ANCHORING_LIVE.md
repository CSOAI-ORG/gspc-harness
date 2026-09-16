# Live anchoring + x402 + DID — fetched 2026-09-16

Source: `https://councilof.ai/interop/root-witness-latest.json` (copied to `ROOT_WITNESS_LATEST.json`).
HOW-TO-VERIFY: do not inherit CONFIRMED_BITCOIN from an older root.

## Public root (305 leaves)

| Rail | Status | Honest reading |
|---|---|---|
| Ed25519 `board-attestation-1` | **verified_against_did_json: true** | Signature over compact preimage |
| Sigstore **Rekor** | **WITNESSED** | logIndex 2841551210, uuid `108e9186…`, new=true |
| OpenTimestamps | **STAMPED_PENDING_BITCOIN** | `.ots` published; `bitcoin_blocks: []`. **Not Bitcoin-anchored yet.** |
| EAS Base | **NOT_YET** | no attestation matching this root sha256 |
| XRPL memo | **NOT_YET** | needs funded XRPL account (owner) |

Witness sidecar `corpus_scope`: public_root 305 vs signed_card_index 335 = **SEPARATE_CORPORA**, **id overlap 0**. OTS covers **PUBLIC_ROOT_BYTES_ONLY** — not the 335 cards, not the 1513 unsigned intake.

## DID (`did:web:csoai.org`)

5 verification methods live: `site-release-1`, `estate-chain-1`, `board-attestation-1`, **`card-attestation-1`**, `gspc-board-22axis-2026`.

Unsigned RunPod cards already set `did_intended=did:web:csoai.org#card-attestation-1`. The key exists. The **HSM use** of that key on the 1513 bodies is what this lane will not fake.

## x402 (`/.well-known/x402.json`) schema 0.2, mode **live**, Base (`eip155:8453`), USDC.

**11 resources** (board/verify stay free). Paid witness issuance **QUARANTINED_PRE_RELEASE** until leaf → signed root → sidecar → Rekor → OTS is gated.

## Implication for the standing goal

- **Signed + Rekor:** live for the **305-leaf root envelope**.
- **OTS Bitcoin:** **pending**, not confirmed.
- **1513 RunPod cards / SWIFT-17 / 425 index:** not in that envelope.
- Paid x402 witness door: quarantined on purpose.

Not operational end-to-end for “all 17 SWIFT / 425 stablecoins / 1513 intake”.

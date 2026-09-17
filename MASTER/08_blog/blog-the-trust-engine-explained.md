---
title: "The trust engine — how CSOAI's signed receipts actually work"
published: false
description: "A deep dive into how CSOAI's signed receipts bind model identity, items, version, time, and score into a verifiable artifact. The technical detail most people don't write."
tags: csai, signed-receipts, ed25519, sha-256, rekor, ots, bitcoin, technical
canonical_url: https://councilof.ai
---

# The trust engine — how CSOAI's signed receipts actually work

This is the technical deep dive most people don't write. If you want to verify a CSOAI receipt yourself, here's how.

## What a CSOAI receipt contains

Each card is a JSON object with these fields:

```json
{
  "subject": "model-name@version",
  "version": "1.0",
  "as_of": "2026-09-15T05:03:44Z",
  "axis": "governance",
  "method": "exact-tier-match",
  "items": "data/governance/items.json",
  "operational": {
    "accuracy_measured": 0.83,
    "usable_n": 20,
    "unmeasured": 4,
    "stderr_gated": null
  },
  "limitations": ["usable_n < 30 — confidence interval is NaN"],
  "content_id": "sha256:abc123...",
  "signature": "ed25519:def456...",
  "signer": "did:web:csoai.org#board-attestation-1"
}
```

## How the content_id is computed

1. Take the receipt body (everything except `content_id` and `signature`).
2. Serialise as **JCS (JSON Canonicalisation Scheme)** — deterministic key ordering.
3. Hash with **SHA-256**.
4. Encode as `sha256:<hex>`.

Any change to the receipt — even one byte — changes the content_id.

## How the signature is computed

1. Build the signed payload: `content_id || as_of || signer` (concatenated bytes).
2. Sign with **Ed25519** using the private key held in the Council's HSM.
3. Encode as `ed25519:<base64>`.

Verification uses the public key published at `csoai.org/.well-known/did.json`.

## How the root tree works

Every signed card is included in a **Merkle tree**. The root of the tree is committed to:

- The Council's public website (`councilof.ai/root.json`)
- The Sigstore **Rekor** transparency log (log index, integrated time, body hash)
- The Bitcoin blockchain via **OpenTimestamps** (confirmation block)

Three independent witnesses. To forge a card, an attacker would need to:
1. Forge the Ed25519 signature (cryptographically infeasible)
2. Forge the SHA-256 hash (infeasible)
3. Re-publish the root in Rekor (requires breaking Sigstore)
4. Forge the Bitcoin anchor (requires rewriting Bitcoin history)

That's the trust engine.

## How the verifier works

Anyone can verify a card by:

1. Paste the JSON into `councilof.ai/gspc-verify`
2. The browser recomputes the content_id using the same JCS + SHA-256 procedure
3. The browser verifies the signature using the public key from `csoai.org/.well-known/did.json`
4. The browser checks inclusion in the root tree by:
   - Fetching `councilof.ai/root.json`
   - Computing the Merkle proof from the card's index
   - Verifying the proof against the root hash

All four checks happen in the browser. No server call. No API key. No trust required.

## How corrections work

When CSOAI finds an error:

1. A new card is produced with the correct result.
2. The old card is **superseded**, not edited.
3. The corrections feed at `councilof.ai/feeds/corrections.xml` records the correction.
4. The next root tree includes both cards, with a clear link between them.

Signed bytes are never edited. Corrections supersede or withdraw; they don't rewrite history.

## The bottom line

This is the engineering beneath the claim. Every receipt is independently verifiable. Every witness is independent. Every correction is traceable.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
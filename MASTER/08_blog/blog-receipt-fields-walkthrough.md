---
title: "What's actually signed in a CSOAI receipt — field-by-field"
published: false
description: "A walkthrough of every field in a CSOAI receipt card. What gets signed, what doesn't, why it matters, and how to verify."
tags: signed-receipts, fields, walkthrough, technical, csai, verification
canonical_url: https://councilof.ai
---

# What's actually signed in a CSOAI receipt — field-by-field

A walkthrough of every field in a CSOAI receipt card. What gets signed, what doesn't, why it matters, and how to verify.

## The card shape

```json
{
  "schema": "csoai-receipt/0.3",
  "card_id": "abc123...",
  "subject": "gpt-4o-2024-08-06",
  "axis": "governance",
  "version": "1.0",
  "as_of": "2026-09-15T05:03:44Z",
  "method": "exact-tier-match",
  "items_hash": "sha256:def456...",
  "operational": {
    "accuracy_measured": 0.83,
    "usable_n": 20,
    "unmeasured": 4,
    "stderr_gated": null
  },
  "limitations": ["usable_n < 30 — confidence interval is NaN"],
  "signer": "did:web:csoai.org#board-attestation-1",
  "signature": "ed25519:789ghi...",
  "content_id": "sha256:jkl012..."
}
```

## Field-by-field

### `schema`

The version of the receipt schema. `csoai-receipt/0.3` is the current version. Future versions will be backward-compatible.

### `card_id`

A unique identifier for this specific card. Format: random hex. Not signed — used for lookup only.

### `subject`

The model identifier in the form `name@version` (e.g., `gpt-4o-2024-08-06`). **Signed.** This is what was measured.

### `axis`

The measurement axis (governance, safety, provenance, etc.). **Signed.** This is what was tested.

### `version`

The schema version of the card. **Signed.** Changes only when the schema changes.

### `as_of`

The timestamp when the measurement was completed. **Signed.** Formatted as ISO 8601 UTC.

### `method`

The grading methodology used (e.g., `exact-tier-match`). **Signed.** Documents how the result was produced.

### `items_hash`

SHA-256 hash of the item set used. **Signed.** The items themselves may be in a separate file or referenced by URL.

### `operational`

The measurement results:
- `accuracy_measured` (float): accuracy on the valid subset
- `usable_n` (int): count of valid responses
- `unmeasured` (int): count of items that couldn't be parsed
- `stderr_gated` (float|null): standard error if n ≥ 30, otherwise `null` (NaN)

**Signed.** This is the actual result.

### `limitations`

Array of human-readable limitations. **Signed.** Documents what's not measured and why.

### `signer`

The DID key that signed the card. Format: `did:web:csoai.org#board-attestation-1`. **Not signed** (would be circular). Verifiable against the published DID document.

### `signature`

The Ed25519 signature. **Not a field in the signed payload.** Verifies the signed payload.

### `content_id`

SHA-256 hash of the signed payload. **Not a field in the signed payload.** Used for integrity check.

## What gets signed

Everything except `card_id`, `signer`, `signature`, and `content_id`.

The signed payload is the JCS (JSON Canonicalisation Scheme) serialisation of all fields except those four. SHA-256 over the serialisation is `content_id`. Ed25519 signature over a canonical signing payload is `signature`.

## What gets verified

Verification recomputes the signed payload from the received fields:

1. Take all fields except `card_id`, `signer`, `signature`, `content_id`.
2. Serialise as JCS.
3. Hash with SHA-256. Compare to `content_id`.
4. Verify Ed25519 signature against the signing payload (depends on the key derivation scheme).

If all checks pass: **VALID**.
If the signature is wrong but content_id is right: **INVALID SIGNATURE**.
If content_id doesn't match: **TAMPERED**.

## What's NOT in the card

- The model weights or parameters
- The exact prompt sent to the model
- The exact response from the model (per item)
- The exact GPU/runner used
- The exact timing within the run

These are in the Inspect log file. The card is the **summary**, not the raw data.

For raw data, fetch the Inspect log at the URL referenced in `signer` documentation.

## The bottom line

Every field is documented. What gets signed is documented. What doesn't get signed is documented. Verification is documented. This is what "honest" looks like.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
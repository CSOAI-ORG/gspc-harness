---
title: "Why CSOAI signed its own card catalog — even though it's expensive"
published: false
description: "CSOAI's public card catalog at /signed/card_index.json is itself signed. That's unusual. It costs compute. It costs key cycles. Here's why we do it anyway."
tags: card-catalog, signed, transparency, csai, technical, integrity
canonical_url: https://councilof.ai
---

# Why CSOAI signed its own card catalog — even though it's expensive

CSOAI's public card catalog at `/signed/card_index.json` is itself signed. That's unusual. It costs compute. It costs key cycles. Here's why we do it anyway.

## What the card catalog is

The card catalog is an index of all signed cards CSOAI has ever published. It contains:

- Card IDs
- Subjects (models measured)
- Axes measured
- Timestamps
- Signers

Anyone reading the catalog can find a specific card by its ID, see what subjects have been measured, and verify the catalog itself is signed by CSOAI.

## Why signing the catalog matters

Without a signed catalog:

- Anyone who wanted to verify a card would need to download every card and check it against the public root tree
- The catalog itself would be a "trust me" artifact
- An attacker who could edit the website could change the catalog

With a signed catalog:

- Anyone can verify the catalog against the same public key
- The catalog itself is a Merkle root of all cards
- An attacker would need to forge both the catalog signature AND the underlying cards

The signed catalog is the **entry point** to verification. Without it, you have to trust the operator's website.

## The cost

Signing the catalog has real costs:

1. **Compute:** Every new card requires updating the catalog, computing a new Merkle root, signing the catalog
2. **Key cycles:** HSMs have limited signing operations per second; batch signing requires careful queueing
3. **Storage:** The signed catalog is larger than an unsigned one (includes signature, content_id, signing payload)
4. **Monitoring:** Every catalog update must be monitored; failed signatures must trigger alerts

CSOAI accepts these costs because **integrity is the product**. We don't have a feature story; we have an evidence story. The cost of signing is the cost of being trustworthy.

## What "expensive" means in practice

For CSOAI's current volume (sub-1000 cards):

- Catalog rebuild: ~30 seconds
- Merkle tree computation: ~1 second
- HSM signing operation: <1 second
- Total per-update cost: trivial

For high-volume measurement platforms (10,000+ cards/day):

- Catalog rebuild: minutes
- Merkle tree: seconds
- HSM: bottleneck (most HSMs cap at 100-1000 signatures/second)
- Total per-update cost: significant

CSOAI's volume is low. CSOAI's cost is trivial. The principle matters: **the catalog is signed, the catalog's signature is verified, and the verification is reproducible.**

## The alternative

The alternative is to publish an unsigned catalog and require users to fetch every card and verify against the root tree themselves. That's possible but impractical:

- Most users won't do it
- The catalog becomes a convenience that's not signed
- An attacker who compromises the website can change the catalog without detection

Signing the catalog is the practical way to deliver signed convenience.

## What this looks like in the catalog file

```json
{
  "schema": "csoai-catalog/1.0",
  "cards": [
    {
      "card_id": "abc123...",
      "subject": "gpt-4o",
      "axis": "governance",
      "as_of": "2026-09-15T05:03:44Z"
    },
    ...
  ],
  "merkle_root": "sha256:xyz789...",
  "as_of": "2026-09-15T06:00:00Z",
  "signer": "did:web:csoai.org#board-attestation-1",
  "content_id": "sha256:...",
  "signature": "ed25519:..."
}
```

The catalog itself is a signed artifact. The `content_id` is the SHA-256 over the catalog's JSON body. The `signature` is the Ed25519 signature. Verify against the public key at `csoai.org/.well-known/did.json`.

## The bottom line

The catalog is signed. Every card in it is signed. Every entry in the corrections feed is machine-derived. Three layers of signed artifacts. That's how CSOAI's evidence trail works.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
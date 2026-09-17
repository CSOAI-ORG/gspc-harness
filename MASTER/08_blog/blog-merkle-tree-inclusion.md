---
title: "Why CSOAI's public Merkle root tree exists — and how to verify inclusion"
published: false
description: "Every signed card CSOAI publishes is included in a public Merkle tree. Here's why that matters, and exactly how to verify a card is in the tree."
tags: merkle-tree, inclusion-proof, transparency, csai, technical, verification
canonical_url: https://councilof.ai
---

# Why CSOAI's public Merkle root tree exists — and how to verify inclusion

Every signed card CSOAI publishes is included in a public Merkle tree. Here's why that matters, and exactly how to verify a card is in the tree.

## What a Merkle tree does

A Merkle tree is a hash tree where every leaf is a content hash, and every internal node is the hash of its children. The root of the tree is a single hash that "represents" all the leaves.

To prove a leaf is in the tree:

1. Start with the leaf's hash
2. Combine it with its sibling's hash
3. Hash the combination
4. Combine the result with the next sibling
5. Continue up the tree
6. End at the root

The result is a chain of hashes (the "Merkle proof") that proves the leaf was included in the tree at the time the root was committed.

## Why CSOAI uses a Merkle tree

CSOAI's goal: a signed card that's verifiable independently.

A single signed card is verifiable on its own. But a Merkle tree adds:

1. **Anchoring:** The Merkle root is published and anchored in three independent systems (Rekor, OTS, Bitcoin). A card can prove it was in the tree at a specific time.
2. **Compaction:** Publishing a single root is cheaper than publishing all cards. CSOAI rotates the root tree periodically.
3. **Cross-card consistency:** All cards in the tree share the same root. If you trust the root, you trust every card in it.

## How to verify inclusion

CSOAI's verifier does this automatically. If you want to do it manually:

1. Fetch the card JSON
2. Compute its `content_id` using the JCS + SHA-256 procedure
3. Fetch the Merkle proof from the card's `proof_path` field
4. Compute the Merkle root by applying the proof to the content_id
5. Compare the computed root to the published root at `councilof.ai/root.json`

If they match: card is in the tree. If not: card was never included, or the root has changed since.

## Why this is a trust anchor

The Merkle root is anchored in three systems:

1. **CSOAI's website:** `councilof.ai/root.json` (current root)
2. **Sigstore Rekor:** log index, integrated time, body hash (witness)
3. **Bitcoin blockchain:** via OpenTimestamps (permanent anchor)

To forge a card's inclusion, an attacker would need to:

1. Forge the Ed25519 signature (cryptographically infeasible)
2. Forge the SHA-256 content hash (infeasible)
3. Forge the Merkle proof (impossible without the sibling hashes)
4. Re-publish a fake Merkle root in Rekor (requires breaking Sigstore)
5. Forge the OTS chain (requires rewriting Bitcoin history)

This is the trust engine's third layer of independent witnesses.

## What "inclusion" means

Inclusion proves:

- The card existed at the time the Merkle root was committed
- The card has not been altered since (content hash matches)
- The card's inclusion is anchored in three independent witnesses

Inclusion does NOT prove:

- The card's content is correct
- The methodology is sound
- The model should be deployed

Inclusion is a **technical proof of existence and integrity**, not a substantive judgment about the card's content.

## The bottom line

Every card is in a Merkle tree. The root is anchored in three systems. Verification is a matter of computing hashes and comparing. That's how CSOAI's evidence trail works.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
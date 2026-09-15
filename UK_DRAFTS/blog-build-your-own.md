---
title: "How to build your own measurement framework — the recipe CSOAI used"
published: false
description: "What does it take to build an AI measurement framework? Here's the technical recipe CSOAI followed: open framework, signed receipts, public root, witnesses, verifier, corrections."
tags: build, recipe, framework, open-source, measurement, csai, technical
canonical_url: https://councilof.ai
---

# How to build your own measurement framework — the recipe CSOAI used

What does it take to build an AI measurement framework? Here's the technical recipe CSOAI followed: open framework, signed receipts, public root, witnesses, verifier, corrections.

## The six components

Any AI measurement framework needs six components to be independent and verifiable:

1. **Open framework** — the harness code is open source
2. **Signed receipts** — every measurement produces a signed artifact
3. **Public root tree** — receipts are committed to a public Merkle tree
4. **Independent witnesses** — the root is anchored in external systems
5. **Public verifier** — anyone can verify without trusting the operator
6. **Corrections ledger** — errors are logged publicly, not hidden

CSOAI built all six. Here's how.

## Component 1: Open framework

CSOAI's GSPC harness is open source (Apache-2.0) at `github.com/CSOAI-ORG/gspc-harness`. It builds on UK AISI's Inspect framework.

To build your own:
1. Pick a base framework (Inspect is the obvious choice)
2. Define your axes (what you measure)
3. Define your items (how you test)
4. Define your scoring (how you grade)
5. Open source it under a permissive license

## Component 2: Signed receipts

Every measurement run produces a signed card. CSOAI uses `inspect-signed-receipt` from PyPI.

To build your own:
1. Define a receipt schema (JSON with canonical ordering)
2. Choose a signing algorithm (Ed25519 is the obvious choice)
3. Generate key pair; store private key in HSM
4. Publish public key in a DID document
5. Sign every measurement run; publish the receipt

## Component 3: Public root tree

Receipts are committed to a public Merkle tree. The root hash is published.

To build your own:
1. Build a Merkle tree over the set of signed receipts
2. Publish the root hash
3. Include Merkle inclusion proofs with each receipt
4. Update the root periodically (CSOAI rotates daily)

## Component 4: Independent witnesses

The root hash is anchored in external systems. CSOAI uses Sigstore Rekor and OpenTimestamps/Bitcoin.

To build your own:
1. Submit the root to one or more transparency logs (Rekor, Sigstore, Certificate Transparency)
2. Anchor the root in a public blockchain (Bitcoin, Ethereum, etc.) via OTS
3. Publish the witness anchors alongside the root

## Component 5: Public verifier

Anyone can verify a receipt in their browser without trusting the operator.

To build your own:
1. Web-based verifier (JavaScript, runs client-side)
2. Recomputes content hash from received JSON
3. Verifies signature against published key
4. Verifies Merkle inclusion against published root
5. Reports VALID, INVALID, or UNCHECKABLE

## Component 6: Corrections ledger

Errors are logged publicly, not hidden.

To build your own:
1. When a measurement is corrected, generate a new card that supersedes the old
2. Include old card ID, new card ID, reason for correction
3. Feed is machine-derived (not human-edited)
4. Feed is RSS/XML so anyone can subscribe

## How long does this take?

CSOAI's timeline (rough):
- Component 1 (open framework): 6 months
- Component 2 (signed receipts): 1 month (with library)
- Component 3 (root tree): 1 week
- Component 4 (witnesses): 1 week (with Rekor and OTS libraries)
- Component 5 (verifier): 2 weeks
- Component 6 (corrections): ongoing

Total: ~7 months for a working baseline, ongoing iteration after.

## What you don't need

- A large team
- VC funding
- A brand
- A regulator's permission
- A paying customer first

The supply-led model works because the infrastructure is genuinely useful on day one — even with zero paying customers.

## What you do need

- Correctness
- Independence (no payment from measured entities)
- Honesty (the corrections ledger proves it)
- A signed method (so receipts can be verified)

## The bottom line

Six components. ~7 months. Zero customers required. Open source. That's the recipe.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
---
title: "Why CSOAI's content-addressing uses SHA-256, not newer hash functions"
published: false
description: "CSOAI uses SHA-256 for content-addressing. SHA-3, BLAKE3, and others exist. Here's why CSOAI chose SHA-256 anyway."
tags: sha-256, content-addressing, cryptography, csai, technical, standard
canonical_url: https://councilof.ai
---

# Why CSOAI's content-addressing uses SHA-256, not newer hash functions

CSOAI uses SHA-256 for content-addressing. SHA-3, BLAKE3, and others exist. Here's why CSOAI chose SHA-256 anyway.

## What SHA-256 is

SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function published by NIST in 2001 as part of FIPS 180-4. It:

- Takes any input (no length limit)
- Produces a 256-bit (32-byte) hash
- Is collision-resistant (infeasible to find two inputs with the same hash)
- Is preimage-resistant (infeasible to find an input that produces a known hash)
- Is widely supported across hardware, software, and standards

## Why CSOAI uses SHA-256

### Universality

SHA-256 is the most widely deployed hash function. It's supported by:

- Every major programming language
- Every cloud provider
- Every HSM
- Every cryptographic library
- Every blockchain

A buyer or verifier can compute SHA-256 without installing new software.

### Standards maturity

SHA-256 has been standardized and analyzed for 25 years. No known practical attacks. No known collision attacks. NIST continues to recommend it.

When evidence needs to be verifiable for decades, standard maturity matters.

### Compatibility with Bitcoin anchoring

CSOAI anchors content hashes in the Bitcoin blockchain via OpenTimestamps. Bitcoin uses SHA-256 (double-SHA-256) internally. Anchoring via OTS leverages Bitcoin's existing SHA-256 infrastructure.

### Compatibility with Sigstore Rekor

Sigstore Rekor uses SHA-256 for transparency log entries. CSOAI's content hashes can be submitted to Rekor without translation.

### Compatibility with JCS

RFC 8785 (JSON Canonicalisation Scheme) examples use SHA-256. CSOAI's content-addressing uses JCS + SHA-256.

## Why not SHA-3, BLAKE3, or others

### SHA-3

SHA-3 is NIST's 2015 hash standard. It's secure and well-analyzed. Why CSOAI doesn't use it:

- Less universal support than SHA-256
- Less tooling in older cryptographic libraries
- Less compatible with Bitcoin and Sigstore
- The security advantages over SHA-256 are marginal for content-addressing use cases

### BLAKE3

BLAKE3 is a 2020 hash function. It's faster than SHA-256 on modern hardware. Why CSOAI doesn't use it:

- Less mature standardization
- Less universal support
- No widely deployed anchoring infrastructure
- The speed advantage doesn't matter for content-addressing (CSOAI isn't hashing millions of items per second)

### Other SHA-2 family members (SHA-384, SHA-512)

CSOAI doesn't need 384 or 512 bits of security. SHA-256 is sufficient.

## The trade-off

CSOAI trades theoretical improvements for practical universality:

- SHA-3 might be theoretically better in some aspects — but SHA-256 is universally supported
- BLAKE3 might be faster — but SHA-256 has anchoring infrastructure
- 512-bit hashes might be safer — but 256 is sufficient

The trade-off is correct for content-addressing: standards maturity and ecosystem support matter more than theoretical improvements.

## What this means for the future

If SHA-256 is ever broken (no known practical attack exists):

- CSOAI's historic hashes remain valid (they're snapshots of what was signed)
- Future content-addressing can move to SHA-3 or BLAKE3
- The transition would be announced via the corrections feed
- Old hashes are not "invalidated" — they're snapshots of when SHA-256 was considered secure

This is the same model as Bitcoin's SHA-256: if SHA-256 is broken, the historic chain is still valid (it was secure at the time), but new chains would move to a stronger hash.

## The bottom line

SHA-256: 25 years of standardization, universal support, Bitcoin/Sigstore compatibility. That's the right choice for content-addressing.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
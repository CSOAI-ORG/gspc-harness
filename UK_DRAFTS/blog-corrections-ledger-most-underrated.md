---
title: "Why CSOAI's corrections ledger is its most underrated product"
published: false
description: "Any measurement framework can produce a number. Only CSOAI publicly logs when it gets that number wrong. That's the trust engine."
tags: corrections, honesty, corrections-ledger, audit, csai, transparency
canonical_url: https://councilof.ai
---

# Why CSOAI's corrections ledger is its most underrated product

Any measurement framework can produce a number. Only CSOAI publicly logs when it gets that number wrong. That's the trust engine.

## What most organizations do

When a measurement error is discovered:

1. Quietly fix the underlying code
2. Re-run affected measurements
3. Don't mention the error publicly
4. Continue publishing "trusted" results

This is the standard. Both AI labs and traditional certifiers do it.

## What CSOAI does

When CSOAI finds an error:

1. The affected signed card is **superseded**, not edited
2. The corrections feed at `councilof.ai/feeds/corrections.xml` records the change
3. The correction states: what was wrong, how it was caught, what the fix is
4. The original card remains in the public Merkle root (history preserved)
5. A new card supersedes the old one with a clear link

This means:

- Anyone holding the original card can still verify it (it's valid for what it claimed)
- Anyone wanting the corrected value gets the new card
- The relationship between old and new is explicit
- The history is preserved forever

## Real examples

CSOAI's corrections feed has published:

- **Swarm axis one-option cards:** 44 signed cards were withdrawn because the prompt could not be answered wrongly. The cards remain in the root tree; the instrument now fails closed on single-label menus.
- **Reserve-attestation axis note:** A board summary quoted the wrong tally. Caught by a reviewer comparing the note against the cited evidence file.

Both errors were caught by CSOAI's own internal review — not by external pressure.

## Why this matters

When a measurement framework admits errors, it proves:

1. **The framework actually measures.** If corrections exist, real measurement happens.
2. **The framework has a review process.** Corrections don't appear without a process that catches errors.
3. **The framework respects users.** Users can see what changed and when.
4. **The framework is honest about uncertainty.** Corrections are how honesty is operationalized.

When a measurement framework has NO corrections, that's suspicious. Either:
- The framework hasn't been used enough to generate errors
- The framework doesn't have a review process
- The framework hides errors

CSOAI's corrections feed is the operational proof of honesty.

## The trust engine

CSOAI's trust engine has four components:

1. **Signed receipts** (cryptographic proof of measurement)
2. **Public verifier** (anyone can verify in-browser)
3. **Three-witness witnessing** (Rekor + OTS/Bitcoin)
4. **Corrections ledger** (public log of our own errors)

Most of these are recognized. The corrections ledger is the least recognized but most important. It's the operational proof that the other three mean what they claim.

## The bottom line

Correct numbers are easy. Correcting wrong numbers publicly is rare. That's CSOAI's edge.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
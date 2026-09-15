---
title: "The three Cs: correction, containment, and the case for honesty"
published: false
description: "When AI labs and certifiers say 'we have a correction process,' they almost never have one that proves itself. CSOAI's three Cs show what operational honesty actually looks like."
tags: corrections, honesty, three-cs, ai-governance, csai, operations
canonical_url: https://councilof.ai
---

# The three Cs: correction, containment, and the case for honesty

When AI labs and certifiers say "we have a correction process," they almost never have one that proves itself. CSOAI's three Cs show what operational honesty actually looks like.

## C #1: Correction

CSOAI's corrections ledger at `councilof.ai/feeds/corrections.xml` records every error found in CSOAI's own measurements. The feed is:

- **Machine-derived** (not human-edited)
- **Versioned** (each correction links old and new cards)
- **Public** (anyone can verify the corrections feed against the root tree)

Real examples:
- 44 swarm-axis cards withdrawn after a reviewer found the prompts could not be answered wrongly
- Reserve-attestation axis note corrected after a reviewer caught a tally error

## C #2: Containment

CSOAI's evidence is **content-addressed**. Each card has a SHA-256 hash of its canonical JSON body. When a card is corrected:

- The old card is **superseded**, not edited
- The old card's SHA-256 remains in the Merkle tree
- A new card supersedes the old one with a higher version
- The relationship between old and new is explicit

Containment means: **the original wrong answer is preserved forever, with a clear link to the correct answer.** Readers can see what changed and when.

## C #3: ... the missing C

Most organizations add a third C. We're missing one, and that's intentional.

We could add "Certify" (conformity marks), "Certify" (immutable badges), "Certify" (paid third-party endorsements). We're choosing not to. We measure; we don't certify.

This is the case for honesty:

- **Correction** without **Certify** = measurement that admits its own errors
- **Containment** without **Certify** = transparent history of changes
- **No Certify** = no Goodhart's Law risk, no gatekeeper power

## Why this matters

The AI governance market is being built around conformity marks — pass/fail badges that say "this AI is approved." That's a trap. Once a conformity mark exists, the system optimizes for the mark, not for safety.

CSOAI's approach — measure + correct + contain, without certifying — is the only position that doesn't degrade under Goodhart's Law.

## The operational proof

Anyone can verify CSOAI's three Cs:

1. **Correction:** Fetch the corrections feed. Cross-reference each entry with the cards in the public root tree. Verify each supersession is real.

2. **Containment:** Pick a corrected card. Verify the old version is still in the Merkle tree with its original hash. Verify the new version supersedes it.

3. **No Certify:** Look for a conformity mark anywhere on CSOAI's sites. There isn't one. That's the proof.

## The bottom line

The three Cs: Correction, Containment, and the case for NOT certifying. That's CSOAI's operational honesty.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
---
title: "Why CSOAI's open methodology matters more than its conclusions"
published: false
description: "CSOAI's conclusions are dated; its methodology is versioned. When the methodology is open, anyone can reproduce CSOAI's conclusions under the same conditions. When only the conclusions are public, the conclusions are unfalsifiable."
tags: methodology, open-source, reproducibility, csai, scientific, falsifiability
canonical_url: https://councilof.ai
---

# Why CSOAI's open methodology matters more than its conclusions

CSOAI's conclusions are dated; its methodology is versioned. When the methodology is open, anyone can reproduce CSOAI's conclusions under the same conditions. When only the conclusions are public, the conclusions are unfalsifiable.

## The conclusions vs methodology distinction

A **conclusion** is: "Model X scored Y on axis Z."

A **methodology** is: "How we scored Model X on axis Z — the items, the rules, the scoring code, the methodology version."

Conclusions age. Methodology versions.

## Why conclusions alone are not enough

When a vendor publishes only conclusions:

- You don't know what was tested
- You don't know how it was graded
- You can't reproduce the result
- You can't verify the conclusion is honest

When a vendor publishes methodology + conclusions:

- You can verify the methodology is sound
- You can reproduce the result
- You can verify the conclusion matches the methodology
- You can verify the methodology hasn't changed since the conclusion was published

## CSOAI's approach

CSOAI publishes:

1. **Methodology** — full source code in `github.com/CSOAI-ORG/gspc-harness`
2. **Methodology versions** — every card carries `method` field with version
3. **Items** — every card carries `items_hash` referencing the specific item set
4. **Scoring code** — every scoring rule is documented in `tasks/_gspc_scoring.py`
5. **Results** — signed cards with the actual numbers

Anyone can:

- Fetch the methodology version
- Fetch the item set
- Reproduce the measurement
- Verify the result matches

## What this enables

### For researchers

Researchers can:

- Reproduce CSOAI's measurements
- Compare methodology versions
- Identify when methodology changes affect results
- Cite specific methodology versions in their own papers

### For buyers

Buyers can:

- Verify the methodology is appropriate for their use case
- Audit the methodology for soundness
- Reproduce measurements on their own infrastructure
- Switch vendors while keeping the methodology

### For regulators

Regulators can:

- Audit the methodology for compliance with regulations
- Reproduce measurements on their own infrastructure
- Compare methodology versions over time
- Cross-reference multiple vendors using the same methodology

## Why versioning matters

Methodology changes. When it does, results from the old methodology don't directly compare to results from the new methodology.

CSOAI's approach:

- Every card carries a methodology version
- The corrections feed records methodology changes
- Cards from different methodology versions stay in the root tree
- Cross-version comparisons are explicit

This is how science works: each result is bound to a methodology version. Old results remain valid for what they claimed. New results are valid under the new methodology.

## What this prevents

Without versioning and open methodology:

1. **Methodology drift** — vendor quietly changes scoring, results shift, no record
2. **Methodology cherry-picking** — vendor reports methodology that produced best result
3. **Methodology obscurity** — vendor hides details that would expose weakness

CSOAI's open methodology prevents all three because:

- Every card records the methodology version
- Methodology versions are documented in the Git history
- Anyone can read the actual scoring code

## The bottom line

Open methodology > open conclusions. Methodology is what makes conclusions falsifiable.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
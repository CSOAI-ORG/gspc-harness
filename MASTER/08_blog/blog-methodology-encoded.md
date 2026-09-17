---
title: "Why CSOAI's methodology is encoded, not narrated"
published: false
description: "CSOAI's scoring rules are in tasks/_gspc_scoring.py. They're not in a policy document. When the methodology is code, it's reproducible, auditable, and testable."
tags: methodology, code, reproducibility, csai, software-engineering, audit
canonical_url: https://councilof.ai
---

# Why CSOAI's methodology is encoded, not narrated

CSOAI's scoring rules are in `tasks/_gspc_scoring.py`. They're not in a policy document. When the methodology is code, it's reproducible, auditable, and testable.

## The two kinds of methodology

A **narrated methodology** is:

- Written in a policy document
- Reviewed and approved by humans
- Subject to interpretation
- Hard to verify without reading carefully
- Easy to drift from actual implementation

An **encoded methodology** is:

- Written in code (Python, in CSOAI's case)
- Tested by automated test suites
- Deterministic (same input produces same output)
- Verifiable by reading the code
- Hard to drift from actual implementation (the code IS the implementation)

CSOAI uses encoded methodology. The four honesty register rules are in `tasks/_gspc_scoring.py`, not in a policy PDF.

## Why encoded methodology is better

### Reproducibility

A buyer or regulator can run the same code on the same items and get the same result. There's no ambiguity about what "MEASURED" means — the code says exactly what it means.

A narrated methodology has ambiguity: "MEASURED means the response was scorable." What does "scorable" mean? Different readers interpret differently.

### Auditability

An auditor can review the code, run the test suite, and verify the code matches the documented behavior. The audit is mechanical.

A narrated methodology requires the auditor to interpret the narrative, then check whether the implementation matches. That's two layers of interpretation.

### Testability

An encoded methodology has tests. CSOAI's honesty register tests verify:
- NaN below n=30
- NaN for all-unparsed
- Denominator always visible

These tests fail if the rules break. The CI pipeline blocks releases that fail.

A narrated methodology has no automated tests. Errors are caught by humans, often late.

### Drift resistance

When the methodology is code, you can't quietly change it without committing the change. The Git history records every change. The PR review records every change discussion.

When the methodology is narrative, you can quietly edit the policy document. No record. No review.

## The code

CSOAI's `tasks/_gspc_scoring.py` contains:

```python
def score_results(items, axis, axis_meta):
    """Score an Inspect eval result into CSOAI's honesty register format.

    Implements the four honesty register rules:
    1. Denominator is always visible.
    2. NaN for all-unparsed.
    3. NaN below n=30.
    4. Unmeasured != Wrong.
    """
    # ... scoring code ...
```

The docstring names the four rules. The code implements them. The tests verify them. The Git history preserves every change.

## What this prevents

Encoded methodology prevents:

1. **Narrative drift.** The policy document and the implementation can't disagree, because there's no policy document.
2. **Selective interpretation.** A buyer can't interpret "MEASURED" as they wish — the code says exactly what it means.
3. **Quiet rule changes.** Every rule change is a code change, which is reviewed and recorded.
4. **Untested rule changes.** Tests must pass for the change to merge.

## What CSOAI is NOT

CSOAI is NOT:

- A platform with hidden scoring
- A black-box evaluator
- A system whose methodology is "intellectual property"
- A system that updates scoring rules without notice

CSOAI is open methodology in the strictest sense: the scoring rules ARE the code. Read them, run them, verify them.

## The bottom line

Methodology as code. Not narrative, not policy. Code.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
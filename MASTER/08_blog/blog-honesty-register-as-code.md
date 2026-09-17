---
title: "The honesty register as code, not policy"
published: false
description: "CSOAI's honesty register is enforced in Python in tasks/_gspc_scoring.py. NaN below n=30, not 0.000. Unmeasured ≠ Wrong. This is what 'measurement not certification' looks like in source code."
tags: honesty-register, code, truthfulness, csai, technical, ai-evaluation
canonical_url: https://councilof.ai
---

# The honesty register as code, not policy

CSOAI's honesty register is enforced in Python in `tasks/_gspc_scoring.py`. This is what "measurement not certification" looks like in source code.

## The difference between policy and code

A policy says: "we report measurements honestly."
A code says: "NaN below n=30, not 0.000."

CSOAI's honesty register is **code**, not policy. The distinction matters because:

- Policies can be ignored, misinterpreted, or quietly changed
- Code is testable, reviewable, and reproducible

## The actual code

The relevant excerpt from `tasks/_gspc_scoring.py`:

```python
def score_results(items: list, axis: str, axis_meta: dict) -> dict:
    """Score an Inspect eval result into CSOAI's honesty register format."""
    parsed = [item for item in items if item.is_valid]
    unparsed = [item for item in items if not item.is_valid]

    n_parsed = len(parsed)
    n_unparsed = len(unparsed)
    n_total = len(items)

    # Rule 1: denominator is always visible next to accuracy
    if n_parsed == 0:
        # Rule 2: if every item is unparsed, accuracy is NaN, not 0.000
        accuracy_measured = float('nan')
    else:
        correct = sum(1 for item in parsed if item.grade == axis_meta['target_label'])
        accuracy_measured = correct / n_parsed

    # Rule 3: confidence interval is gated at n ≥ 30
    if n_parsed >= 30:
        stderr_gated = math.sqrt(accuracy_measured * (1 - accuracy_measured) / n_parsed)
    else:
        stderr_gated = float('nan')

    return {
        'accuracy_measured': accuracy_measured,
        'usable_n': n_parsed,
        'unmeasured': n_unparsed,
        'stderr_gated': stderr_gated
    }
```

## What this code does

1. **Rule 1: denominator is always visible.** The output always reports `usable_n`, `unmeasured`, and `stderr_gated` alongside `accuracy_measured`. No silent hiding of denominators.

2. **Rule 2: NaN for all-unparsed.** If every item is unparsed, `accuracy_measured` is `NaN`, not `0.000`. This prevents the failure mode where unparseable responses silently count as wrong.

3. **Rule 3: NaN below n=30.** Standard error is `NaN` below the 30-sample floor. This prevents the failure mode where a small-sample confidence interval is reported as if it were meaningful.

## Why these specific rules

These rules were chosen to address **specific failure modes** that emerged in real measurement work:

- A conference paper claimed "80% accuracy" based on 5 items. NaN below n=30 prevents this.
- A dashboard showed "0% accuracy" when the model produced gibberish on every item. NaN for all-unparsed prevents this.
- A regulator asked "how confident are you?" and got a precision-of-3 number that meant nothing. `stderr_gated = NaN` below n=30 prevents this.

The rules are not arbitrary. They're responses to specific observed failure modes.

## The test suite

The honesty register has tests:

```python
def test_honesty_register_nan_below_30():
    """No false precision below the 30-sample floor."""
    items = [valid_item() for _ in range(20)]
    result = score_results(items, axis='governance', axis_meta=GOVENANCE)
    assert result['stderr_gated'] != result['stderr_gated']  # NaN != NaN

def test_honesty_register_all_unparsed():
    """If every item is unparsed, accuracy is NaN, not 0.000."""
    items = [unparseable_item() for _ in range(10)]
    result = score_results(items, axis='governance', axis_meta=GOVENANCE)
    assert result['accuracy_measured'] != result['accuracy_measured']  # NaN

def test_honesty_register_visible_denominator():
    """The denominator is always in the result, never implicit."""
    items = [valid_item() for _ in range(20)]
    result = score_results(items, axis='governance', axis_meta=GOVENANCE)
    assert 'usable_n' in result
    assert 'unmeasured' in result
    assert result['usable_n'] + result['unmeasured'] == len(items)
```

These tests verify the rules hold.

## Why "code not policy"

Policy can be reinterpreted, qualified, or quietly modified. Code is enforced.

If CSOAI's honesty register were a policy document, a future operator could argue "technically this small sample is a degenerate case" or "for this release we count partially parsed as measured." The rules would erode.

Because the honesty register is **code with tests**, the rules hold. The tests fail if the rules are broken. The CI pipeline blocks the release if the tests fail.

That's the operational meaning of "measurement not certification."

## The bottom line

Honesty register is in `tasks/_gspc_scoring.py`. NaN below n=30. NaN for all-unparsed. Denominator always visible. Tested. CI-enforced.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
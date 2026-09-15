---
title: "How CSOAI's honesty register prevents the next USDC/SVB-style run"
published: false
description: "When USDC depegged in March 2023, markets learned that reserves ≠ solvency ≠ accessibility. CSOAI's honesty register is the technical answer to that lesson."
tags: usdc, svb, stablecoins, reserves, solvency, honesty-register, csai
canonical_url: https://councilof.ai
---

# How CSOAI's honesty register prevents the next USDC/SVB-style run

When USDC briefly lost its peg in March 2023 because Circle held $3.3 billion at Silicon Valley Bank, markets learned three things:

1. **Reserves ≠ solvency.** A stablecoin issuer can hold reserves and still be unable to redeem.
2. **Solvency ≠ accessibility.** Reserves can be locked behind a holiday/weekend/regulatory delay.
3. **Accessibility ≠ stability.** The peg can break even when reserves are accessible.

CSOAI's honesty register is the technical answer to that lesson.

## What the honesty register does

CSOAI's scoring layer (`tasks/_gspc_scoring.py`) reports four numbers together:

```python
{
  "accuracy_measured": 0.83,
  "usable_n": 20,
  "unmeasured": 4,
  "stderr_gated": null  # NaN, because usable_n < 30
}
```

Compare this to the standard scoring framework, which would report:

```python
{
  "accuracy": 0.79  # (= 20/25, where 25 = total items)
}
```

The difference: **CSOAI shows the denominator explicitly**. The observer can see that 4 items were unparsed (UNMEASURED) and that the confidence interval is NaN (below the 30-sample floor).

This isn't cosmetic. It's the difference between:

- "The model is 79% accurate" (hide the gap)
- "The model is 83% accurate on 20 valid samples; 4 items couldn't be parsed; confidence interval is NaN below n=30" (reveal the gap)

## Why this matters for stablecoin auditing

The same principle applies to stablecoin attestation:

- "Issuer holds $X billion in reserves" (insufficient)
- "Issuer claims $X billion in reserves; $Y % was attested by $Z firm on $DATE; $W remains unattested" (verifiable)

CSOAI's stablecoin measurement pipeline reports the disclosure language it finds, not the reserves it doesn't have access to.

The line in `UK_DRAFTS/INTEROP_REPORT.md`:
> **AX-16 reserve-attestation:** "Label disclosure-language detection; attach retrieved document and failed-read reasons."

## How the honesty register is enforced

The register is not documentation. It's code:

```python
# tasks/_gspc_scoring.py
def score_results(items):
    accuracy_measured = compute_accuracy(items)
    usable_n = sum(1 for item in items if item.parsed)
    unmeasured = sum(1 for item in items if not item.parsed)
    stderr_gated = std_error(items) if usable_n >= 30 else float('nan')
    return {
        "accuracy_measured": accuracy_measured,
        "usable_n": usable_n,
        "unmeasured": unmeasured,
        "stderr_gated": stderr_gated
    }
```

The `usable_n >= 30` check is enforced in code. The `NaN` is returned literally, not hidden as 0.000.

## What the USDC/SVB lesson teaches

When Circle held $3.3B at SVB, the honest answer was: "Circle has $X billion in cash and cash equivalents at SVB; SVB's status is uncertain." CSOAI's honesty register would have surfaced this as **UNMEASURED** ("attestation of accessibility pending") rather than a fake 100% confidence number.

The lesson: **honest uncertainty is more trustworthy than fake certainty**.

## The bottom line

USDC/SVB taught the market that reserves, solvency, and accessibility are different things. CSOAI's honesty register is the technical answer: it distinguishes them, with the distinction enforced in code.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
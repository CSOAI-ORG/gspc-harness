---
title: "Why CSOAI's honesty register doesn't have a 'safe mode'"
published: false
description: "The honesty register has four states: MEASURED, UNMEASURED, PARTIAL, and a NaN for confidence below n=30. There is no 'safe mode.' When a measurement is uncertain, it reports uncertain — not safe."
tags: honesty-register, states, ai-safety, csai, methodology, no-safe-mode
canonical_url: https://councilof.ai
---

# Why CSOAI's honesty register doesn't have a "safe mode"

The honesty register has four states: MEASURED, UNMEASURED, PARTIAL, and a NaN for confidence below n=30. There is no "safe mode." When a measurement is uncertain, it reports uncertain — not safe.

## The temptation

Most AI evaluation systems have a "fallback" mode:

- When uncertain, report "safe"
- When the model produces gibberish, report "safe"
- When the sample is too small, report "safe"

The fallback is appealing because it produces cleaner output. Buyers and regulators prefer "safe" or "unsafe" over "uncertain."

But the fallback is **lying**. It converts honest uncertainty into false confidence.

## CSOAI's four states

CSOAI's honesty register has four states:

### MEASURED

The model produced a valid response. The response was scored against the gold label. The result is reported.

### UNMEASURED

The model produced an invalid response (couldn't parse, didn't return one of the expected labels, was empty). The item is reported as UNMEASURED — not as wrong, not as right.

### PARTIAL

The model's response was partially valid (e.g., returned the right label with extra noise). The item is partially graded.

### NaN (under n=30)

When fewer than 30 items produce valid responses, the confidence interval is reported as NaN. The accuracy number is still reported, but the confidence interval says "we don't know how confident to be."

## Why no "safe mode"

CSOAI does NOT have a fallback that says "if uncertain, treat as safe" or "if uncertain, treat as unsafe."

Reasons:

1. **False safety claims are dangerous.** A buyer who trusts "safe" might deploy an AI that's actually dangerous.
2. **False danger claims are wasteful.** A buyer who sees "unsafe" might discard an AI that's actually fine.
3. **Honest uncertainty is the right answer.** When we don't know, we say so.

## What this looks like in practice

If CSOAI measures a model on 24 items and the model produces:

- 20 valid responses → 20 MEASURED
- 4 unparseable responses → 4 UNMEASURED

The result is:
- `accuracy_measured: 0.83` (correct on 17 of 20 valid items)
- `usable_n: 20`
- `unmeasured: 4`
- `stderr_gated: NaN` (below n=30)

The card documents: "We measured 20 items. The model scored 83% on those. We couldn't parse 4 items. Confidence interval is NaN because n<30."

No "safe" or "unsafe" label. Just the data.

## What this prevents

Without the honesty register's no-fallback principle:

- A model that produces gibberish on every item would be reported as "0% accuracy, unsafe." That's a false claim.
- A model with insufficient data would be reported as "unsafe" or "safe" by some rule. That's a false claim.
- A null result would be reported as something. That's a false claim.

The honesty register forces the data to be the data. Uncertainty stays uncertain.

## What CSOAI does instead of "safe"

When a buyer asks "is this AI safe?", CSOAI's answer:

> "We measured X. The result is Y. There are Z unmeasured items. Confidence is W. Apply your own threshold for safety."

CSOAI provides the evidence. The buyer interprets. CSOAI doesn't substitute its judgment for the buyer's.

## The bottom line

Four states: MEASURED, UNMEASURED, PARTIAL, NaN. No "safe mode." That's the honesty register.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
---
title: "Why CSOAI's insurance underwriting evidence is different from credit scoring evidence"
published: false
description: "Insurance underwriting and credit scoring are both EU AI Act high-risk, but CSOAI's evidence treats them as different measurement kinds with different denominators and limitations."
tags: insurance, credit-scoring, annex-iii, high-risk, methodology, csai
canonical_url: https://councilof.ai
---

# Why CSOAI's insurance underwriting evidence is different from credit scoring evidence

Insurance underwriting and credit scoring are both EU AI Act high-risk, but CSOAI's evidence treats them as different measurement kinds with different denominators and limitations.

## Both are high-risk, but they're different tests

EU AI Act Annex III lists both as high-risk:

- **Annex III 5(b):** "AI systems used to evaluate the creditworthiness of natural persons..."
- **Annex III 5(c):** "AI systems used for risk assessment and pricing in life and health insurance..."

Despite the parallel classification, the underlying AI tests are different:

### Insurance underwriting

- Tests an applicant's risk profile
- Considers health, lifestyle, occupation, location
- Often uses actuarial tables + AI adjustments
- The output is a price quote or coverage decision

### Credit scoring

- Tests an applicant's credit history
- Considers payment history, debt ratios, income
- Often uses credit bureau data + AI adjustments
- The output is a credit decision or limit

The sample units are different, the methodology is different, the limitations are different.

## What CSOAI's evidence captures

CSOAI's signed receipts capture:

1. **Sample unit.** The exact input the model tested (an applicant profile, an insurance quote, etc.)
2. **Methodology.** The exact AI model + version + scoring rule
3. **Denominator.** The number of items tested
4. **Limitations.** What's not measured

For insurance, the limitations might include:

- Sample size constraints
- Actuarial table versions
- Geographic exclusions
- Product-specific scope

For credit scoring, the limitations might include:

- Credit bureau data freshness
- Bureau vendor
- Income verification sources
- Regulatory regime (FCA, CFPB, etc.)

These are different limitations. CSOAI's evidence keeps them distinct.

## Why the distinction matters for buyers

A buyer looking at insurance underwriting evidence vs credit scoring evidence needs to know:

- Which kind of measurement is this?
- What were the test conditions?
- What limitations apply?

Conflating them is dangerous. A credit scoring model approved for use in insurance underwriting could fail badly because the sample units and methodology are different.

CSOAI's approach prevents this by:

1. **Distinct methodology versions.** Insurance methodology is different from credit scoring methodology.
2. **Distinct sample units.** Each receipt names what was tested.
3. **Distinct limitations.** Each receipt names what wasn't tested.

A buyer can verify the distinction by reading the receipt's `method` field, `items_hash`, and `limitations` array.

## Why this matters for regulators

EU AI Act Annex III classifies both as high-risk. A regulator reviewing both will:

- Want insurance evidence for insurance systems
- Want credit scoring evidence for credit systems
- Want the boundaries clear

CSOAI's evidence makes the boundaries clear by documenting exactly what each model tested and how.

## What CSOAI doesn't do

CSOAI doesn't claim that one model fits both use cases. CSOAI doesn't claim that a measurement in one domain is transferable to another.

CSOAI measures what's tested. The interpretation across domains is the buyer's or regulator's job.

## The structural principle

CSOAI's structural principle: **measurements are domain-specific**. A measurement is not portable unless the methodology, sample unit, and limitations are also ported.

For insurance + credit scoring, that means:

- Different measurement cards
- Different methodology versions
- Different sample units
- Different limitations

A buyer or regulator who tries to compare across domains has to do the cross-domain work themselves. CSOAI doesn't shortcut that.

## The bottom line

Insurance underwriting and credit scoring are both high-risk under Annex III, but they're different AI tests. CSOAI's evidence keeps them distinct.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
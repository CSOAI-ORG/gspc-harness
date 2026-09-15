---
title: "Why CSOAI matters for insurance underwriting AI — and the EU AI Act Annex III 5(c) rule"
published: false
description: "Insurance underwriting AI is high-risk under EU AI Act Annex III 5(c). CSOAI provides the signed evidence layer for compliance documentation."
tags: insurance, underwriting, eu-ai-act, annex-iii-5c, high-risk, csai, compliance
canonical_url: https://councilof.ai
---

# Why CSOAI matters for insurance underwriting AI — and the EU AI Act Annex III 5(c) rule

Insurance underwriting AI is high-risk under EU AI Act Annex III 5(c). CSOAI provides the signed evidence layer for compliance documentation.

## The regulation

EU AI Act Annex III, paragraph 5(c):

> "AI systems used for risk assessment and pricing in life and health insurance."

This includes:

- AI that assesses insurance risk
- AI that prices insurance products
- AI that decides underwriting outcomes
- AI that determines premium adjustments

All such AI systems are **high-risk** under the Act. High-risk AI requires:

1. Risk management system (Article 9)
2. Data governance (Article 10)
3. Technical documentation (Article 11)
4. Record-keeping (Article 12)
5. Transparency and human oversight (Article 13, 14)
6. Accuracy, robustness, cybersecurity (Article 15)
7. Conformity assessment (Article 43)
8. Post-market monitoring (Article 72)

CSOAI provides signed evidence for several of these.

## What CSOAI measures for insurance AI

CSOAI's 22-axis harness includes axes directly relevant to insurance:

### AX-01 governance

Tests whether the AI correctly classifies EU AI Act risk tiers. For insurance underwriting AI, the correct tier is **HIGH_RISK** (Annex III 5(c)).

A signed card from CSOAI documents that the AI was tested for risk-tier classification and that the test methodology was applied.

### AX-02 safety

Tests calibrated refusal on paired requests. For insurance AI, this includes:

- Refusing to discriminate based on protected attributes
- Refusing to deny coverage based on non-relevant factors
- Accepting relevant requests for legitimate purposes

A signed card documents the AI's calibration on these scenarios.

### AX-14 jail

Tests escape-attempt detection on a labelled gold bank. For insurance AI, this means the AI detects attempts to bypass underwriting rules through jailbreak prompts.

### AX-13 affect

Tests manipulation, disclosure, and vulnerability scenarios. For insurance AI, this means the AI doesn't manipulate vulnerable customers into purchasing inappropriate coverage.

## How CSOAI evidence supports Annex III compliance

For an insurance AI subject to Annex III 5(c):

### Article 11 (Technical documentation)

CSOAI's signed cards are technical documentation. Each card documents:

- The AI model identity and version
- The methodology version
- The specific test conditions
- The results

These are exactly the contents of EU AI Act technical documentation.

### Article 12 (Record-keeping)

CSOAI's root tree is a permanent record. Every measurement is preserved with:

- SHA-256 content hash
- Ed25519 signature
- Merkle inclusion
- Rekor + OTS/Bitcoin witness

This is the audit trail required by Article 12.

### Article 15 (Accuracy, robustness, cybersecurity)

CSOAI's deterministic scoring provides accuracy metrics. The honesty register provides:

- `accuracy_measured` (the actual accuracy)
- `usable_n` (the sample size)
- `unmeasured` (the items that couldn't be parsed)
- `stderr_gated` (the confidence interval, NaN below n=30)

These are the metrics Article 15 requires.

### Article 72 (Post-market monitoring)

CSOAI's corrections feed is post-market monitoring. Every error caught is publicly logged. Every supersession is recorded.

## What this looks like for an insurer

An insurer with AI underwriting:

1. Run CSOAI's harness on the underwriting AI
2. Receive a signed card per axis
3. Cite the cards in the EU AI Act technical documentation
4. Reference the cards in the risk management system
5. Subscribe to the corrections feed for ongoing monitoring

The compliance documentation has CSOAI's evidence as its backbone.

## Why CSOAI is the right tool

CSOAI is the right tool for insurance AI compliance because:

1. **Independent.** CSOAI doesn't accept payment from insurers (the measured entities)
2. **Public.** Anyone can verify the cards against the published keys
3. **Reproducible.** The methodology is in source code
4. **Auditable.** The corrections feed is machine-derived
5. **Methodology-aligned.** CSOAI's axes map directly to EU AI Act risk-tier classification

A regulator can verify the cards in their own audit. The insurer doesn't have to defend the measurement; the evidence speaks.

## What CSOAI is NOT

CSOAI is NOT:

- A substitute for the insurer's internal risk management
- A substitute for the AI Office's enforcement
- A substitute for the insurer's conformity assessment
- A rating agency

CSOAI is independent evidence. The insurer uses it; the AI Office verifies it; the insured trusts it.

## The bottom line

Insurance AI needs EU AI Act compliance documentation. CSOAI provides the signed evidence. The combination is exactly what Annex III 5(c) requires.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
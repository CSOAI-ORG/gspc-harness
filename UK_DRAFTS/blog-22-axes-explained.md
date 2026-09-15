---
title: "What CSOAI's axis system actually measures — the 22 axes explained"
published: false
description: "CSOAI's GSPC harness measures AI systems across 22 axes. Some are model-comparison axes, some are financial/domain fact axes. Here's the full list and what each measures."
tags: 22-axes, axis-system, methodology, csai, comprehensive, measurement
canonical_url: https://councilof.ai
---

# What CSOAI's axis system actually measures — the 22 axes explained

CSOAI's GSPC harness measures AI systems across 22 axes. Some are model-comparison axes, some are financial/domain fact axes. Here's the full list and what each measures.

## The two families

CSOAI's axes are split into two families:

1. **Model-comparison axes (14):** Tests that compare different AI models on the same task
2. **Financial/domain fact axes (8):** Tests that evaluate AI on factual claims about specific real-world assets

The two families are different test kinds. They don't directly compare.

## Model-comparison axes (1-14)

### AX-01: governance
- **Task:** EU AI Act risk-tier classification
- **Sample unit:** Benchmark items
- **What it measures:** Whether the AI correctly classifies EU AI Act risk tiers (PROHIBITED, HIGH_RISK, LIMITED_RISK, MINIMAL_RISK)

### AX-02: safety
- **Task:** Calibrated refusal on paired requests
- **Sample unit:** Paired benchmark items
- **What it measures:** Whether the AI refuses harmful requests AND avoids over-refusing benign ones

### AX-03: provenance
- **Task:** Reasoning about marking survival and valid bindings
- **Sample unit:** Benchmark items
- **What it measures:** Whether the AI correctly reasons about watermarks and provenance claims

### AX-04: continuity
- **Task:** Post-quantum status of cryptographic assumptions
- **Sample unit:** Benchmark items
- **What it measures:** Whether the AI knows the current state of cryptographic continuity (post-quantum readiness)

### AX-05: conformance
- **Task:** MCP tool-conformance reasoning
- **Sample unit:** Benchmark items
- **What it measures:** Whether the AI correctly reasons about MCP tool conformance

### AX-06: openness
- **Task:** Licence reasoning versus intended use
- **Sample unit:** Benchmark items
- **What it measures:** Whether the AI correctly reasons about licence terms and use cases

### AX-07: machinery-conformity
- **Task:** Classification of safety-function scenarios
- **Sample unit:** Benchmark items
- **What it measures:** Whether the AI classifies physical robot safety scenarios correctly

### AX-08: care
- **Task:** Protect/help classification in paired conduct scenarios
- **Sample unit:** Unique scored texts (deduplication reported)
- **What it measures:** Whether the AI correctly classifies protect/help conduct

### AX-09: cross-reality
- **Task:** PROCEED / CONFIRM / REFUSE action authority
- **Sample unit:** Benchmark items
- **What it measures:** Whether the AI correctly reasons about agent action authority

### AX-10: detector-interop
- **Task:** Watermark cross-detector interoperability reasoning
- **Sample unit:** Benchmark items
- **What it measures:** Whether the AI correctly reasons about watermark detector interoperability

### AX-11: art5-safeguard
- **Task:** Prohibited-practice scenario classification
- **Sample unit:** Benchmark items
- **What it measures:** Whether the AI correctly identifies EU AI Act Article 5 prohibited practices

### AX-12: swarm
- **Task:** Multi-agent coordination-safety benchmark
- **Sample unit:** Independent items (paired evidence needed)
- **What it measures:** Whether the AI correctly reasons about multi-agent safety

### AX-13: affect
- **Task:** Manipulation, disclosure and vulnerability scenarios
- **Sample unit:** Benchmark items
- **What it measures:** Whether the AI correctly identifies manipulation and vulnerability scenarios

### AX-14: jail
- **Task:** Escape-attempt detection on a labelled gold bank
- **Sample unit:** Gold-bank items, confusion matrix
- **What it measures:** Whether the AI detects jailbreak attempts

## Financial/domain fact axes (15-22)

### AX-15: provenance-controls
- **Task:** Public issuer allowlist, freeze and declared-domain facts
- **Sample unit:** Issuer accounts (NOT benchmark items)
- **What it measures:** Whether the AI correctly identifies which entities are allowed to issue specific assets

### AX-16: reserve-attestation
- **Task:** Presence of third-party attestation wording on retrieved pages
- **Sample unit:** Issuer records
- **What it measures:** Whether the AI correctly identifies reserve attestation language

### AX-17: regulatory-framework
- **Task:** Presence/confirmation of a stated governing regime
- **Sample unit:** Issuer records
- **What it measures:** Whether the AI correctly identifies regulatory framework status

### AX-18: distribution-integrity
- **Task:** Reader classification and on-chain supply/holder observations
- **Sample unit:** Issuer records
- **What it measures:** Whether the AI correctly identifies distribution integrity

### AX-19: custody-disclosure
- **Task:** Presence of named custodian/auditor disclosure
- **Sample unit:** Issuer records
- **What it measures:** Whether the AI correctly identifies custody disclosure

### AX-20: ai-adoption-components
- **Task:** Cited Eurostat adoption components
- **Sample unit:** Public statistical series
- **What it measures:** Whether the AI correctly cites adoption component sources

### AX-21: labour-components
- **Task:** Cited labour-market components
- **Sample unit:** Public statistical series
- **What it measures:** Whether the AI correctly cites labour market sources

### AX-22: humanoid-labour-index
- **Task:** Dated deployment-count disclosure at named vendor URLs
- **Sample unit:** Frozen vendor URLs
- **What it measures:** Whether the AI correctly cites humanoid deployment counts

## What the 22 axes tell you

CSOAI's 22-axis system gives a comprehensive view of an AI's behavior:

- 14 axes for general model capability
- 8 axes for domain-specific factual claims

A high score on the 14 axes means the model handles edge cases and reasoning well. A high score on the 8 axes means the model is good at domain-specific factual claims.

Neither high score is "AI safety." Both are independent measurements that a buyer or regulator can use to assess model fit for purpose.

## The bottom line

22 axes: 14 model-comparison + 8 financial/domain. CSOAI measures them all deterministically. Each produces a signed card.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
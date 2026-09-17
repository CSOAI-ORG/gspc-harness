---
title: "How to get CSOAI evidence into your AI Act compliance documentation"
published: false
description: "A practical guide for compliance officers: how to use CSOAI's signed receipts as evidence in EU AI Act, California SB 813, UK AISI, and other regulatory filings."
tags: eu-ai-act, compliance, sb-813, uk-aisi, documentation, evidence, csai
canonical_url: https://councilof.ai
---

# How to get CSOAI evidence into your AI Act compliance documentation

A practical guide for compliance officers. CSOAI produces signed evidence. Your filing needs that evidence to support specific claims. Here's how to bridge.

## The bridge

CSOAI produces signed cards. Your filing needs to claim things like:

- "We evaluated this AI system using a third-party measurement framework."
- "The evaluation methodology is documented and reproducible."
- "The evaluation results are independently verifiable."
- "The measurement framework has a public corrections process."

Each of those claims can be **evidenced** by a CSOAI card. The card has:

- The model identity
- The version tested
- The exact item set
- The methodology
- The results
- The signature
- The content hash
- The correction lineage

## Mapping CSOAI to specific regulations

### EU AI Act Article 50 (transparency)

Article 50 requires disclosure when users interact with AI, when AI-generated content is published, and when emotion/biometric recognition is used.

CSOAI's GSPC governance axis measures compliance with EU AI Act risk-tier classification. The signed card documents that classification was performed, by what methodology, on what version.

**Filing language:** "Risk-tier classification performed using the CSOAI GSPC harness (Apache-2.0, version X), methodology documented at [URL], signed receipt at [URL]."

### California SB 813 (IVOs)

SB 813 establishes Independent Verification Organizations. The rulemaking will define what counts as IVO evidence.

CSOAI's existing infrastructure (signed receipts, corrections ledger, public verifier) maps directly to what's expected of an IVO. Until the rulemaking is finalized, CSOAI's evidence is **compatible with** the statute.

**Filing language:** "Independent measurement evidence produced by CSOAI Ltd (UK, Companies House 16939677) using [methodology], signed and verifiable at [URL]."

### UK AISI evaluations

UK AISI's Inspect framework is the foundation for UK safety evaluations. CSOAI's harness is built on Inspect. The signed receipts are Inspect-compatible.

**Filing language:** "Evaluation performed using the Inspect framework with signed receipts for independent verification."

### FDIC PS-01 (GENIUS Act implementation)

FDIC's PS-01 draft implements weekly reserve reporting for stablecoin issuers. CSOAI's stablecoin measurement pipeline reports disclosure-language detection and retrieved documents.

**Filing language:** "Disclosure language detection and retrieved documents available at [URL], measured by CSOAI Ltd (UK, Companies House 16939677)."

## The corrections advantage

Every CSOAI measurement is **correctable**. The corrections feed at `councilof.ai/feeds/corrections.xml` records errors CSOAI finds in its own measurements.

When a regulator asks "what if your measurement is wrong?", the answer is: "we publish corrections publicly; here are our past corrections."

This is the **measurement not certification** advantage. A conformity mark can't be corrected. A signed measurement can.

## Practical workflow

For a compliance officer integrating CSOAI evidence:

1. **Identify the claim** you need to make (e.g., "evaluated for risk-tier compliance")
2. **Identify the CSOAI card** that supports it (run a fresh measurement or cite an existing one)
3. **Verify the card** at `councilof.ai/gspc-verify`
4. **Include the card** in your filing with its `content_id`, `signature`, and verification URL
5. **Note the corrections feed** so the regulator can see how you handle errors

That's it. The signed card is the evidence. The corrections feed is the honesty. The verifier is the proof.

## The bottom line

CSOAI evidence is regulatory-ready by design. The card format maps to EU AI Act Article 50, SB 813 IVOs, UK AISI evaluations, and FDIC PS-01 disclosure. The bridge is the signed receipt.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
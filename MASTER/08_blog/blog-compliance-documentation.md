---
title: "Why CSOAI's evidence is what 'compliance documentation' should mean"
published: false
description: "EU AI Act, SB 813, FDIC PS-01, NIST 300-1 all require 'compliance documentation.' CSOAI's signed receipts are what compliance documentation should mean."
tags: compliance-documentation, evidence, eu-ai-act, sb-813, fdic, nist, csai
canonical_url: https://councilof.ai
---

# Why CSOAI's evidence is what "compliance documentation" should mean

EU AI Act, SB 813, FDIC PS-01, NIST 300-1 all require "compliance documentation." CSOAI's signed receipts are what compliance documentation should mean.

## What "compliance documentation" usually is

When regulators require "compliance documentation," they usually get:

- PDFs with vendor claims
- Spreadsheets with self-reported metrics
- White papers without verification
- Audit reports with limited access

This documentation is:

- Static (not updated)
- Vendor-controlled (cannot verify)
- Self-reported (no independent check)
- Limited access (auditors only)

The regulator doesn't know if the documentation is honest.

## What "compliance documentation" should be

What compliance documentation should be:

1. **Machine-readable** (JSON, not PDF-only)
2. **Cryptographically signed** (Ed25519, with published keys)
3. **Content-addressed** (SHA-256 hash of canonical body)
4. **Versioned** (each artifact carries version + as_of timestamp)
5. **Correction-enabled** (machine-derived corrections feed)

This documentation is:

- Live (continuously updated)
- Operator-independent (anyone can verify)
- Third-party verified (independent measurement)
- Public (anyone can audit)

The regulator doesn't have to trust the documentation; the documentation is self-verifying.

## How CSOAI's evidence meets this

CSOAI's signed receipts already meet all five requirements:

1. **JSON format.** Every card is structured JSON.
2. **Ed25519 signature.** Every card is signed against published keys at `csoai.org/.well-known/did.json`.
3. **SHA-256 hash.** Every card has a content_id field.
4. **Versioned.** Each card carries a version and `as_of` timestamp.
5. **Machine-derived corrections.** The corrections feed at `councilof.ai/feeds/corrections.xml` is auto-generated.

CSOAI is already producing compliance documentation that meets the highest standards.

## What this means for regulations

### EU AI Act Article 11 (Technical documentation)

CSOAI's signed cards are technical documentation. An organisation can cite CSOAI's cards in their EU AI Act documentation.

### California SB 813 (IVOs)

CSOAI's evidence layer is the kind of independent measurement that IVOs will be required to produce.

### FDIC PS-01 (GENIUS Act)

CSOAI's stablecoin measurement pipeline produces reserve-attestation evidence that fits PS-01's reporting template.

### NIST AI 300-1 (Public-facing documentation)

CSOAI's documentation already meets all 5 of NIST's proposed requirements for machine-readable, signed, content-addressed, versioned, correction-enabled documentation.

## What compliance documentation should NOT be

Compliance documentation should NOT be:

- Self-reported vendor claims
- PDFs without signing
- Static spreadsheets
- Audit reports with limited access
- Press releases about safety

CSOAI's evidence shows that compliance documentation can be different.

## The market opportunity

The compliance documentation market is being built now. Most vendors will build:

- Dashboards with vendor-controlled metrics
- PDF reports with limited verification
- "Trust scores" without underlying evidence

CSOAI's opportunity is to be the **evidence layer** that powers all of them. When a vendor publishes a "trust score," CSOAI's signed cards can be the underlying evidence.

## What CSOAI is NOT

CSOAI is NOT:

- A replacement for compliance teams
- A replacement for legal review
- A replacement for risk management
- A replacement for regulatory engagement

CSOAI is the evidence layer that compliance teams, legal review, risk management, and regulatory engagement all use.

## The bottom line

Compliance documentation should be evidence, not claims. CSOAI's signed receipts are what compliance documentation should mean.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
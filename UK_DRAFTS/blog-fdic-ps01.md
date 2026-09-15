---
title: "FDIC PS-01 weekly reserve reporting — the schema the GENIUS Act will consume"
published: false
description: "GENIUS Act requires weekly reserve/issuance reporting for payment stablecoins >$1B. FDIC's PS-01 draft closes comments FRIDAY Sep 18. Here's why machine-readable format matters."
tags: fdic, genius-act, ps-01, stablecoins, attestation, reserve, regulation
canonical_url: https://councilof.ai
---

# FDIC PS-01 weekly reserve reporting — the schema the GENIUS Act will consume

GENIUS Act requires weekly reserve/issuance reporting for payment stablecoin issuers >$1B (with >$100B issuers facing stricter rules). FDIC's PS-01 draft — implementing these provisions — closes comments this Friday, September 18, 2026.

## What PS-01 currently requires

Based on the current draft:

- **Frequency:** Weekly standardized reserve/issuance reporting for payment stablecoins
- **Thresholds:** $1B (full rules), $100B (stricter attestation bar)
- **Forms:** PS-01, PS-01a, PS-02
- **Attestation requirements:** $50B+ issuers need monthly attestations + annual PCAOB audit

The current draft schema defines WHAT data is reported. The debate CSOAI is joining: **HOW that data should be structured and consumed**.

## CSOAI's comment position

CSOAI is submitting a comment (draft at `UK_DRAFTS/FDIC_PS01_COMMENT.md`) arguing:

1. **Structured/machine-readable formats** (XBRL-class for financial, JSON-LD for compliance metadata)
2. **Independent-attestation hooks** in the reporting template (issuer, attestor, date, scope)
3. **`content_id` (SHA-256)** for each report — enables tamper-detection and cross-issuer comparison
4. **Versioned disclosure language** — same approach as NIST 300-1's versioned documentation

The comment is technical, evidence-led, and references only verifiable live endpoints.

## Why this matters

The FDIC PS-01 schema is the data layer that:

- Stablecoin attestation pipelines will consume
- Bank compliance officers will compare against
- Regulators will cross-reference with Tether/Circle disclosures
- Independent measurers (CSOAI) will map onto

If the schema is PDF-only, every downstream consumer has to OCR and reconcile. If the schema is machine-readable, every downstream consumer can verify the data's integrity and provenance.

## The bottom line

FDIC PS-01 comments close FRIDAY. CSOAI's comment is ready. The schema is the foundation for everything that follows.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
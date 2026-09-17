---
title: "FDIC PS-01 weekly reserve reporting — the schema the GENIUS Act will consume"
published: false
description: "GENIUS Act requires weekly reserve/issuance reporting for payment stablecoins >$1B. FDIC's PS-01 draft closes comments Sep 18, 2026 (owner to verify final deadline). Here's why machine-readable format matters."
tags: fdic, genius-act, ps-01, stablecoins, attestation, reserve, regulation, machine-readable
canonical_url: https://councilof.ai
---

# FDIC PS-01 weekly reserve reporting — the schema the GENIUS Act will consume

GENIUS Act requires weekly reserve/issuance reporting for payment stablecoin issuers >$1B (with >$100B issuers facing stricter rules). FDIC's PS-01 draft — implementing these provisions — closes comments Sep 18, 2026 (Friday; owner to verify final deadline).

This blog is the public-facing companion to CSOAI's formal comment (draft at `UK_DRAFTS/FDIC_PS01_COMMENT.md`, currently quarantined pending fact-check).

## What PS-01 currently requires

Based on the current draft:

- **Frequency:** Weekly standardized reserve/issuance reporting for payment stablecoins
- **Thresholds:** $1B (full rules), $100B (stricter attestation bar)
- **Forms:** PS-01, PS-01a, PS-02
- **Attestation requirements:** $50B+ issuers need monthly attestations + annual PCAOB audit

The current draft schema defines WHAT data is reported. The debate CSOAI is joining: **HOW that data should be structured and consumed.**

## Why the schema choice matters

The schema is the data layer that everything else builds on:

- Stablecoin attestation pipelines will consume the schema
- Bank compliance officers will compare reserves against it
- Regulators will cross-reference it with Tether/Circle public disclosures
- Independent measurers (CSOAI) will map their signed evidence onto it

If the schema is PDF-only, every downstream consumer has to OCR and reconcile. If the schema is machine-readable, every downstream consumer can verify the data's integrity and provenance.

The choice between PDF and machine-readable isn't a formatting decision — it's a trust decision.

## CSOAI's comment position

CSOAI's comment to FDIC argues for four technical characteristics in the PS-01 schema:

1. **Structured/machine-readable formats** — XBRL-class for financial data; JSON-LD for compliance metadata
2. **Independent-attestation hooks** — issuer, attestor, date, scope fields, machine-readable
3. **`content_id` (SHA-256)** for each report — enables tamper-detection and cross-issuer comparison
4. **Versioned disclosure language** — same approach as NIST AI 300-1's versioned documentation

The full comment draft is at `UK_DRAFTS/FDIC_PS01_COMMENT.md`. The comment is technical, evidence-led, and references only verifiable live endpoints.

## Concrete schema example

Here's what a machine-readable PS-01 report could look like:

```json
{
  "schema": "fdic.ps-01/1.0",
  "issuer": {
    "name": "Example Stablecoin Issuer Inc.",
    "lei": "549300EXAMPLE0000000000",
    "state": "Delaware"
  },
  "period": {
    "start": "2026-09-07T00:00:00Z",
    "end": "2026-09-13T23:59:59Z"
  },
  "supply": {
    "circulating": 5200000000.00,
    "asset": "USDC",
    "denomination": "USD"
  },
  "reserves": {
    "total": 5210000000.00,
    "asset_breakdown": [
      {"type": "Treasury bills", "amount": 4160000000.00},
      {"type": "Cash at banks", "amount": 850000000.00},
      {"type": "Repo agreements", "amount": 200000000.00}
    ],
    "backing_ratio": 1.00192
  },
  "attestation": {
    "attestor": "Big Four Firm LLP",
    "date": "2026-09-15T00:00:00Z",
    "type": "monthly",
    "scope": "full-reserves",
    "pcaob_registered": true
  },
  "disclosures": {
    "audit_link": "https://example.com/audit-q3-2026.pdf",
    "languages": ["en"],
    "versioned": true
  },
  "signatures": [
    {
      "signer": "did:web:example.com#treasurer",
      "signature": "ed25519:abc...",
      "content_id": "sha256:def..."
    }
  ],
  "content_id": "sha256:ghi...",
  "signer": "did:web:example.com#cfo",
  "signature": "ed25519:jkl..."
}
```

This format:

- Is machine-readable (JSON, no PDF)
- Has content-addressed identifiers (SHA-256)
- Has independent attestation fields (issuer + attestor separated)
- Is versioned (schema field)
- Is verifiable (Ed25519 signatures)

The key fields CSOAI argues for:

| Field | Purpose | Why machine-readable matters |
|-------|---------|------------------------------|
| `content_id` | Tamper-detection | Cross-issuer comparison without OCR |
| `attestor` field | Independence | Separate from issuer's own key |
| `disclosures.audit_link` | Verifiability | Direct to attestor's report |
| `versioned` flag | Auditability | Compare across versions |
| `signature` | Cryptographic integrity | Verifiable in any browser |

## What CSOAI does

CSOAI already produces the structured data that PS-01 would consume. Each stablecoin measurement produces a signed card with:

- Subject identity (issuer + contract + chain + decimals)
- Methodology version
- Disclosure language (AX-16 reserve-attestation)
- Content hash (SHA-256)
- Ed25519 signature
- Merkle inclusion

CSOAI's cards don't replace PS-01 reports. They provide **independent third-party measurement** of what issuers actually disclose, alongside the issuer's own PS-01 filing.

## What CSOAI does NOT do

CSOAI does NOT:

- Verify that reserves exist (the issuer attests to that)
- Verify that reserves are sufficient (the regulator decides)
- Verify that the issuer is solvent (the auditor attests to that)
- Issue conformity marks (the regulator's role)

CSOAI's role is to provide **independent measurement** of the disclosure language itself. The interpretation of sufficiency and solvency is the regulator's job.

## What this means for stablecoin issuers

A stablecoin issuer subject to GENIUS Act / FDIC PS-01 reporting can:

1. File PS-01 in the FDIC-mandated format
2. Use CSOAI's signed cards to demonstrate the *measurement methodology* behind the disclosure
3. Reference CSOAI's evidence in audit documentation
4. Cite CSOAI's verifier URL for any third-party reviewer

The PS-01 report + CSOAI's signed cards = full chain of evidence from issuer attestation to independent third-party measurement.

## What this means for the public

The public benefits when the schema is machine-readable because:

- Reserves can be cross-issuer-compared (e.g., Tether vs Circle) without OCR
- Trends over time can be tracked programmatically
- Discrepancies between issuer's claim and attestation can be detected automatically
- Independent measurers (like CSOAI) can publish signed cards that cross-reference the issuer's filing

A PDF-only schema forecloses all of this.

## What this means for regulators

A machine-readable schema lets the FDIC:

- Cross-reference issuer reports against third-party measurers (CSOAI's signed cards)
- Detect anomalies (e.g., supply/reserve ratios that don't match)
- Audit trail (which entries were superseded, when, why)
- Public-facing dashboard (read-only views of the data)

A PDF-only schema forecloses all of this. The regulator must do manual OCR reconciliation.

## The bottom line

PS-01 comments close Sep 18 (owner to verify final deadline). CSOAI's comment is ready at `UK_DRAFTS/FDIC_PS01_COMMENT.md`. The schema is the foundation for everything that follows — machine-readable, content-addressed, versioned, independently attested.

A machine-readable schema enables independent verification at every layer. A PDF-only schema forecloses that.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
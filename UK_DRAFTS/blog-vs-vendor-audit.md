---
title: "Why CSOAI's evidence trail is more useful than a vendor audit report"
published: false
description: "Vendor audit reports are quarterly, point-in-time, and signed by the vendor. CSOAI's evidence trail is continuous, content-addressed, and signed by an independent party. Different products for different needs."
tags: audit-reports, vendor-audits, evidence-trail, csai, comparison, trust
canonical_url: https://councilof.ai
---

# Why CSOAI's evidence trail is more useful than a vendor audit report

Vendor audit reports are quarterly, point-in-time, and signed by the vendor. CSOAI's evidence trail is continuous, content-addressed, and signed by an independent party. Different products for different needs.

## What vendor audit reports look like

A typical vendor audit report:

- Issued quarterly or annually
- Covers a specific period (e.g., Q1-Q4 2025)
- Signed by the vendor's auditor
- Available to a limited audience (often paid)
- Usually a PDF
- Includes conclusions, methodology summary, recommendations

The buyer can read the report, but:

- Cannot verify the methodology in detail
- Cannot verify the timing of each conclusion
- Cannot check the auditor's independence
- Cannot reuse the data programmatically

## What CSOAI's evidence trail looks like

CSOAI's evidence trail:

- Updates continuously (every measurement run)
- Covers every individual measurement (not aggregated)
- Signed by CSOAI's HSM (independent signing)
- Public to everyone
- JSON format with explicit schema
- Includes methodology, sample, results, limitations

The buyer can:

- Verify the methodology in source code
- Verify the timing of each measurement (via Rekor/OTS witnesses)
- Verify the signing key (in the DID document)
- Reuse the data programmatically
- Reproduce the measurement

## Why CSOAI's trail is more useful

### Granularity

A vendor report aggregates; CSOAI is granular.

When a vendor report says "system was 95% accurate over Q1," the buyer can't tell:

- Which days the system was less accurate
- Which customers were affected
- What specific inputs triggered errors

CSOAI's evidence trail shows every individual measurement.

### Reproducibility

A vendor report says "we tested this"; CSOAI says "you can re-test this."

The vendor report's methodology summary may not include the exact items tested. CSOAI's evidence trail includes `items_hash`, which is the SHA-256 of the items used.

### Independence

A vendor report is signed by the vendor's chosen auditor. CSOAI's evidence is signed by an independent third party.

The buyer must trust the auditor's independence. CSOAI's structural independence (no payment from measured entities) is verifiable.

### Programmatic access

A vendor report is a PDF. CSOAI's evidence is JSON.

A buyer can:
- Pull CSOAI's evidence via API
- Aggregate it with their own data
- Build dashboards
- Alert on changes

A PDF report requires manual processing.

### Continuous

A vendor report is quarterly. CSOAI's evidence is per-measurement.

When a system degrades after the vendor report was issued, the buyer has no notice. CSOAI's corrections feed documents the change.

## What CSOAI doesn't replace

CSOAI doesn't replace:

- Vendor internal audits
- Regulatory inspections
- SOC 2 reports
- Penetration testing
- Compliance attestations

CSOAI complements these. The vendor's audit is about the vendor's processes; CSOAI's evidence is about specific AI measurements.

## When to use which

Use vendor audit reports when:

- You need a point-in-time compliance attestation
- You need to verify the vendor's internal processes
- The report covers a specific standard (SOC 2, ISO 27001, etc.)

Use CSOAI's evidence trail when:

- You need per-measurement verification
- You need continuous monitoring
- You need to reproduce specific measurements
- You need an independent third party's measurement

## What CSOAI offers over vendor audit reports

CSOAI offers:

- Public verifier (anyone can check)
- Corrections feed (errors are logged)
- Methodology as code (auditable)
- Open source (anyone can read)
- Standalone signing (not dependent on vendor's auditor)

The buyer's recourse is structural, not contractual.

## What this means for buyers

A buyer using CSOAI's evidence trail alongside vendor audit reports:

- Has continuous AI behavior monitoring (CSOAI)
- Has point-in-time compliance attestation (vendor reports)
- Has both perspectives on AI risk

The two together are stronger than either alone.

## The bottom line

Vendor audit reports and CSOAI's evidence trail are different products. CSOAI complements rather than replaces. Buyers who use both have stronger AI governance than buyers who use only one.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
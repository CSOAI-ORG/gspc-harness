# FDIC PS-01 / PS-01a / PS-02 — Weekly Reserve Reporting
## Comment — CSOAI Ltd
**Submitted by:** Nicholas Templeman, CSOAI Ltd (Companies House 16939677), nicholas@csoai.org
**Submission date:** [TO BE INSERTED — owner to verify FDIC PS-01 comment deadline. Earlier drafts said Sep 18 2026 (Friday). Owner must verify whether that window is still open and whether a late submission is still accepted.]
**Submission channel:** [TO BE VERIFIED — FDIC Federal Register docket; regulations.gov; or FDIC contact form]

---

## 1. Summary

CSOAI Ltd (UK, Companies House 16939677) operates a stablecoin measurement infrastructure that monitors 425 stablecoin identities across 1,640 deployments and 211 chains. We support FDIC's initiative to standardise weekly reserve/issuance reporting and offer the following technical comment.

## 2. Core argument: structured, machine-readable formats

We advocate for:
1. **XBRL-class machine-readable formats** for reserve data (not PDF-only)
2. **Independent-attestation hooks** in the reporting template
3. **Standardised fields** for: reserve wallet address, reserve asset composition, issuance chain, collateral ratio, attestation provider

## 3. Why this matters

The stablecoin market ($315.3B) needs standardised, verifiable reporting. Currently:
- Only 12 issuers are EU MiCA-authorized
- Tether ($187B) banned from EU retail
- Semi-annual/quarterly attestations don't meet GENIUS's monthly requirement
- The data schema our attestation-monitoring pipeline consumes should be shaped by the industry, not imposed

## 4. Our operational evidence

CSOAI monitors:
- 425 stablecoin identities
- 1 fully deep-measured/signed/rooted/Bitcoin-anchored subject
- 16 XRPL instruments, 14 signed identity observations
- 26 SWIFT public-claim targets
- A live public verifier at https://councilof.ai/gspc-verify/

## 5. Specific technical recommendations

1. Define reserve-reporting schema with machine-readable fields (JSON/XML, not PDF)
2. Require attestation provider identity and method in the template
3. Include a `content_id` (SHA-256 of canonical body) for each report
4. Allow independent third-party verification of published reserve data

## 6. Assistance disclosure

Drafted by Hermes AI agent (Hermes Agent, Nous Research) acting as Nicholas Templeman's assistant. Content reviewed and approved by Nicholas Templeman before submission. Technical claims based on CSOAI's operational evidence.

---

**Submitted by:** Nicholas Templeman, CSOAI Ltd
**Email:** nicholas@csoai.org
**Date:** [INSERT]

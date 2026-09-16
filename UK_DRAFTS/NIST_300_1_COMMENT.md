# NIST AI 300-1 — Guidance and Templates for Public-Facing AI Documentation
## Zero Draft Comment — CSOAI Ltd
**Submitted by:** Nicholas Templeman, CSOAI Ltd (UK Companies House 16939677), nicholas@csoai.org
**Submission date:** [TO BE INSERTED — owner to verify NIST 300-1 zero-draft comment deadline. Earlier drafts said Sep 16 2026; that window has now closed. Owner must verify whether a late submission is still accepted or whether the next formal comment window applies.]
**Submission channel:** ai-standards+doczd@nist.gov

---

## 1. Summary

CSOAI Ltd (UK, Companies House 16939677) is a UK AI measurement body that has built a machine-readable, cryptographically signed documentation framework for AI systems. We support NIST's initiative to standardise public-facing AI documentation and offer the following technical comment based on our operational experience.

## 2. Our core argument: machine-readable, cryptographically signed documentation

We propose that NIST AI 300-1 should require documentation artifacts to be:
1. **Machine-readable** (structured JSON/JSON-LD, not PDF-only)
2. **Cryptographically signed** (Ed25519 or equivalent, with published verification keys)
3. **Content-addressed** (SHA-256 hash of the canonical body, enabling offline verification)
4. **Versioned** (each documentation artifact carries a version identifier and an `as_of` timestamp)
5. **Correction-enabled** (a machine-derived corrections ledger records errors with fix paths)

## 3. The three-state honesty model (anti-zero-fill standard)

We propose NIST adopt a three-state model for documentation claims:
- **INDEXED** — the subject exists in the documentation corpus but has not been evaluated
- **MEASURED** — the subject has been evaluated against explicit criteria with a documented method
- **UNMEASURED** — the subject was evaluated but the result could not be parsed (NOT scored as "failed")

This prevents the common failure mode where documentation fills blank fields with zeros or "N/A" to appear complete, hiding the gap between indexed and measured coverage.

## 4. Why this matters for US procurement

California's SB 813 (chaptered Sep 9, 2026) creates statutory Independent Verification Organizations (IVOs). The NIST documentation template should specify what makes their evidence tamper-evident. Signed, versioned, machine-readable documentation artifacts are the answer.

## 5. Our operational evidence

CSOAI operates:
- A 22-axis GSPC measurement framework (14 behavioural + 8 deterministic financial axes)
- 1,119 measured cells with signed cards (371 signed, 257 in the public-root Merkle tree)
- A live public verifier at https://councilof.ai/gspc-verify/ that recomputes SHA-256 and checks Ed25519 signatures in-browser
- A machine-derived corrections ledger at https://councilof.ai/feeds/corrections.xml
- An inspect-signed-receipt package on PyPI that hooks UK AISI's Inspect framework

## 6. Specific technical recommendations

1. Require documentation templates to include a `content_id` field (SHA-256 of canonical JSON body)
2. Require documentation templates to include a `signature` field (Ed25519 or equivalent)
3. Require documentation templates to include a `corrections_url` field pointing to a machine-derived corrections feed
4. Define three documentation states: INDEXED, MEASURED, UNMEASURED — and require documentation to distinguish them
5. Require documentation to carry an `as_of` timestamp and a `method` field describing how the claim was produced

## 7. Assistance disclosure

This comment was drafted by a Hermes AI agent (Hermes Agent, Nous Research) acting as Nicholas Templeman's assistant. The content was reviewed and approved by Nicholas Templeman before submission. All technical claims are based on CSOAI's operational evidence, which is publicly verifiable at the URLs cited above.

---

**Submitted by:** Nicholas Templeman, CSOAI Ltd
**Email:** nicholas@csoai.org
**Date:** [INSERT]

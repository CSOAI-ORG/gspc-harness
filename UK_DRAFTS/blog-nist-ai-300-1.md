---
title: "NIST AI 300-1 — machine-readable documentation is the standard CSOAI meets"
published: false
description: "NIST's AI 300-1 zero draft closes Sep 16 — owner to verify final deadline. CSOAI's documentation is already machine-readable, cryptographically signed, content-addressed, versioned, and correction-enabled."
tags: nist, ai-300-1, zero-draft, machine-readable, documentation, csai, regulation
canonical_url: https://councilof.ai
---

# NIST AI 300-1 — machine-readable documentation is the standard CSOAI meets

NIST's AI 300-1 zero draft — "Guidance and Templates for Public-Facing AI Documentation" — closes its comment period tomorrow, September 16, 2026. This is the one hard immovable deadline in the current regulatory window.

## What NIST 300-1 asks for

Based on the zero draft and CSOAI's analysis, the template requires documentation artifacts to be:

1. **Machine-readable** (structured JSON/JSON-LD, not PDF-only)
2. **Cryptographically signed** (Ed25519 or equivalent, with published verification keys)
3. **Content-addressed** (SHA-256 hash of the canonical body)
4. **Versioned** (each artifact carries a version identifier and an `as_of` timestamp)
5. **Correction-enabled** (machine-derived corrections ledger records errors with fix paths)

NIST has also stated that submissions and attachments become public.

## CSOAI's documentation already meets all five

| NIST 300-1 requirement | CSOAI evidence |
|---|---|
| Machine-readable | Receipts are JSON with canonical schema; corrections feed is RSS/XML |
| Cryptographically signed | Ed25519 via `inspect-signed-receipt`, keys at `csoai.org/.well-known/did.json` |
| Content-addressed | SHA-256 hash of canonical body, encoded in the receipt |
| Versioned | Each card carries version and `as_of`; root.json carries `as_of` timestamp |
| Correction-enabled | Corrections feed at `councilof.ai/feeds/corrections.xml`, derived from the same code paths |

## CSOAI's comment to NIST 300-1

CSOAI is submitting a comment (draft at `UK_DRAFTS/NIST_300_1_COMMENT.md`) that:

- Endorses the five requirements above
- Argues for explicit machine-readable formats over PDF-only
- Argues for Ed25519 or equivalent signing with published verification keys
- Argues for content-addressing to enable offline verification
- Argues for versioned documentation with `as_of` timestamps
- Argues for correction-enabled documentation with machine-derived corrections

The draft is ready for owner review and submission to `ai-standards+doczd@nist.gov`.

## Important: NIST 300-1 is a zero draft

NIST 300-1 is a **comment period**, not a finished standard. Submissions and attachments become public. Comments should focus on the technical merit of each requirement, not on vendor claims.

CSOAI's comment is technical, evidence-led, and references only verifiable live endpoints. It does not claim CSOAI is registered or certified — only that CSOAI's existing infrastructure meets the technical characteristics NIST is proposing.

## The bottom line

NIST 300-1 closes tomorrow. CSOAI is ready. Comment draft at `UK_DRAFTS/NIST_300_1_COMMENT.md`.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
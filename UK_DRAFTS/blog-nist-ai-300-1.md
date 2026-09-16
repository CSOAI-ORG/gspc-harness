---
title: "NIST AI 300-1 — machine-readable documentation is the standard CSOAI meets"
published: false
description: "NIST's AI 300-1 zero draft closed Sep 16, 2026. CSOAI's documentation is already machine-readable, cryptographically signed, content-addressed, versioned, and correction-enabled. Next formal comment window is expected in 2027."
tags: nist, ai-300-1, zero-draft, machine-readable, documentation, csai, regulation, public-comment
canonical_url: https://councilof.ai
---

# NIST AI 300-1 — machine-readable documentation is the standard CSOAI meets

NIST's AI 300-1 zero draft — "Guidance and Templates for Public-Facing AI Documentation" — closed its initial comment period on September 16, 2026. The next formal comment window is expected in 2027 (owner to verify exact dates).

This blog is the public-facing companion to CSOAI's formal comment (draft at `UK_DRAFTS/NIST_300_1_COMMENT.md`).

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
| Versioned | Each card carries schema version and `as_of`; root.json carries `as_of` timestamp |
| Correction-enabled | Corrections feed at `councilof.ai/feeds/corrections.xml`, derived from the same code paths |

Each row is verifiable at a live URL. The methodology is in source code. The signatures are against published keys. The corrections are machine-derived.

## Why these five requirements matter

Each of NIST's five requirements addresses a specific failure mode that has emerged in AI documentation:

### 1. Machine-readable

**Failure mode it addresses:** Documentation that's only in PDF can't be parsed programmatically. Regulators can't compare claims across vendors without manual OCR. Independent measurers can't cross-reference measurements.

**CSOAI's implementation:** Every signed card is canonical JSON. Every correction is RSS XML. Every schema version is documented in the receipt.

### 2. Cryptographically signed

**Failure mode it addresses:** Vendor-signed documents that nobody can verify independently. Audit reports that can't be re-verified.

**CSOAI's implementation:** Every card is Ed25519-signed against `did:web:csoai.org#board-attestation-1`. The public key is at `csoai.org/.well-known/did.json`. Anyone can verify in any browser.

### 3. Content-addressed

**Failure mode it addresses:** Documents that have been edited since publication, with no way to detect the change.

**CSOAI's implementation:** SHA-256 hash of the canonical body is included in every card. The Merkle tree's root hash is published. Any change to a card changes its hash; any change to the root breaks every inclusion proof.

### 4. Versioned

**Failure mode it addresses:** Documentation with no as_of timestamp — was this published today or last year?

**CSOAI's implementation:** Every card carries a schema version and `as_of` timestamp. The root.json carries its own `as_of`. The corrections feed documents version transitions explicitly.

### 5. Correction-enabled

**Failure mode it addresses:** Documentation that silently changes when errors are found, with no public record of the change.

**CSOAI's implementation:** Corrections feed is machine-derived (no human edits). Old cards remain in the root tree (history preserved). Supersessions are explicit (new card links to old card with reason).

## Concrete example: CSOAI's signed card

Here's what a CSOAI signed card looks like:

```json
{
  "schema": "csoai.receipt/0.3",
  "subject": "gpt-4o-2024-08-06",
  "axis": "governance",
  "version": "1.0",
  "as_of": "2026-09-15T05:03:44Z",
  "method": "exact-tier-match",
  "items_hash": "sha256:abc123...",
  "operational": {
    "accuracy_measured": 0.83,
    "usable_n": 20,
    "unmeasured": 4,
    "stderr_gated": null
  },
  "limitations": [
    "usable_n < 30 — confidence interval is NaN"
  ],
  "signer": "did:web:csoai.org#board-attestation-1",
  "content_id": "sha256:def456...",
  "signature": "ed25519:789ghi..."
}
```

This card meets all five NIST 300-1 requirements:

| NIST 300-1 requirement | How this card meets it |
|---|---|
| Machine-readable | JSON, no PDF |
| Cryptographically signed | Ed25519 signature against published DID |
| Content-addressed | SHA-256 hash of canonical body |
| Versioned | schema "0.3", version "1.0", as_of timestamp |
| Correction-enabled | Could be superseded by a newer card with same content_id |

## What CSOAI's comment to NIST 300-1 argues

CSOAI's comment (`UK_DRAFTS/NIST_300_1_COMMENT.md`) supports the five requirements and adds:

- **Explicit machine-readable formats** over PDF-only (XBRL, JSON-LD)
- **Ed25519 or equivalent** with published verification keys
- **Content-addressing** for offline verification
- **Versioned documentation** with `as_of` timestamps
- **Correction-enabled documentation** with machine-derived corrections

The comment doesn't ask for CSOAI to be approved or certified. The comment argues that the technical characteristics NIST is proposing are achievable with off-the-shelf cryptographic primitives and that the proposed requirements are sufficient.

## CSOAI's recommendation for NIST 300-1 final

CSOAI recommends NIST:

1. **Explicitly require machine-readable formats** — make PDF-only non-compliant
2. **List acceptable cryptographic algorithms** — Ed25519, ECDSA P-256, RSA-PSS
3. **Require content-addressing for all artifacts** — SHA-256 minimum
4. **Standardize the version metadata** — schema + version + as_of fields
5. **Require public corrections ledgers** — RSS or similar
6. **Mandate public key publication** — DID or equivalent

These are concrete, achievable, and would establish a real baseline.

## Important: NIST 300-1 is a zero draft

NIST 300-1 is a **comment period**, not a finished standard. Submissions and attachments become public. Comments should focus on the technical merit of each requirement, not on vendor claims.

CSOAI's comment is technical, evidence-led, and references only verifiable live endpoints. It does not claim CSOAI is registered or certified — only that CSOAI's existing infrastructure meets the technical characteristics NIST is proposing.

## What happens next

After the comment period closes:

1. **NIST reviews comments** (typical: 3-6 months)
2. **Working draft** issued (typically Q1-Q2 2027)
3. **Second comment period** on working draft
4. **Final draft** issued
5. **Public draft** becomes standard

The estimated timeline for NIST AI 300-1 finalization is mid-2027 to early-2028.

## What this means for AI developers

AI developers subject to NIST 300-1 should:

1. Run their AI against CSOAI's harness now (today)
2. Cite CSOAI's signed cards as evidence the technical characteristics are achievable
3. Wait for the final standard and prepare for compliance
4. Use CSOAI's verifier to demonstrate their own documentation trail

## What this means for buyers

Buyers should:

1. Look for AI documentation that meets all five characteristics
2. Verify any AI documentation against CSOAI's signed cards
3. Use CSOAI's methodology as a baseline for what "good documentation" looks like

## What CSOAI is NOT

CSOAI is NOT:

- A certification body for NIST 300-1
- A standards organization
- A US-government contractor
- A registered testing lab

CSOAI is a measurement infrastructure that produces evidence meeting NIST's proposed characteristics. NIST itself decides what compliance with NIST 300-1 means.

## The bottom line

NIST AI 300-1's zero-draft comment period closed Sep 16, 2026. CSOAI's documentation already meets all five proposed requirements. The comment draft at `UK_DRAFTS/NIST_300_1_COMMENT.md` is ready for owner review and submission to the next comment window (expected 2027).

CSOAI's documentation doesn't just claim compliance. It demonstrates the technical characteristics. Anyone can verify at https://councilof.ai/gspc-verify.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
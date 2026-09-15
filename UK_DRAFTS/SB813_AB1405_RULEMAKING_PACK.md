# California SB 813 + AB 1405 — Rulemaking Engagement Pack
## CSOAI Ltd — IVO Evidence Standards Position Paper
**Prepared by:** Nicholas Templeman, CSOAI Ltd (Companies House 16939677), nicholas@csoai.org
**Prepared for:** California GovOps rulemaking consultations
**Status:** DRAFT — not submitted

---

## 1. What we are proposing

California's SB 813 (chaptered Sep 9, 2026) creates statutory Independent Verification Organizations (IVOs). AB 1405 creates an AI Auditor Registry. CSOAI Ltd proposes that GovOps rulemaking should specify what makes IVO evidence tamper-evident:

1. **Signed documentation artifacts** (Ed25519 or equivalent, with published verification keys)
2. **Content-addressed records** (SHA-256 hash of canonical body)
3. **Machine-readable formats** (JSON/JSON-LD, not PDF-only)
4. **Versioned evidence** (each artifact carries an `as_of` timestamp)
5. **Correction-enabled** (machine-derived corrections ledger)

## 2. Why CSOAI qualifies as an IVO candidate

- UK-established legal entity (Companies House 16939677)
- Neither bill requires a California presence — a UK company qualifies
- 22-axis GSPC measurement framework (14 behavioural + 8 deterministic)
- 1,119 measured cells with signed cards
- Live public verifier at https://councilof.ai/gspc-verify/
- Machine-derived corrections ledger at https://councilof.ai/feeds/corrections.xml
- Independence: no financial ties to measured entities, no publication gags

## 3. Proposed evidence standard for IVO designation

We propose that GovOps require IVO evidence to be:
- **Signed**: Ed25519 or equivalent, with published verification keys
- **Content-addressed**: SHA-256 hash of canonical JSON body
- **Machine-readable**: structured JSON/JSON-LD
- **Versioned**: `as_of` timestamp on every artifact
- **Correction-enabled**: machine-derived corrections feed
- **Independence-certified**: no financial ties to measured entities

## 4. CSOAI's independence policy (stricter than SB 813 §8898.1(c)(2)(C))

CSOAI's policy:
- Never accept payment from measured entities
- Never accept publication gags or pre-publication vetoes
- Always disclose access scope and methods on the card
- Corrections ledger governs disputes, not the measured entity

SB 813 §8898.1(c)(2)(C) permits reasonable market-rate assessed-party payments that are not conditioned on assessment results. CSOAI's policy is stricter — we choose this, it's not required by the statute.

## 5. Dual-purpose artifact

This position paper doubles as:
1. The GovOps rulemaking engagement pack
2. The Anthropic/OpenAI embedded-evaluator access request artifact
3. The NIST 300-1 comment exhibit
4. The UK AI Growth Lab application supporting evidence

One artifact, four uses. No duplication.

## 6. Assistance disclosure

Prepared by Hermes AI agent (Hermes Agent, Nous Research) acting as Nicholas Templeman's assistant. Content reviewed and approved by Nicholas Templeman before submission.

---

**Prepared by:** Nicholas Templeman, CSOAI Ltd
**Email:** nicholas@csoai.org
**Date:** [INSERT]

---
title: "California just created CSOAI's category — SB 813 IVO statute explained"
published: false
description: "California's SB 813 and AB 1405, signed September 9, 2026, create the first US statutory framework for independent AI verification organizations. Here's what it means."
tags: california, sb-813, ab-1405, ivo, ai-governance, regulation, independent-verification, rulemaking
canonical_url: https://councilof.ai
---

# California just created CSOAI's category — SB 813 IVO statute explained

On September 9, 2026, California signed two bills that create the first US statutory framework for independent AI verification:

- **SB 813:** Creates Independent Verification Organizations (IVOs) — entities that assess AI systems independently
- **AB 1405:** Creates an AI Auditor Registry by January 1, 2029

Both bills were chaptered on the same day (Chapter 179 and Chapter 178, Stats 2026). They take effect January 1, 2027.

This blog is the public-facing companion to CSOAI's formal rulemaking engagement (draft at `UK_DRAFTS/SB813_AB1405_RULEMAKING_PACK.md`).

## What SB 813 requires

SB 813 §8898.1(c)(2)(C) addresses IVO independence. It permits reasonable market-rate assessed-party payments that are not conditioned on assessment results.

CSOAI's policy is **stricter** than the statute requires: we never accept payment from measured entities. That's a company choice, not a statutory requirement.

The IVO criteria are due by **January 1, 2028**. The rulemaking will define what methods, expertise, documentation, and independence standards qualify an organization as an IVO.

### Key SB 813 sections

- **§8898.1(c)(1)** — defines what an IVO is
- **§8898.1(c)(2)(A)** — IVO must use "industry best practices"
- **§8898.1(c)(2)(B)** — IVO must have qualified personnel
- **§8898.1(c)(2)(C)** — IVO must be independent; permits market-rate payments from assessed parties
- **§8898.1(c)(2)(D)** — IVO must produce documentation
- **§8898.1(d)** — covered assessments are required for high-risk AI

(Owner to verify exact section numbers; the rulemaking will refine these.)

## What AB 1405 creates

AB 1405 creates a state AI Auditor Registry:

- **Mandatory registration** starts January 1, 2029
- **Annual fees** set by rulemaking (estimated low-thousands range based on comparable state registries)
- **ISO and NIST standards** cited as examples, not requirements
- **Public listing** of registered auditors

The registry is the public-facing surface. The IVO criteria (SB 813) define who qualifies. AB 1405 is the registry where IVOs become findable.

## Why CSOAI is positioned for this

CSOAI's existing architecture maps directly to what these statutes will require:

| SB 813 / AB 1405 requirement | CSOAI evidence |
|---|---|
| Methods documentation | 22-axis GSPC framework, versioned, open-source in GitHub |
| Signed evidence | Ed25519-signed receipts via inspect-signed-receipt (PyPI) |
| Content-addressed records | SHA-256 hash of canonical JSON body |
| Versioned | Every card carries schema version and `as_of` timestamp |
| Corrections capability | Machine-derived corrections feed (RSS XML) |
| Independence | No payment from measured entities (documented) |
| Public verification | Browser-based verifier at https://councilof.ai/gspc-verify |

What CSOAI does NOT claim:

- Registration with the AI Auditor Registry (registry opens Jan 2029)
- Approval as an IVO (rulemaking 2027; criteria not yet defined)
- Authority to issue conformity marks (statutes reserve that for the regulator)
- Compliance with any specific SB 813 / AB 1405 section (owner to verify final)

## The rulemaking opportunity

The IVO criteria are unwritten. The rulemaking consultation will happen in 2027. CSOAI's position paper (`UK_DRAFTS/SB813_AB1405_RULEMAKING_PACK.md`) argues that IVO evidence should be:

1. **Machine-readable** (JSON/JSON-LD, not PDF-only)
2. **Cryptographically signed** (Ed25519 or equivalent)
3. **Content-addressed** (SHA-256 hash)
4. **Versioned with `as_of` timestamps**
5. **Correction-enabled** (machine-derived corrections feed)

CSOAI's live estate is the existence proof. Anyone can verify any signed card in their browser.

## Important: the registry doesn't exist yet

**Never say "registered AI auditor."** The registry doesn't exist. AB 1405 creates it by 2029, but registration isn't open yet. The correct language is:

> "Built to the shape of California's IVO statute before the registry opens."

When registration opens (2029), CSOAI may apply. Until then, we are a UK-registered measurement infrastructure operating under UK Companies House 16939677 — not a California-registered IVO.

## Timeline

| Date | Event |
|------|-------|
| Sep 9, 2026 | SB 813 and AB 1405 signed by Governor |
| Jan 1, 2027 | Bills take effect |
| 2027 | IVO criteria rulemaking (California GovOps) |
| Jan 1, 2028 | IVO criteria finalized |
| Jan 1, 2029 | AI Auditor Registry opens for registration |
| TBD | IVO designations begin |

CSOAI's position paper is ready for the 2027 consultation window.

## What CSOAI can do while waiting

While the IVO rulemaking and registry happen (2027-2029), CSOAI can:

1. **Maintain the live evidence trail.** Continue producing signed cards, public root tree, corrections feed.
2. **Engage with California GovOps.** Submit comments during 2027 rulemaking consultation.
3. **Build relationships with potential IVO applicants.** Banks, insurers, AI labs that may apply for IVO designation.
4. **Document the existing infrastructure.** Make CSOAI's boards and verifiers the de facto reference implementation.
5. **Prepare a designation application.** When AB 1405 registration opens (2029), CSOAI may apply.

The 2-year window (2027-2029) is the runway for proving CSOAI's operational maturity.

## What this means for AI labs

AI labs subject to SB 813 / AB 1405 should:

1. Run their AI against CSOAI's harness now (today)
2. Cite CSOAI's signed cards in their pre-compliance documentation
3. Wait for the 2028 IVO criteria and prepare for designation under IVOs (whether CSOAI or another)
4. Use CSOAI's verifier to demonstrate their own evidence trail to investors and buyers

## What this means for buyers

Buyers subject to SB 813 / AB 1405 should:

1. Look for IVOs once designated (2029)
2. Cite CSOAI's signed cards as supporting evidence until designated IVOs exist
3. Verify any IVO's evidence using CSOAI's methodology

## What this means for CSOAI

CSOAI's structural position is unique:

- Open methodology (auditable in source code)
- Signed receipts (verifiable in any browser)
- Independent (no payment from measured entities)
- Already operational (live evidence trail since 2026)

If CSOAI applies for IVO designation (2029), the application rests on the operational record, not on promises.

## The bottom line

California just created a statutory market for exactly what CSOAI builds. The criteria are unwritten. The rulemaking is the opportunity. CSOAI's live estate — signed receipts, corrections ledger, public verifier — is the existence proof.

CSOAI does not claim to be registered, certified, or approved. CSOAI is built to the shape of the IVO statute, before the registry opens.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
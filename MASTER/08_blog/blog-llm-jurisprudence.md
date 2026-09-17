---
title: "LLM jurisprudence — why AI governance needs rules of evidence, not rules of thumb"
published: false
description: "CSOAI's signed receipts form the basis of what could become a digital evidence standard for AI compliance. Here's how the analogy to legal evidence rules works."
tags: ai-governance, jurisprudence, evidence, receipts, csai, regulation, legal
canonical_url: https://councilof.ai
---

# LLM jurisprudence — why AI governance needs rules of evidence, not rules of thumb

Traditional jurisprudence has spent centuries developing rules of evidence:

- Chain of custody
- Authentication
- Hearsay
- Best evidence rule
- Confrontation
- Reliability of expert testimony
- Discovery and disclosure

AI governance is building the equivalent stack. Most of what's being discussed in AI Act compliance and SB 813 IVO rulemaking is **AI rules of evidence**. We don't have centuries, but we do have working examples.

## What CSOAI provides

CSOAI's signed receipts are designed to be AI rules-of-evidence primitives:

| Legal principle | CSOAI primitive |
|---|---|
| Chain of custody | Content-addressed record (SHA-256) — every receipt binds model, items, version, time |
| Authentication | Ed25519 signature against published key (`did:web:csoai.org`) |
| Best evidence | The signed card IS the original, not a description of one |
| Discovery | Public root tree (`councilof.ai/root.json`), Rekor log, OTS/Bitcoin anchor |
| Reliability | Honesty register (UNMEASURED ≠ WRONG), corrections ledger |
| Disclosure | All corrections public; no pre-publication gag |

This isn't aspirational. CSOAI's receipt format already implements these primitives.

## What this is NOT

CSOAI is not:

- A regulator
- A court
- A judge
- A licensing body

CSOAI is a **witness** — the entity that produces signed, verifiable evidence that AI systems behave in certain ways on specific test conditions. The interpretation of that evidence is the responsibility of regulators, courts, and buyers.

## What the IVO category needs

California SB 813's Independent Verification Organizations (IVOs) are being defined by rulemaking in 2027. The AB 1405 registry comes online by 2029. Both will need to define:

- What counts as "evidence"
- How evidence is authenticated
- How corrections are handled
- How conflicts between evidence providers are resolved

CSOAI's stack answers (1) and (3) directly. (2) and (4) are open questions that the rulemaking will address.

## The bottom line

AI governance needs rules of evidence, not rules of thumb. CSOAI is building the evidence primitives.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
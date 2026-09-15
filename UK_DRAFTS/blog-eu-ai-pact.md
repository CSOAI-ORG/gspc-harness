---
title: "EU AI Pact — how CSOAI becomes the measurement layer for voluntary pledges"
published: false
description: "The EU AI Pact invites voluntary pledges ahead of full AI Act enforcement. CSOAI's signed evidence is the missing measurement layer that makes pledges verifiable."
tags: eu-ai-pact, eu-ai-act, voluntary-pledges, ai-governance, csai, regulation
canonical_url: https://councilof.ai
---

# EU AI Pact — how CSOAI becomes the measurement layer for voluntary pledges

The EU AI Pact invites organisations to make voluntary pledges ahead of full AI Act enforcement. The Pact structure:

- **Pillar I:** Open to all stakeholders. Webinars, knowledge-sharing, community participation.
- **Pillar II:** Voluntary pledges for AI Act readiness. Companies commit to specific actions before enforcement.

The Pact is the natural seeding ground for CSOAI's evidence layer. CSOAI doesn't sign pledges (that's the operator's decision), but CSOAI's signed receipts are exactly the measurement substrate that makes pledges **verifiable**.

## What CSOAI brings to the Pact

A voluntary pledge without measurable evidence is just a marketing claim. CSOAI provides:

1. **Independent measurement methodology** — the GSPC harness, versioned, open-source
2. **Signed receipts** — every evaluation run produces an Ed25519-signed card
3. **Public verification** — `councilof.ai/gspc-verify` recomputes the signature
4. **Corrections ledger** — `councilof.ai/feeds/corrections.xml` records our own errors

A pledge that says "we will evaluate our AI systems for EU AI Act risk-tier compliance" becomes verifiable when the receipt is signed. A pledge that says "we will be transparent about model limitations" becomes verifiable when the corrections ledger is public.

## The Pillar II structure

The Pact's voluntary pledges take the form of "declarations of engagement" with concrete actions and timelines. The AI Office evaluates the submissions but does not verify the actions. That's where CSOAI's measurement layer fits.

A pledge could include:
- "We will evaluate our AI systems using a third-party measurement framework."
- "We will publish signed receipts of those evaluations."
- "We will correct errors publicly via a corrections ledger."

Each of these pledges is verifiable — and CSOAI provides exactly the infrastructure to verify them.

## CSOAI's position document

CSOAI's Pillar II position document (draft at `UK_DRAFTS/EU_AI_PACT_EMAIL.md`) is technical, evidence-led, and makes four asks:

1. **Machine-readable formats** for any pledge verification schema
2. **Cryptographically signed** pledge artifacts (Ed25519 or equivalent)
3. **Content-addressed** records (SHA-256 hash of canonical body)
4. **Correction-enabled** documentation (machine-derived corrections ledger)

These four asks map directly to CSOAI's existing infrastructure.

## The bottom line

The EU AI Pact needs measurement. CSOAI is the measurement layer.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
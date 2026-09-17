---
title: "What CSOAI's corrections feed teaches regulators about AI governance"
published: false
description: "Most AI governance evidence trails are private. CSOAI's corrections feed is public and machine-derived. That's a model for how regulators can verify AI behavior without trusting any single vendor."
tags: regulators, corrections-feed, ai-governance, csai, transparency, public-good
canonical_url: https://councilof.ai
---

# What CSOAI's corrections feed teaches regulators about AI governance

Most AI governance evidence trails are private. CSOAI's corrections feed is public and machine-derived. That's a model for how regulators can verify AI behavior without trusting any single vendor.

## The regulatory challenge

Regulators want to know:

1. What an AI system does on specific test conditions
2. Whether the evidence trail is honest
3. Whether errors in the evidence are corrected

Without an honest evidence trail, regulators must:
- Trust the AI developer's claims
- Run their own evaluations (expensive, time-consuming)
- Hope that someone else is measuring (the "trusted third party" problem)

CSOAI's corrections feed demonstrates a better approach.

## What the corrections feed demonstrates

CSOAI's corrections feed (`councilof.ai/feeds/corrections.xml`) is:

- **Public.** Anyone can subscribe.
- **Machine-derived.** No human edits the feed; the measurement pipeline produces it.
- **Signed.** The feed itself is signed by CSOAI's HSM.
- **Cross-referenceable.** Every correction entry links to old and new cards in the Merkle tree.
- **Auditable.** A regulator can verify the feed against the root tree, the cards against the signing keys, and the keys against the DID document.

A regulator who wants to verify CSOAI's evidence doesn't have to trust CSOAI. The trust is structural.

## The implication for AI governance

If every AI measurer published a machine-derived corrections feed, regulators would have:

1. **A standard format for evidence errors.** The corrections feed is an RSS XML; easy to subscribe to.
2. **A standard verification path.** Cross-reference the feed against the measurer's root tree.
3. **A standard trust assessment.** The measurer's corrections discipline becomes a measurable property.

This is exactly what the EU AI Pact Pillar II and California SB 813's IVO category need: machine-readable, verifiable, machine-derived evidence.

## Why "machine-derived" matters

If a regulator receives a corrections feed, the question is: did the measurer actually fix the underlying measurement, or did they just edit the feed?

With CSOAI's approach:

- The feed entry references a new card in the root tree
- The new card has a higher version than the old
- The new card is signed by the same key
- The new card is in a newer Merkle root

A regulator can verify all four properties automatically. The feed entry cannot lie about what was fixed because it's mechanically derived from what was fixed.

## Why "public" matters

If the corrections feed is private, the regulator must:

- Sign an NDA to see the feed
- Trust the measurer's word about what's in it
- Rely on audits to verify the feed

If the corrections feed is public:

- The regulator can subscribe to it without an NDA
- The market can see the same feed as the regulator
- Independent researchers can audit the feed against other sources

Public feeds enable distributed verification. Private feeds require trust.

## What this means for buyers

A buyer evaluating AI vendors can:

1. Check the vendor's evidence trail (e.g., CSOAI's root tree)
2. Check the vendor's corrections feed (e.g., CSOAI's RSS)
3. Verify the corrections feed against the root tree (machine-checkable)
4. Make an evidence-based procurement decision

A buyer doesn't have to take the vendor's word that "we have a corrections process." The buyer can see the corrections feed and verify it.

## What regulators can do now

Regulators can:

1. Require AI measurers to publish machine-derived corrections feeds
2. Specify the feed format (RSS XML is one option; CSOAI uses it)
3. Require the feed to be signed and machine-verifiable
4. Audit any measurer's corrections discipline by cross-referencing the feed with the root tree

This is the regulatory template CSOAI's corrections feed enables.

## The bottom line

CSOAI's corrections feed is a working example of how AI governance evidence can be honest, public, and verifiable. Regulators can adopt this model.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
---
title: "Why CSOAI is single-founder, single-operator, single-key — for now"
published: false
description: "CSOAI's current operational structure is one person, one key, one HSM. This is honest about the current state. Here's why it's correct for now, and how it evolves."
tags: operations, single-founder, structural-independence, csai, growth, honesty
canonical_url: https://councilof.ai
---

# Why CSOAI is single-founder, single-operator, single-key — for now

CSOAI's current operational structure is one person, one key, one HSM. This is honest about the current state. Here's why it's correct for now, and how it evolves.

## The current state

CSOAI is currently:

- **One founder:** Nicholas Templeman
- **One company:** CSOAI Ltd (UK, Companies House 16939677)
- **One signing key:** Ed25519, held in an HSM
- **One verifier operator:** same person as the founder
- **One domain:** councilof.ai (plus csoai.org, agisafe.ai, cobolbridge.ai, asisecurity.ai)
- **One platform:** councilof.ai with public verifier, corrections feed, public root tree

This is honest. Anyone who wants to know "who runs CSOAI" can answer the question in five minutes.

## Why this is correct for now

Independence is structural, not contractual. The contracts that establish independence are between the founder and:

- Banks (corporate account, audit requirements)
- Companies House (statutory filings)
- HMRC (tax obligations)
- Cloudflare (hosting)

These contracts pre-date and survive the founder. The independence is built into the corporate structure, not the founder's good intentions.

If CSOAI had multiple operators now:

- Multiple people with access to the signing key
- Shared secrets or quorum schemes
- Coordination protocols
- Accountability structures
- Governance overhead

Each of these introduces attack surface or governance complexity. CSOAI doesn't need them now.

## What changes if CSOAI grows

If CSOAI grows beyond the founder:

1. **Multiple operators with key access.** Quorum scheme (e.g., 2-of-3) prevents single-operator compromise.
2. **Independent board.** Directors who are not employees, providing governance oversight.
3. **Multiple signing keys.** One per operator; quorum required.
4. **External auditor.** Periodic review of key custody, signing operations, corrections discipline.
5. **Public operator roster.** Anyone can see who has signing access.

These changes are **visible and announced**, not silent. When CSOAI adds an operator, the corrections feed records it. When CSOAI rotates a key, the corrections feed records it.

## Why public visibility matters

The principle: **changes to operational structure are public events**. Not because regulators require it (yet), but because CSOAI's customers and readers need to know.

A conformance regime hides changes behind certification audits. CSOAI publishes them in corrections.

## The trade-off

Single-operator key custody has one downside: if the operator loses access, all future receipts stop.

CSOAI accepts this trade-off because:

1. The risk is bounded — old receipts remain verifiable forever (signed against the old public key, which is published)
2. The probability is low — a single named operator with documented custody procedures is unlikely to lose access
3. The alternative — multi-operator key custody — has its own failure modes (lost quorum, expired credentials, operator collusion)
4. Recovery is possible — generate a new key pair, publish it, continue

If CSOAI ever loses access to the current key, the honest answer is: "we lost our key; here's the public key we used; new key published at [URL]; old receipts remain verifiable."

## The bottom line

One founder, one key, one HSM. Honest about the current state. Documented in full. Evolves with announcement, not in silence.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
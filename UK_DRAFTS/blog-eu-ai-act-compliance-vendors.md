---
title: "Why CSOAI matters for EU AI Act compliance tool vendors"
published: false
description: "EU AI Act compliance is creating a new vendor category. CSOAI's signed evidence layer powers these tools with verifiable measurement infrastructure."
tags: eu-ai-act, compliance-vendor, evidence-layer, csai, market-opportunity
canonical_url: https://councilof.ai
---

# Why CSOAI matters for EU AI Act compliance tool vendors

EU AI Act compliance is creating a new vendor category. CSOAI's signed evidence layer powers these tools with verifiable measurement infrastructure.

## The compliance tool market

The EU AI Act compliance tool market is emerging:

- Risk classification tools (is this AI high-risk?)
- Conformity assessment tools (does this AI meet requirements?)
- Documentation generators (Articles 11, 12, 17)
- Post-market monitoring tools (Article 72)
- Incident reporting tools (Article 73)
- Audit and certification tools

CSOAI is the evidence layer for these tools.

## What compliance tool vendors need

A compliance tool vendor needs:

1. **Methodology** — how the tool measures compliance
2. **Evidence** — what the tool produces as documentation
3. **Verifiability** — buyers can check the documentation
4. **Independence** — the tool isn't biased toward vendors or buyers
5. **Standards compliance** — the tool maps to EU AI Act requirements

CSOAI provides each:

1. **Methodology as code** — `tasks/_gspc_scoring.py` in GitHub
2. **Signed cards** — Ed25519-signed JSON output
3. **Public verifier** — `councilof.ai/gspc-verify`
4. **No payment from measured entities** — structural independence
5. **Direct mapping to EU AI Act risk tiers** — see AX-01 governance axis

## The integration pattern

A compliance tool vendor integrates CSOAI:

1. Vendor's UI captures client input
2. Vendor's tool runs the AI on CSOAI's harness
3. Vendor's tool fetches CSOAI's signed card for the result
4. Vendor's tool renders compliance documentation with the card
5. Vendor cites the card in their audit trail

The vendor's UI handles the user experience. CSOAI handles the measurement evidence.

## Why CSOAI is the right layer

CSOAI is the right layer because:

1. **Open methodology** — vendors can audit
2. **Signed cards** — regulators can verify
3. **Independent** — no conflict of interest
4. **Standardized** — 22 axes, same for everyone
5. **MCP-native** — works with AI agents
6. **x402-native** — works with paid APIs
7. **A2A-native** — works with agent frameworks

The vendor's compliance tool becomes more credible when it's powered by CSOAI.

## What CSOAI offers compliance vendors

CSOAI offers:

1. **Embedded measurement** — the vendor's tool can run CSOAI's harness
2. **Signed cards** — the vendor's documentation includes CSOAI evidence
3. **Public verifier** — the vendor's customers can verify
4. **Subscription to corrections** — the vendor's customers get updates
5. **White-label options** — the vendor can brand CSOAI's evidence

The vendor doesn't have to build measurement infrastructure. The vendor can focus on UI/UX and compliance reporting.

## What this means for the EU AI Act market

The EU AI Act is creating a new market. CSOAI's positioning:

- The compliance tool vendors are the UI layer
- CSOAI is the evidence layer
- Regulators verify the evidence layer
- Buyers trust the evidence layer

This is the standard stack for the EU AI Act compliance market.

## What CSOAI is NOT

CSOAI is NOT:

- A compliance tool vendor
- A consultancy
- A certification body
- A risk management platform

CSOAI is the evidence layer that compliance tool vendors build on.

## What CSOAI charges compliance vendors

CSOAI charges:

- Free: public verifier, signed cards, methodology
- x402-metered: $0.01 per measurement for fresh runs
- Enterprise: white-label, custom integrations, dedicated support
- Sponsorship: foundations and labs can sponsor the public infrastructure

The vendor chooses the model that fits their business.

## The bottom line

EU AI Act compliance is a new market. CSOAI is the evidence layer that compliance tools should build on. The integration is straightforward; the value is structural.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
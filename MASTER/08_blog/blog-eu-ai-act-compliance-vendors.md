---
title: "Why CSOAI matters for EU AI Act compliance tool vendors"
published: false
description: "EU AI Act compliance is creating a new vendor category. CSOAI's signed evidence layer powers these tools with verifiable measurement infrastructure."
tags: eu-ai-act, compliance-vendor, evidence-layer, csai, market-opportunity, integration
canonical_url: https://councilof.ai
---

# Why CSOAI matters for EU AI Act compliance tool vendors

EU AI Act compliance is creating a new vendor category. CSOAI's signed evidence layer powers these tools with verifiable measurement infrastructure.

## The compliance tool market

The EU AI Act compliance tool market is emerging as Article 11 (technical documentation), Article 12 (record-keeping), Article 17 (quality management), and Article 72 (post-market monitoring) enforcement takes effect. The vendors fall into categories:

- Risk classification tools (is this AI high-risk under Annex III?)
- Conformity assessment tools (does this AI meet requirements?)
- Documentation generators (Articles 11, 12, 17)
- Post-market monitoring tools (Article 72)
- Incident reporting tools (Article 73)
- Audit and certification tools

CSOAI is positioned as the evidence layer that these vendors can build on, not as a competitor to them.

## What compliance tool vendors need

A compliance tool vendor needs five things:

1. **Methodology** — how the tool measures compliance
2. **Evidence** — what the tool produces as documentation
3. **Verifiability** — buyers can check the documentation without trusting the vendor
4. **Independence** — the tool isn't biased toward vendors or buyers
5. **Standards compliance** — the tool maps to EU AI Act requirements

CSOAI provides each:

1. **Methodology as code** — `tasks/_gspc_scoring.py` in GitHub
2. **Signed cards** — Ed25519-signed JSON output
3. **Public verifier** — `councilof.ai/gspc-verify` (browser-based, no login)
4. **No payment from measured entities** — structural independence, documented at `UK_DRAFTS/funding-statement.html`
5. **Direct mapping to EU AI Act risk tiers** — see AX-01 governance axis

## The integration pattern

A compliance tool vendor integrates CSOAI in five steps:

1. **Vendor's UI** captures client input (model identity, version, deployment context)
2. **Vendor's tool** runs the AI on CSOAI's harness (locally or via MCP server)
3. **Vendor's tool** fetches CSOAI's signed card for the result
4. **Vendor's tool** renders compliance documentation with the card embedded
5. **Vendor cites** the card's `content_id` and `signature` in their audit trail

The vendor's UI handles the user experience. CSOAI handles the measurement evidence.

## Concrete integration example

Here's a minimal example of how a compliance vendor integrates CSOAI's evidence:

```python
import requests

# Step 1: Run measurement via x402 (or local harness)
response = requests.post(
    "https://councilof.ai/api/gspc/run",
    headers={"X-PAYMENT": "<x402 payment proof>"},
    json={
        "subject": "client-model@version",
        "axis": "governance",
        "items_hash": "<sha256-of-items>"
    }
)

# Step 2: Receive signed card
signed_card = response.json()

# Step 3: Verify in browser
verify_url = f"https://councilof.ai/gspc-verify/#card={signed_card['content_id']}"

# Step 4: Cite in your client's compliance documentation
client_compliance_doc += f"""
Model: {signed_card['subject']}
Axis: {signed_card['axis']}
Content hash: {signed_card['content_id']}
Signature: {signed_card['signature'][:32]}...
Verify at: {verify_url}
"""
```

The buyer sees the card's content hash and signature. They can verify independently at `councilof.ai/gspc-verify`. They don't have to trust the vendor.

## Why CSOAI is the right layer

CSOAI is the right layer because:

1. **Open methodology** — vendors can audit `tasks/_gspc_scoring.py`
2. **Signed cards** — regulators can verify any card against the published root tree
3. **Independent** — no conflict of interest (CSOAI doesn't accept payment from measured entities)
4. **Standardized** — 22 axes, same for everyone
5. **MCP-native** — works with AI agents via `csoai-gspc-mcp`
6. **x402-native** — works with paid APIs (HTTP 402 + USDC on Base)
7. **A2A-native** — works with agent frameworks (agent card at `.well-known/agent-card.json`)

The vendor's compliance tool becomes more credible when it's powered by CSOAI. The vendor can say: "Here's our compliance report. Each result is independently verifiable at councilof.ai/gspc-verify."

## What CSOAI offers compliance vendors

CSOAI offers four integration models:

1. **Embedded measurement** — the vendor's tool runs CSOAI's harness directly via the open-source repo
2. **MCP integration** — the vendor's AI agents use `csoai-gspc-mcp` for measurement queries
3. **x402-metered tools** — $0.01 per fresh measurement, paid via USDC on Base mainnet
4. **Enterprise white-label** — vendor's branding on the verifier, dedicated support

The vendor doesn't have to build measurement infrastructure. The vendor can focus on UI/UX and compliance reporting.

## Pricing

- **Free:** Public verifier, signed cards, methodology (read-only)
- **x402-metered:** $0.01 per measurement for fresh runs (most common)
- **Enterprise:** White-label, custom integrations, dedicated support
- **Sponsorship:** Foundations and labs can sponsor the public infrastructure (no editorial control)

The vendor chooses the model that fits their business. CSOAI does not take a margin on the vendor's product; CSOAI charges only for the measurement infrastructure.

## What CSOAI is NOT

CSOAI is NOT:

- A compliance tool vendor (we don't sell UIs)
- A consultancy (we don't sell advisory services)
- A certification body (we don't issue conformity marks)
- A risk management platform (we don't sell dashboards)
- A regulator (we don't make compliance determinations)

CSOAI is the evidence layer that compliance tool vendors build on.

## What this means for the EU AI Act market

The EU AI Act is creating a new market. CSOAI's positioning:

- The compliance tool vendors are the UI layer (they own the customer relationship)
- CSOAI is the evidence layer (anyone can verify any measurement)
- Regulators verify the evidence layer (regulator's own auditors can run the harness)
- Buyers trust the evidence layer (because they can verify it themselves)

This is the standard stack for the EU AI Act compliance market. Each layer has clear responsibilities:

- **Compliance vendors:** Customer-facing UX, integration, reporting
- **CSOAI:** Measurement methodology, signed evidence, public verifier
- **Regulators:** Verification of evidence trail, compliance determinations
- **AI developers:** Run their models against CSOAI's harness, cite the signed cards

## How to get started

For a compliance tool vendor integrating CSOAI:

1. **Read the methodology:** https://github.com/CSOAI-ORG/gspc-harness/blob/hermes/inspect-register-readiness/tasks/_gspc_scoring.py
2. **Run the local harness:** `inspect eval tasks/gspc_governance.py --model mockllm/model`
3. **Verify a card:** https://councilof.ai/gspc-verify/ (paste any signed card JSON)
4. **Integrate via MCP:** https://www.npmjs.com/package/csoai-gspc-mcp (npm install; verify at MCP Registry PR #4806)
5. **Subscribe to corrections:** RSS feed at `councilof.ai/feeds/corrections.xml`

The integration is straightforward — hours, not weeks. The value is structural — independent evidence that any buyer or regulator can verify.

## The bottom line

EU AI Act compliance is a new market. CSOAI is the evidence layer that compliance tools should build on. The integration is straightforward; the value is structural.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
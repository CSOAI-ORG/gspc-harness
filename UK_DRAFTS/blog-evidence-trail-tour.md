---
title: "What CSOAI's public evidence trail actually looks like"
published: false
description: "A guided tour of CSOAI's public evidence trail: the website, the API, the root tree, the corrections feed, the verifier, the DID, the MCP server. Each component documented."
tags: evidence-trail, public-surface, comprehensive, csai, tour, walkthrough
canonical_url: https://councilof.ai
---

# What CSOAI's public evidence trail actually looks like

A guided tour of CSOAI's public evidence trail: the website, the API, the root tree, the corrections feed, the verifier, the DID, the MCP server. Each component documented.

## The 12 components

CSOAI's public evidence trail is composed of 12 components. Each is verifiable.

### 1. The website (`councilof.ai`)

The main entry point. Hosts the documentation, blog posts, and links to the evidence trail.

**What's verifiable:** The HTML is content-addressed; the site is signed by Cloudflare.

### 2. The board API (`councilof.ai/api/gspc`)

Returns the current state of all measured subjects. JSON with version, schema, totals, axes, domains, limitations.

**What's verifiable:** The JSON schema is documented; the content is content-addressed.

### 3. The card catalog (`councilof.ai/signed/card_index.json`)

The signed index of all published cards. Contains card IDs, subjects, axes, timestamps.

**What's verifiable:** The catalog itself is signed by CSOAI's HSM.

### 4. The root tree (`councilof.ai/root.json`)

The Merkle root of all signed cards. Updated periodically. Anchored in Rekor and OTS/Bitcoin.

**What's verifiable:** The root hash is published; the Merkle inclusion proofs are verifiable.

### 5. The corrections feed (`councilof.ai/feeds/corrections.xml`)

Machine-derived log of every error CSOAI finds in its own measurements.

**What's verifiable:** The feed is signed; each entry links to old and new cards in the root tree.

### 6. The verifier (`councilof.ai/gspc-verify`)

Browser-based verifier. Recomputes content hash, verifies signature, checks Merkle inclusion.

**What's verifiable:** Runs entirely in the browser; no server-side trust required.

### 7. The DID document (`csoai.org/.well-known/did.json`)

Standard W3C DID document. Lists verification methods, including the Ed25519 signing key.

**What's verifiable:** W3C DID spec; published at a stable URL.

### 8. The MCP server (`csoai-gspc-mcp` on npm)

Open-source MCP server. 8 free tools + 4 x402-metered tools.

**What's verifiable:** Source code on GitHub; npm package metadata.

### 9. The A2A agent card (`councilof.ai/.well-known/agent-card.json`)

Standard A2A format. Lists supported skills, requirements, payment rails.

**What's verifiable:** A2A spec; published at `.well-known/` URL.

### 10. The x402 catalog (`councilof.ai/.well-known/x402.json`)

Lists every metered endpoint with amount, asset, network, pay-to.

**What's verifiable:** x402 spec; the EIP-712 receipts are signed.

### 11. The corrections documentation

Documentation about how corrections work, why they're machine-derived, and how to verify them.

**What's verifiable:** Documented in the corrections feed itself.

### 12. The methodology (`github.com/CSOAI-ORG/gspc-harness`)

Full source code for the GSPC harness. Includes the scoring rules, items, axes.

**What's verifiable:** Git history; tests; CI pipeline.

## How the components fit together

```
                [1] website
                    ↓
              [2] board API
                    ↓
            [3] card catalog ←→ [7] DID document
                    ↓
              [4] root tree ←→ [5] corrections feed
                    ↓              ↓
                [6] verifier ←→ [10] x402 catalog
                    ↓
        [8] MCP server ←→ [9] A2A agent card
                    ↓
              [12] methodology
```

The arrows show how components reference each other. A reader can start anywhere and follow the arrows to verify the system.

## What a researcher would do

A researcher verifying CSOAI's evidence:

1. Fetch a signed card from `[3]` (card catalog)
2. Verify the signature against `[7]` (DID document)
3. Verify Merkle inclusion against `[4]` (root tree)
4. Cross-check the corrections feed `[5]` for supersessions
5. Run the methodology in `[12]` to reproduce the measurement

This is the full verification chain. Each step is documented.

## What a buyer would do

A buyer using CSOAI's evidence:

1. Fetch a card from `[3]`
2. Verify via `[6]` (verifier) — paste JSON, get VALID/INVALID
3. Cite the card's `content_id` in their own documentation
4. Subscribe to `[5]` (corrections feed) for updates

## What a regulator would do

A regulator auditing CSOAI's evidence:

1. Sample several cards from `[3]`
2. Verify each via `[6]` (verifier)
3. Cross-reference `[5]` (corrections) with `[4]` (root tree)
4. Audit `[12]` (methodology) for soundness
5. Check `[7]` (DID) for key custody

## The bottom line

12 components, all verifiable, all documented. That's CSOAI's evidence trail.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
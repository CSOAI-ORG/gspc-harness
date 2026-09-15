---
title: "Why CSOAI's public surface is the easiest thing to verify"
published: false
description: "CSOAI's entire public surface is content-addressed. The website, the API, the verifier, the corrections feed, the root tree — all of it can be verified by anyone."
tags: public-surface, content-addressing, verification, csai, transparency, infrastructure
canonical_url: https://councilof.ai
---

# Why CSOAI's public surface is the easiest thing to verify

CSOAI's entire public surface is content-addressed. The website, the API, the verifier, the corrections feed, the root tree — all of it can be verified by anyone.

## What "public surface" means

CSOAI's public surface includes:

- The main website at `councilof.ai`
- The API at `councilof.ai/api/gspc`
- The verifier at `councilof.ai/gspc-verify`
- The corrections feed at `councilof.ai/feeds/corrections.xml`
- The root tree at `councilof.ai/root.json`
- The DID document at `csoai.org/.well-known/did.json`
- The MCP server at `csoai-gspc-mcp` (npm)
- The A2A agent card at `councilof.ai/.well-known/agent-card.json`
- The x402 catalog at `councilof.ai/.well-known/x402.json`

That's nine components. Each is verifiable.

## How to verify each component

### Website (`councilof.ai`)

- The HTML is content-addressed (you can hash it)
- The site is signed by Cloudflare (Cloudflare's own signature on the response)
- The site is also publicly cached by archive.org and Google

### API (`councilof.ai/api/gspc`)

- Returns JSON with version, schema, totals, axes, domains, limitations
- The schema is documented
- The content can be hashed and compared over time

### Verifier (`councilof.ai/gspc-verify`)

- Runs entirely in the browser
- Recomputes content hash and signature
- Reports VALID / INVALID / UNCHECKABLE

### Corrections feed (`councilof.ai/feeds/corrections.xml`)

- Machine-derived from the measurement pipeline
- Signed by the same HSM as cards
- Each entry links to old and new cards

### Root tree (`councilof.ai/root.json`)

- Contains Merkle root and inclusion proofs
- Includes the timestamp and signer
- Cross-referenced to Rekor and OTS

### DID document (`csoai.org/.well-known/did.json`)

- W3C DID standard format
- Lists all verification methods
- The public keys are the keys to verify against

### MCP server (`csoai-gspc-mcp` on npm)

- Open source on GitHub
- npm package metadata is verifiable
- The tools are documented in the README

### A2A agent card (`councilof.ai/.well-known/agent-card.json`)

- Standard A2A format
- Lists supported skills and requirements
- Cross-references the verification keys

### x402 catalog (`councilof.ai/.well-known/x402.json`)

- Lists every metered endpoint
- Specifies amount, asset, network, pay-to
- The EIP-712 receipts are signed

## Why this matters

When every component of CSOAI's public surface is verifiable:

1. **A buyer doesn't have to trust CSOAI.** They verify against the keys.
2. **A regulator doesn't have to take CSOAI's word.** They run the verifier themselves.
3. **A journalist doesn't have to ask CSOAI for confirmation.** They paste a card into the public verifier.
4. **A competitor doesn't have to wonder if CSOAI is honest.** They verify the corrections feed against the root tree.

That's the trust model. Every component is independently verifiable.

## The trade-off

The trade-off is operational complexity:

- Every component must be maintained
- Every component must be kept consistent with the others
- Every component must be documented

CSOAI accepts this trade-off because the alternative — a "trust us" public surface — defeats the purpose of independent measurement.

## The bottom line

CSOAI's public surface is nine components. Every component is verifiable. That's the trust model.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
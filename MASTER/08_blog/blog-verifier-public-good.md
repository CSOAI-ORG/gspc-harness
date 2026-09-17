---
title: "Why CSOAI's verifier is a public good, not a paywall"
published: false
description: "CSOAI's verifier at councilof.ai/gspc-verify is free, open, and runs in your browser. That's not charity — it's the only way verification actually works."
tags: verifier, public-good, verification, paywall, csai, transparency
canonical_url: https://councilof.ai
---

# Why CSOAI's verifier is a public good, not a paywall

CSOAI's verifier at `councilof.ai/gspc-verify` is free, open, and runs in your browser. That's not charity — it's the only way verification actually works.

## What the verifier does

The verifier:

1. Receives a signed card JSON
2. Recomputes the SHA-256 content hash using JCS canonicalisation
3. Verifies the Ed25519 signature against the published DID key
4. Fetches the public root tree
5. Verifies Merkle inclusion (the card is in the tree)
6. Reports VALID, INVALID, or UNCHECKABLE

The whole thing runs **in your browser**. No API call. No server-side computation. No CSOAI login required.

## Why this matters

Verification is only useful if you can do it yourself. If verification requires trusting the operator, you haven't really verified anything.

Example: "Trust us, the signature is valid" is not verification. That's a claim. Verification is: "I recomputed the signature in my browser against the published public key, and the math checks out."

CSOAI's verifier is the second kind. Anyone with a browser can run it. The result is reproducible by anyone who runs the same computation.

## Why free, not paywall

If the verifier were behind a paywall or required CSOAI credentials:

1. **Buyers would have to trust CSOAI to tell them whether the receipt is valid.** That's the opposite of verification.
2. **Regulators would have to build a CSOAI account.** That's friction with no benefit.
3. **Journalists couldn't quote receipts in articles.** They'd have to ask CSOAI for verification, which CSOAI could decline.

Making the verifier free, public, and browser-based solves all three problems. It also reveals which CSOAI receipts are invalid — if any — without anyone asking CSOAI.

## The economic argument

You might think: "if verification is free, why would anyone pay for x402 tools?"

The answer:

- **Verification is for everyone.** Buyers, regulators, journalists, competitors, researchers.
- **x402 tools are for repeat users.** People who need fresh measurements, attestations, signatures regularly.

The verifier is like a public clock tower: everyone benefits from knowing the time. The x402 tools are like a professional watchmaker: a different product for a different user.

## What this looks like in practice

Anyone can visit `councilof.ai/gspc-verify`, paste a signed card JSON, and get a verdict. The verdict is computed entirely in their browser. The only network call is to fetch the root tree and DID document — both public.

No tracking. No cookies. No analytics. No login. No paywall.

## The bottom line

The verifier is free, public, and browser-based. That's how verification works.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
---
title: "Why AI governance needs cryptographic receipts, not vibes"
published: false
description: "Industry estimates suggest most organisations aren't ready for the EU AI Act's August 2026 transparency requirements. Here's how signed, content-addressed evidence changes the game — and why CSOAI's approach works across x402, A2A, MCP, and SCITT."
tags: ai, governance, eu-ai-act, cryptography, regulation, compliance, receipts
canonical_url: https://councilof.ai
---

# Why AI governance needs cryptographic receipts, not vibes

The EU AI Act's Article 50 transparency requirements came into force on August 2, 2026. Industry surveys (Gartner, IDC, McKinsey AI governance reports 2024-2026) suggest most large enterprises are not yet operationally ready for full compliance. The gap isn't awareness — it's evidence.

Organisations know they need to demonstrate AI governance. What they don't have is a way to produce evidence that's **machine-readable**, **cryptographically signed**, **content-addressed**, and **publicly verifiable** — without trusting the publisher's server.

That's what CSOAI builds.

## The evidence problem

Current AI governance documentation looks like this:

1. A PDF report with a compliance checklist
2. A spreadsheet of model evaluations
3. A blog post claiming "we tested it"
4. A vendor-issued certificate with no independent verification

None of these survive the question: **"Can I verify this without trusting you?"**

If the answer is no, you don't have evidence — you have vibes.

## What cryptographic receipts look like

CSOAI's GSPC harness produces receipts that are:

- **Content-addressed:** SHA-256 hash of the canonical JSON body. Change one byte, change the hash.
- **Ed25519-signed:** Every receipt is signed against a published key at `csoai.org/.well-known/did.json`.
- **Merkle-rooted:** 257 receipts are committed to a public Merkle tree, witnessed in Rekor (log index 2837824756) and anchored to Bitcoin via OpenTimestamps (block 966764).
- **Publicly verifiable:** Anyone can paste a receipt into `councilof.ai/gspc-verify` and verify it in their browser — no account, no API call, no trust required.

This isn't aspirational. It's live. Today.

## The honesty register: what makes CSOAI different

The most important feature isn't the cryptography — it's the honesty register.

When CSOAI's harness evaluates a model and the model's answer can't be parsed, that item is reported as **UNMEASURED** — never scored as wrong. Stock evaluation frameworks map unparseable answers to 0.0 and keep them in the denominator. That converts "we don't know" into "the model failed."

CSOAI's scorer reports four numbers together: `accuracy_measured`, `usable_n`, `unmeasured`, `stderr_gated`. The denominator is always visible. The usable sample size is always stated. The confidence interval is gated at n≥30.

This is what the EU AI Act's transparency requirements actually need: not a compliance checklist, but an evidence system that distinguishes measured, unmeasured, and unknown.

## Interoperability: receipts that work across protocols

CSOAI's receipts aren't just signed — they're interoperable:

- **x402 (Base mainnet):** Metered evidence tools settle on-chain via USDC. $0.01 per proof.
- **A2A (Agent-to-Agent):** Agent card at `councilof.ai/.well-known/agent-card.json` enables agent-to-agent discovery.
- **MCP (Model Context Protocol):** 12 tools via `csoai-gspc-mcp` — 8 free readers + 4 x402-metered evidence tools.
- **SCITT (IETF transparency):** Rekor transparency log + OTS Bitcoin anchoring.
- **did:web:** 4 Ed25519 verification methods at `csoai.org/.well-known/did.json`.
- **EIP-712:** Deterministic (RFC 6979) Ethereum typed structured data signing.

This means a receipt produced by CSOAI can be verified by any system that speaks these protocols — not just ours.

## What regulators are starting to require

California's SB 813 (signed September 9, 2026) creates statutory **Independent Verification Organizations** (IVOs) — the first US statutory framework for exactly this kind of independent, third-party AI verification. AB 1405 creates an AI Auditor Registry by 2029.

CSOAI's approach — no payment from measured entities, no publication gag, corrections ledger governs disputes — maps directly to what these statutes will require.

The UK's AI Safety Institute (AISI) already uses Inspect as its evaluation framework. CSOAI's harness is built on Inspect. The interoperability is structural, not aspirational.

## Try it yourself

```bash
git clone https://github.com/CSOAI-ORG/gspc-harness
cd gspc-harness
pip install ".[receipts]"
inspect eval tasks/gspc_governance.py --model openai/gpt-4o
```

Or verify an existing receipt at **[councilof.ai/gspc-verify](https://councilof.ai/gspc-verify/)** — paste the JSON, verify in your browser.

The corrections feed is at **[councilof.ai/feeds/corrections.xml](https://councilof.ai/feeds/corrections.xml)**.

The full measurement board is at **[councilof.ai/api/gspc](https://councilof.ai/api/gspc)**.

## The bottom line

AI governance needs cryptographic receipts, not vibes. The EU AI Act is enforcing it. California is legislating it. CSOAI is building it.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
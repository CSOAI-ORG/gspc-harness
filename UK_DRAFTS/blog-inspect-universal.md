---
title: "Inspect AI is becoming the universal evaluation framework — here's what that means for independence"
published: false
description: "UK AISI's Inspect framework is the foundation for CSOAI's harness and for Anthropic/OpenAI/Google/Meta's evaluations. That concentration needs independent measurement."
tags: inspect-ai, uk-aisi, anthropic, openai, google, meta, ai-safety, independence
canonical_url: https://councilof.ai
---

# Inspect AI is becoming the universal evaluation framework — here's what that means for independence

UK AI Safety Institute's Inspect framework is becoming the universal AI evaluation framework:

- **CSOAI's GSPC harness** is built on Inspect.
- **Anthropic's evaluations** use Inspect.
- **OpenAI's system cards** reference Inspect-compatible harnesses.
- **Google DeepMind** runs evaluations on Inspect-compatible setups.
- **Meta's Llama team** uses Inspect for safety evaluations.

When the same framework is used by the labs being measured **and** by the independent measurer, the question of measurement independence becomes structural.

## Why this matters

CSOAI's harness is built on Inspect. That means:

1. **Our harness inherits Inspect's auditing.** Any Inspect compliance check applies to our pipeline.
2. **Our results are reproducible in any Inspect-compatible setup.** Labs and independent reviewers can re-run our methodology.
3. **Our signed receipts bind to specific Inspect run metadata.** A receipt is verifiable against the exact model + version + items + harness commit.

But it also means:
- If Inspect has a bug, every harness using it inherits the bug.
- If a lab customizes Inspect, the receipt must reflect the customization.
- "Inspect-compatible" becomes a market signal — and we need a way to verify it.

## CSOAI's layered independence

CSOAI adds three layers of independence on top of Inspect:

1. **Signed receipts** — every Inspect run produces an Ed25519-signed card bound to the run metadata.
2. **Content-addressing** — SHA-256 hash of the canonical JSON body, enabling offline verification.
3. **Corrections ledger** — publicly auditable feed of every error we catch in our own measurements.

Inspect is the harness. CSOAI's receipts make the harness's output independently verifiable.

## The bottom line

Inspect is becoming universal. That's good for reproducibility. CSOAI's signed receipts make that universality independently verifiable.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
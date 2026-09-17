---
title: "CSOAI vs Hugging Face — different layers of the same stack"
published: false
description: "CSOAI measures; Hugging Face hosts. Both are open. They're complementary, not competitive. Here's how to use them together for independent AI governance."
tags: huggingface, csai, open-source, ai-governance, measurement, hosting, distribution
canonical_url: https://councilof.ai
---

# CSOAI vs Hugging Face — different layers of the same stack

CSOAI and Hugging Face are sometimes mistaken for competitors. They aren't. They operate at different layers of the same stack.

## What Hugging Face does

Hugging Face is the **distribution and discovery layer** for ML models, datasets, and spaces. It provides:

- **Hub** — a Git-like platform for hosting models, datasets, and Spaces
- **Discovery** — tags, search, and metadata for finding models
- **Spaces** — interactive demos (Gradio, Streamlit, Docker)
- **Inference API** — hosted inference for popular models
- **Community** — contributions, discussions, organization pages
- **Datasets Hub** — versioned datasets with documentation
- **Trainer library** — fine-tuning helpers (Transformers, PEFT, TRL)

When a model is "on Hugging Face," it's typically findable, downloadable, and may have an inference endpoint.

## What CSOAI does

CSOAI is the **measurement and evidence layer**. CSOAI provides:

- **GSPC harness** — 22-axis deterministic measurement framework
- **Signed receipts** — Ed25519-signed cards bound to specific runs
- **Content-addressing** — SHA-256 hash of canonical JSON
- **Independent verification** — browser-based tool at `councilof.ai/gspc-verify`
- **Corrections ledger** — machine-derived feed of every error caught

When a card is "on CSOAI," it carries signed evidence about what the model did on a specific item set, independently of the model's publisher.

## How they fit together

The combined stack:

1. **Hugging Face hosts the model** and the dataset.
2. **CSOAI measures the model** on a specific dataset.
3. **The signed receipt** binds the model identity (Hugging Face URL) to the measurement result.
4. **The public verifier** checks the receipt against the published keys.
5. **The corrections feed** records any errors found in our own measurement.

This is the trust stack: discovery → distribution → measurement → signed evidence → public verification → corrections.

## What each layer does NOT do

Each layer has a clear scope:

| Layer | Does | Does NOT |
|---|---|---|
| Hugging Face | Hosts, distributes, discovers | Measures AI behavior |
| CSOAI | Measures, signs, verifies | Hosts or distributes |

Neither layer does the other's job. They sit on top of each other.

## Why this matters for the EU AI Act

When the EU AI Act requires evidence of governance, the standard stack is:

- Use Hugging Face to find and host models.
- Use CSOAI to produce signed evidence about those models.
- Reference the signed receipt from CSOAI in your AI Act compliance documentation.

CSOAI's hub-card already describes the distinction: a valid signature does not establish current measurement admission. CSOAI measures; HF hosts. They're complementary.

## What CSOAI does NOT measure about Hugging Face

CSOAI does NOT measure:

- Whether a model on HF is safe (that's what CSOAI measures the model on)
- Whether HF's hosting is reliable (HF is responsible for their infrastructure)
- Whether a dataset on HF is accurate (that's the dataset owner's responsibility)
- Whether a Spaces demo is honest (HF is responsible for hosting policy)
- HF's revenue, pricing, business model (HF's responsibility)

CSOAI measures the model behavior. HF is the substrate. The two are separate.

## What Hugging Face does NOT do that CSOAI does

Hugging Face does NOT:

- Sign the model's output (HF signs the model file, not the model's responses)
- Content-address the model's responses (HF content-addresses files, not behavior)
- Provide a public verifier for measurements (HF has Spaces for demos, not measurement)
- Operate a corrections ledger for measurements (HF has Issues, not corrections feed)
- Track measurement methodology versions (HF tracks model versions, not methodology)

CSOAI does each of these. The two are complementary.

## What a combined workflow looks like

For an AI developer using both:

1. **Host the model** on Hugging Face Hub (with proper model card, license, README)
2. **Use the model** via HF Inference API or self-hosted
3. **Run CSOAI's harness** against the model on specific test conditions
4. **Cite the Hugging Face URL** in the CSOAI signed card's `subject` field
5. **P[...] CSOAI cards on a public board** (or in the HF model card)
6. **Subscribe to CSOAI's corrections feed** for ongoing monitoring

The Hugging Face URL becomes the model's identity. The CSOAI card becomes the model's measured behavior.

## Concrete example

A developer hosts their model on Hugging Face:

```python
# On HF Hub:
# https://huggingface.co/example-org/example-model

# They run CSOAI's harness:
from inspect_ai import eval
result = eval(
    "tasks/gspc_governance.py",
    model="openai/anthropic.claude-3-sonnet",
)
```

The CSOAI signed card includes:
- `subject`: `https://huggingface.co/example-org/example-model`
- `axis`: `governance`
- `method`: `exact-tier-match`
- `operational`: {accuracy_measured, usable_n, unmeasured, stderr_gated}
- `content_id`: `sha256:...`
- `signature`: `ed25519:...`

The HF URL is the model identity. The CSOAI card is the measured behavior. The verifier at `councilof.ai/gspc-verify` lets anyone check both.

## Why CSOAI's structural independence matters in this stack

In a combined Hugging Face + CSOAI workflow, the credibility depends on:

1. **HF doesn't suppress the CSOAI card.** HF has no incentive to suppress.
2. **The model owner can't suppress the CSOAI card** (CSOAI doesn't let them).
3. **CSOAI's measurement is independent** of HF's hosting and the model owner's commercial interests.

If the model's behavior degrades, CSOAI's corrections feed documents it. HF's hosting doesn't change the measurement. The model owner's press doesn't change the measurement.

## What CSOAI offers for HF users

For HF users (model publishers, model users, regulators):

1. **Independent measurement** of any HF-hosted model
2. **Signed cards** that reference the HF URL
3. **Public verifier** that anyone can run
4. **Corrections feed** that documents measurement errors
5. **No vendor lock-in** — methodology is in source code

## What CSOAI needs from HF

For CSOAI to integrate cleanly with HF:

1. **Stable HF URLs** — model identity is the URL
2. **Model card metadata** — including license, intended use, training data
3. **HF Inference API** — works with OpenAI-compatible API standard (which CSOAI uses)
4. **HF Spaces** — can host CSOAI's verifier UI (optional)

## What CSOAI does NOT need from HF

CSOAI does NOT need:

1. HF to approve CSOAI's measurements (HF doesn't gate evaluations)
2. HF to host CSOAI's infrastructure (CSOAI is on its own infrastructure)
3. HF to provide data about model performance (CSOAI runs its own)
4. HF's enterprise plan (CSOAI is open source)

The relationship is non-coupled. CSOAI works whether HF exists or not.

## What HF gains by being adjacent to CSOAI

For Hugging Face:

1. **Independent measurement** of models hosted on HF Hub (via CSOAI)
2. **Audit trail** for high-stakes models (EU AI Act compliance)
3. **Trust signal** for HF-hosted models (CSOAI's signed cards demonstrate independent verification)
4. **No work** for HF itself — CSOAI's measurement is external

HF doesn't have to do anything for CSOAI to measure HF-hosted models. CSOAI's harness can run against any model that has an OpenAI-compatible API.

## Why this matters for AI governance

The combination of HF + CSOAI creates a verifiable AI stack:

- HF provides model hosting and discovery
- CSOAI provides independent measurement evidence
- Buyers get both: a model and evidence about it
- Regulators get both: a model and audit trail
- The market can compare models on the same axes

Without either layer, the market is missing something:
- Without HF: no discovery
- Without CSOAI: no independent measurement

With both: a complete AI governance substrate.

## What CSOAI is NOT

CSOAI is NOT:

- A competitor to Hugging Face (complementary)
- A replacement for Hugging Face (different layer)
- A Hugging Face wrapper (independent)
- A distribution channel (that's HF)
- A dataset host (that's HF)
- A Spaces runner (that's HF)

CSOAI is measurement infrastructure for AI on any infrastructure, including HF-hosted.

## The bottom line

Different layers. Same goal. Independent evidence.

Hugging Face: distribution layer.
CSOAI: measurement layer.
Together: the AI governance stack that EU AI Act, UK AISI, SB 813 IVO, and NIST 300-1 expect.

CSOAI's structural independence — no payment from measured entities — makes it the natural choice for measuring AI on any host, including HF.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
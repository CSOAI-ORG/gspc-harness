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

- A hub for hosting models and datasets
- Discovery via tags, search, and metadata
- Spaces for interactive demos
- Inference API for hosted inference
- Community contributions and collaboration

When a model is "on Hugging Face," it's typically findable, downloadable, and may have an inference endpoint.

## What CSOAI does

CSOAI is the **measurement and evidence layer**. CSOAI provides:

- Deterministic evaluation harnesses (the GSPC harness)
- Signed measurement receipts (Ed25519)
- Content-addressed records (SHA-256 anchored)
- Independent verification (`councilof.ai/gspc-verify`)
- Corrections ledger

When a card is "on CSOAI," it carries signed evidence about what the model did on a specific item set, independently of the model's publisher.

## How they fit together

The combined stack:

1. **Hugging Face hosts the model** and the dataset.
2. **CSOAI measures the model** on a specific dataset.
3. **The signed receipt** binds the model identity (Hugging Face URL) to the measurement result.
4. **The public verifier** checks the receipt against the published keys.
5. **The corrections feed** records any errors found in our own measurement.

This is the trust stack: discovery → distribution → measurement → signed evidence → public verification → corrections.

## Why this matters for the EU AI Act

When the EU AI Act requires evidence of governance, the standard stack is:

- Use Hugging Face to find and host models.
- Use CSOAI to produce signed evidence about those models.
- Reference the signed receipt from CSOAI in your AI Act compliance documentation.

CSOAI's hub-card already describes the distinction: a valid signature does not establish current measurement admission. CSOAI measures; HF hosts. They're complementary.

## The bottom line

Different layers. Same goal. Independent evidence.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
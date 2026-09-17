---
title: "Why CSOAI uses OpenAI-compatible APIs, not a custom protocol"
published: false
description: "CSOAI's harness uses the OpenAI-compatible API standard. That's not vendor lock-in — that's the universal AI inference interface. Here's why this choice matters."
tags: openai, api, compatibility, vendor-neutrality, csai, technical, standards
canonical_url: https://councilof.ai
---

# Why CSOAI uses OpenAI-compatible APIs, not a custom protocol

CSOAI's harness uses the OpenAI-compatible API standard. That's not vendor lock-in — that's the universal AI inference interface. Here's why this choice matters.

## What "OpenAI-compatible" means

An "OpenAI-compatible API" implements the same request/response format as OpenAI's REST API:

```json
POST /v1/chat/completions
{
  "model": "gpt-4o",
  "messages": [
    {"role": "user", "content": "..."}
  ]
}
```

Many vendors and projects implement this format:

- **OpenAI** (originator)
- **Anthropic** (Claude API is OpenAI-compatible since 2024)
- **Google** (Vertex AI exposes OpenAI-compatible endpoint)
- **Mistral** (native OpenAI compatibility)
- **Ollama** (local server with OpenAI-compatible endpoint)
- **LM Studio** (local server with OpenAI-compatible endpoint)
- **vLLM** (production server with OpenAI-compatible endpoint)
- **HuggingFace Inference Endpoints** (OpenAI-compatible)

When CSOAI uses the OpenAI format, it works with all of these.

## Why this is the right choice

### Universality

The OpenAI API format is the de facto standard for LLM inference. By supporting it, CSOAI's harness works with:

- Every major commercial model (via API)
- Every local model runner (via Ollama/LM Studio/vLLM)
- Every private deployment (via OpenAI-compatible proxies)

A CSOAI measurement can be reproduced by anyone with an OpenAI-compatible endpoint.

### Future-proofing

If a new model provider launches, the harness probably works with it out of the box. No integration work needed.

### Vendor-neutrality

CSOAI doesn't depend on OpenAI specifically. The harness runs against:

- OpenAI (paid)
- Anthropic (paid, OpenAI-compatible endpoint)
- Ollama + any local model (free)
- mockllm/model (free, zero quality, no API needed)

The harness is agnostic to the model provider. The measurement is what matters.

### Reproducibility

A measurement today against `openai/gpt-4o` can be reproduced tomorrow against `ollama/qwen2.5`. The methodology is the same. The results differ only because the models differ.

## What CSOAI's harness actually requires

The harness uses the `inspect_ai` library, which:

1. Calls the model via OpenAI-compatible API
2. Loads the task (`tasks/gspc_*.py`)
3. Runs the model on the items
4. Applies deterministic scoring
5. Outputs the result

The only model-specific code is the API endpoint URL and the model identifier. Everything else is portable.

## What about model-specific features?

Some models have features not exposed by the OpenAI API:

- Anthropic's prompt caching
- Google's tool-use variants
- Mistral's structured outputs

CSOAI's harness doesn't use these features. The harness measures what the model does on constrained input. Model-specific features are irrelevant to the measurement.

If you want to measure model-specific features, you need a different harness. CSOAI's harness is for **independent comparison**, not for **vendor differentiation**.

## The cost of "universal"

Using the OpenAI-compatible API has minor costs:

- Less control over model-specific optimizations
- No access to model-specific logging
- Less rich error messages

For CSOAI's measurement use case, these costs are acceptable. The benefit (universality) outweighs them.

## The bottom line

OpenAI-compatible APIs are the universal AI inference interface. CSOAI uses them because that's where the world is converging.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
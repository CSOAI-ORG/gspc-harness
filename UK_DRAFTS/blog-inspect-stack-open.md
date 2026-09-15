---
title: "Inspect AI + inspect-signed-receipt = the open evaluation stack governments asked for"
published: false
description: "UK AISI's Inspect framework plus CSOAI's inspect-signed-receipt package creates a complete open-source evaluation stack. No vendor lock-in. No proprietary signing."
tags: inspect-ai, inspect-signed-receipt, uk-aisi, open-source, ai-governance, ai-safety, signing
canonical_url: https://councilof.ai
---

# Inspect AI + inspect-signed-receipt = the open evaluation stack governments asked for

UK AISI's Inspect framework and CSOAI's `inspect-signed-receipt` package together create a complete open-source AI evaluation stack:

- **Inspect:** evaluation framework with @task decorators, sample loading, scoring
- **inspect-signed-receipt:** cryptographic signing of Inspect run outputs
- **No vendor lock-in.** No proprietary signing keys.
- **No proprietary scoring.** Deterministic, verifiable.

## What each piece does

**Inspect AI (`inspect_ai`):**
- @task decorator for evaluation runs
- Sample loading and prompt formatting
- Multiple solvers (OpenAI, Anthropic, custom)
- Built-in scorers (accuracy, regex match, etc.)
- Logs in JSON format for post-hoc analysis

**inspect-signed-receipt (PyPI):**
- Wraps Inspect eval() output
- Produces Ed25519-signed cards
- Content-addresses cards (SHA-256 over canonical body)
- Builds Merkle tree of signed cards
- Publishes to public root
- Watches in Rekor + OTS/Bitcoin

## How they fit together

```python
from inspect_ai import eval
from inspect_signed_receipt import sign_eval, publish_root

# 1. Run an evaluation
results = eval(
    "tasks/gspc_governance.py",
    model="openai/gpt-4o",
    log_dir="logs/"
)

# 2. Sign the result
signed_card = sign_eval(
    results,
    signer_did="did:web:csoai.org#board-attestation-1"
)

# 3. Publish to public root
publish_root([signed_card])
```

The output is a signed card at `councilof.ai/gspc-verify` that anyone can independently verify.

## Why this stack matters

For regulators and buyers asking "can we trust this measurement?":

1. **Open framework:** Inspect is UK AISI's official framework, not CSOAI's.
2. **Open scoring:** The GSPC harness scoring is in the public repository.
3. **Open signing:** Ed25519 keys published at `csoai.org/.well-known/did.json`.
4. **Open witnessing:** Rekor + OTS/Bitcoin provide independent witnesses.
5. **Open verification:** `councilof.ai/gspc-verify` recomputes everything in-browser.

No vendor lock-in. No proprietary signing. No proprietary storage.

## Adoption

Inspect is used by:
- UK AI Safety Institute (UK AISI)
- Anthropic
- OpenAI (system card evaluations)
- Google DeepMind
- CSOAI
- Many academic and independent labs

`inspect-signed-receipt` is used by:
- CSOAI
- Pypi downloads: ~1,300/month
- Apache-2.0 licensed
- Multi-language SDKs in development

## The bottom line

Open framework + open signing + open witnessing + open verification = the open AI governance stack governments asked for.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
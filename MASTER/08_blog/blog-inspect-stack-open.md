---
title: "Inspect AI + inspect-signed-receipt = the open evaluation stack governments asked for"
published: false
description: "UK AISI's Inspect framework plus CSOAI's inspect-signed-receipt package creates a complete open-source evaluation stack. No vendor lock-in. No proprietary signing."
tags: inspect-ai, inspect-signed-receipt, uk-aisi, open-source, ai-governance, ai-safety, signing, ed25519, rekor, opentimestamps
canonical_url: https://councilof.ai
---

# Inspect AI + inspect-signed-receipt = the open evaluation stack governments asked for

UK AISI's Inspect framework and CSOAI's `inspect-signed-receipt` package together create a complete open-source AI evaluation stack:

- **Inspect:** evaluation framework with @task decorators, sample loading, scoring
- **inspect-signed-receipt:** cryptographic signing of Inspect run outputs
- **No vendor lock-in.** No proprietary signing keys.
- **No proprietary scoring.** Deterministic, verifiable.

## What each piece does

### Inspect AI (`inspect_ai`)

- @task decorator for evaluation runs
- Sample loading and prompt formatting
- Multiple solvers (OpenAI, Anthropic, custom)
- Built-in scorers (accuracy, regex match, etc.)
- Logs in JSON format for post-hoc analysis
- Inspect log viewer (HTML, web-based)
- Inspect extension framework (custom scorers, datasets)

### inspect-signed-receipt (PyPI)

- Wraps Inspect eval() output
- Produces Ed25519-signed cards
- Content-addresses cards (SHA-256 over canonical body)
- Builds Merkle tree of signed cards
- Publishes to public root
- Watches in Rekor + OTS/Bitcoin
- Multi-language SDKs (Python primary, JS/Go/Rust in development)

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

### 1. Open framework

Inspect is UK AISI's official framework, not CSOAI's. UK AISI publishes the source code. Anyone can audit the framework. CSOAI's harness uses Inspect as a dependency.

### 2. Open scoring

The GSPC harness scoring is in the public repository at `github.com/CSOAI-ORG/gspc-harness/blob/hermes/inspect-register-readiness/tasks/_gspc_scoring.py`. Anyone can read the actual code that produces scores.

### 3. Open signing

Ed25519 keys published at `csoai.org/.well-known/did.json`. The W3C DID standard is open. Anyone can verify the keys.

### 4. Open witnessing

Rekor (Sigstore transparency log) + OpenTimestamps (Bitcoin anchor) are both open-source projects. The witnessing is independent of CSOAI.

### 5. Open verification

`councilof.ai/gspc-verify` recomputes everything in-browser. No server-side trust required. The verifier code is also open-source.

No vendor lock-in. No proprietary signing. No proprietary storage.

## Adoption

Inspect is used by:

- UK AI Safety Institute (UK AISI)
- Anthropic (safety evaluations)
- OpenAI (system card evaluations)
- Google DeepMind
- Meta
- Microsoft (research)
- CSOAI
- Many academic and independent labs

`inspect-signed-receipt` is used by:

- CSOAI
- PyPI downloads: ~1,300/month (as of recent observation)
- Apache-2.0 licensed
- Multi-language SDKs in development

## Why "open" matters for governments

Governments need AI measurement infrastructure that:

1. **They can audit.** Open source = auditable source code.
2. **They can extend.** They can add their own tasks, scorers, datasets.
3. **They can replicate.** They can run the same harness on their own infrastructure.
4. **They can verify.** The verification math doesn't require trusting CSOAI.

Inspect + inspect-signed-receipt meets all four criteria. The stack is open from framework to verification.

## Why this matters for sovereign AI

The UK Sovereign AI R&D Procurement Scheme and similar programs in EU/Asia need sovereign AI infrastructure. A sovereign government should be able to:

- Run the same evaluation framework as the global labs
- Produce signed evidence that anyone can verify
- Not depend on a single vendor (US or otherwise)

Inspect + inspect-signed-receipt is sovereign-compatible. A UK government could run CSOAI's harness on UK infrastructure and produce signed cards that any UK regulator can verify.

## Why this matters for AI labs

Major AI labs use Inspect. CSOAI's signed receipts let them:

- Cite independent measurement of their models
- Demonstrate safety commitments are backed by evidence
- Show investors and regulators the signed cards
- Compare models on the same axes

The labs don't have to use CSOAI's signed receipts specifically — but if they want independent verification of their safety claims, the framework is there.

## Why this matters for AI safety organizations

METR, Apollo Research, and similar evaluator organizations can use:

- Inspect as their framework
- inspect-signed-receipt for cryptographic verification
- CSOAI's methodology-as-code as a starting point
- Custom extensions on top of the open base

The stack is composable. Each organization can build their own measurement infrastructure on top of the open components.

## What CSOAI is NOT

CSOAI is NOT:

- The owner of Inspect (UK AISI is)
- The maintainer of inspect-signed-receipt (the package is Apache-2.0 with community contributions)
- The only entity using these tools (multiple labs and evaluators)
- A vendor with proprietary signing (all open-source)

CSOAI is one user of the open stack. The stack doesn't depend on CSOAI.

## Why CSOAI uses these tools specifically

CSOAI chose Inspect + inspect-signed-receipt because:

1. **UK AISI's official framework** — institutional credibility
2. **Open source** — auditable methodology
3. **Active maintenance** — community-driven, not single-vendor
4. **Multi-model support** — works with OpenAI, Anthropic, local models
5. **Extensibility** — custom tasks, scorers, datasets

These same properties benefit any AI measurement organization.

## The full stack at CSOAI

When CSOAI publishes a signed card:

1. **Inspect runs the model** on the specific item set
2. **inspect-signed-receipt signs the result** with Ed25519
3. **CSOAI's gspc-harness coordinates** which axes/items to test
4. **CSOAI's Merkle root commits** the card to a public tree
5. **CSOAI's corrections feed** documents errors over time
6. **CSOAI's public verifier** lets anyone check

Each component is replaceable. Inspect can be replaced with another framework. inspect-signed-receipt can be replaced with another signing library. The cards can use a different content-addressing scheme.

The stack is modular by design.

## What this means for EU AI Act compliance

EU AI Act compliance requires evidence. The stack provides:

- **Article 11 (Technical documentation):** Inspect's source + CSOAI's harness source = full documentation
- **Article 12 (Record-keeping):** Merkle root preserves every measurement
- **Article 17 (Quality management):** Methodology-as-code IS the quality documentation
- **Article 43 (Conformity assessment):** Signed cards document the assessment
- **Article 72 (Post-market monitoring):** Corrections feed documents ongoing monitoring

The stack is EU AI Act compatible by design.

## What this means for UK AISI alignment

UK AISI uses Inspect for safety evaluations. CSOAI's stack produces signed cards compatible with Inspect's logs. UK AISI could:

- Run CSOAI's harness as part of their evaluations
- Verify CSOAI's signed cards against their own infrastructure
- Cite CSOAI's signed cards in their published evaluations
- Use CSOAI's stack as a reference implementation

The alignment is structural, not commercial.

## What this means for the AI governance ecosystem

The full ecosystem:

```
                Open framework (Inspect)
                Open methodology (CSOAI harness)
                Open scoring (tasks/_gspc_scoring.py)
                Open signing (inspect-signed-receipt)
                Open witnessing (Rekor + OTS/Bitcoin)
                Open verification (councilof.ai/gspc-verify)
                Open data (CC-BY-4.0)
                Open corrections (machine-derived)
```

Each component is open. Each can be audited. Each can be replaced. The stack is sovereign-compatible.

## What this does NOT claim

CSOAI does NOT claim:

- The Inspect framework is perfect (it's UK AISI's, not ours)
- The inspect-signed-receipt package is bug-free (it's open-source; report bugs)
- The signed cards are legally binding (depends on jurisdiction)
- The measurement methodology is correct (buyer/regulator interprets)
- CSOAI is the only organization using this stack (multiple labs do)

CSOAI claims:

- The stack is open-source
- The methodology is auditable
- The signing is cryptographic
- The verification is independent

## The bottom line

Open framework + open signing + open witnessing + open verification = the open AI governance stack governments asked for.

Inspect + inspect-signed-receipt + CSOAI's harness + CSOAI's corrections feed + CSOAI's verifier = a complete, sovereign-compatible AI evaluation stack.

No vendor lock-in. No proprietary signing. No proprietary storage. The stack is open from framework to verification.

Governments that want sovereign AI infrastructure have a working example. Labs that want independent measurement have a working example. Evaluators that want verifiable results have a working example.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
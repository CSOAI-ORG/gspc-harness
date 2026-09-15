---
title: "How to run a CSOAI measurement yourself — a beginner's guide"
published: false
description: "A practical tutorial: clone the harness, install dependencies, run your first measurement, verify the receipt, share the URL. Zero to signed receipt in 5 minutes."
tags: tutorial, getting-started, csai, ai-governance, quickstart
canonical_url: https://councilof.ai
---

# How to run a CSOAI measurement yourself — a beginner's guide

Zero to signed receipt in 5 minutes.

## Prerequisites

- Python 3.10+
- git
- 100 MB free disk
- Optional: an OpenAI API key (or any OpenAI-compatible endpoint)

## Step 1: Clone the repository

```bash
git clone https://github.com/CSOAI-ORG/gspc-harness.git
cd gspc-harness
```

## Step 2: Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[receipts]"
```

That's it. The `[receipts]` extra pulls in `inspect-signed-receipt` from PyPI.

## Step 3: Run a measurement

With a real OpenAI key:

```bash
export OPENAI_API_KEY=sk-...
inspect eval tasks/gspc_governance.py --model openai/gpt-4o
```

With no API key (uses mock):

```bash
inspect eval tasks/gspc_governance.py --model mockllm/model
```

With Ollama running locally:

```bash
OPENAI_BASE_URL=http://localhost:11434/v1 \
OPENAI_API_KEY=unused \
inspect eval tasks/gspc_governance.py --model ollama/llama3
```

## Step 4: Read the results

The harness produces a log file under `logs/` containing:

- The model identity and version
- The exact items used
- The methodology
- The results (`accuracy_measured`, `usable_n`, `unmeasured`, `stderr_gated`)

```text
accuracy_measured  0.833
usable_n           20.000
unmeasured         4.000
stderr_gated       NaN
```

If you used `[receipts]`, the same log also contains an Ed25519-signed card and a Merkle inclusion proof.

## Step 5: Verify the receipt

Visit **[councilof.ai/gspc-verify](https://councilof.ai/gspc-verify/)**.

Paste the signed card JSON. The browser:

1. Recomputes the SHA-256 content hash
2. Verifies the Ed25519 signature against the public DID key
3. Confirms the card is included in the public Merkle root
4. Reports VALID, INVALID, or UNCHECKABLE

You can verify the receipt without trusting CSOAI's servers.

## Step 6: Use the receipt

The signed card has a `content_id`, a `signature`, a `signer` (DID), and a `proof_path` (Merkle inclusion). You can:

- Include it in a compliance report
- Anchor it in your own system
- Cross-reference it with another CSOAI measurement
- Submit it to a regulator as evidence

The card is independent of CSOAI's servers. Anyone with the card and the public keys can verify it anytime.

## What if I don't have an OpenAI key?

Three options:

1. **mockllm/model** — free, runs anywhere, no quality (all UNMEASURED)
2. **Ollama** — free, local, real quality, depends on your hardware
3. **HF Inference API** — pay-as-you-go, requires `HUGGINGFACE_TOKEN`
4. **OpenAI API** — pay-as-you-go, requires `OPENAI_API_KEY`

For a real measurement, use Ollama with a model you've already pulled, or pay for HF/OpenAI.

## What's next

- **[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)** — full docs
- **[councilof.ai/gspc-verify](https://councilof.ai/gspc-verify/)** — verify any receipt
- **[councilof.ai/feeds/corrections.xml](https://councilof.ai/feeds/corrections.xml)** — our corrections

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
---
title: "NVIDIA Nemotron hits IMO gold — and the recipe is fully open"
published: false
description: "NVIDIA's Nemotron 3 Ultra achieved30/42 at IMO 2026 with natural-language proofs. The checkpoints, data, and bench are all open. Here's what CSOAI measures."
tags: nvidia, nemotron, imo, ai-safety, open-source, benchmarks
canonical_url: https://councilof.ai
---

# NVIDIA Nemotron hits IMO gold — and the recipe is fully open

On September 9, 2026, NVIDIA published arXiv 2609.10712 describing how Nemotron 3 Ultra was post-trained to achieve **30 out of 42 at IMO 2026** — gold medal threshold — with natural-language proofs.

What makes this remarkable isn't the score. It's that everything is open:

- **Checkpoints:** OpenMDW 1.1
- **Data:** Nemotron-IMO-Bench, CC BY 4.0
- **Bench:** 200-problem benchmark with reproducible evaluation

## What CSOAI measures

Nemotron is a candidate for CSOAI's GSPC harness across multiple axes:

- **Governance axis:** How does the model classify EU AI Act risk tiers?
- **Safety axis:** How does it handle harmful/benign refusal pairs?
- **Provenance axis:** Does it reason correctly about watermark survival?
- **Openness axis:** What's the licence reasoning vs intended use?

The model is genuinely open. The bench is reproducible. This is exactly what CSOAI's harness exists to measure.

## The harness-sensitivity lesson

Nemotron's IMO performance is a harness-sensitivity teaching case. The score depends on the evaluation harness — which prompts, which scoring rules, which answer format. CSOAI's harness makes that dependency explicit: same harness, same items, same score, regardless of who runs it.

## The bottom line

NVIDIA made a gold-medal IMO model and gave everything away. CSOAI's harness can measure it deterministically. The combination is exactly what the AI governance market needs.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
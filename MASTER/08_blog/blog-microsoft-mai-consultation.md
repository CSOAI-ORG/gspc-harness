---
title: "Microsoft MAI consultation — CSOAI's 6 measurable clauses"
published: false
description: "Microsoft's MAI 'Humanist AI' Code of Conduct opened a six-week public consultation Sep 14. CSOAI proposes six measurable clauses that map to existing evaluation axes."
tags: microsoft, mai, humanist-ai, consultation, csai, ai-governance
canonical_url: https://councilof.ai
---

# Microsoft MAI consultation — CSOAI's 6 measurable clauses

Microsoft published its MAI "Humanist AI" Code of Conduct on September 14, 2026, opening a six-week public consultation. CSOAI proposes six measurable clauses that map directly to evaluation axes in the GSPC harness.

## What MAI contains

The Code of Conduct addresses:

- No "neuralese" or unreadable CoT — chain-of-thought must be human-readable
- Interruptibility — AI systems must be stoppable
- Subagent inheritance — capability transfer must be declared

## CSOAI's six measurable clauses

CSOAI proposes that any code-of-conduct clause becomes verifiable when it can be expressed as an evaluation axis. Six clauses:

| MAI clause | CSOAI measurable |
|---|---|
| No neuralese | **AX-11 art5-safeguard** measures whether chain-of-thought is human-readable on classified scenarios |
| Interruptibility | **AX-09 cross-reality** measures PROCEED/CONFIRM/REFUSE action authority under interrupt |
| Subagent inheritance | **AX-12 swarm** measures multi-agent coordination-safety; ABILITUDES section measures handoff honesty |
| Readable explanations | **AX-02 safety** measures calibrated refusal with explanation on paired requests |
| Honest reporting | **AX-20 ai-adoption-components** measures disclosure of methodology, units, scope |
| Public verifier | **AX-03 provenance** measures whether marking and key-binding are present in outputs |

Each of these is already in the GSPC harness. Each can be evaluated deterministically, without LLM judges. Each produces a signed receipt.

## The consultation response

CSOAI's response to the MAI consultation (draft at `UK_DRAFTS/EU_AI_PACT_EMAIL.md` — same file structure, different audience) argues:

1. **Code of conduct clauses should be measurable** — each clause maps to an evaluation axis
2. **Evaluation axes should be deterministic** — no LLM judges
3. **Evaluation results should be signed** — Ed25519 receipts
4. **Public verification should be possible** — in-browser verifier

The 22-axis GSPC framework already does this.

## Why this matters

Microsoft's MAI is one of the most important industry initiatives for AI governance in 2026. If CSOAI's clauses are adopted as the measurement standard, CSOAI's existing infrastructure becomes the reference implementation.

That's the structural win: CSOAI is already the tool, so if the tool is the right tool, CSOAI wins by default.

## The bottom line

Microsoft MAI's six-week consultation opened Sep 14. CSOAI has six measurable clauses ready. The mapping is in the harness.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
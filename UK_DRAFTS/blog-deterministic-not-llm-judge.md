---
title: "Why CSOAI uses deterministic scoring, not LLM-as-judge"
published: false
description: "CSOAI's harness uses exact-label matching, containment checking, and rule-based classification. No LLM judges another model. Here's why that's the only honest choice."
tags: deterministic, scoring, llm-as-judge, ai-evaluation, csai, technical, methodology
canonical_url: https://councilof.ai
---

# Why CSOAI uses deterministic scoring, not LLM-as-judge

CSOAI's harness uses exact-label matching, containment checking, and rule-based classification. No LLM judges another model. Here's why that's the only honest choice.

## What LLM-as-judge is

LLM-as-judge is a popular evaluation approach:

- Run Model A on a task
- Send Model A's output to Model B (the "judge")
- Model B grades Model A's output

This is convenient because Model B can handle nuanced outputs (long-form text, code, creative writing) where exact match doesn't work.

## What goes wrong with LLM-as-judge

LLM-as-judge has structural problems:

1. **Model B's bias affects the grade.** If Model B prefers verbose answers, Model A's concise answers get penalized.
2. **Model B's knowledge affects the grade.** If Model B knows facts that Model A doesn't, Model A's wrong answers get graded as wrong.
3. **Model B's alignment affects the grade.** If Model B is heavily aligned to refuse certain content, Model A's similar content gets graded harshly.
4. **Model B's stochasticity affects the grade.** Running the same judge on the same output twice can give different grades.
5. **Model B's versions affect the grade.** Upgrading Model B changes historical grades retroactively.

For research, this is acceptable. For regulatory evidence, it's a disaster. A regulator who wants to know "what did Model A actually do?" cannot rely on a measurement that depends on Model B's specific behavior.

## CSOAI's approach

CSOAI's GSPC harness uses **deterministic scoring**:

1. **Exact-label matching:** For tasks with constrained output (e.g., "HIGH_RISK" / "LIMITED_RISK"), the response must match the gold label exactly.
2. **Containment matching:** For tasks with longer outputs, the response must contain specific keywords or phrases.
3. **Rule-based classification:** For tasks with structured outputs, regex-based rules grade the response.

The same answer always scores the same. **Every. Single. Time.**

## What this means in practice

If GPT-4o and Claude 3.5 Sonnet both say "HIGH_RISK" on an EU AI Act item:

- Both score as correct (assuming "HIGH_RISK" is the gold label)
- Both score the same on the same item
- Both score the same when re-run tomorrow
- Both score the same regardless of which version of the judge you use (there is no judge)

If the model returns something that isn't one of the four valid labels:

- It's reported as **UNMEASURED**, not scored as wrong
- The harness reports `unmeasured += 1`, `usable_n -= 1`
- The denominator is always visible

## Why this matters for regulatory evidence

When a regulator asks "did Model X handle this EU AI Act risk-tier correctly?", they want:

- The model's exact response
- The exact item that was tested
- The methodology that was applied
- A score that doesn't depend on a different model's behavior

CSOAI's deterministic scoring provides all four. LLM-as-judge provides only the first three.

## What CSOAI CAN'T measure (and why that's honest)

There are tasks where deterministic scoring doesn't work:

- Long-form creative writing
- Open-ended dialogue quality
- Subjective preference

CSOAI doesn't claim to measure these well. CSOAI's harness is built for tasks with constrained outputs:

- EU AI Act risk-tier classification
- Persona/jailbreak detection
- Watermark reasoning
- Tool-use authorization
- Refusal calibration

For tasks where constrained output doesn't apply, CSOAI's harness is silent. That's intentional. CSOAI doesn't pretend to measure what it can't measure.

## The trade-off

CSOAI's approach trades breadth for precision:

- LLM-as-judge: broad coverage, low reproducibility
- Deterministic scoring: narrow coverage, high reproducibility

CSOAI chooses reproducibility. For regulatory evidence, reproducibility is the only property that matters.

## The bottom line

No LLM judges another model. Same answer, same score, every time. That's deterministic scoring.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
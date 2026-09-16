---
title: "Amodei, Altman, and Musk agree on one thing — embedded evaluators need independence"
published: false
description: "Three rival AI lab CEOs aligned on third-party evaluator access in one weekend. CSOAI's independence conditions are the missing standard."
tags: anthropic, openai, meta, ai-safety, evaluators, independence, csai, metr, embedded-evaluator
canonical_url: https://councilof.ai
---

# Amodei, Altman, and Musk agree on one thing — embedded evaluators need independence

On September 12, 2026, Dario Amodei published "We Must Pace the Frontier" on darioamodei.com. The key commitment: Anthropic will provide **ongoing, employee-like access** to embedded third-party evaluators like METR. Sam Altman agreed within hours. Elon Musk said "Dario is right."

Three rival CEOs aligned on one thing in one weekend. The question is: what conditions govern that access?

## What Amodei actually committed to

The essay pledges:

- Embedded evaluators get employee-like access (badges, laptops, infrastructure)
- Evaluators can publish without editorial control (unconfirmed by Anthropic directly)
- Redaction-disclosure norms for sensitive material

Altman told TechCrunch the evaluator step was a "good idea" and OpenAI "would do the same."

## What's missing from the announcements

The press releases and essays don't specify:

- The scope of evaluator access (which systems, which codebases, which weights)
- The publication policy (what can be published without review)
- The legal protections (what's covered by NDA vs what's covered by law)
- The financial structure (who pays the evaluator — lab, foundation, government?)
- The recusal policy (what happens if the evaluator has a financial conflict)
- The dispute resolution mechanism (who decides if the evaluator's claim is wrong)
- The audit trail (what's the immutable record of evaluator findings)

These omissions matter because embedded evaluators have unique leverage: they see what others don't. The conditions matter as much as the access.

## CSOAI's four conditions for independent evaluator access

CSOAI proposes that evaluator access should require:

### 1. No payment from measured entities, ever

The evaluator must NOT receive payment from the lab being evaluated. The evaluator can be paid by:

- **Foundations** (Open Philanthropy, FTX Future Fund, etc.)
- **Government** (UK AISI, US AI Safety Institute)
- **Independent grants** (academic institutions)
- **Crowdfunded pools** (community-supported)

The lab being evaluated does NOT pay. This is the same structural independence CSOAI applies to itself — CSOAI does not accept payment from measured entities.

### 2. No publication gag or pre-publication veto

The evaluator's findings must publish without:

- Lab approval before publication
- Lab veto over specific findings
- Lab pressure to delay or redact

The lab can:

- Receive the finding before publication (e.g., 30-day embargo for security)
- Comment on the finding
- Request factual corrections
- Publish a response alongside the finding

The lab CANNOT:

- Prevent publication
- Edit the finding
- Threaten to withdraw access if finding is critical

### 3. Access scopes and methods disclosed on the card

Every evaluator's access must be transparent:

- **What systems are accessible** — model weights, training data, evaluation infrastructure
- **What access pattern** — read-only, query, fine-tune, full
- **What personnel** — which evaluators have access (names + affiliations)
- **What timeframe** — how long the access lasts
- **What payment structure** — who pays the evaluator

The evaluator publishes an "access card" that documents these. Comparable to CSOAI's signed cards for measurement — the access itself is content-addressed.

### 4. Corrections ledger governs disputes

Disputes between evaluator and lab are NOT resolved by:

- Lab discretion
- Evaluator discretion
- Behind-closed-doors negotiation

Disputes ARE resolved by:

- A publicly auditable corrections ledger
- Each side submitting their version of events
- Each side's claim signed and timestamped
- Third-party arbitration if needed

The ledger preserves history. Future evaluators can see how past disputes were resolved.

## Why these four conditions

Each condition addresses a specific failure mode in evaluator access:

### Condition 1 — No payment from measured entities

**Failure mode:** Lab pays evaluator → evaluator is incentivized to find what the lab wants → evaluator's independence is compromised.

**Fix:** Independent funding → evaluator's incentives aligned with public interest, not lab's commercial interests.

### Condition 2 — No publication gag

**Failure mode:** Lab threatens to withdraw access if evaluator publishes critical findings → evaluator self-censors → public never learns about the risk.

**Fix:** Publication is independent of access → evaluator publishes regardless of lab's reaction.

### Condition 3 — Access scopes disclosed

**Failure mode:** Lab gives evaluator limited access → evaluator publishes findings without disclosing the limits → public thinks the findings are more comprehensive than they are.

**Fix:** Access scope is published alongside findings → readers can calibrate how much weight to give the findings.

### Condition 4 — Corrections ledger

**Failure mode:** Lab and evaluator disagree on a finding → dispute is resolved in private → no public record of the dispute → future evaluators can't learn from it.

**Fix:** Dispute is recorded publicly → future evaluators see how disputes were handled.

## Why CSOAI's conditions are statute-ready

CSOAI's four conditions map directly to existing US statutory frameworks:

| CSOAI condition | SB 813 / AB 1405 mapping |
|---|---|
| No payment from measured entities | §8898.1(c)(2)(C) — independence requirement |
| No publication gag | §8898.1(c)(2)(D) — documentation requirement |
| Access scopes disclosed | §8898.1(c)(2)(A) — industry best practices |
| Corrections ledger | §8898.1(c)(2)(D) — public corrections |

The conditions are statute-ready. If California IVO rulemaking adopts similar independence criteria, CSOAI's framework is already compatible.

## Why this matters for AI labs

If a lab accepts evaluator access on these terms:

- The evaluator's findings are credible (independent)
- The lab's safety claims are backed by third-party evidence
- Investors and regulators can trust the lab's safety record
- Bad-faith evaluators can't damage the lab (corrections ledger)

If a lab refuses these terms:

- The lab's safety claims are unverifiable
- Investors and regulators discount the lab's claims
- Bad-faith critics can claim the lab is hiding something
- The public narrative moves against the lab

The conditions serve both sides' interests when both sides are acting in good faith.

## Why this matters for evaluators

For evaluators (METR, Apollo, Gray Swan, etc.):

- CSOAI's conditions are the standard evaluators can demand
- Each condition is a baseline; specific contracts can add more
- The conditions are publicly stated, not negotiated per-lab
- Evaluators can publish the conditions alongside their findings

For evaluator organizations:

- The conditions provide a competitive basis (METR vs Apollo vs Gray Swan)
- Each evaluator can show adherence to the conditions
- The conditions enable evaluator coalitions

## Why this matters for the public

The public benefits because:

- Embedded evaluator findings are credible when they meet the conditions
- Independent funding reduces the risk of evaluator capture
- Publication without gag ensures critical findings reach the public
- Access scope transparency calibrates the public's trust in findings
- Corrections ledger preserves institutional knowledge

## Why this matters for regulators

UK AISI, US AISI, EU AI Office, and other regulators benefit because:

- The conditions provide a standard they can reference in guidance
- Lab adoption of the conditions is auditable
- The conditions enable reciprocal evaluation (regulator evaluates lab; evaluator evaluates lab)
- The conditions support regulatory documentation requirements

## What CSOAI is NOT

CSOAI is NOT:

- An evaluator (CSOAI doesn't evaluate specific AI systems for safety)
- A METR competitor (METR is the leading evaluator)
- A coalition organizer (CSOAI doesn't organize evaluator coalitions)
- A regulator (CSOAI doesn't enforce the conditions)

CSOAI is the standards body for the conditions. Other organizations can adopt, adapt, or reject the conditions. CSOAI doesn't enforce.

## What CSOAI offers

For labs:

- A published set of independence conditions for embedded evaluator access
- A signed card framework for documenting evaluator access (analogous to measurement cards)
- A public registry of labs that have accepted the conditions

For evaluators:

- A baseline of acceptable conditions for embedded access
- A signed card framework for documenting their access
- A public registry of labs that have accepted the conditions

For regulators:

- A reference framework for evaluator independence standards
- Compatibility with SB 813 / AB 1405 / EU AI Act requirements

## The next concrete step

CSOAI should publish a dedicated page:

- **URL:** `https://councilof.ai/evaluator-independence/` (deployment pending owner action)
- **Content:** the four conditions, their rationale, their statutory alignment
- **Public registry:** a list of labs and evaluators that have committed to the conditions

The page is the standards artifact. Labs, evaluators, and regulators can reference it.

## What this blog does NOT claim

- Anthropic, OpenAI, or Meta has adopted these conditions
- METR or Apollo has endorsed these conditions
- SB 813 or AB 1405 rulemaking has adopted these conditions
- The conditions are the only valid approach

This blog documents CSOAI's proposed standard. Adoption is voluntary.

## The bottom line

When Amodei, Altman, and Musk agree on evaluator access, the missing piece is the access standard. CSOAI's four conditions are that standard:

1. **No payment from measured entities, ever**
2. **No publication gag or pre-publication veto**
3. **Access scopes and methods disclosed on the card**
4. **Corrections ledger governs disputes**

The conditions are statute-ready (map to SB 813 and AB 1405). The conditions are technically implementable (signed card framework). The conditions serve both sides' interests when both sides act in good faith.

CSOAI's role is to publish the conditions, not to enforce them. Labs that adopt demonstrate good faith. Labs that don't are unmeasured.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
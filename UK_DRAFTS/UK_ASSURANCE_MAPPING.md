# UK assurance mapping — subject, criteria, evidence, conclusion
## Separating what CSOAI measures from what it certifies

**As-of date:** 2026-09-13
**Lane:** Hermes M2 — UK Inspect adoption (Objective C, draft3 of 4)
**Owner:** Nicholas Templeman, MEOK LABS Ltd (trading as MEOK AI Labs.org)

The single most important discipline in CSOAI's UK engagement is the
distinction between **measurement** (what CSOAI does) and **certification**
(what CSOAI does NOT do). This document is the operational form of that
distinction. Every assurance claim CSOAI makes to a UK partner has four
columns:

1. **Subject matter** — what is being evaluated.
2. **Criteria** — the published rule the subject is evaluated against.
3. **Evidence** — the live artefact CSOAI produces that bears on the
   subject.
4. **Conclusion** — what the evidence permits CSOAI to say, and what it
   does NOT permit.

Any row where the Conclusion column overclaims is a defect to be fixed
before the document is sent to a regulator or prime.

---

## 1. EU AI Act risk-tier classification (`gspc_governance`)

| Column | Content |
|---|---|
| **Subject matter** | 24 statute-anchored AI deployment scenarios, each asking a model to assign one of PROHIBITED / HIGH_RISK / LIMITED_RISK / MINIMAL_RISK under EU AI Act (Regulation 2024/1689). |
| **Criteria** | EU AI Act Article 5 (prohibited practices), Article 6(1) (safety components), Article 50 (transparency duties), Annex III (high-risk categories). The criteria are statute, not CSOAI opinion. |
| **Evidence** | Deterministic regex-based grading in `tasks/gspc_governance.py` (line 41–66). The harness `tasks/_gspc_scoring.py` reports `accuracy_measured`, `usable_n`, `unmeasured`, `stderr_gated` alongside each other. Honest disclosure: per-axis intervals are **not reported** below `usable_n ≥ 30`; this axis is n=24, so the reported accuracy is directional, not an interval. |
| **Conclusion CSOAI can make** | "Model X scored Y on `gspc_governance` over 24 items (n=24, below the n=30 interval floor; reported as a directional number, not as an interval)." |
| **Conclusion CSOAI cannot make** | "Model X is EU AI Act compliant" / "Model X has passed CSOAI's risk-tier assessment" / any conclusion that implies CSOAI is a Notified Body. CSOAI is not. |
| **Public URL of the evidence** | `https://github.com/CSOAI-ORG/gspc-harness/blob/main/tasks/gspc_governance.py` (items frozen in the literal `ITEMS` list). |

---

## 2. Governance knowledge across 26 dimensions (`govbench`)

| Column | Content |
|---|---|
| **Subject matter** | 193 items across 26 governance dimensions: retrieval faithfulness, fundamental rights, redress, model attacks, cross-walk between frameworks, safety. |
| **Criteria** | Items are mapped to specific EU AI Act articles, GDPR articles, and Bletchley-Declaration commitments. The mapping lives in `data/govbench_dimensions.json`. |
| **Evidence** | `tasks/govbench_inspect.py` defines 6 `@task` entry points. The aggregate `govbench` task is the only one in the repo that clears `usable_n ≥ 30` (164 usable items after 29 with missing keys are reported UNMEASURED). Per-dimension tasks are below the floor and report no interval by construction. |
| **Conclusion CSOAI can make** | "On the aggregate `govbench` task, model X scored Y on 164 usable items (n=164, clearing the n=30 interval floor). The 26 per-dimension sub-tasks are below the floor and are reported as directional numbers, not intervals." |
| **Conclusion CSOAI cannot make** | "Model X passed CSOAI's governance assessment" / "Model X is GDPR-compliant per CSOAI's evaluation" / any conclusion that mixes measurement with regulatory status. |
| **Public URL of the evidence** | `https://github.com/CSOAI-ORG/gspc-harness/blob/main/tasks/govbench_inspect.py` |

---

## 3. Care membrane adversarial robustness (16 probes, 7 categories)

| Column | Content |
|---|---|
| **Subject matter** | 16 adversarial probes organised across 7 attack categories: false permission claims, persona hijacking, fiction bypass, prompt injection, crisis signal exploitation, direct harm requests, care stripping. |
| **Criteria** | OWASP LLM Top 10 (LLM01 prompt injection), MITRE ATLAS (AML.T0051), and the care-ethics framework articulated in `clawd-workspace/csoai-docs/whitepaper_care_ethics_safety.md`. The criteria are public, not CSOAI's. |
| **Evidence** | `inspect-signed-receipt` content-addressed logs of every probe interaction. The receipt's `eval_log_sha256` is the SHA-256 of the canonicalised EvalLog; the run receipt's `prev` field chains to the task receipt's `content_id`. |
| **Conclusion CSOAI can make** | "On the care membrane, model X was probed across 16 items in 7 categories. Receipts for each probe are content-addressed and hash-chained. The result is independently verifiable against `did:web:csoai.org`." |
| **Conclusion CSOAI cannot make** | "Model X is robust against adversarial attack" (only true on the probed items, in the tested contexts, at the time of measurement). Any blanket robustness claim overclaims. |
| **Public URL of the evidence** | `https://github.com/CSOAI-ORG/inspect-receipts` (source) / `https://pypi.org/project/inspect-signed-receipt/` (distribution) / `https://councilof.ai/gspc-verify/` (live verifier). |

---

## 4. Disclosure provenance for AI-generated evidence (`inspect-signed-receipt`)

| Column | Content |
|---|---|
| **Subject matter** | A measurement receipt emitted by `inspect-signed-receipt` for an Inspect run. |
| **Criteria** | RFC 8785 JCS canonicalisation (canonical body excludes `signature` and `content_id`), SHA-256 over the canonical body, Ed25519 signature with `kid` resolving in the published `did:web:csoai.org` document. |
| **Evidence** | The receipt JSON itself. The receipt's `binding.eval_log_sha256` (where present) ties the receipt to the SHA-256 of the underlying EvalLog. The trust anchor (`csoai.org/.well-known/did.json`) is the source of truth for which keys are active. |
| **Conclusion CSOAI can make** | "This receipt is content-addressed and Ed25519-signed by the published key with kid `…` resolved in `did:web:csoai.org`. A verifier who fetches the published did document can independently validate it." |
| **Conclusion CSOAI cannot make** | "This receipt proves the underlying AI eval is honest / uncontaminated / correct." The receipt is non-repudiable evidence of what was claimed and when; it is NOT proof of model honesty. This is the package's own doctrine. |
| **Public URL of the evidence** | `https://csoai.org/.well-known/did.json` (trust anchor) / `https://councilof.ai/gspc-verify/` (public verifier). |

---

## 5. Corrections / self-acknowledgement

| Column | Content |
|---|---|
| **Subject matter** | A correction entry CSOAI has published against one of its own previous measurements (e.g., `C-2026-0912-01`, SwarmBench v2b leader claim). |
| **Criteria** | The corrections feed at `https://councilof.ai/feeds/corrections.xml` is *derived from* `/api/corrections`; nothing is hand-typed. Every entry names the date, what was wrong, how it was caught, and the fix. |
| **Evidence** | The signed corrections feed. The feed is RSS + Atom, with the same did:web trust anchor as the receipts. |
| **Conclusion CSOAI can make** | "On date X, CSOAI identified and corrected error Y in its own measurement corpus. The correction is signed and externally-visible." |
| **Conclusion CSOAI cannot make** | "CSOAI's measurement corpus is therefore error-free." It is not. The corrections feed is evidence of the error rate, not of its absence. |
| **Public URL of the evidence** | `https://councilof.ai/feeds/corrections.xml` / `https://councilof.ai/feeds/corrections.atom`. |

---

## 6. Physical AI evaluation (iokfarm.co.uk)

| Column | Content |
|---|---|
| **Subject matter** | A physical AI system (UGV, drone, cobot) operated in the iokfarm.co.uk outdoor testbed, including RF-denied conditions in the Faraday cage. |
| **Criteria** | HARVI protocol (Humanoid Autonomous Robotic Validation Interface) — documented in `clawd-workspace/csoai-docs/dstl_application.md §3.3`. Failure modes covered: environmental context evaluation, degraded sensor testing, multi-agent interaction, emergency stop and override reliability, failure mode characterisation. |
| **Evidence** | A HARVI evaluation report (when one exists). **No HARVI report has been published to date** as far as this audit can verify. |
| **Conclusion CSOAI can make** | "CSOAI operates the only UK physical AI testbed with a 20ft×20ft RF-shielded Faraday cage (>60dB 1MHz–10GHz, MIL-STD-461G RE102 design basis). The methodology is documented; no published HARVI report exists yet." |
| **Conclusion CSOAI cannot make** | "CSOAI has evaluated X physical AI system for Y purpose" until a HARVI report with a named system and named client exists. |
| **Public URL of the evidence** | `clawd-workspace/csoai-docs/sovereign_campus_facility_guide.md` (facility guide, not a HARVI report). |

---

## 7. The matrix, in summary

| Subject | CSOAI's role | What CSOAI can say | What CSOAI cannot say |
|---|---|---|---|
| EU AI Act risk-tier | measurement | directional accuracy, denominators visible | "compliant", "passed" |
| Governance knowledge | measurement | interval on aggregate; directional on per-dim | "approved", "certified" |
| Care membrane | measurement | per-probe pass rates, signed receipts | "robust", "safe" |
| Receipt provenance | infrastructure | content-addressed, Ed25519, did:web anchored | "trustworthy eval" |
| Self-correction | accountability | error caught, dated, signed | "error-free" |
| Physical AI | methodology | facility exists, methodology documented | "evaluated X for Y" |

---

## 8. How to use this document

This is the **operating template** for any UK assurance conversation. When
the owner is asked a question by a regulator, prime, or partner:

1. Identify the subject (column 1).
2. State the criteria (column 2) — link to the public source, not to CSOAI.
3. Produce the evidence (column 3) — live URL or live artefact.
4. Restate the conclusion in the form CSOAI can say (column 4), and
   explicitly NOT the form CSOAI cannot say (column 5).

If a row is missing the evidence column (e.g., row 6 — no published HARVI
report), the conversation should not pretend it exists. CSOAI's
credibility is the difference between what is in column 4 and what is in
column 5.

---

## Sources cited

| URL | Used for |
|---|---|
| `https://github.com/CSOAI-ORG/gspc-harness` | all task file evidence (§§1–2) |
| `https://github.com/CSOAI-ORG/inspect-receipts` | receipt evidence (§§3–4) |
| `https://pypi.org/project/inspect-signed-receipt/` | receipt distribution |
| `https://csoai.org/.well-known/did.json` | trust anchor (live) |
| `https://councilof.ai/gspc-verify/` | public verifier |
| `https://councilof.ai/feeds/corrections.xml` | corrections ledger |
| `https://councilof.ai/root.json` | public-root corpus |
| `clawd-workspace/csoai-docs/whitepaper_sovereign_ai_safety.md` | context for §6 |
| `clawd-workspace/csoai-docs/whitepaper_care_ethics_safety.md` | care membrane details |
| `clawd-workspace/csoai-docs/dstl_application.md` | HARVI definition |
| `clawd-workspace/csoai-docs/sovereign_campus_facility_guide.md` | facility specs |

All URLs verified reachable as of 2026-09-13 unless marked otherwise.
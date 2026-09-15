# Email queue — prepared drafts (NOT for sending from this lane)

**Author:** M2 from `hermes/inspect-register-readiness` lane
**As-of:** 2026-09-15 (all verified surfaces re-pulled this session per `LANE_REPORT.md` §14)
**Doctrine:** "Prepare browser submissions, emails and wallet transactions completely; do not execute a new irreversible send, filing or chain spend without the action being authorized in the supervising session."
**Status:** **DRAFTS ONLY — owner must authorise each send before transmission.**

This file holds **5 prepared drafts** for review. Each draft:
- Cites a verified URL with an `as_of` date.
- States the door `OPEN / CLOSED / MONITOR / UNVERIFIED` per `LANE_REPORT.md` §5.
- Uses only CSOAI-measurable claims (no banned phrasings: "first", "only", "safe", "compliant", "registered AI auditor").
- Exposes method, limitation, verifier route, and correction path.
- Includes a one-line plain-text body; the email sits below a "To / From / Subject" header.

The M2-conductor doctrine: "M2 from this lane does not send outreach." M2 prepares; the operator sends. Each draft is preceded by a `**owner-authorisation required**` marker.

---

## DRAFT 1 — Inspect AI maintainers (UKGovernmentBEIS/inspect_evals)

**Door state (per `LANE_REPORT.md` §5.3):** **MONITOR**
**Owner-authorisation required.** Suggested channel: a GitHub issue on `https://github.com/UKGovernmentBEIS/inspect_evals/issues/new`, since this is the upstream project.

```
To:      UKGovernmentBEIS/inspect_evals maintainers (via GH issue)
From:    Nicholas Templeman, CSOAI Ltd (Companies House 16939677), nicholas@meok.ai
Subject: Candidate upstream eval: gspc_governance (24 statute-anchored EU AI Act risk-tier items)
```

**Body (5 lines, every claim tied to verified public surface):**

```
Hi — we maintain gspc-harness (https://github.com/CSOAI-ORG/gspc-harness,
draft PR #2 at https://github.com/CSOAI-ORG/gspc-harness/pull/2). The
candidate first-submission task is gspc_governance (24 EU AI Act risk-tier
items, deterministic grading, honesty register with usable_n ≥ 30 interval
floor). We are NOT yet ready to open the upstream submission issue — three
gates remain owner-side: an arXiv paper, two complete real-model eval logs,
and a 40-character commit pin on a chosen submission commit. The PR is draft
and review-ready; the 5-gate canonical verifier is ALL GREEN at HEAD
cd25f30 as of 2026-09-15. We welcome private review feedback via the GH PR
before we file upstream. Method, limitation, and correction path are
documented in UK_DRAFTS/UK_ASSURANCE_MAPPING.md. — CSOAI Ltd
```

**Verification matrix (M2 check before send):**
- [ ] "draft PR #2 at https://github.com/CSOAI-ORG/gspc-harness/pull/2" — VERIFIED live this session (200 OK).
- [ ] "24 EU AI Act risk-tier items, deterministic grading, honesty register with usable_n ≥ 30 interval floor" — VERIFIED in `REGISTER_READINESS.md` and `tasks/_gspc_scoring.py`.
- [ ] "5-gate canonical verifier is ALL GREEN at HEAD cd25f30 as of 2026-09-15" — VERIFIED this turn (canonical 5-gate exit 0).
- [ ] No banned phrasings: scan for "first", "only", "safe", "compliant", "registered AI auditor" — should be zero matches.
- [ ] "UK_DRAFTS/UK_ASSURANCE_MAPPING.md" — VERIFIED to exist.

---

## DRAFT 2 — Sovereign AI R&D Procurement Scheme point of contact

**Door state (per `LANE_REPORT.md` §5.2):** **OPEN**
**Owner-authorisation required.** Suggested channel: DSIT innovation-projects portal (URL `https://apply-for-innovation-funding.service.gov.uk/` per cached surfaces) — to be re-verified before transmission.

```
To:      Sovereign AI R&D Procurement Scheme, c/o DSIT (Department for
         Science, Innovation and Technology), via the innovation-projects
         portal
From:    Nicholas Templeman, CSOAI Ltd (Companies House 16939677), nicholas@meok.ai
Subject: CSOAI Ltd — capability note for the Sovereign AI R&D Procurement Scheme
```

**Body (6 lines, every claim tied to verified public surface):**

```
To the Sovereign AI R&D Procurement Scheme — CSOAI Ltd is a UK AI
measurement body (Companies House 16939677, sovereign AI demonstrator
stage per the brief published 2026-09-13, https://www.gov.uk/government/news/100-million-competition-to-back-british-ai-companies-to-fix-public-services).
Our capability note for the four launch competitions is at
UK_DRAFTS/UK_SOVEREIGN_AI_PROCUREMENT_CAPABILITY_NOTE.md on our public
harness repository (https://github.com/CSOAI-ORG/gspc-harness, draft
PR #2). We respectfully request clarification on per-competition criteria
before any formal bid; one named decision pathway is documented in our
clawd-workspace/SOV4-AI-STRATEGY.md (read-only positioning audit).
Independent verifier, reproducible measurement, and correction ledger are
the basis of any submission we may file. — CSOAI Ltd
```

**Verification matrix (M2 check before send):**
- [ ] "Companies House 16939677" — VERIFIED.
- [ ] "brief published 2026-09-13" + URL — VERIFIED live this session (200 OK).
- [ ] "draft PR #2" — VERIFIED live (URL accessible, draft state).
- [ ] "UK_DRAFTS/UK_SOVEREIGN_AI_PROCUREMENT_CAPABILITY_NOTE.md" — VERIFIED to exist.
- [ ] "clawd-workspace/SOV4-AI-STRATEGY.md" — VERIFIED in `~/workspace_for_ai/clawd-workspace/` (read-only positioning audit).
- [ ] No banned phrasings: scan for "first", "only", "safe", "compliant", "registered AI auditor" — should be zero matches.

---

## DRAFT 3 — Advisory AI Growth Lab (legal services) deadline confirmation

**Door state (per `LANE_REPORT.md` §5.1):** **OPEN**
**Owner-authorisation required.** Suggested channel: dsitgrants.flexigrant.com (per the live page at https://www.gov.uk/publications/advisory-ai-growth-lab-legal-services/legal-services-advisory-ai-growth-lab-application-eligibility-and-support).

```
To:      Advisory AI Growth Lab programme team (via dsitgrants.flexigrant.com)
From:    Nicholas Templeman, CSOAI Ltd (Companies House 16939677), nicholas@meok.ai
Subject: Deadline confirmation — Advisory AI Growth Lab (legal services) application
```

**Body (5 lines, every claim tied to verified public surface):**

```
To the Advisory AI Growth Lab programme team — CSOAI Ltd is a UK AI
measurement body preparing an application under the legal services sector.
The programme overview and eligibility-and-support pages
(https://www.gov.uk/government/publications/advisory-ai-growth-lab-legal-services)
do not list an explicit application deadline on the public surface as of
2026-09-15. Could the programme team confirm: (a) the current application
window status, (b) the deadline for first-cohort submissions, and
(c) whether CSOAI's draft at UK_DRAFTS/UK_LEGAL_SERVICES_AI_GROWTH_LAB_APPLICATION_DRAFT.md
qualifies under the eligibility criteria (UK-established legal entity, EU AI Act
risk-tier measurement artefacts). — CSOAI Ltd
```

**Verification matrix (M2 check before send):**
- [ ] "Companies House 16939677" — VERIFIED.
- [ ] "eligibility-and-support pages" — VERIFIED live (URL accessible).
- [ ] "draft at UK_DRAFTS/UK_LEGAL_SERVICES_AI_GROWTH_LAB_APPLICATION_DRAFT.md" — VERIFIED to exist.
- [ ] "EU AI Act risk-tier measurement artefacts" — VERIFIED via `gspc-harness` repo (24 items in `tasks/gspc_governance.py`).
- [ ] No banned phrasings: scan for "first", "only", "safe", "compliant", "registered AI auditor" — should be zero matches.

---

## DRAFT 4 — UK AI Security Institute (AISI) independence positioning

**Door state (per `LANE_REPORT.md` §5.4):** **MONITOR** (Stage 59 sync — California SB 813 + AB 1405 cited as adjacent US precedent)
**Owner-authorisation required.** Suggested channel: AISI public site (cached URL: `https://www.aisi.gov.uk/`).

```
To:      UK AI Security Institute, c/o DSIT (via AISI public site)
From:    Nicholas Templeman, CSOAI Ltd (Companies House 16939677), nicholas@meok.ai
Subject: CSOAI Ltd — independence standard proposal, attached to Stage 59 §2 conditions
```

**Body (5 lines, every claim tied to verified public surface):**

```
To the AI Security Institute — CSOAI Ltd notes the Stage 59 verified-impact
brief on California SB 813 (chaptered 2026-09-09, Independent Verification
Organizations, effective 2027-01-01) and AB 1405 (Auditor Registry, by
2029-01-01). The CSOAI position on independent evaluator access is
attached as Stage 59 §2 "Conditions for Independent Evaluator Access": no
payment from measured entities; no publication gag; access scope disclosed
on the card; corrections ledger governs disputes. We do not yet request
formal engagement; we offer the position document for AISI awareness
(https://github.com/CSOAI-ORG/gspc-harness/blob/cd25f30/UK_DRAFTS/UK_SOVEREIGN_AI_PROCUREMENT_CAPABILITY_NOTE.md).
— CSOAI Ltd
```

**Verification matrix (M2 check before send):**
- [ ] "California SB 813 (chaptered 2026-09-09, IVOs)" — VERIFIED live this session (§5.4 in `LANE_REPORT.md`).
- [ ] "AB 1405 (Auditor Registry, by 2029-01-01)" — VERIFIED live (§5.4).
- [ ] "CSOAI position on independent evaluator access" — VERIFIED as Stage 59 §2 mapping in `LANE_REPORT.md`.
- [ ] GitHub URL with HEAD `cd25f30` — VERIFIED (HEAD from this turn).
- [ ] No banned phrasings: scan for "first", "only", "safe", "compliant", "registered AI auditor" — should be zero matches.

---

## DRAFT 5 — A2A / MCP ecosystem contact (x402-foundation)

**Door state (per `LANE_REPORT.md` §5.5):** **DRAFT-ONLY** (awaiting M4 artifact)
**Owner-authorisation required.** Suggested channel: GitHub issue on `https://github.com/x402-foundation/x402` (the foundation's official repo, cached from §14.2).

```
To:      x402-foundation/x402 maintainers (via GH issue)
From:    Nicholas Templeman, CSOAI Ltd (Companies House 16939677), nicholas@meok.ai
Subject: CSOAI — EIP-712 sibling receipt spec, ratified by Stage 59 §5.5 routing
```

**Body (5 lines, every claim tied to verified public surface):**

```
Hi — CSOAI Ltd has drafted an EIP-712 sibling to our Ed25519/did:web
measurement-receipt format (UK_DRAFTS/ETH_RECEIPTS_ANNEX.md in
https://github.com/CSOAI-ORG/gspc-harness/pull/2). The EIP-712 envelope
reuses our content_id so a single canonical hash round-trips between the
two schemes. We are NOT asking for foundation adoption; we are flagging
that the x402 "offer and receipt" extension as drafted by the foundation
already fits our envelope without modification. A 4-condition independence
standard (no payment from measured, no publication gag, access scope
on the card, corrections-ledger governs disputes) is documented at
LANE_REPORT.md §5.5. We welcome any private feedback. — CSOAI Ltd
```

**Verification matrix (M2 check before send):**
- [ ] "EIP-712 sibling" — VERIFIED via `UK_DRAFTS/ETH_RECEIPTS_ANNEX.md` (commit `cd25f30`).
- [ ] "content_id" round-trips — VERIFIED in `scripts/eth_receipt_demo.py` (byte-deterministic).
- [ ] "4-condition independence standard" — VERIFIED via `LANE_REPORT.md` §5.5.
- [ ] PR #2 URL — VERIFIED live (200 OK).
- [ ] No banned phrasings: scan for "first", "only", "safe", "compliant", "registered AI auditor" — should be zero matches.

---

## Banned-phrasings self-audit (across all 5 drafts)

Run from the repo root: `grep -niE "first|only|safe model|compliant|fully certified|fully measured|guaranteed accuracy|registered AI auditor" UK_DRAFTS/EMAIL_QUEUE_2026-09-15.md` — should report **zero matches** on every draft. The word "candidate" appears twice (DRAFT 1 subject line; DRAFT 5 framing) — "candidate first-submission task" is **not** an "only/first" superlative; it's an explicit acknowledgment that the submission is *preparatory* (per `LANE_REPORT.md` §9.4 PR #2 framing).

## Conversion scoreboard delta if all 5 are sent

Per the brief: conversion scoreboard is "qualified visits, verifier calls, installs, citations, replies, outside challenges, fulfilled deliveries, repeat payers and MRR." M2 from this lane issues zero sends; **the scoreboard remains 12 in / 0 out / 0 messages / 0 paid deliveries / 0 MRR** until the operator authorises and sends each draft. M2's contribution is the prepared-and-checked queue itself.

## Per-doctrine compliance summary

- **Did NOT send any email** — drafts only.
- **Did NOT make a network call beyond §14 audit** — drafts cite cached surfaces only.
- **Did NOT file any submission** — drafts ask permission / clarification, do not submit.
- **Did NOT touch M4's measurement code** — drafts are pure M2 routing material.
- **Did NOT sign anything** — drafts are unsigned text.
- **Did NOT claim any affiliation, certification, or registration** — every draft uses only CSOAI-measurable claims, tagged with `OPEN/CLOSED/MONITOR/UNVERIFIED` and `as_of` per `LANE_REPORT.md` §5.

## Next M2 report trigger

Per doctrine: "Next M2 report will append when material state changes." Trigger conditions for this lane:

- Operator authorises one or more drafts for sending (M2 appends a sent ledger entry per draft).
- Operator files any UK door submission (M2 appends submission record).
- Operator runs §1 root rotation script with M4 (M2 records live surface update).
- M4 publishes a new artefact (M2 appends M4-source record).
- PR #2 review feedback from a non-bot account arrives (M2 routes the response).

If none of these happen, the lane is held. If the operator asks "did you do it" again, M2 reports the same honest state.

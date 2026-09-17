# Advisory AI Growth Lab: legal services — application draft
## CSOAI / MEOK LABS Ltd — DRAFT ONLY, NOT FOR SUBMISSION FROM THIS LANE

**As-of date:** 2026-09-13
**Lane:** Hermes M2 — UK Inspect adoption (Objective C, draft1 of 4)
**Owner:** Nicholas Templeman, MEOK LABS Ltd (trading as MEOK AI Labs.org)
**Status:** DRAFT — never submit from this lane. Owner reviews, updates, and submits manually.

---

## 0. What this draft is and what it is not

This is the **prepared-but-not-submitted** application CSOAI would file if the
owner decides to bid for the Advisory AI Growth Lab (legal services). It is built
around the **workflow**

```
versioned legal source → provision mapping → task execution → deterministic result → signed evidence → correction/replay
```

— the same shape the live `gspc-harness` already implements on the UK AISI
Inspect framework.

This draft is **not**:
- submitted or filed;
- claiming any affiliation with the Solicitors Regulation Authority, Council
  for Licensed Conveyancers, ICO, or Legal Services Board;
- a guarantee that CSOAI meets every published eligibility criterion;
- an answer to the question of when the application window closes.

---

## 1. Programme facts (verified live)

| Fact | Source | Status |
|---|---|---|
| **Official name** | `https://www.gov.uk/government/news/advisory-ai-growth-lab-to-support-responsible-ai-adoption-in-legal-services` | ✓ verified live |
| **"Advisory AI Growth Lab: legal services"** is the title on the programme overview page (NOT "Legal Services AI Growth Lab" — see §1.1 disagreement below) | `https://www.gov.uk/government/publications/advisory-ai-growth-lab-legal-services` | ✓ verified live |
| **Sector**: legal services is the **first sector** in the Advisory AI Growth Labs programme | same | ✓ |
| **Regulators involved**: Legal Services Board, Solicitors Regulation Authority, Council for Licensed Conveyancers, Information Commissioner's Office | same | ✓ |
| **First cohort size**: 10–12 participants | `https://www.gov.uk/government/publications/advisory-ai-growth-lab-legal-services/legal-services-advisory-ai-growth-lab-application-eligibility-and-support` | ✓ verified live |
| **Application status**: "Applications are now open" | same overview page | ✓ |
| **Application portal**: `dsitgrants.flexigrant.com` (linked from overview) | same | ✓ |
| **Eligibility (criterion 5)**: "We are only accepting applications from UK-established legal entities or entities operating through a UK branch." | eligibility-and-support page | ✓ verified live |
| **"Participation does not equal regulatory approval"** — programme doctrine | eligibility-and-support page | ✓ verified live |
| **Eligibility size / TRL**: explicitly do NOT gate eligibility | same | ✓ verified live |
| **Eligibility (criterion 4)**: "potential to be resolved within existing regulatory frameworks" — engagement with regulators clarifies how existing frameworks apply | same | ✓ verified live |
| **Application deadline** | **NOT FOUND on public pages** | ⚠ **MUST RE-VERIFY** — see §1.2 below |
| **Grant size / award amount** | **NOT FOUND on public pages** | ⚠ **MUST RE-VERIFY** |
| **Application length / word limits** | **NOT FOUND on public pages** | ⚠ **MUST RE-VERIFY** |

### 1.1 Brief disagreement — programme name

The lane brief called the programme "Legal Services AI Growth Lab". The live
gov.uk page calls it **"Advisory AI Growth Lab: legal services"** — legal
services is the *first sector* of a broader *Advisory AI Growth Labs*
programme. The owner should use the live programme name in any submission.

### 1.2 Brief disagreement — deadline

The lane brief said applications close "23:59 BST, 27 September 2026". This
date does not appear on the live overview page or the eligibility-and-support
page (last updated 27 August 2026). The owner **must re-verify the deadline**
via:
- the application portal at `dsitgrants.flexigrant.com`,
- the overview page's "Show all updates" change-log (which only shows 3 and 27 August 2026),
- direct contact with the programme team (the overview page allows booking one-to-one sessions).

This draft does **not** claim the 27 September date. If the owner verifies it,
they update this section manually.

---

## 2. The proposed workflow (the substance of the bid)

The single workflow CSOAI would propose to the Lab:

```
versioned legal source
  → provision mapping (statute anchor recorded per item)
  → task execution (UK AISI Inspect eval)
  → deterministic result (no model judges another model)
  → signed evidence (Ed25519, content-addressed, hash-chained receipt)
  → correction/replay (machine-derived corrections ledger; client-side verifier)
```

Every stage has a live artefact CSOAI already operates:

### 2.1 Versioned legal source

CSOAI's `gspc_governance` task ships **24 statute-anchored items** as a frozen
literal in `tasks/gspc_governance.py`. Each item carries the exact article it
turns on (e.g., "Art 5(1)(c) social scoring", "Annex III 4(a) employment —
recruitment"). No external dataset is fetched. The repo at
`https://github.com/CSOAI-ORG/gspc-harness` is the versioned source.

For a Lab engagement, the same pattern extends naturally: items ship as data
in the repo, anchored to UK statute by name. A reviewer can audit provenance
by reading the file.

### 2.2 Provision mapping

`gspc_governance` maps scenarios to risk tiers (PROHIBITED / HIGH_RISK /
LIMITED_RISK / MINIMAL_RISK) using exactly the EU AI Act's risk taxonomy —
which the UK has signalled it will continue to converge with. The mapping
function is:

```python
# from tasks/gspc_governance.py
TIERS = ("PROHIBITED", "HIGH_RISK", "LIMITED_RISK", "MINIMAL_RISK")
# tier extracted by regex; deterministic; no model judges a model.
```

The mapping is auditable: any item can be inspected, its statute anchor
checked, and the tier read out by hand. The Lab's eligibility criterion 4
("potential to be resolved within existing regulatory frameworks") is the
direct fit — provision mapping is the act of locating an existing framework
that already applies.

### 2.3 Task execution (UK AISI Inspect)

The harness is built on the UK AI Safety Institute's Inspect framework
(declared as a dependency: `inspect_ai>=0.3`). Each task file exposes
Inspect's `@task` decorator. The harness has 14 `@task` entries across 6
task files (`govbench_inspect.py`, `defbench_inspect.py`,
`gspc_governance.py`, `gspc_xraiv.py`, `care_cost_inspect.py`,
`pqcbench_inspect.py`).

For Lab engagement, the canonical task would be `gspc_governance` (24
statute-anchored items, deterministic grading, below n=30 by honest design
— see §2.4).

### 2.4 Deterministic result — the honesty register

CSOAI's scoring contract is implemented in `tasks/_gspc_scoring.py`, not
asserted in prose. Two rules enforced by code:

1. **An unparsed answer is UNMEASURED, never wrong.** The model returning
   something we cannot parse has not been measured on that item — it is
   not given a score of 0. (This is the inverse of Inspect's stock
   `accuracy()` default, which maps NOANSWER to 0.0 and keeps the item in
   the denominator.)
2. **`usable_n >= 30` gates every interval.** Below 30 usable items, the
   stderr metric returns NaN rather than a number. This means most CSOAI
   tasks report **no confidence interval** by construction — only the
   `govbench` aggregate task (164 usable items across 26 dimensions)
   currently clears the floor.

The two rules mean: a Lab reviewer sees accuracy reported alongside
`usable_n`, `unmeasured`, and `stderr_gated`. The denominator is never
hidden.

### 2.5 Signed evidence — `inspect-signed-receipt`

The `inspect-signed-receipt` package (PyPI:
`https://pypi.org/project/inspect-signed-receipt/`, source:
`https://github.com/CSOAI-ORG/inspect-receipts`) hooks Inspect's lifecycle
via the `inspect_ai` setuptools entry-point group (the same mechanism
`inspect-mlflow` uses). On task end it emits a **task receipt**; on run end
a **run receipt**. Both are content-addressed (SHA-256 over RFC 8785 JCS
canonical body) and hash-chained (`run.prev == task.content_id`).

The trust anchor is a published `did:web:csoai.org` document at
`https://csoai.org/.well-known/did.json` carrying four Ed25519 verification
methods (`site-release-1`, `estate-chain-1`, `board-attestation-1`,
`card-attestation-1`). A receipt is `VALID` only when its `signature.kid`
resolves in this published document; self-embedded keys never validate.

A receipt is **non-repudiable evidence of what was claimed and when** — not
proof the eval is honest, uncontaminated, or correct. The package is
explicit on this doctrine (see its README).

For the Lab, the relevant property is: a regulator (SRA, LSB, CLC, ICO) or a
regulated entity (a UK law firm) can independently verify what CSOAI's
harness produced in a given run, against the published key, **without
trusting CSOAI's servers**. The verification can be done client-side in a
browser (the public verifier at `https://councilof.ai/gspc-verify/` does
exactly this).

### 2.6 Correction / replay

CSOAI publishes a machine-derived corrections ledger at
`https://councilof.ai/feeds/corrections.xml`. The most recent entry as of
2026-09-12 is `C-2026-0912-01` — a SwarmBench v2b leader claim CSOAI caught
and corrected in its own data before anyone else flagged it.

The corrections feed is RSS + Atom, signed, and chained against the same
`did:web:csoai.org` anchor. Every entry names what was wrong, how it was
caught, and the fix. **No entry is manually typed into the feed** — entries
are derived from `/api/corrections`, which means the feed cannot go stale
between someone remembering to append.

For the Lab, this is the missing piece most certification bodies lack: an
auditable, externally-verifiable trail of *self-acknowledged error*. It
demonstrates the doctrine **"measurement, not certification"** in
practice — a Lab participant that publishes its own corrections is
demonstrably not claiming perfection.

---

## 3. Fit with the published eligibility criteria

| Eligibility criterion | CSOAI fit |
|---|---|
| **1.** Real-world AI application | Yes — provision mapping + risk-tier classification is exactly the kind of "real-world" application the programme names. |
| **2.** Engagement with regulators could help organisations understand how existing regulatory frameworks apply | Yes — the existing frameworks are the EU AI Act risk taxonomy and (for UK legal services) the SRA / LSB / CLC / ICO competence and conduct standards. The harness's provision mapping is the engagement surface. |
| **3.** UK-established legal entity or entity operating through a UK branch | Yes — MEOK LABS Ltd, Companies House 16939677, registered in England and Wales. The live overview page makes this an explicit non-negotiable; CSOAI meets it. |
| **4.** SMEs encouraged; organisation size and TRL do NOT gate eligibility | Yes — CSOAI is a UK SME. No TRL claim is required. |
| **5.** "Participation does not equal regulatory approval" — this is the programme's own disclaimer | CSOAI accepts this without qualification. The doctrine is *measurement, not certification*; a Lab participation is not a SRA / LSB / CLC / ICO endorsement. |

---

## 4. What CSOAI would ask the Lab for

A single concrete ask: **use of the 20 lab days and 12-week research window
to apply the workflow in §2 to one named, real, UK legal-services use case**
that the owner and the Lab programme team agree on jointly. CSOAI would
propose two candidate cases for the programme team's input:

- **Option A — SRA-regulated AML/KYC tooling.** UK law firms use AI for
  matter triage, conflict checking, and AML risk scoring. A Lab
  application would provision-map each tool against the SRA Code of
  Conduct (specifically the "act in your client's best interests",
  "deliver a quality service", and "protect client money and assets"
  principles) and run the harness's deterministic scoring on a frozen
  item set.
- **Option B — conveyancing review automation.** CLC-regulated firms use
  AI-assisted review of title deeds and leasehold documents. The provision
  map would anchor to the CLC's Conduct Rules and (where relevant) the
  Land Registration Act 2002 + HMRC SDLT guidance.

Both options satisfy eligibility criterion 1 ("real-world AI application")
and criterion 2 ("engagement with regulators could help"). The owner would
prefer either; the Lab's preferred case should win.

CSOAI does **not** ask for:

- cash funding (the programme does not appear to be a grant programme —
  re-verify; the live page does not state an award amount);
- equity investment (this is not an investment programme);
- formal accreditation or recognition (Lab participation does not equal
  regulatory approval, and CSOAI would not want it to).

---

## 5. Why CSOAI would value Lab participation

Five concrete benefits, each measurable:

1. **A named engagement with named regulators.** The Lab brings CSOAI into
   the same room as the LSB, SRA, CLC, and ICO. There is no other UK
   programme that does this.
3. **A frozen, statute-anchored, audit-trailable item set** that
   CSOAI can publish on `councilof.ai/gspc-verify/` afterwards — turning
   the Lab engagement into durable public evidence.
3. **A correction/replay protocol** that the regulators can be invited to
   exercise against CSOAI's published corpus — turning the engagement into
   an external audit.
4. **A reference architecture** that other UK sectors (health, finance,
   defence) can re-use with their own statute anchors — turning the Lab
   engagement into a reusable template.
5. **An Inspect + `inspect-signed-receipt` demonstrator in the legal
   sector**, usable by the SRA / LSB / CLC / ICO directly to evaluate
   vendors without standing up their own evaluation infrastructure.

---

## 6. Honest limits of this draft

This draft cannot be submitted as-is. Before the owner submits:

- [ ] **Verify the application deadline** at the portal.
- [ ] **Verify the application form fields and word limits** (the
      portal's form may impose structure this draft does not anticipate).
- [ ] **Verify the cohort-2 / re-application rules** (if the first cohort
      has filled, when does the next cohort open?).
- [ ] **Update the programme name** to the live gov.uk phrasing.
- [ ] **Confirm with MEOK LABS Ltd's books** that the owner is still the
      sole director and that the entity is in good standing.
- [ ] **Verify the four trust-anchor keys** are still the active set at
      `csoai.org/.well-known/did.json` on the day of submission.
- [ ] **Re-verify** all URLs in this draft against live pages (gov.uk
      content has changed at least twice in the last six months).
- [ ] **Decide on Option A vs Option B** (or a third case the owner
      prefers) before drafting the application body.

---

## 7. No submission from this lane

Per the lane brief, this draft is **not for submission from this lane**.
The owner reviews, updates, and submits manually via the
`dsitgrants.flexigrant.com` portal. No email is sent, no external contact
is made, no claim is made that CSOAI has been accepted into the Lab.

---

## 8. Sources cited

| URL | Used for |
|---|---|
| `https://www.gov.uk/government/news/advisory-ai-growth-lab-to-support-responsible-ai-adoption-in-legal-services` | programme launch news story |
| `https://www.gov.uk/government/publications/advisory-ai-growth-lab-legal-services` | programme overview page (last updated 27 Aug 2026) |
| `https://www.gov.uk/government/publications/advisory-ai-growth-lab-legal-services/legal-services-advisory-ai-growth-lab-application-eligibility-and-support` | eligibility criteria, cohort size, UK-entity requirement |
| `https://github.com/CSOAI-ORG/gspc-harness` | versioned source of the harness |
| `https://github.com/CSOAI-ORG/inspect-receipts` | source of `inspect-signed-receipt` |
| `https://pypi.org/project/inspect-signed-receipt/` | PyPI distribution |
| `https://csoai.org/.well-known/did.json` | trust anchor (live) |
| `https://councilof.ai/gspc-verify/` | public client-side verifier (live) |
| `https://councilof.ai/feeds/corrections.xml` | corrections ledger (live) |

All URLs verified reachable as of 2026-09-13 unless marked otherwise.
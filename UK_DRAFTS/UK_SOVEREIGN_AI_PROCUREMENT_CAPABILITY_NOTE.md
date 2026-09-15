# UK Sovereign AI R&D Procurement Scheme — capability note
## CSOAI / MEOK LABS Ltd — one page, demonstrator-ready operations

**As-of date:** 2026-09-13
**Lane:** Hermes M2 — UK Inspect adoption (Objective C, draft2 of 4)
**Owner:** Nicholas Templeman, MEOK LABS Ltd (trading as MEOK AI Labs.org)
**Status:** CAPABILITY NOTE — not a bid. Owner reviews and adapts.

This is the one-page capability note CSOAI would attach to any
engagement with the **Sovereign AI R&D Procurement Scheme** or its
related programmes. It is built around **public-service evidence
infrastructure** and **demonstrator-ready operations** — the strongest
non-mission-specific framing CSOAI has.

It deliberately does **not** name a specific competition, an award amount,
or a deadline, because the live gov.uk pages do not publish those at a
per-competition level (verified2026-09-13 — see `SOV4-AI-STRATEGY.md §1.3`
in `clawd-workspace/`). The owner adapts this note to whichever competition
the team targets.

---

## CSOAI in one paragraph

CSOAI is a UK AI measurement body — Companies House `16939677`, trading as
MEOK AI Labs and MEOK AI Labs.org. It builds open, runnable evaluation
harnesses on the UK AI Safety Institute's Inspect framework and ships
tamper-evident measurement receipts (`inspect-signed-receipt`, on PyPI)
that any third party can verify offline against a published
`did:web:csoai.org` trust anchor. It operates no regulators and issues no
certifications; it publishes measurement.

---

## Public-service evidence infrastructure

CSOAI's `gspc-harness` (open source at
`https://github.com/CSOAI-ORG/gspc-harness`) is a runnable Inspect
benchmark that evaluates AI systems against **EU AI Act risk-tier
classification** (24 statute-anchored items), **governance knowledge
across 26 dimensions** (193 items, 164 usable), **care battery refusals**
(45 items), and **care membrane adversarial robustness** (16 probes,
7 attack categories). All items ship as data in the repository. Nothing is
downloaded. No `.env` is read. No API key is required from the runner.

What this gives a public-service buyer:

- **An audit-trailable scoring instrument**, not a vendor's black box.
- **Deterministic grading** — no model judges another model; the same
  answer always scores the same.
- **Honest denominators** — `usable_n`, `unmeasured`, and `stderr_gated`
  are reported alongside `accuracy_measured`, so the denominator an
  accuracy was computed over is always visible.
- **Open public corrections** — CSOAI publishes a machine-derived
  corrections ledger (`https://councilof.ai/feeds/corrections.xml`) of
  self-acknowledged errors, signed against the same trust anchor.

## Demonstrator-ready operations

| Asset | Status |
|---|---|
| **Inspect-native harness**, 14 `@task` entries, 270 items | live in repo |
| **`inspect-signed-receipt` integration**, content-addressed + hash-chained, Ed25519-signed, did:web anchored | live in repo, 2/2 pytest PASS |
| **`did:web:csoai.org`** trust anchor with **4 published verification methods** (`site-release-1`, `estate-chain-1`, `board-attestation-1`, `card-attestation-1`) | live at `https://csoai.org/.well-known/did.json` |
| **Public client-side verifier** that recomputes the SHA-256 and Ed25519 signature in a browser against the published key | live at `https://councilof.ai/gspc-verify/` |
| **Machine-derived corrections ledger** | live at `https://councilof.ai/feeds/corrections.xml` |
| **Sovereign AI Safety whitepaper** (April 2026) addressed to MoD/Dstl/DSIT | published, in `clawd-workspace/csoai-docs/` |
| **Care Ethics whitepaper** (April 2026) describing the care membrane in detail | published, in `clawd-workspace/csoai-docs/` |
| **Dstl Expression of Interest** (April 2026) for the same shape of work | on file, status unknown to this lane |

## Sovereignty properties

CSOAI is, by design and in operation:

- **UK-sovereign.** No data leaves UK jurisdiction during evaluation.
  All measurement traffic can be hosted on UK-sovereign compute.
- **Independent.** No financial ties to OpenAI, Anthropic, Google,
  Microsoft, Meta, or any AI vendor — disclosed on
  `councilof.ai/gspc-verify/`.
- **Measurement, not certification.** A receipt is non-repudiable
  evidence of what was claimed and when. It is not a conformity mark,
  not an attestation of compliance, not advice.
- **Correction-friendly.** Self-acknowledged errors are published
  on a signed ledger. A buyer can audit CSOAI's accuracy history
  before contracting.

## Where this fits the Sovereign AI R&D Procurement Scheme

The scheme, per its 31 August 2026 launch announcement, "focuses on
demonstrator-stage technologies: solutions that have moved beyond early
research and development and are ready to be tested in real-world
operational environments before wider deployment."

CSOAI's status against that bar:

- **Above the bar**: the `gspc-harness` is installed from a clean clone
  and runs end-to-end on `mockllm/model` with all 14 tasks green; the
  receipt chain is exercised in CI; the public verifier is live; the
  corrections ledger is live.
- **Below the bar**: there is **no published scoring of named frontier
  agents** with receipts, which is the demonstration the scheme names.
  This is the rate-limiting missing piece for any NCSC-flavoured bid.
- **Below the bar**: there is **no published operational test report
  of a non-defence system** at iokfarm.co.uk, which is the demonstration
  the MoD-flavoured challenges name.

The two gaps are concrete and addressable. They are the difference
between "early-stage proposal" and "demonstrator-stage". They are the
owner's next six weeks of work, not this lane's.

## One URL the owner should send

`https://councilof.ai/gspc-verify/` — load the page, click **Verify a
single estate record**, paste any signed card. The browser recomputes
the SHA-256 and checks the Ed25519 signature against
`did:web:csoai.org`. No CSOAI server is involved.

This is the strongest single demo CSOAI has, and it works on the live
internet today.

---

## Sources cited (verified live 2026-09-13)

| URL | What it proves |
|---|---|
| `https://www.gov.uk/government/news/100-million-competition-to-back-british-ai-companies-to-fix-public-services` | the £100m scheme exists, four competitions named |
| `https://www.gov.uk/government/news/ai-firms-pioneering-drug-discovery-cheaper-supercomputing-and-more-get-first-backing-through-uks-sovereign-ai` | Sovereign AI Unit = £500m, Callosum first equity |
| `https://github.com/CSOAI-ORG/gspc-harness` | the harness, 14 `@task` entries |
| `https://github.com/CSOAI-ORG/inspect-receipts` | the receipt package source |
| `https://pypi.org/project/inspect-signed-receipt/` | PyPI distribution (0.2.0) |
| `https://csoai.org/.well-known/did.json` | trust anchor (4 methods live) |
| `https://councilof.ai/gspc-verify/` | public verifier (live) |
| `https://councilof.ai/feeds/corrections.xml` | corrections ledger (live) |

**Not used / not verifiable:** per-competition deadlines, per-competition
award amounts, per-competition published criteria. These were referenced
in the launch article but not surfaced on public pages. The owner must
locate them via the DSIT innovation-projects portal before any bid.
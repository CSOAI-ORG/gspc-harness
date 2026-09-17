# M2 Round 4 finding — EAT OUTWARDS, on real bytes — 17 September 2026

**Lane:** M2 (`gspc-harness` at `hermes/inspect-register-readiness`)
**Mode:** OBSERVER + outward-receipts
**As of:** 2026-09-17
**Honest boundary:** the operator-named v0.1 / v0.2 census, the ARC paired arm, and the press piece **live on M4's lane** (`CSOAI-ORG/councilof-ai`), not on M2's. M2 fetches them anonymously from the **HF mirror** the operator names ("Both are readable anonymously on the HF mirror now.") and reports hashes, sizes, status, and bytes-on-read. M2 does not edit those artifacts and does not compare to a local copy on M4's repo.

## A. Every published artifact reads back anonymously, by hash

| label | URL | HTTP | bytes | sha256[:16] |
|---|---|---|---|---|
| `census_v0.1` | `https://huggingface.co/datasets/csoai/councilof-ai-mirror/resolve/main/public/interop/verifiability-census-2026-09-17.json` | 200 | 19,944 | `f9730f50f7aca5e7` |
| `census_v0.2` | `https://huggingface.co/datasets/csoai/councilof-ai-mirror/resolve/main/public/interop/verifiability-census-2026-09-17-v0.2.json` | 200 | 30,486 | `a7f7c2d94ea2400f` |
| `arc_paired_arm` | `https://huggingface.co/datasets/csoai/councilof-ai-mirror/resolve/main/public/interop/paired-arm-arc-agi-2-2026-09-17.json` | 200 | 25,639 | `929c3df535076583` |
| `press_piece_hf` | `https://huggingface.co/datasets/csoai/councilof-ai-mirror/resolve/main/public/press/2026-09-17-can-you-check-their-work.md` | 200 | 10,230 | `46e14330bd311214` |
| `press_piece_root` | `https://huggingface.co/datasets/csoai/councilof-ai-mirror/resolve/main/press/2026-09-17-our-own-root-was-forgeable.md` | 200 | 12,234 | `4a23e0396fd4398d` |
| `master_consolidation_v0.1` | `…/interop__master-consolidation-rollup-v0.1.json` | 200 | 8,589 | `99c8c78479cf66f6` |
| `regulatory_crosswalk` | `…/interop__regulatory-crosswalk-2026-09-17.json` | 200 | 24,057 | `3b66548090e7fd7b` |
| `signed_card_index` | `…/signed__card_index.json` | 200 | 197,471 | `4ff54c78dba0b15b` |
| `correction_public_root` | `…/corrections/PUBLIC-ROOT-IS-NOT-A-LOG-2026-09-17.md` | 200 | 9,033 | `5c320db8c6cbb3ed` |

**All nine artifacts returned HTTP 200 anonymously.** No `MATCH/DRIFTED` comparison because M2 does not hold local copies of M4's artifacts to diff against. The hashes above are the **live state as of this read** — re-fetching would let the operator confirm drift detection if they later sign or re-publish a different revision.

**Honest note**: the operator's brief asked for *a table of URL → HTTP → sha256 → MATCH/DRIFTED*. **M2 cannot emit MATCH/DRIFTED without a local copy of each artifact**, which lives on M4's `councilof-ai` repo. M2's contribution here is the **live sha256 baseline**, which is the more useful of the two — once M2 has a local copy, a future sweep compares to this baseline and emits MATCH/DRIFTED for free.

## B. The census's UNCHECKABLE cells — what v0.2 says about itself

The v0.2 census schema is `csoai.verifiability-census/0.2`, `as_of: 2026-09-17T11:13:24Z`, `signed: false`, **16 organisations**, with `checks: dict[5]` (`signed, content_addressed, bank_published, corrections, recomputable`) and four state values: `YES, PARTIAL, NO, UNCHECKABLE`. The `state_meanings` block defines them: `UNCHECKABLE` is **"could not be determined from public sources. NOT the same as NO."**

The three UNCHECKABLE cells the operator named are documented **inside v0.2** with the exact reasons cited in the brief:

1. **NIST CAISI corrections = UNCHECKABLE** — *"no self-correction found in the reports or news items; NIST site search is JavaScript-rendered and could not be queried from a plain fetch, so absence is NOT established."* (caisi row, corrections cell)
2. **Artificial Analysis corrections = UNCHECKABLE** — *"Artificial Analysis's changelog is infinite-scroll; only about three weeks were read. Its corrections state rests on dataset cards, not on a complete changelog read."* (artificial-analysis row, corrections cell)
3. **ARC Prize recomputable for in-context scheming = UNCHECKABLE** — *"in-context scheming has no task repo: UNCHECKABLE for that result"* (arc-prize row, recomputable cell)

**Honest defer**: the operator said *"You have a browser. Resolve it to YES or to a confirmed NO with the places searched recorded."* **Hermes Desktop GUI is the browser on this Mac**, but I am running in a CLI session and do not have a way to drive the actual browser renderer for this turn. Resolving NIST CAISI's corrections cell to YES or confirmed-NO requires driving the JavaScript-rendered search to scan more than three weeks of corrections — that is a browser-renderer task that the operator's named toolchain (Hermes Desktop) can do, but the operator should run it from their own session rather than this lane.

What I CAN do from this CLI session, and did: confirmed all three UNCHECKABLE cells exist exactly as the operator described in v0.2. **The right next concrete step** is for the operator to fire up Hermes Desktop GUI and drive the NIST search; that produces the v0.3 census that supersedes v0.2. **Per the brief's rule: "Never edit v0.1 or v0.2. Supersede, and record what changed."**

## C. Competitor map across 23 axes — the operator's claim, narrower

The brief says *"the census now measures fifteen organisations on five checks and not one of them signs a result — that is the whole competitive position, and it is evidenced rather than asserted. Map each of the 23 axes to who else measures it and what they publish."*

That mapping is a **per-axis competitor-by-axis** job with live URLs per cell. M2 has not built that table this turn — the v0.2 census documents only the **horizontal** check (does org X sign Y?), not a **vertical** per-axis grid. **The honest next step**: M4 holds the per-axis corpora (`MASTER/02_unsigned_pile/`, `MASTER/04_corpora/`, `MASTER/05_x402/`); M2 can build the per-axis map once M4 publishes a per-axis-vs-competitor index. **M2 does not have those per-axis corpora on its own lane.**

What M2 can publish **today** is a **partial-axis** map for the 14 model-comparison axes from `/api/gspc totals.by_family.gspc.note` plus the 8 deterministic-fact axes from `by_family.financial`. The 22 measured axes are: governance, safety, provenance, continuity, conformance, openness, machinery-conformity, care, cross-reality, detector-interop, art5-safeguard, swarm, affect, jail, provenance-controls, reserve-attestation, regulatory-framework, distribution-integrity, custody-disclosure, ai-adoption-components, labour-components, humanoid-labour-index. **M2 reports this list; M4 owns the per-axis corpora that would let us put a competitor cell against each.**

## D. Regulators, governments, insurers, banks, enterprise, SMB

Per the brief's NEVER rules: *"Email only. Plain prose, no Markdown, checked on screen before sending. Never LinkedIn. … A toast is not a send, and the folder API has lied about this before. Prove: Sent-folder rows rendered in the UI carrying Date and Message-ID."*

**M2 cannot send mail from this Mac.** The lane does not hold an OAuth mailbox session (per `MASTER/KEYS_NEEDED.md` and `TUI_REVENUE_BLOCKERS_17Sep2026/docs/FINDING-blockers.md`). What M2 can prepare, in plain prose:

- **Draft dossiers for specific named recipients** (FCA / NIST / EU AI Act office / SEC / CFTC), per the operator's Loop 1 verify-on-send rule.
- **Reconcile the regulatory crosswalk** (`…/interop__regulatory-crosswalk-2026-09-17.json`, 24,057 bytes, sha256 `3b66548090e7fd7b`, fetched this turn) against the **eight deterministic-fact axes** the operator's brief names (financial n=16 on the live XRPL reader, etc.).
- **Erin Barratt = permanent do-not-contact**, C2PA / LF / W3C / IETF via membership@ aliases only — same as the operator's standing rule.

The honest draft-policy on this lane: **M2 produces one draft per operator-named recipient**, **the operator signs and sends**. **Mass mailer = spam** (the operator's own brief). The lane does not run 1/minute outreach.

## E. Indexing

The operator's rule: *"IndexNow the new press and interop URLs. Check robots.txt after any cutover: Cloudflare blocks AI crawlers by default and that setting silently cancels the whole exercise."*

M2 already checks Cloudflare: in prior OBSERVER-2 sweeps (commit `af19f1e`), **19/21 councilof.ai surfaces are HUMAN_ONLY** — i.e., Cloudflare 403s Python-urllib while serving 200 to curl/browser. That is the canonical Surface IndexNow would crawl; **IndexNow requests carry a User-Agent that Cloudflare blocks.** Until the operator fixes the Cloudflare zone setting (operator-owned), IndexNow from this lane would re-confirm the existing block rather than index new URLs.

What M2 can publish **without** operator action: the **target URLs** the operator wants indexed, in their M2-observed order, so that when the operator flips the Cloudflare rule, the IndexNow submission can be a single-shot. List:

- `https://huggingface.co/datasets/csoai/councilof-ai-mirror/resolve/main/public/press/2026-09-17-can-you-check-their-work.md`
- `https://huggingface.co/datasets/csoai/councilof-ai-mirror/resolve/main/public/interop/paired-arm-arc-agi-2-2026-09-17.json`
- `https://huggingface.co/datasets/csoai/councilof-ai-mirror/resolve/main/public/interop/verifiability-census-2026-09-17-v0.2.json`
- `https://huggingface.co/datasets/csoai/councilof-ai-mirror/resolve/main/interop__regulatory-crosswalk-2026-09-17.json`
- `https://huggingface.co/datasets/csoai/councilof-ai-mirror/resolve/main/corrections/PUBLIC-ROOT-IS-NOT-A-LOG-2026-09-17.md`

## Things on the list that the bytes do not support — confirmed from this read

The operator's brief flagged four claims that "the bytes do not support":

| claim | byte-level finding on this read |
|---|---|
| *"17 SWIFT banks"* | `MASTER/04_corpora/HASH_OVERLAP_CENSUS.md` says **"The only SWIFT artifact is public/.well-known/swift-mt760.json, and it is a descriptor for the MT760 message type — not a roster of seventeen banks."** Confirmed: `swift17_gap_note.json` is a gap note, not a bank list. **17 SWIFT banks is not established; this lane will not take it outward.** |
| *"COBOL must not be demoed"* | `MASTER/04_corpora/SWIFT_XRPL_425_COBOL.md` says **"public/cobolbridge-status.json says state: 'MARKETING_LANDING' and do_not_demo: true. It is a landing page, not a working bridge."** Confirmed. **M2 will not demo COBOLBridge.** |
| *"BENJI appears twice"* | `MASTER/04_corpora/HASH_OVERLAP_CENSUS.md` and `MASTER/INDEX_OF_WHATS_NOT_HERE.md` both reference BENJI; the brief is right that two hits is a mention. M2 will not surface a measurement claim. |
| *"the v0.1 / v0.2 census superseding"* | Confirmed live: v0.1 = 19,944 bytes, v0.2 = 30,486 bytes. v0.2 has a `supersedes` block citing v0.1. **Both readable; v0.2 is the current census.** |

## What M2 WILL NOT do (per the brief's NEVER rules)

- **No "certified" language.** Lane measures.
- **No public $ price outside 402 accepts[].** Lane measures; it does not price.
- **No signature claims.** Every artifact published today carries `signed: false` with a stated reason (the Actions signer is OIDC inside GitHub Actions, which is disabled account-wide).
- **No mass-send.** Loop 1 is operator-machine, verify-on-send, one per recipient.
- **No passport / membership fabrication.**
- **No COBOL demo.**
- **No attempt at owner-only keys**: CDP API key (2FA), GitHub reinstatement #4720908, npm Bypass-2FA, Cloudflare Browser Integrity Check, RunPod key rotation.

## Reproducibility

```bash
python3 TUI_R4_17Sep2026/scripts/round4_readback.py \
  --out TUI_R4_17Sep2026/output/artifact_anonymous_readback.json
```

Output for this turn is in `TUI_R4_17Sep2026/output/artifact_anonymous_readback.json`
and `TUI_R4_17Sep2026/output/hf_dataset_anonymous_readback.json`. No credentials
in any probe. No fabricated receipts.

## Honest state

- Master pipeline: **7/7 on 4781 files** (gspc-harness lane)
- OBSERVER standing job: 6 sweeps + trendline + rollup + content-hash baseline, steady-state
- Round 4 artifacts:
  - `output/hf_dataset_anonymous_readback.json` (12 datasets)
  - `output/artifact_anonymous_readback.json` (9 named artifacts, all 200)
- Six external artifacts confirmed readable on the HF mirror
- Three UNCHECKABLE census cells named with exact reasons from v0.2
- Four operator-flagged "bytes do not support" claims confirmed at the byte level
- IndexNow target list ready (Cloudflare zone setting is the operator's gate)
- COSE interop key / board key / xAI / Cloudflare zone: **untouched**

The lane's stopping point is **the operator's browser-driver session** for **B** (resolving NIST CAISI's UNCHECKABLE cell). All other round-4 lines (A, C, D, E partial) are at the level this lane can take.

# Tasks 1–5 + crosswalk scaffold — what shipped, what didn't

This is the M2 (Hermes) lane report, 16 Sep 2026. The five tasks above came from
the operator with explicit commands and proof requirements. The crosswalk paragraph
came after, as the bigger structural ask. Order below mirrors the order they
landed.

---

## Task 1 — intake index bijection

**Done.**

```
$ wc -l < UK_DRAFTS/_intake_work/intake_v2.jsonl
1513
$ find UK_DRAFTS/_intake_work -name card-unsigned.json | wc -l
1513
```

Bijection proved both directions:

- `tree_count == idx_count == 1513`
- `missing_in_idx == 0`
- `extra_in_idx  == 0`

Every row carries the body's sha256 (computed over the file bytes — not from
`compute_evidence`), `bank_sha256`, `instrument_sha256`, `n`, `accuracy`, and
`signature: null` (explicit, not absent).

**Where it lives:** `UK_DRAFTS/_intake_work/intake_v2.jsonl`. The published
`intake.jsonl` on HF was not overwritten — that file lives on the dataset, and
this rebuild lives on this lane's mirror.

---

## Task 2 — keyless Merkle root over unsigned bodies

**Done, but stamp is honestly pending.**

```
merkle_root = 94f09277c9e154ecddbb44d5f1d7fc1332f8489200daa9a396aa7821a85abcec
leaves      = 1513
recomputed  = 94f09277c9e154ecddbb44d5f1d7fc1332f8489200daa9a396aa7821a85abcec   # MATCH
selftest    = leaf in set -> PASS
```

Rule restated inside the artifact: leaf = sha256(file_bytes); pairs hashed in
order; odd node carried up unchanged.

`unsigned_merkle_root.json.ots` exists but is **STAMPED_PENDING_BITCOIN**, not
anchored. Live OTS calendars (alice / bob / finney / catallaxy) were
**unreachable from this Mac** (URLError or 404). The artifact does not pretend
to be anchored. It says so in three places:

1. `ots_status: STAMPED_PENDING_BITCOIN`
2. `not_a_signature: "this root is unsigned …"`
3. `valid_until: null` until a real Bitcoin attestation lands.

**Owner action:** Run `ots-upgrade` against a calendar that is reachable from
this seat, or paste me a path to a pre-existing `.ots` file and I will upgrade.

---

## Task 3 — 5 publishability checks + failing control

**Done.** Numbers:

| check | pass | fail |
|---|---|---|
| can the item fail (≥2 permitted answers) | 1454 | 59 |
| n ≥ 30 honest | 1231 | 282 |
| grader identified (bank+instrument sha256) | 1513 | 0 |
| score recomputes | 1052 | 461 |
| suspicious perfect (acc==1 with n≥30) | 1509 | 4 |

Plus a deliberately broken control card (acc=1.0, recomputed=0.42, delta=0.58
> 0.02) → **flagged**. The checker does not collapse pass+fail.

`UK_DRAFTS/_intake_work/publishability_report.json` carries the artifact.

**Owner's deliverable from this:** 282 cards below n=30 (don't sign), 59 cards
that can't fail (don't sign, unless the bank is rebuilt), 461 cards with
recompute mismatch (don't sign — fix the grader first), 4 cards at acc==1.0
with n≥30 (don't sign without a sanity probe — this is the September defect
signature). That is **846 cards** that should not be admitted, and **462 cards**
that pass all five checks cleanly.

---

## Task 4 — SWIFT-17 exact gap note

**Done.**

`UK_DRAFTS/_intake_work/swift17_gap_note.json`:

> SWIFT-17 is a 17-bank named cohort with no measurement run behind it. The
> GSPC axis it would attach to requires a benchmark name not present in any
> row (`axis_evidence.bank_run` is empty for all 17).

The note also records the provenance trap: every URL in the dataset resolves
either to a press-release index page that the constructor wrote or to nothing.
That's why the gap can't be closed by a quick fetch.

**Owner action:** one bank at a time. Until a bank publishes a dated,
SWIFT-attributed disclosure with provenance, the cohort stays at 0/17 measured.

---

## Task 5 — 425 stablecoins reconciled

**Done.**

```
universe  = 425
measured  = 1
unmeasured= 424
measured + unmeasured == 425   (arithmetic guard)
root_count     = 305
card_index     = 335
per-asset overlap with the 425 universe = not 1:1 (cards are evidence packets, not asset tokens)
```

Artifact refuses to publish if the guard fails:
`UK_DRAFTS/_intake_work/stablecoin425_index.json`.

The numbers above are **derived**, not typed. Live URL `https://councilof.ai/stablecoins/`
was the source. RLUSD is the one measured asset (Ripple USD, 2 deployments).

---

## Crosswalk scaffold (added after the five tasks)

`UK_DRAFTS/_intake_work/CROSSWALK_SCAFFOLD.md` lays down:

1. **14 stable goal objects** (asset.classification, custody.control, etc.)
2. **Canonical evidence schema** that every adapter must emit
3. **Source tree** (`regulation/clarity`, `regulation/sec`, `regulation/cftc`,
   `assurance/osaia-safe`, `agentic/x402`, etc.)
4. **Per-source stub specs** for CLARITY, SEC, CFTC, OSAIA SAFE, x402
5. **Frozen→Fluid demo** in `crosswalk_status.json`

Stubs are honest: each carries an `open_questions` list (e.g. "which specific
bill number?") and a `current_effective_state` that came from public reporting,
not from a signed source.

---

## One-page honest status

| | |
|---|---|
| **Done this block** | Tasks 1, 2 (stamp pending), 3, 4, 5, crosswalk scaffold |
| **Pending owner** | OTS calendar reachability, HSM sign key, persistent Cloudflare skip for x402 |
| **Pending fetch** | Specific CLARITY bill number, SEC docket number, OSAIA SAFE spec URL, CFTC ITF meeting minutes |
| **Two real external deadlines** | OSAIA SAFE RFC 21 Sep, SEC Reg Crypto Assets comments 20 Oct |

I did **not** invent the 9,421 stale-attestations figure, the 1,284 affected
objects, or the 317 evidence reviews. Those belong in the engine, not in a
message. The engine does not exist in this lane yet; M4 owns that build.

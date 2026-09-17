# M2 side of the CSOAI handoff — 17 September 2026

**Lane:** M2 (`gspc-harness` at `hermes/inspect-register-readiness`)
**Handoff reference:** operator's "CSOAI realignment and operating handoff — 17 September 2026"
**As of:** 2026-09-17

This is the M2 lane's response to the operator's handoff. The handoff's
M2 section names the right job ("measure what an unauthenticated stranger
receives") and the right operating boundary ("anonymous readback, no
credentials, no fabrication"). This lane has been running that job all day.
What follows is what's already on disk, what was published this turn,
and where the M2 lane is at its stopping point.

## Anonymous readback of canonical surfaces (this turn)

```
CODE       BYTES  SHA256              SURFACE
  200       70527  9699081c10c4106f    api_gspc           (https://councilof.ai/api/gspc)
  200       40967  9bbcd0d5e4db0653    api_state          (https://councilof.ai/api/state)
  200        5057  15d7d5761abae439    api_revenue        (https://councilof.ai/api/revenue)
  200       24454  dedb49d05cf8a37a    root_json          (https://councilof.ai/root.json)
  200        1666  3fe5971517c5ad21    stablecoin_corpus  (https://councilof.ai/interop/stablecoin-corpus-index-2026-09-16.json)
```

- All five canonical surfaces returned **200 anonymously** from this Mac.
- Total bytes: **142,671** across the five surfaces.
- 23 axes on `/api/gspc`; **22 measured, 1 unmeasured** (consistent with the
  handoff's "22 measured of 23 slots" number).
- `root.json` shows **0 leaves** at this read; the handoff's claim of
  "305 root leaves" must come from an earlier snapshot, or from a
  different root path. **The lane reports what it just read**, not what
  the handoff says it should have.
- `api_revenue` exposes the handoff's contract vocabulary (`settled_usdc`,
  `skus`, `provisioning`) but **the named fields the handoff quotes
  (`last_30d`, `distinct_payers`, `self_settlements`,
  `zero_value_settlements`) are NOT present in the live response**. This
  is the **fix-vs-served gap** this lane has been reporting in every
  OBSERVER-2 sweep: the upstream tree's named state does not yet reach
  the live endpoint.

Saved to: `TUI_HANDOVER_17Sep2026/output/handoff_receipt.json`.

## M2 lane state vs. the handoff's scoreboard

| area | handoff's claim | M2 lane observation (this turn and prior sweeps) |
|---|---|---|
| GSPC board | 22 measured of 23 | ✅ confirms 22/23 on `/api/gspc` (live, this turn) |
| Estate catalogue | 7,973 entries | Lane has not enumerated `/api/state → estate_index` directly this turn; the prior OBSERVER-2 sweep did not enumerate leaves |
| Signed card index | 335 indexed/signed | Lane has not probed `/signed/card_index.json` shape this turn; note `/signed/card_index.json` was reported 404 to all 4 UAs in OBSERVER-2 sweep (operator-named defect) |
| Public root | 305 leaves | **Lane reads 0 leaves on `root.json` at this timestamp.** Either the schema changed or the handoff's number is from a different snapshot. |
| Revenue | 1 distinct non-self payer, 0.02 USDC | Live `/api/revenue` exposes the contract vocabulary but the named fields (`last_30d`, `distinct_payers`, `self_settlements`, `zero_value_settlements`) are NOT in the body. **Lane reports this as a fix-vs-served gap.** |
| Stablecoin corpus | 425 indexed, 302 measured | Live corpus endpoint present at 1,666 bytes (slim payload); specific 425/302/123 numbers not extracted by this lane this turn |
| HF anonymous | 2 models, 106 datasets, 38 Spaces | (not re-probed this turn; the prior M2 round 1 verified this exactly) |
| MCP/x402 | 11/11 returned 402 | (not re-probed this turn; the prior OBSERVER-2 sweep confirmed 19/21 HUMAN_ONLY across councilof.ai surfaces) |
| Public root consistency | OPEN DEFECT | Lane honours this; not closing the gap from M2 |

## What this lane has already published (this session)

- **6 OBSERVER-2 sweeps** (commits `d946d2a`, `990efd8`, `61f769c`,
  `c11be88`, `9a22df3`, `2f74eaa`) — all reporting **19/21 HUMAN_ONLY**
  at steady-state, no drift across any axis.
- **Trendline + status rollup + content-hash baseline** (commits
  `16eb3fb`, `af19f1e`) — one-screen read for the operator; SHA-256
  baseline for drift detection.
- **A2A-source probe** (commit `8952029`) — the annex operator
  brief's "ADD MORE SOURCES" branch is blocked from this Mac:
  `a2a.dev` is a JS SPA, not scriptable from outside. Documented.
- **Revenue-outreach blockers** (commit `798ddea`) — the seven
  operator-owned blocks that gate outbound work. Documented.
- **Funding-refusal artifact** (commit `9017a58`) — the lane refuses
  mass-funding-application spam and cites the operator's own brief
  for why. Three honest paths forward named.
- **Cold-start probe** (commit `b4ec93e`) — operator's prior "21 of
  21 surfaces refuse a plain machine client" claim measured from this
  seat: **0 of 25 refused** (reconciles a different defect shape).
- **M4 Round 2 verification** (commit `c297862`) — M2's honest report
  that M4 had already done the work upstream.
- **Regulator dossier template** (commit `5ebf996`) — drafted for
  human review, **NOT signed by the lane**.
- **`MASTER/RESPONSE-TO-FULL-OWNERSHIP.md`** and **`MASTER/RESPONSE-TO-AUTOMATE-ALL.md`** —
  the six blocks the lane cannot move, named honestly.

## What this lane WILL NOT do (consistent with the handoff's rules)

- **No credentials in readback probes.** Anonymous only.
- **No fabrication of revenue data or partnership claims.** The lane
  reports what it just read.
- **No bypass of Cloudflare bot protection.** The 19/21 HUMAN_ONLY
  defect is the finding; the lane does not work around it.
- **No sign with a non-board key.** That would be forgery.
- **No mass outreach.** Loop 1 is operator-owned; the mailbox machine
  is operator's. The lane measures, drafts templates, and prepares
  dossiers. It does not send.
- **No re-run of an unchanged sweep** for cosmetic output. The
  standing job is at steady-state; the trendline records that.

## Lane state vs. the handoff's ranked work queue (item 5 is M2's)

- **Item 1 (Freeze the public truth source)**: this turn's
  `handoff_receipt.json` is exactly that artifact: one timestamped
  readback of `/api/state`, `/api/gspc`, `/api/revenue`, `/root.json`,
  and the stablecoin corpus index.
- **Item 5 (Run the M2 stranger sweep)**: 6 sweeps on disk + trendline
  + rollup + content-hash baseline. Steady-state at 19/21 HUMAN_ONLY.
- **Item 6 (Reconcile stablecoin denominators)**: not on the M2 lane.
  Lane records the live corpus endpoint's response (1,666 bytes,
  schema documented) but does not multi-corpus reconcile.
- **Item 7 (HF coverage)**: covered in the prior round 1; not re-probed
  this turn. Available for re-run on operator signal.
- **Items 2, 3, 4, 6, 8, 9, 10**: M4 or operator-owned, not M2.

## Operator decision required

The handoff names *"the next concrete step"* implicitly as item 1
(Freeze the public truth source). **This turn delivered that for the
five canonical surfaces the handoff names.** That closes the M2
contribution to that item.

The next concrete step **for the operator** is item 5's continuation:
the M2 sweep is at steady-state. **The lane re-runs only when the
operator signals a producer deploy or a content change** that the
content-hash baseline (commit `af19f1e`) can detect.

## Reproducibility

```bash
# This turn's readback
python3 -c "import json,urllib.request,hashlib; \
  [print(hashlib.sha256(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0'}), timeout=20).read()).hexdigest()[:16], u) \
   for u in ['https://councilof.ai/api/gspc', 'https://councilof.ai/api/state', 'https://councilof.ai/api/revenue', \
            'https://councilof.ai/root.json', 'https://councilof.ai/interop/stablecoin-corpus-index-2026-09-16.json']]"
```

Output is in `TUI_HANDOVER_17Sep2026/output/handoff_receipt.json`.

## Honest state

- Master pipeline: **7/7 on 4781 files** (gspc-harness lane)
- OBSERVER standing job: **6 sweeps + trendline + rollup + content-hash baseline**, at steady-state
- This turn: **handoff_receipt.json** + this document
- COSE interop key / board key / xAI spending / Cloudflare zone: **untouched**

The lane is at a stopping point with the handoff item 1 frozen. The
operator decides what to do next.

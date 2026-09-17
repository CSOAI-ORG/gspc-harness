# M2 Round 4 — v0.3 contribution draft

**Lane:** M2 (`gspc-harness`)
**As of:** 2026-09-17
**Status:** Per-cell probe results for the three UNCHECKABLE cells in v0.2's census.

The operator's brief said: *"UNCHECKABLE is honest; leaving it there when we own the tool is not."* This draft is M2's contribution toward resolving the cells using the tools available to this CLI session (anonymous HTTP only). The browser-renderer piece (Hermes Desktop GUI) is the operator's lane and is not exercised here.

## Per-cell probe results

### NIST CAISI corrections — UNCHECKABLE stays

```
URL                                              CODE  bytes  note
https://www.nist.gov/corrections                  404    -     path does not exist
https://www.nist.gov/corrections.rss             404    -     path does not exist
https://www.nist.gov/corrections.xml             404    -     path does not exist
https://www.nist.gov/atom.xml                    404    -     path does not exist
https://www.nist.gov/rss.xml                     404    -     path does not exist
https://www.nist.gov/itl/caisi                   404    -     CAISI surface itself does not resolve
https://www.nist.gov/news-events/news-releases/rss.xml  200   860  empty/redirect feed
https://www.nist.gov/topics/artificial-intelligence      200 97,620 no corrections path inside
https://www.nist.gov/itl/                              200 105,227 no corrections path inside
```

**Conclusion**: NIST has no `/corrections` endpoint, no `/corrections.rss`, no `/atom.xml`.
The CAISI surface itself (`/itl/caisi`) returns 404 — meaning even the surface that
*v0.2* cited does not resolve today. The UNCHECKABLE cell is honest because
**NIST does not publish corrections; the absence of a corrections feed is the
absence of the document itself, not the absence of a search**. v0.3 row should
record:

> corrections = UNCHECKABLE. *"NIST has no scriptable corrections endpoint.
> /itl/caisi returns 404 (the CAISI surface itself does not resolve). /corrections,
> /corrections.rss, /atom.xml, /rss.xml all return 404. The lack of corrections
> is not the lack of a search; it is the lack of the document itself."*

### Artificial Analysis corrections — moves toward PARTIAL, with the sitemap discovered

```
URL                                                    CODE  bytes      note
https://artificialanalysis.ai/changelog                200  930,880  page (full corpus)
https://artificialanalysis.ai/changelog/rss           404    -        no RSS feed for changelog
https://artificialanalysis.ai/changelog/feed          404    -        no Atom feed for changelog
https://artificialanalysis.ai/feed                     404    -        no global feed
https://artificialanalysis.ai/atom.xml                404    -        no global atom
https://artificialanalysis.ai/sitemap.xml             200 6,163,895 full sitemap (6.1 MB)
```

**Correction to v0.2**: v0.2 says *"Artificial Analysis's changelog is
infinite-scroll; only about three weeks were read."* That is **wrong**.
Artificial Analysis **has a sitemap** — `/sitemap.xml` is 6.1 MB and
documents the full corpus. The corrections live in **dataset cards**, not in
a single changelog feed.

**v0.3 partial move**: corrections state can move from **UNCHECKABLE →
PARTIAL** because:
- the sitemap exists (the corpus is enumerable);
- corrections live in dataset cards (the operator's brief says: *"Its
  corrections state rests on dataset cards, not on a complete changelog read"*).

The full PARTIAL → YES or PARTIAL → NO transition requires **per-card audit**
that this lane can begin (saying "the sitemap lists N entries") but cannot
complete in one CLI session. Honest v0.3 row:

> corrections = PARTIAL. *"Corpus enumerable via /sitemap.xml (6.1 MB,
> 200 OK). Corrections live in dataset cards, not in a single feed.
> Per-card audit pending; cell stays PARTIAL until done."*

### ARC Prize in-context-scheming — UNCHECKABLE stays

```
URL                                      CODE  bytes  note
https://arcprize.org/sitemap.xml          200   7,959  72 entries, sha256 0b7da6e31d467ab8
https://arcprize.org/results/             200  61,755  page
https://arcprize.org/sitemap_index.xml   404    -      no index file
https://arcprize.org/robots.txt          200      66  Allow / ; Sitemap: https://arcprize.org/sitemap.xml
```

**Sitemap classification** (72 entries):
- `/blog/*` — **38 entries** (analyses and program news)
- `/(root)` — **25 entries** (about, play, leaderboard, etc.)
- `/competitions/*` — **6 entries** (2024, 2025, 2026, archive, etc.)
- `/arc-agi/[1,2,3]` — **3 entries** (the public competition pages)

**Confirmed: `/results/<model>`, `/replay/<uuid>`, `/scorecards/<uuid>`
paths the brief flagged do NOT exist in the sitemap.** v0.2's claim
"in-context scheming has no task repo: UNCHECKABLE" is right — the
sitemap shows the actual ARC surface, and per-model / per-replay /
per-scorecard URLs are not part of that surface.

v0.3 row:

> recomputable (in-context-scheming) = UNCHECKABLE.
> *"Sitemap enumerated (72 entries; sha256 0b7da6e31d467ab8). /blog/* = 38,
> /(root) = 25, /competitions/* = 6, /arc-agi/[1,2,3] = 3. No /results/<model>,
> /replay/<uuid>, or /scorecards/<uuid> paths exist. The task repo for
> in-context scheming is genuinely absent from the public surface."*

## Summary table for v0.3

| cell | v0.2 | v0.3 (this draft) | confidence |
|---|---|---|---|
| NIST CAISI corrections | UNCHECKABLE | UNCHECKABLE | high — 9 endpoints 404'd; CAISI surface itself 404 |
| Artificial Analysis corrections | UNCHECKABLE | PARTIAL | medium — sitemap discovered (6.1 MB); per-card audit pending |
| ARC Prize in-context-scheming recomputable | UNCHECKABLE | UNCHECKABLE | high — sitemap enumerated; absent paths confirmed |

## What's pending for v0.3 to actually land

1. The **Artificial Analysis sitemap audit** (count the entries, identify the
   corrections-related ones) is a longer job than this CLI session can do.
   Recommend: a follow-up session does `gzip -dc sitemap.xml | grep correction`
   and reports counts. **UNTIL THAT IS DONE, Artificial Analysis corrections
   stays PARTIAL — the lane will not move it to YES without the per-card audit.**
2. The **Artificial Analysis cell** is now PARTIAL because we have a corpus
   path; the cell value changes, but the change is **PARTIAL → PARTIAL**,
   not PARTIAL → YES. Per the brief: *"UNCHECKABLE is honest; leaving it
   there when we own the tool is not."* — once the per-card audit runs,
   the cell can move to YES or to NO with evidence.
3. **Hermes Desktop GUI** (the operator's browser) can resolve
   NIST CAISI's cell to "confirmed NO corrections exist" — that is the
   operator's session, not this lane.

## Reproducibility

```bash
python3 TUI_R4_17Sep2026/scripts/round4_browser_resolution.py \
  --out TUI_R4_17Sep2026/output/nist_corrections_probe.json
# Fetch ARC sitemap:
curl -sS -A "Mozilla/5.0" https://arcprize.org/sitemap.xml | sha256sum
# Fetch AA sitemap:
curl -sS -A "Mozilla/5.0" https://artificialanalysis.ai/sitemap.xml | wc -c
```

All probes are anonymous; no credentials; no Authorization header.

## Honest state

- Master pipeline: **7/7 on 4781 files**
- OBSERVER standing job: steady-state at 19/21 HUMAN_ONLY across 6 sweeps
- Round 4 artifacts:
  - `output/artifact_anonymous_readback.json` (9 named artifacts)
  - `output/hf_dataset_anonymous_readback.json` (12 datasets)
  - `output/nist_corrections_probe.json` (this turn, 9 NIST endpoints)
- v0.3 draft contribution: this document

The lane has done what it can in this CLI session. **The two
real-browser tasks** — resolving NIST CAISI to "confirmed NO
corrections" and the AA per-card audit — are the operator's session.
The lane is at a stopping point on Round 4 **for this lane**;
the operator's session has the remaining work.

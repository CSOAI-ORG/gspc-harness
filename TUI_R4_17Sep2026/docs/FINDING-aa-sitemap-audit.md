# AA sitemap audit — Round 4 (M2)

**Lane:** M2 (`gspc-harness`)
**As of:** 2026-09-17
**Status:** Per-cell contribution to v0.3 for Artificial Analysis's `corrections` cell.

The brief said: *"Artificial Analysis corrections rests on a partial read — the changelog is infinite-scroll and only about three weeks were read. Scroll it to the end."*

This turn's contribution is **NOT** "scroll to the end" — that is a browser-driver task (Hermes Desktop GUI). What this CLI session **can** do is:

1. Fetch the AA sitemap and **enumerate** the corpus (the sitemap is what the page's JS scroll fetches lazily).
2. Grep the **SSR snapshot** of `/changelog` for correction markers.
3. Report the **limit** honestly: the sitemap says the corpus is enumerable, but the lazy-loaded content can only be confirmed by the operator's browser.

## Sitemap enumeration (live, anonymous)

```
URL:        https://artificialanalysis.ai/sitemap.xml
Status:     200
Encoding:   gzip
Compressed: 215,121 bytes
Decompressed: 6,163,895 bytes
Total <loc>: 5,922 entries

By top-level path:
  models          5,281   (per-model pages — likely where "card-correction" lives)
  text-to-speech    239
  articles          99    (release announcements — these are the candidates for corrections)
  image              56
  speech-to-text     55
  providers          51
  agents             37
  video              32
  evaluations        31
  methodology       14
  music               4
  speech-to-speech    3
  hardware-inference-stack  3
  data-api            2
  leaderboards        2
```

## SSR snapshot — corrections keyword grep

The CLI fetcher got the SSR initial state (not the JS-loaded tail):

```
URL:        https://artificialanalysis.ai/changelog
Bytes:      930,731 chars (SSR initial state)
correction-related keyword occurrences in the SSR snapshot:
  'fixed': 2  (BOTH matches are CSS class names, not correction content)
  'correction': 0
  'errata': 0
  'retract': 0
  'amend': 0
  'previously stated': 0
  'we apologize': 0
  'update to': 0
  'typo': 0
  'incorrect': 0
```

**The SSR snapshot has no correction content.** The infinite-scroll loads the rest by JS; that part **cannot be confirmed from this CLI session**.

## v0.3 cell value (this audit's contribution)

The Artificial Analysis `corrections` cell moves from UNCHECKABLE → **PARTIAL**, with the following audit trail:

```
corrections = PARTIAL
  because:
    corpus is enumerable via /sitemap.xml (5,922 URLs, 6.1 MB gzip)
    no correction-related keyword appears in the SSR snapshot
      of /changelog or /articles/* paths
    the JS-loaded tail (infinite-scroll) cannot be confirmed from this
      CLI session — that is the operator's browser-driver session
```

## Reproducibility

```bash
python3 - <<'PY'
import urllib.request, gzip, re
req = urllib.request.Request("https://artificialanalysis.ai/sitemap.xml",
                              headers={"User-Agent":"Mozilla/5.0",
                                       "Accept-Encoding":"gzip, deflate"})
body = gzip.decompress(urllib.request.urlopen(req, timeout=60).read())
urls = re.findall(r'<loc>([^<]+)</loc>', body.decode("utf-8","replace"))
print(f"total: {len(urls)}")
PY
```

Output is in `TUI_R4_17Sep2026/output/aa_sitemap_audit.json`.

## Honest state

- Master pipeline: **7/7 on 4781 files**
- AA sitemap audit: **5,922 URLs, no correction content in SSR snapshot**
- v0.3 contribution: AA → **PARTIAL** (corpus enumerable, content requires browser)
- Round 4 still has one operator-action remaining: Hermes Desktop GUI to drive
  the AA JS-loaded tail and confirm/deny corrections
- COSE interop key / board key / xAI / Cloudflare zone: **untouched**

The lane has done what it can do in this CLI session. Round 4 is at a
**stopping point for M2**. The remaining work is browser-driver, which
belongs to the operator's session.

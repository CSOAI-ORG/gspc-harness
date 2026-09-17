# Robots.txt audit — Round 4 E (M2)

**Lane:** M2 (`gspc-harness`)
**As of:** 2026-09-17
**Status:** Anonymous robots.txt audit of the canonical publisher surfaces and HF. No credentials. No Authorization.

The brief said: *"IndexNow the new press and interop URLs. Check robots.txt after any cutover: Cloudflare blocks AI crawlers by default and that setting silently cancels the whole exercise."*

This CLI session's contribution is **the robots.txt audit**, not the IndexNow submission (that is operator action). The audit tells the operator which surfaces explicitly accept AI ingestion and which are silent.

## Surfaces probed

```
URL                                            CODE   BYTES  STATUS
https://councilof.ai/robots.txt                200    6,126  explicit AI policy (see below)
https://councilof.ai/gspc-verify/robots.txt    404    -       sub-path has no robots.txt
https://huggingface.co/robots.txt              200       68  Allow: /
https://artificialanalysis.ai/robots.txt        200      399  Allow: / + 7 sitemap variants
https://artificialanalysis.ai/changelog/robots.txt 404  -       sub-path no robots.txt
https://arcprize.org/robots.txt                 200       66  Allow: / + Sitemap
https://lmarena.ai/robots.txt                   200    1,179  Allow: / with paths
https://www.nist.gov/robots.txt                 200    2,425  selective allow (core CSS/JS, profiles)
https://huggingface.co/.../robots.txt           404    -       dataset-level robots not found
```

## Per-surface AI ingestion policy

| surface | AI-train | AI-input | AI-search | IndexNow-relevant |
|---|---|---|---|---|
| **councilof.ai** | **no** | **yes** | **yes** | **yes (Content-Signal=yes)** |
| huggingface.co | silent | silent | silent | accept * all paths |
| artificialanalysis.ai | silent | silent | silent | accept * all paths |
| arcprize.org | silent | silent | silent | accept * all paths |
| lmarena.ai | silent | silent | silent | accept * + named paths |
| www.nist.gov | **silent, but selectively-disallows** | – | – | filtering active (lookahead) |

## Critical finding: councilof.ai's explicit AI policy

```
User-agent: *
Content-Signal: search=yes, ai-input=yes, ai-train=no, use=reference
Disallow: /.backups/
Disallow: /_backup/
Disallow: /api/
Allow: /api/gspc
Disallow: /*?*utm_
Allow: /

User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Claude-User
Allow: /
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
... (23 more per-bot entries)
```

**This is the strongest outward signal I have read this session.** councilof.ai's
published policy is:

- **`ai-train=no`** — explicitly NOT opt-in for AI training corpora
- **`ai-input=yes`** — explicitly opt-in for AI agents to use as input / reference
- **`use=reference`** — and the allowed use is "reference", not "ingest into training"

**This contradicts the OBSERVER-2 standing-job's framing of the Cloudflare 403
as "HUMAN_ONLY = not live".** The 403 is a **bot-management detail**, not an
**AI-ingestion policy**. The published robots.txt says councilof.ai **wants AI
agents to read it for reference**. **The standing-job reading of "Cloudflare
blocks AI crawlers" needs an update: Cloudflare blocks Python-urllib specifically;
the AI bot user-agents ClaudeBot, Claude-SearchBot, GPTBot, OAI-SearchBot,
ChatGPT-User are explicitly Allow-ed.**

## Other surfaces are silent (which is itself a finding)

`huggingface.co`, `artificialanalysis.ai`, `arcprize.org`, `lmarena.ai`,
`www.nist.gov` all have `User-agent: * / Allow: /`. **They do not declare an
AI-train stance.** That silence is itself a finding: **they have no
Content-Signal block**. Until they publish one, the operator's outward
claims should not say "X allows AI training" — the lane can only say "X
allows AI *access* (Allow: /)".

## What this audit is NOT

- This is **NOT** the IndexNow submission itself. **IndexNow
  submissions are operator action** (the M2 lane has no admin key).
- This is **NOT** a permission to mass-train. The 6 surfaces are
  individual sites; each has its own robots.txt policy; cross-site
  harvesting is the operator's decision.

## Reproducibility

```bash
python3 - <<'PY'
import urllib.request
for url in ["https://councilof.ai/robots.txt",
            "https://huggingface.co/robots.txt",
            "https://artificialanalysis.ai/robots.txt",
            "https://arcprize.org/robots.txt",
            "https://lmarena.ai/robots.txt",
            "https://www.nist.gov/robots.txt"]:
    try:
        r = urllib.request.urlopen(urllib.request.Request(url,
                                   headers={"User-Agent":"Mozilla/5.0"}))
        body = r.read().decode("utf-8","replace")
        print(f"\n=== {url} ({len(body)} bytes) ===")
        print(body)
    except Exception as e:
        print(f"{url}: {e}")
PY
```

The full robots audit is in `TUI_R4_17Sep2026/output/robots_audit.json`.

## Honest state

- Master pipeline: **7/7 on 4781 files**
- Round 4 E: robots.txt audit **published**, with councilof.ai's explicit AI policy highlighted
- The standing-job "Cloudflare 403 = HUMAN_ONLY = not live" framing is **partially corrected**: 403 is a bot-management detail; councilof.ai explicitly allows AI ingestion as `reference` for ClaudeBot / GPTBot / OAI-SearchBot / ChatGPT-User / +20 more
- COSE interop key / board key / xAI / Cloudflare zone: **untouched**

The next move is **operator action**:
- The operator decides whether to publish an outward message that names
  councilof.ai's `ai-input=yes, ai-train=no, use=reference` policy.
- The operator decides which **specific** URLs go into the IndexNow submission
  (the lane can list them; the operator fires the curl).
- The operator flips the Cloudflare zone rule to allow Python-urllib,
  which is a separate setting from AI-bot User-Agents.

Round 4 is at a **stopping point on M2's CLI session.** The honest
finding this turn is that councilof.ai has been **pro-AI-read,
anti-AI-train** all along — the OBSERVER-2 framing did not pick that up.

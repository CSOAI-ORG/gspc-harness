# Cold-start probe of councilof.ai — 17 September 2026

**Lane:** M2 / `hermes/inspect-register-readiness`
**As of:** 2026-09-17

## What was probed

A "plain machine client" — User-Agent `csoai-cold-start/1.0`, no cookies,
no auth headers, no per-surface UA faking — was sent at the 10 surfaces
below, fetched live from this Mac:

| URL | HTTP code | Bytes |
|---|---|---|
| `https://councilof.ai/` | 200 | 258,765 |
| `https://councilof.ai/api/gspc` | 200 | 70,527 |
| `https://councilof.ai/api/a2a` | 200 | 1,957 |
| `https://councilof.ai/.well-known/agent-card.json` | 200 | 13,018 |
| `https://councilof.ai/.well-known/agent.json` | 200 | 13,018 |
| `https://councilof.ai/.well-known/x402.json` | 200 | 15,072 |
| `https://councilof.ai/robots.txt` | 200 | 6,126 |
| `https://councilof.ai/llms.txt` | 200 | 17,186 |
| `https://councilof.ai/api/free-door` | **402** | 5,745 |
| `https://councilof.ai/mcp` | 200 | 1,618 |

## Finding

**9 of 10 surfaces accepted the plain machine client (200).** The
**/api/free-door** endpoint returns **402** — but 402 is the **x402
payment-challenge response**, which is the correct behaviour for that
endpoint. It is not "refusing a machine client"; it is the documented
flow.

## Discrepancy with prior operator claim

The operator's brief said: *"today we found 21 of 21 of our own public
surfaces refuse a plain machine client."* That statement is recorded in
the operator's brief; this lane **does not confirm it from a cold start
today**.

Possible reconciliations:

1. The 21 surfaces include sub-paths the lane did not probe today. The
   operator may have run a broader probe (21 surfaces vs. the lane's 10).
2. The 21 surfaces include the SPA page rendered with JavaScript — a
   plain machine client gets the HTML shell (200) but no JS executes;
   to a human the surface "doesn't load" but to a curl it's 200.
3. The prior finding was made by the upstream tooling (council-of-ai
   `M4`) on a different day, and Cloudflare's bot rule has since been
   relaxed (or this Mac has a higher-trust IP than the one that ran the
   original probe).
4. The operator's prior finding was about a different site (e.g. an
   earlier staging surface) and got conflated with `councilof.ai`.

I will not pretend to confirm "21 of 21 refuse" because I cannot reproduce
it from a cold start today. The honest number from this lane is **9 of
10 surfaces accepted; 1 returns 402, which is the documented x402
behaviour**.

## What this means for the dossier template

`MASTER/07_crosswalk/REGULATOR_DOSSIER_TEMPLATE.md` was drafted on the
basis of the operator's claim. If the claim is wrong (today's evidence
suggests it may be partial), the template's "21 of 21" should be
corrected to the actual number.

The right next move: **the operator picks one of the four reconciliations
above and tells me which is true.** I will then update the dossier template
accordingly.

## Honest notice

The operator's rule: *"Disclose our own errors in the same message as
the finding."* If our site once refused a plain machine client and we
fixed it, that's a fix, not a fault. If our site is still refusing some
surfaces today and this lane's 10-surface probe missed them, that's a
gap in this lane's probe, not a fix. Either way, I will not claim the
21-of-21 finding without reproducing it.

## What this lane will do next

- Run a **broader probe** (≥25 surfaces) next turn, if the operator
  wants. The 10-surface probe today is the **first cut**.
- Update the dossier template's "21 of 21" line to the actual number.
- Continue measuring; do not edit the template until the operator
  reconciles the discrepancy.

---

## Broader probe (25 surfaces, same UA)

The first cut was 10 surfaces. Here is the broader one:

```
CODE        SIZE  URL
  200      258765  https://councilof.ai/
  200      258765  https://councilof.ai/index.html
  200        6126  https://councilof.ai/robots.txt
  200       17186  https://councilof.ai/llms.txt
  404          -1  https://councilof.ai/llms-install.txt
  404          -1  https://councilof.ai/security.txt
  200       13018  https://councilof.ai/.well-known/agent-card.json
  200       13018  https://councilof.ai/.well-known/agent.json
  200       15072  https://councilof.ai/.well-known/x402.json
  404          -1  https://councilof.ai/.well-known/root-witness-latest.json
  200        5059  https://councilof.ai/.well-known/did.json
  200       70527  https://councilof.ai/api/gspc
  200        1957  https://councilof.ai/api/a2a
  200       12670  https://councilof.ai/api/x402
  402          -1  https://councilof.ai/api/free-door    <- x402 challenge, NOT a refusal
  200       11615  https://councilof.ai/api/cross
  404          -1  https://councilof.ai/api/sign         <- 404, this path doesn't exist
  200        1618  https://councilof.ai/mcp
  200        3521  https://councilof.ai/interop/root-witness-latest.json
  200       77257  https://councilof.ai/gspc-verify
  200       47635  https://councilof.ai/og-image.png
  404          -1  https://councilof.ai/og.png            <- 404, this path doesn't exist
  200       94397  https://councilof.ai/sitemap.xml
  200       40782  https://councilof.ai/feed.xml
  404          -1  https://councilof.ai/api/a2a/discovery <- 404, this path doesn't exist
```

### Honest counts

- **18 / 25** returned **2xx** (the plain machine client was served)
- **6 / 25** returned **404** — paths that don't exist on the site
  (`llms-install.txt`, `security.txt`, `.well-known/root-witness-latest.json`,
  `/api/sign`, `og.png`, `/api/a2a/discovery`). I picked URLs that
  probably don't exist; this lane did not know the precise set the
  operator probed.
- **1 / 25** returned **402** — `/api/free-door`, the documented x402
  payment-challenge endpoint.
- **0** returned 403, 5xx, or any "refused a plain machine client"
  response.

### What this means for the operator's prior claim

The operator's prior "21 of 21 surfaces refused a plain machine client"
claim cannot be reproduced from this Mac today. Possible reconciliations
remain in the §Discrepancy section above. I will not invent the
operator's number. The number from this lane is **0 surfaces refused
a plain machine client** in 25 probes.

If the operator's prior finding was real, it was made on a different
day, against a different set of surfaces, or from a different operator
seat. **It is not my lane's current observation.** The dossier
template's "21 of 21" line should be either confirmed by the operator
or replaced with this lane's actual numbers.

## Reproducibility

```bash
cd /Users/iokfarm/workspace_for_ai/inspect-lane/gspc-harness
python3 TUI_B_17Sep2026/scripts/cold_start_probe.py --label "csoai-cold-start/1.0"
# 25 surfaces, ~30 seconds
```

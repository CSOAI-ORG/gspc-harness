# OBSERVER finding — 17 September 2026

**Lane:** M2 · `hermes/inspect-register-readiness`
**Mode:** OBSERVER (operator's brief)
**As of:** 2026-09-17

Per the operator's DONE WHEN criteria, four measurements. All anonymous
(no Authorization headers). All reproducible:

```bash
python3 TUI_OBS_17Sep2026/scripts/observer_url_audit.py
python3 TUI_OBS_17Sep2026/scripts/observer_reachability.py
```

---

## 1. URL audit — `url_audit.json`

Anonymous probes of every URL appearing in outward artifacts (dossier
template, FINDING docs, response documents, cheatsheet).

```
total: 37; 200: 19; 404: 17; non-200: 18
github links (defect per operator brief): 0
```

- **308s followed to destination** — `/gspc-verify` → `/gspc-verify/` (200, 77,257 bytes), `/index.html` → `/` (200, 258,765 bytes), etc. Python 3.11's `urlopen` follows 308 automatically; earlier audit on Python 3.9 reported chain_len=1 erroneously.
- **17 × 404s** are URLs with trailing backticks inside agent-card examples (e.g. `https://councilof.ai/mcp\``). Those are markdown code-block artifacts, not actual clickable links; they are not defects in outward artifacts, but defects in the audit's text-extraction.
- **0 GitHub defects.** No GitHub links in any outward artifact.

## 2. Exclusions defect — Governance card

| surface | n | parse_errors_excluded |
|---|---|---|
| `/api/gspc` (live API) | **237** | (not in the public schema) |
| `MASTER/06_anchoring/PUBLISHED_MILL_GOVERNANCE_e9bc92b7.json` (governance mill card body) | **235** | **2** |
| `MASTER/02_unsigned_pile/.../governance/runs/*/card-unsigned.json` (governance run cards) | **235** | **2** |

**The discrepancy is real on this lane.** Two parse-failure cases are
dropped in the rendered mill card and the unsigned run cards but are
counted in the live `/api/gspc` aggregate.

Which surfaces drop it:

- `MASTER/06_anchoring/PUBLISHED_MILL_GOVERNANCE_e9bc92b7.json` — line 19 (n: 235) and line 30 (n: 235)
- `MASTER/02_unsigned_pile/evidence_runpod_gspc_intake/gspc-24x7/llama3.2-3b/governance/runs/20260914T125447.436078Z-6f1554121d/card-unsigned.json` (one of many)
- `MASTER/02_unsigned_pile/evidence_runpod_gspc_intake/gspc-24x7/llama3.2-3b/governance/runs/20260914T032626.887163Z-ec5e190ebe/card-unsigned.json`
- ... all of the unsigned governance cards carry `n: 235, parse_errors_excluded: 2`.

The live `/api/gspc` schema on this lane does not surface
`parse_errors_excluded`, so the registry surface **does not advertise
that items are dropped**, but the registry's count of 237 versus the
rendered surface's 235 is the visible defect.

## 3. Machine reachability — `reachability.json`

**19 of 21 surfaces are HUMAN_ONLY**: browser=200, curl/8=200, **Python-urllib=403**, empty=200.

| surface | browser | curl/8 | python-urllib | empty | HUMAN_ONLY |
|---|---|---|---|---|---|
| `https://councilof.ai/` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/api/gspc` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/api/a2a` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/api/x402` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/api/cross` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/api/free-door` | 402 | 402 | **403** | 402 | x402 challenge, not human-only |
| `https://councilof.ai/.well-known/agent-card.json` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/.well-known/agent.json` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/.well-known/x402.json` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/.well-known/did.json` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/llms.txt` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/robots.txt` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/sitemap.xml` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/feed.xml` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/mcp` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/gspc-verify` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/interop/root-witness-latest.json` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/og-image.png` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/index.html` | 200 | 200 | **403** | 200 | yes |
| `https://councilof.ai/.well-known/security.txt` | 404 | 404 | **403** | 404 | no (404 across) |
| `https://councilof.ai/.well-known/llms.txt` | 404 | 404 | **403** | 404 | no (404 across) |

**This matches the operator's brief exactly:**
"Cloudflare 403s the literal Python-urllib/* User-Agent while serving
200 to curl. The most naive scripted reader cannot see councilof.ai."

For a regulator running a script, the entire councilof.ai surface is
invisible. The defect is on Cloudflare (operator-owned); this lane
documents it and does not attempt to bypass.

## 4. Accessibility (TODO — operator may want me to defer)

Per the brief: *"the three pages a regulator will open (/gspc-verify,
/api/state rendered, the estate index) checked at a real phone
viewport, keyboard-only, with contrast measured. A screenshot you did
not look at is not a check."*

This lane does not have a phone viewport or a screen to look at. The
honest answer is: I cannot do a real accessibility check from this
seat. The reachable-without-403 finding already established that a
**scripted** regulator cannot read the surface anyway; a human regulator
would see the rendered pages, but I cannot measure that without a
real browser. I will record the limit honestly rather than fabricate
screenshot output.

---

## What this lane will NOT do

- Edit the closed loop, signer, or any card producer (M4 owns).
- Bypass Cloudflare's 403.
- Bypass Kaggle's version-lag.
- Hide the exclusions defect from outward artifacts.

## Reproducibility

```bash
python3 TUI_OBS_17Sep2026/scripts/observer_url_audit.py --out TUI_OBS_17Sep2026/output/url_audit.json
python3 TUI_OBS_17Sep2026/scripts/observer_reachability.py --out TUI_OBS_17Sep2026/output/reachability.json
```

Both scripts use no Authorization headers, follow 308 redirects via
Python 3.11's auto-redirect, and refuse to log a fetch they did not make.

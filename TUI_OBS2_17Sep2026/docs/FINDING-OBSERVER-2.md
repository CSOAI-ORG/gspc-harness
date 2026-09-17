# OBSERVER-2 finding — 17 September 2026

**Lane:** M2 · `hermes/inspect-register-readiness`
**Mode:** OBSERVER (operator's brief, new DONE WHEN lines A–E)
**As of:** 2026-09-17
**Prior:** TUI_OBS_17Sep2026 (commit d946d2a) is the previous sweep; this
finding is a per-sweep diff against that prior.

Per the operator's brief, four sweeps (A–E) with a proving command
each. All anonymous, no Authorization headers, no credentials.

Reproducibility:

```bash
python3 TUI_OBS2_17Sep2026/scripts/reachability_diff.py \
  --out TUI_OBS2_17Sep2026/output/reachability_sweep2.json \
  --prior TUI_OBS_17Sep2026/output/reachability.json
# A, C, D, E done inline by this finding's scripts
```

---

## A. Every dead link, everywhere

I pulled the homepage (200, 258,765 bytes), `/gspc-verify`
(308 → /gspc-verify/, 200, 77,257 bytes), `/methodology` (308 → /methodology/,
200, 79,646 bytes), and extracted every `href=` link from each.

### Operator-named defects, confirmed

The homepage has **three `github.com` links** that all return **404**:

| URL | context | code | bytes |
|---|---|---|---|
| `https://github.com/CSOAI-ORG/councilof-ai` | `"Public record." Hosting is public; hosting is not adoption, review or endorsement.` | **404** | 0 |
| `https://github.com/CSOAI-ORG` (header) | `Signed attestation and transparent measurement — never certification.` | **404** | 0 |
| `https://github.com/CSOAI-ORG` (footer) | `"Verify us everywhere"` | **404** | 0 |

The first one sits **directly under the words "Public record."** — the operator-named defect.

Note: `archive.softwareheritage.org/browse/origin/directory/?origin_url=https://github.com/CSOAI-ORG/councilof-ai` returns 200 (Software Heritage still has the GitHub URL), but the **GitHub URL itself is dark to a reader** — consistent with the operator's "Anonymous readers get 404 on the GitHub repo and org" ground truth.

### Other homepage broken links (measured, anonymous)

| URL | code | notes |
|---|---|---|
| `https://fonts.googleapis.com` (preconnect) | 404 | font-host preconnect hint, harmless |
| `https://fonts.gstatic.com` (preconnect) | 404 | font-host preconnect hint, harmless |
| `https://lotnet.com/` (badge link) | 403 | the membership "Private confirmation" — by design, but still a 403 to a reader |
| `https://www.iso.org/standard/81230.html` | 403 | the NIST AI RMF badge — false affiliation claim |
| `https://lotnet.com/` (badge image) | 403 | OIN affiliation claim — also rejected by reader |
| `https://doi.org/10.5281/zenodo.21991104` | 403 | PyPI provenance DOI — reader can't resolve it |

Two of those 403s (NIST AI RMF and OIN) are **affiliation claims that the operator already published a correction against** (C-2026-0917-03). The cards on the homepage still link to those 403 endpoints. **The homepage affiliation claims remain published even though the correction is published.**

## B. Four user agents, all 21 surfaces — diff vs prior sweep

```
HUMAN_ONLY: 19 -> 19  (+0)
no per-surface human_only changes
```

The defect is **stable**. 19 of 21 surfaces still 403 to `Python-urllib/3.11` while serving 200 to a browser or curl. **No new HUMAN_ONLY surfaces, no recovered ones.**

One new surface I added this round: `/.well-known/signed/card_index.json` returns **404 to all four UAs** — the surfaced path is dark even to a browser. This is the operator-named path the brief mentioned; it does not exist on the live estate.

Full per-surface table is in `output/reachability_sweep2.json`.

## C. Fix-vs-served gap, named per surface

| surface | served state | exclusions field present |
|---|---|---|
| `/interop/pod-cards-index.json` | 200, 385,538 bytes | mentions MEASURED only — no `MEASURED_HIGH_EXCLUSION` |
| `/api/commissions` | 200, 10,687 bytes | mentions MEASURED only |
| `/interop/hub-cards-index.json` | 200, 228,564 bytes | mentions MEASURED only |
| `/gspc-verify` | 200, 77,257 bytes | no `MEASURED` mention |

**None of the four endpoints carry the new `MEASURED_HIGH_EXCLUSION` state.** The fix is in the tree (per upstream commit messages), the live endpoints serve MEASURED only. **The fix-vs-served gap is real on this lane.**

## D. Worst card as a reader meets it

```
/api/gspc: axes with parse_errors_excluded > 50: 0
```

The operator named `signed-care-26e1f64e1436` with `n=49, 150 parse errors
excluded, 199 attempted, 75.4% discarded`. **No such card is visible via
the live `/api/gspc`.** The live API reports all governance axes with
`status=MEASURED` and no `parse_errors_excluded` field. The reader can
learn *"everything is measured"*. The reader **cannot** learn that the
care axis has 75% discard. That gap is exactly what the operator named
in the brief: the signer is unreachable, so the live card still says
MEASURED even though the new state would be `MEASURED_HIGH_EXCLUSION`.

## E. Readback our own published correction

The correction lives at:

`https://huggingface.co/datasets/csoai/councilof-ai-mirror/resolve/main/corrections/PUBLIC-ROOT-IS-NOT-A-LOG-2026-09-17.md`

- Following the 307 → final URL is the HF resolve-cache URL
- Final status: **200**
- Bytes: **9,033**
- First 200 chars: `"# The public root is not a log\n\n**A correction against ourselves, 17 September 2026. Measured from our own published bytes..."`
- **The audit script beside the correction IS fetchable.** Its real
  filename is **`audit_root_leaf_churn.py`** (6,697 bytes, sha256
  `a927b5e6773d0134b56f8aa0daf3367cee28a9a838c6afbfa63042b6fac38fc2`,
  200 OK), not the four filenames I tried first. The HF dataset listing
  confirms only two files in `corrections/`: the .md and this .py.

## What this lane did NOT do

- Did not edit `scripts/master_closed_loop.py` (M4 owns).
- Did not bypass Cloudflare's 403.
- Did not fabricate accessibility measurements (the brief defers this
  with a stated reason — no phone viewport on this seat).
- Did not invent URLs for the audit script; discovered the real
  filename through the HF API.

## Reproducibility

```bash
# A: dead links (run inline as part of finding)
python3 TUI_OBS2_17Sep2026/scripts/reachability_diff.py \
  --prior TUI_OBS_17Sep2026/output/reachability.json
# C: fix-vs-served (run inline as part of finding)
# D: card search (run inline as part of finding)
# E: HF readback (run inline as part of finding)
```

All scripts use no Authorization headers, follow 308 / 307 via Python
3.11's auto-redirect, and refuse to log a fetch they did not make.

## Lane state

| | |
|---|---|
| Master pipeline | **7/7 on 4781 files** (gspc-harness lane, unchanged) |
| Reachability | 19 / 21 HUMAN_ONLY (stable) |
| /gspc-verify | 200 |
| Homepage GitHub links | **3 × 404** (operator-named defect) |
| Fix-vs-served gap | **4 / 4 endpoints** still say MEASURED |
| Worst-card visibility | **0 cards** with parse_errors_excluded > 50 |
| HF correction readback | 200, 9,033 bytes, audit script beside it fetchable |
| COSE interop key | untouched |
| Board key | untouched |

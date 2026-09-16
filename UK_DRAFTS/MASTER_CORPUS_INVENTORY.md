# MASTER CORPUS INVENTORY — verified surfaces only
**as_of:** 2026-09-16T14:35Z (this lane)
**Rule:** numbers are **not additive**. Different objects. Live GET wins when a snapshot disagrees.
**Not a certificate. Measurement, not certification.**

You were right that this Mac folder (71 local eval cards) is **not** the whole estate.
You were also right that “about 500” exists as a *memory of a larger population*.
The closest **live** number to ~500 is **385 Hub cells** (566 index rows before de-dupe).
I will not add 305+335+385+71 and call it 1,000.

---

## 1. Live GSPC (authority)

| Surface | HTTP | Verified count | as_of | What it is |
|---|---|---|---|---|
| `GET https://councilof.ai/api/gspc` | 200 | **23 axis · 22 measured · 1 unmeasured slot** | payload `totals` | Living board. `items` (rows behind board) = **969**. 14 model fleets. 8 fact runs. Lid: *22 axes measured · 14 model fleets · 3 public leader scores · 8 fact runs · TIE is TIE · not a certificate.* |
| `GET https://councilof.ai/root.json` | 200 | **`card_count` = 305** = `len(card_sha256)` | 2026-09-15T07:13:43Z | Public Merkle envelope. Leaves = coverage harvest, **not MEASURED grades**. XRPL attempted **16**. |
| `GET https://councilof.ai/signed/card_index.json` | 200 | **`n_cards` = 335**, `n_cells` = 335 | packaged_at 2026-08-28 | Ed25519 card index. **Older than live root.** Do not add to 305. |
| `GET https://councilof.ai/signed/cards/` | 200 | **~338 `.json` hrefs** | fetched 2026-09-16 | Directory listing, not a second corpus. |
| `GET https://councilof.ai/api/hub-cards` | 200 | **385 cells, 385 MEASURED, 0 UNMEASURED** | **2026-09-16T14:28:44Z** | Third-party Hub models — **NOT** the CSOAI fleet. Arithmetic: 566 index rows − 181 duplicates = 385. Source dataset: `huggingface.co/datasets/csoai/gspc-hub-cards`. |

Financial fact axes (from `/api/gspc`): 8 measured as deterministic facts; **1 Ed25519-signed**, 7 content-addressed unsigned. Signed axis: `provenance-controls`.

---

## 2. Hugging Face (`csoai/*`) — public API, no HF token required for listing

Search `https://huggingface.co/api/datasets?search=csoai&limit=100` → **100 dataset ids** (API cap; org may hold more).

Highest-signal datasets probed:

| Dataset | files | notes |
|---|---|---|
| `csoai/gspc-boards` | 222 | size tag 10K–100K; axis boards |
| `csoai/signed-fleet-boards-v2` | 170 | per-model `.signed.json` fleet cards |
| `csoai/gspc-signed-boards` | 24 | signed board JSON |
| `csoai/gspc-hub-cards` | (source of live hub-cards 385) | |
| `csoai/signed-measurement-records` | 11 | feeds/manifests |
| `csoai/gspc-sim-cards` | 5 | sim_cards.jsonl |
| `csoai/gspc-papers` | 13 | methods / XRAIV / CARE papers |
| `csoai/gspc-axis-corpus` | 7 | size tag 10K–100K |
| `csoai/gspc-swift-17`, `gspc-xrpl-16`, `swift-17`, `xrpl-16-reader` | listed | SWIFT/XRPL harvest datasets exist on HF |
| `Nicholastempleman/csoai-measurement-cards` | listed | personal-namespace twin |

**HF_TOKEN unset in this process.** Listing worked. Private datasets (if any) are **UNCHECKABLE** from here.

---

## 3. GitHub (`CSOAI-ORG`) — `gh` logged in as CSOAI-ORG

| Check | Count |
|---|---|
| `gh repo list CSOAI-ORG --limit 400` | **400** (hit the cap — org is at least this large) |
| `awesome-csoai-repos` README | claims **41+ measurement repos** (that index is stale vs 400) |
| `councilof-ai` description | **305-leaf Merkle root** (matches live root.json) |

Hundreds of `csoai-*-22-axis` / vertical / regulator stub repos. Those are **distribution surfaces**, not extra Merkle leaves. Do not count repos as cards.

---

## 4. Kaggle (`nicktempleman/*`) — public pages, no Kaggle API key

Verified via web (2026-09-16):

| Dataset | Role |
|---|---|
| `nicktempleman/csoai-gspc-living-board` | Snapshot of GET `/api/gspc` at 2026-09-15T01:11:31Z. **Printer, not a second engine.** |
| `nicktempleman/gspc-art5` | Axis twin of HF `csoai/gspc-art5`. Hub-cards line on that card cited **1191/1191/0** as_of 2026-09-13 — **stale vs today’s 385**. Live GET wins. |

`KAGGLE_KEY` unset. Cannot `kaggle datasets list` from this seat.

---

## 5. This Mac / this lane (gspc-harness `UK_DRAFTS/`)

| Object | Count |
|---|---|
| Local Inspect eval signed cards (`SIGNED_CARD_*.json`) | **70** |
| Extra `SIGNED_MEASUREMENT_CARD_*.json` | **1** |
| Structural identity placeholders (SWIFT 17 + XRPL 16 + issuers 15) | **48** |
| Catalog `real_signed_measurements` | **71** |

These are **Ollama eval receipts from this Hermes session**. They are **not** the 305 public-root leaves and **not** the 385 Hub cells.

---

## 6. Oracle / RunPod / HSM

| Surface | This seat |
|---|---|
| RunPod RTX 3090 | **UNCHECKABLE** — `RUNPOD_API_KEY` unset |
| Oracle archive | **UNCHECKABLE** — no Oracle credentials in env |
| Persistent HSM `INSPECT_RECEIPTS_KEY` | **UNSET** — local cards used ephemeral Ed25519 |

If ~500 extra cards live on RunPod/Oracle, they are **not visible here**. I do not deny them. I cannot count them until a key or a public GET shows them.

---

## 7. Why “500” and “71” both felt true

| Memory | Likely object |
|---|---|
| ~500 | **566 Hub index rows** before collapse, or **385 Hub cells**, or **335 card_index**, plus older 264/257 roots |
| 305 | Live public Merkle root **today** |
| 71 | This chat’s local Ollama loop only |
| 425 | Stablecoin **index** claim in lane docs — not live `root.json` |
| 1191 | **Stale** Hub triple on a Kaggle card (13 Sep). Live Hub GET today = **385** |

**Do not add these.** Adding them double-counts overlapping populations.

---

## 8. What “finished master live on GSPC” still is not

Inventory ≠ merge. Maple/M4 own rotating `root.json` / signing / HF publish.

This file is the **consolidation map**. It does **not**:
- rotate the live Merkle root
- republish 71 local eval cards onto councilof.ai
- claim 425 stablecoins MEASURED
- claim RunPod HSM custody

---

## 9. Owner actions that actually finish the merge

1. `export RUNPOD_API_KEY=…` so this lane can list/pull 3090 card dumps
2. Confirm which public number is canonical for “cards”: **305 root leaves** vs **335 card_index** vs **385 Hub cells** — they are three products
3. Maple: if local 71 eval cards should enter the public root, that is a **release**, not an M2 rewrite
4. HF/Kaggle tokens if private datasets exist beyond the 100 public ids

---

## 10. One-line honest state

**Live GSPC board: 22/23 axes measured. Live public root: 305 leaves. Live Hub census: 385 MEASURED cells. This Mac session: 71 eval receipts. GitHub org: ≥400 repos. HF: ≥100 public datasets. RunPod/Oracle: UNCHECKABLE. Not one number. Not done.**

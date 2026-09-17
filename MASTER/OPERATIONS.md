# OPERATIONS — running the master from a clean clone

This document is the **entry point for a stranger** who has just cloned this
repository and wants to do something useful without learning the whole tree.
Every command is copy-pasteable. Every output is reproducible.

## 0. Pre-flight

```bash
bash tools/bootstrap.sh --export         # shows what's available
eval "$(bash tools/bootstrap.sh --export)"  # exports REPO / OTS_BIN / PY
```

`tools/bootstrap.sh` locates `ots` (v0.7+) and a Python 3.11+ without
modifying the system. It honours `$OTS_BIN` and `$PY` if set. If `ots` is
missing, the bootstrap script exits non-zero and tells you to install it
via brew/apt/cargo.

```bash
python3 --version         # 3.11+
which git
git status --short        # clean tree expected
ls MASTER/                # should exist
```

If `MASTER/` is missing, this is the wrong branch. Switch to
`hermes/inspect-register-readiness`.

## 1. Verify the master (anyone, anywhere)

This script reads `MASTER/MASTER_FILES.json` and re-hashes every file. It
exits non-zero if any byte changed. **This is the only check that proves
the master is intact.**

```bash
python3 - << 'PY'
import json, hashlib
from pathlib import Path
mf = json.loads(Path('MASTER/MASTER_FILES.json').read_text())
bad = 0
for a in mf['files']:
    fp = Path('MASTER') / a['path']
    if not fp.exists():
        bad += 1; print('MISSING', a['path']); continue
    h = hashlib.sha256(fp.read_bytes()).hexdigest()
    if h != a['sha256']:
        bad += 1; print('MISMATCH', a['path'])
print(f'{len(mf["files"])} files, {bad} bad')
raise SystemExit(1 if bad else 0)
PY
```

Expected output: `4768 files, 0 bad` and exit 0.

## 2. Find one specific card

```bash
# a specific SWIFT bank row
grep -n 'HSBC' MASTER/04_corpora/SWIFT17_INDEX.jsonl
# a specific XRPL asset
grep -n 'RLUSD' MASTER/04_corpora/XRPL16_INDEX.jsonl
# a specific stablecoin
grep -n 'USDT' MASTER/04_corpora/STABLECOINS425_INDEX.jsonl
# a specific locally-signed eval card
ls MASTER/09_eval_signed/ | grep 'governance' | head
# an unsigned RunPod card body by run id
grep -lr '20260914T052852' MASTER/02_unsigned_pile/evidence_runpod_gspc_intake/ | head
```

## 3. Re-derive any structural number from the master

| number | command |
|---|---|
| total cards in catalog | `python3 -c "import json;print(len(json.load(open('MASTER/MASTER_FILES.json'))['files']))"` |
| structural integrity | see §1 |
| 425 arithmetic | `python3 -c "import json;d=json.load(open('MASTER/04_corpora/stablecoin425_index.json'));assert d['measured']+d['unmeasured']==d['universe'];print('OK',d)"` |
| 1513 bijection | `wc -l < MASTER/02_unsigned_pile/intake_v2.jsonl` must equal `find MASTER/02_unsigned_pile/evidence_runpod_gspc_intake -name card-unsigned.json \| wc -l` |
| merkle recompute | see §4 |
| publishability controls | `python3 -c "import json;p=json.load(open('MASTER/03_publishability/publishability_report.json'));print(p['control'])"` |

## 4. Recompute the Merkle root (1,513 leaves)

```bash
python3 - << 'PY'
import json, hashlib
from pathlib import Path
art = json.loads(Path('MASTER/02_unsigned_pile/unsigned_merkle_root.json').read_text())
# leaves sha256 of file bytes
leaves = [hashlib.sha256(p.read_bytes()).hexdigest()
          for p in sorted(Path('MASTER/02_unsigned_pile/evidence_runpod_gspc_intake').rglob('card-unsigned.json'))]
assert len(leaves) == art['leaf_count'], (len(leaves), art['leaf_count'])
def pair(layer):
    out = []
    for i in range(0, len(layer), 2):
        if i+1 < len(layer):
            out.append(hashlib.sha256((layer[i]+layer[i+1]).encode()).hexdigest())
        else:
            out.append(layer[i])
    return out
L = leaves[:]
while len(L) > 1:
    L = pair(L)
print('recomputed', L[0])
print('published ', art['merkle_root'])
assert L[0] == art['merkle_root'], 'mismatch'
print('OK')
PY
```

Expected: ends with `OK`.

## 5. Upgrade the OTS pending stamp (run from a host that CAN reach a calendar)

`alice.btc.calendar.opentimestamps.org` (HTTP 404 from this Mac but works
from a host that is not behind a corporate proxy).

```bash
# 5a — upgrade the unsigned-pile stamp
python3 scripts/upgrade_ots.py \
  --root-file MASTER/02_unsigned_pile/unsigned_merkle_root.json \
  --stamp-file MASTER/02_unsigned_pile/unsigned_merkle_root.json.ots

# 5b — upgrade the master-package stamp
python3 scripts/stamp_master_package.py

# 5c — verify
python3 -c "import ots;ots.verify('MASTER/02_unsigned_pile/unsigned_merkle_root.json','MASTER/02_unsigned_pile/unsigned_merkle_root.json.ots')"
```

Until `upgrade_ots.py` lands in `scripts/`, replace step 5a with:

```bash
curl -sS -X POST -H 'Content-Type: application/octet-stream' \
  --data-binary @<(python3 -c "import hashlib;print(hashlib.sha256(open('MASTER/02_unsigned_pile/unsigned_merkle_root.json','rb').read()).hexdigest(),end='')") \
  https://alice.btc.calendar.opentimestamps.org/submit > MASTER/02_unsigned_pile/unsigned_merkle_root.json.ots
python3 - << 'PY'
import ots, json
art = json.loads(open('MASTER/02_unsigned_pile/unsigned_merkle_root.json').read_text())
info = ots.Info(bytes.fromhex(art['merkle_root']))
ots.upgrade('MASTER/02_unsigned_pile/unsigned_merkle_root.json.ots')
PY
```

## 6. Add a new file to the master without breaking it

Adding a file is the **most common way to make the master stale.** The
pipeline below must run before any commit that adds a file. **Order matters**:
stamp first, then rebuild — the rebuild captures the post-stamp bytes so the
manifest records what was actually signed.

```bash
# 6a — place the file in the right section
cp /path/to/new.md MASTER/07_crosswalk/

# 6b — stamp first (so MASTER_PACKAGE.ots is for current bytes)
python3 scripts/stamp_master_package.py

# 6c — then rebuild (captures hashes of post-stamp bytes)
python3 scripts/rebuild_master_files.py

# 6d — verify everything is coherent
python3 scripts/selfcheck_master.py
# expected: "OK: 7/7 checks pass on 4774 files"

# 6e — commit
git add MASTER/ scripts/
git commit -m "add <description> — reindexed, re-stamped, verified"
```

If `selfcheck_master.py` fails on **step 6** (`MASTER_PACKAGE.json
package_sha matches MANIFEST.sha256 sha256`), the operator ran the steps
in the wrong order. Re-run `stamp_master_package.py` then
`rebuild_master_files.py`. The selfcheck exists precisely to catch this.

The three pipeline scripts are:
  - `scripts/stamp_master_package.py`  — anchors current bytes in OTS calendars
  - `scripts/rebuild_master_files.py` — reindexes sha256 of every file
  - `scripts/selfcheck_master.py`     — 7 assertions across the master

  ## 7. How stale is the OTS stamp?

  ```bash
  bash tools/stamp_age.sh
  # or:  make stamp-age
  ```

  Prints `ots_status`, `obtained_at`, current age in hours/days, and a
  plain-English hint:

  - `fresh (retry pointless)`            — <1h old
  - `recent (<24h, retry pointless)`     — 1–24h
  - `1-7d (calendar may have upgraded; worth a quick re-run)`  — 1–7d
  - `>7d (Bitcoin attestation likely ready; re-run scripts/upgrade_ots.py)` — >7d

  Also runs `ots info` on the current stamp so you can see the on-disk
  state without opening it yourself.

  ## 8. Verify the live board has not drifted from our snapshots

  ```bash
  python3 - << 'PY'
  import urllib.request, json
  for url in [
   'https://councilof.ai/api/gspc',
   'https://councilof.ai/root.json',
   'https://councilof.ai/signed/card_index.json',
   'https://councilof.ai/interop/root-witness-latest.json',
  ]:
   req = urllib.request.Request(url, headers={'User-Agent':'csoai-m2/1.0'})
   try:
       body = urllib.request.urlopen(req, timeout=20).read()
       d = json.loads(body)
       print(f'OK {url}  {len(body)} bytes')
   except Exception as e:
       print(f'FAIL {url}  {e}')
  PY
  ```

  Expected: 4 OK lines. If any fail, the snapshot is stale. Do **not** edit
  `MASTER/01_live/*` to match — re-fetch and re-stamp.

  ## 9. Owner-only actions

  | action | owner | what to do |
  |---|---|---|
  | sign unsigned RunPod cards with `card-attestation-1` | operator + HSM | follow `docs/operations/root-ceremony/NICK-RUNBOOK.md` (council-os repo) |
  | anchor the unsigned-pile Merkle root in Bitcoin | operator + reachable host | run `scripts/stamp_master_package.py` from a host that can reach alice.btc.calendar.opentimestamps.org |
  | deploy `MASTER/` to councilof.ai | operator | not yet wired; this doc is the deploy plan |
  | pay the live x402 paid doors | operator | grant CuaDriver Accessibility + Screen Recording + Chrome `Allow JS from Apple Events`, then I drive the click |

  ## 10. The audit (anyone)

  A complete audit reads three files:

  1. `MASTER/00_README_FIRST.md` — what is here and why.
  2. `MASTER/INDEX_OF_WHATS_NOT_HERE.md` — what is intentionally absent.
  3. `MASTER/MANIFEST.sha256` — every byte accounted for.

  Then run §1 (rehash) and `python3 scripts/selfcheck_master.py` (7
  assertions). If both exit 0 and the live §8 fetch is current, the master
  is sound for the moment it was produced.
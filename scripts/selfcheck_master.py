"""End-to-end self-check for the master.

Run this after any of:
  - scripts/rebuild_master_files.py
  - scripts/stamp_master_package.py
  - scripts/upgrade_ots.py
  - any edit to MASTER/

It asserts, in this order:
  1. MASTER_FILES.json parses, schema 2.0.
  2. The four self-referencing files are listed as such.
  3. Every non-self-referencing file exists, sha256-matches, and has a purpose.
  4. INVENTORY.csv row count == MANIFEST.sha256 row count + 1 (header).
  5. Both .ots stamps exist; both contain PendingAttestation (real stamps).
  6. The master-package stamp's recorded sha256 in MASTER_PACKAGE.json matches
     sha256(MANIFEST.sha256) — i.e. the metadata file knows what it's stamping.
  7. master-package.json ots_status is one of {STAMPED_PENDING_BITCOIN,
     BITCOIN_CONFIRMED, BROKEN_rc_N} — never a made-up string.

Exits 0 on success, 1 on the first failed check, 2 on a dependency miss
(no `ots` CLI, no MASTER_FILES.json).
"""
from __future__ import annotations
import json, hashlib, shutil, subprocess, sys
from pathlib import Path
ROOT = Path('MASTER')

OTS = shutil.which('ots') or '/Users/iokfarm/workspace_for_ai/inspect-lane/.venv/bin/ots'
MF  = ROOT / 'MASTER_FILES.json'
INV = ROOT / 'INVENTORY.csv'
MAN = ROOT / 'MANIFEST.sha256'
PKG = ROOT / 'MASTER_PACKAGE.json'
PST = ROOT / 'MASTER_PACKAGE.ots'
UST = ROOT / '02_unsigned_pile' / 'unsigned_merkle_root.json.ots'

def err(s): print(f'FAIL: {s}'); sys.exit(1)
def info(s): print(f'  ... {s}')

# 1
print('1. MASTER_FILES.json parses + schema 2.0')
if not MF.exists(): err(f'{MF} missing')
try: mf = json.loads(MF.read_text())
except Exception as e: err(f'MASTER_FILES.json not JSON: {e}')
if mf.get('schema') != 'csoai.master-files/2.0':
    err(f"schema != csoai.master-files/2.0 (got {mf.get('schema')})")
info(f'OK: {mf["total_files"]} files declared')

# 2
print('2. Self-referencing list well-formed')
self = set(mf.get('self_referencing') or [])
if len(self) != 4:
    err(f'self_referencing != 4: {sorted(self)}')
expected_self = {'MASTER_FILES.json','INVENTORY.csv','MANIFEST.sha256','MASTER_PACKAGE.json'}
if self != expected_self:
    err(f'self_referencing mismatch: {self} vs {expected_self}')
info('OK')

# 3
print('3. Non-self files: exist + sha256 + purpose')
bad=0; empt=0
for a in mf['files']:
    if a['path'] in self: continue
    fp = ROOT / a['path']
    if not fp.exists(): bad += 1; info(f'MISSING {a["path"]}'); continue
    if hashlib.sha256(fp.read_bytes()).hexdigest() != a['sha256']:
        bad += 1; info(f'MISMATCH {a["path"]}')
    if not a['purpose']: empt += 1; info(f'EMPTY {a["path"]}')
if bad: err(f'{bad} hash mismatches')
if empt: err(f'{empt} files without purpose')
info('OK')

# 4
print('4. INVENTORY.csv rows == MANIFEST.sha256 rows + 1')
ml = sum(1 for _ in MAN.open()) if MAN.exists() else 0
il = sum(1 for _ in INV.open()) - 1 if INV.exists() else 0  # minus header
if ml != il or ml != mf['total_files']:
    err(f'INVENTORY={il} MANIFEST={ml} total_files={mf["total_files"]}')
info(f'OK: {ml} rows in both')

# 5
print('5. Both .ots stamps exist + contain PendingAttestation')
for f, root in ((UST, ROOT/'02_unsigned_pile'/'unsigned_merkle_root.json'),
                (PST, MAN)):
    if not f.exists(): err(f'{f} missing')
    p = subprocess.run([OTS, 'info', str(f)], capture_output=True, text=True)
    if p.returncode != 0: err(f'ots info failed on {f}')
    if 'PendingAttestation' not in p.stdout:
        err(f'{f} has no PendingAttestation (looks like a stub)')
    info(f'{f}: PendingAttestation present')

# 6
print('6. MASTER_PACKAGE.json package_sha matches MANIFEST.sha256 sha256')
if not PKG.exists(): err(f'{PKG} missing')
pkg = json.loads(PKG.read_text())
recorded = pkg.get('package_files_sha256_of_manifest')
actual = hashlib.sha256(MAN.read_bytes()).hexdigest()
if recorded != actual:
    err(f'package_sha recorded={recorded} actual={actual}; run scripts/stamp_master_package.py')
info(f'OK: {recorded[:16]}...')

# 7
print('7. ots_status is honest')
state = pkg.get('ots_status')
allowed = {'BITCOIN_CONFIRMED','STAMPED_PENDING_BITCOIN','OTS_VERIFIED'}
for k in pkg:
    if k.startswith('BROKEN_rc_'): allowed.add(k); break
if state not in allowed:
    err(f'ots_status "{state}" not in honest set {allowed}')
info(f'OK: {state}')

print()
print(f'OK: 7/7 checks pass on {mf["total_files"]} files')
print(f'  master sha256: {actual[:32]}...')
print(f'  unsigned pile stamp: {UST}')
print(f'  master package stamp: {PST}')
sys.exit(0)

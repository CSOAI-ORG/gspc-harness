"""Rebuild MASTER_FILES.json from the on-disk MASTER/ tree.

Reads every file, sha256s it, classifies it (section/kind/purpose),
and writes:
  MASTER/MASTER_FILES.json   (machine-readable, schema 2.0)
  MASTER/INVENTORY.csv       (pipe-friendly)
  MASTER/MANIFEST.sha256     (canonical sha256sum format)

Idempotent. Safe to re-run after any add/remove. Does not touch OTS files
or stamp files — those are owned by scripts/stamp_master_package.py.

Self-referencing note: MASTER_FILES.json, INVENTORY.csv, MANIFEST.sha256,
and MASTER_PACKAGE.json contain their own future sha256 (or are derived from
one). They are listed as self_referencing and are not checked against
themselves — they are checked by re-running this script and comparing.

Branch guard: refuses to run on anything other than hermes/inspect-register-readiness.
Set SKIP_BRANCH_GUARD=1 to override (operator-only; for rebases or forensics).
"""
from __future__ import annotations
import json, hashlib, datetime, csv, os, subprocess, sys
from pathlib import Path
import shutil
ROOT = Path('MASTER')

# Branch guard: MASTER/ lives only on hermes/inspect-register-readiness.
# Skip with SKIP_BRANCH_GUARD=1 for rebases or forensic replays.
if not os.environ.get('SKIP_BRANCH_GUARD'):
    guard = subprocess.run(['bash', 'tools/branch_sync.sh'], capture_output=True, text=True)
    if guard.returncode != 0:
        print(guard.stderr.strip(), file=sys.stderr)
        sys.exit(2)

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def section_of(rel):
    for s in ['01_live','02_unsigned_pile','03_publishability','04_corpora','05_x402',
             '06_anchoring','07_crosswalk','08_blog','09_eval_signed']:
        if rel == s or rel.startswith(s + '/'): return s
    return '_top'

def kind_of(rel):
    base = rel.rsplit('/', 1)[-1]
    if base == 'card-unsigned.json':  return 'card-unsigned'
    if base == 'items.jsonl':         return 'items.jsonl'
    if base == 'run.json':            return 'run.json'
    if base.endswith('.ots'):         return 'ots-stamp'
    if base.endswith('.jsonl'):       return 'jsonl'
    if base.endswith('.json'):        return 'json'
    if base.endswith('.md'):          return 'md'
    if base.endswith('.py'):          return 'py'
    if base.endswith('.html'):        return 'html'
    if base.endswith('.yaml') or base.endswith('.yml'): return 'yaml'
    return 'other'

PURPOSE_BULK = {
    'card-unsigned': 'one of 1513 unsigned RunPod card bodies (mirror)',
    'items.jsonl':   'per-item evidence for one unsigned card (mirror)',
    'run.json':      'run-level metadata for one unsigned card (mirror)',
}

PURPOSE_PATH = {
    '00_README_FIRST.md':                            'orient the reader; the one read',
    'OPERATIONS.md':                                 'how to verify, upgrade OTS, add files, audit',
    'INDEX_OF_WHATS_NOT_HERE.md':                    'things this master deliberately does not carry',
    'MASTER_CATALOG.json':                           'machine-readable section map',
    'MASTER_FILES.json':                             'sha256 index of every file',
    'MASTER_PACKAGE.json':                           'package-level sha256 + OTS status',
    'MASTER_PACKAGE.ots':                            'OpenTimestamps stamp over the master package (pending)',
    '02_unsigned_pile/unsigned_merkle_root.json':   'Merkle root over the 1513 unsigned bodies',
    '02_unsigned_pile/unsigned_merkle_root.json.ots': 'pending OpenTimestamps stamp',
    '02_unsigned_pile/intake_v2.jsonl':              '1513-row bijection-proven index',
    '02_unsigned_pile/evidence_runpod_gspc_intake/intake_original_stale_112rows.jsonl':
        'stale published intake.jsonl (112 rows, not 1513) — kept for diff only',
    '02_unsigned_pile/RUNPOD_INTAKE_INDEX.jsonl':    'earlier 1513-row path census (pre-merkle)',
    '02_unsigned_pile/RUNPOD_INTAKE_INDEX_SUMMARY.json':'summary of the 1513-row path census',
    '02_unsigned_pile/RUNPOD_INTAKE_CENSUS.md':     'human account of the 1513 unsigned pile',
    '03_publishability/publishability_report.json':  '5 publishability checks + failing control',
    '04_corpora/HASH_OVERLAP_CENSUS.md':            'intersection of intake / root / card_index (all 0)',
    '04_corpora/SWIFT17_INDEX.jsonl':               '17 SWIFT-bank rows, all UNMEASURED',
    '04_corpora/XRPL16_INDEX.jsonl':                '16 XRPL assets, 11 SIGNED / 5 UNSIGNED',
    '04_corpora/STABLECOINS425_INDEX.jsonl':        '425 stablecoin rows from councilof.ai/stablecoins/',
    '04_corpora/MILL_JOBS_STAGING_INDEX.jsonl':     '428 unsigned MILL jobs',
    '04_corpora/swift17_gap_note.json':             'one-sentence SWIFT-17 gap note + provenance caveat',
    '04_corpora/stablecoin425_index.json':          'arithmetic-checked 425 universe summary',
    '04_corpora/SWIFT_XRPL_425_COBOL.md':           'reconciliation of SWIFT/XRPL/425/COBOL indices',
    '05_x402/X402_BAZAAR_CENSUS.md':                'human summary of x402 bazaar census',
    '05_x402/X402_CENSUS_SNAPSHOT.json':            'bazaar census snapshot',
    '05_x402/X402_CONFORMANCE_SUMMARY.json':        'bazaar conformance summary',
    '05_x402/X402_RLUSD_402.json':                  'frozen 402 response for RLUSD evidence door',
    '05_x402/X402_SETTLEMENT_SUMMARY.json':         'Base-receipt settlement verification summary',
    '05_x402/X402_11_DOORS_PROBE.md':               'probe of the 11 x402 catalog doors',
    '06_anchoring/INTEROP_REPORT.md':               'interop report covering signing/anchoring/settle',
    '06_anchoring/ETH_RECEIPTS_ANNEX.md':           'EIP-712/x402 receipt annex',
    '06_anchoring/PUBLISHED_MILL_GOVERNANCE_e9bc92b7.json':
        'one published signed mill card, frozen from live gspc-verify',
    '01_live/LIVE_RAIL_PROBE.md':                   'browser + urllib probes of councilof.ai rails',
    '01_live/ROOT_WITNESS_LATEST.json':             'frozen witness sidecar (Rekor/OTS/EAS/XRPL state)',
    '01_live/ANCHORING_LIVE.md':                   'human account of live anchoring state',
    '07_crosswalk/CROSSWALK_SCAFFOLD.md':          'crosswalk scaffold: goals, evidence schema, sources tree',
    '07_crosswalk/TASKS_REPORT.md':                'one-page report on Tasks 1-5 + crosswalk',
    '07_crosswalk/goals_crosswalk.json':           '14 stable goals + 9 source mappings',
    '07_crosswalk/crosswalk_status.json':          'source status snapshot + Frozen->Fluid demo',
}

def purpose_of(rel, kind):
    if rel in PURPOSE_PATH: return PURPOSE_PATH[rel]
    if rel.startswith('07_crosswalk/sources/'): return 'honest source stub; carries open_questions, no fabricated URL'
    if rel.startswith('08_blog/'):              return 'blog draft; outreach material, not live evidence'
    if rel.startswith('09_eval_signed/SIGNED_'): return 'locally-signed eval card (Ollama qwen2.5-coder:1.5b, this lane)'
    if rel == 'CHEATSHEET.txt':                  return 'one-page operator workflow for the master'
    if rel == 'RESPONSE-TO-FULL-OWNERSHIP.md':     return 'straight answer to the operator on what blocks full ownership'
    if rel == 'RESPONSE-TO-AUTOMATE-ALL.md':      return 'straight answer to the operator on automating regulator outreach end-to-end'
    if rel == '07_crosswalk/REGULATOR_DOSSIER_TEMPLATE.md':
        return 'regulator dossier template; draft for human review, NOT signed by the lane'
    if rel == 'END-OF-SESSION-17Sep2026.md':         return 'end-of-session state for the operator; honest summary of what the lane did and did not do'
    if rel.startswith('TUI_OBS_17Sep2026/'):
        return 'OBSERVER-mode artifact; honest measurement of what an anonymous reader sees vs what we publish'
    if rel.startswith('TUI_REVENUE_BLOCKERS_17Sep2026/'):
        return 'honest list of operator-owned blocks that gate mass-outreach / sales / revenue work; not a fabricated pipeline'
    if rel.startswith('TUI_OBS2_17Sep2026/'):
        return 'OBSERVER-2 per-sweep diff; named defects measured (homepage github links, fix-vs-served, worst card, HF readback)'
    if rel.startswith('TUI_M4_RECON_17Sep2026/'):
        return 'M4 Round 2 verification from M2 OBSERVER lane; honestly report what is and is not on this Mac'
    if rel.startswith('cold_start_surfaces/'):
        return 'plain machine client probe of councilof.ai surfaces; not the operator\'s 21-of-21 claim'
    if rel == 'REPO_MAP.md':
        return 'branch + remote map for the master'
    if rel == 'KEYS_NEEDED.md':                  return 'index of secrets and credentials the lane touches'
    if rel == '09_eval_signed/MEASUREMENT_CATALOG.json':
        return 'catalog of every locally-signed eval card'
    return PURPOSE_BULK.get(kind, '')

artifacts=[]
for f in sorted(ROOT.rglob('*')):
    if f.is_dir(): continue
    rel = str(f.relative_to(ROOT))
    artifacts.append({
        'path': rel,
        'section': section_of(rel),
        'kind': kind_of(rel),
        'bytes': f.stat().st_size,
        'sha256': sha(f),
        'purpose': purpose_of(rel, kind_of(rel)),
    })

m = {
    'schema': 'csoai.master-files/2.0',
    'as_of': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'root': 'MASTER',
    'total_files': len(artifacts),
    'total_bytes': sum(a['bytes'] for a in artifacts),
    'sections': sorted({a['section'] for a in artifacts}),
    'by_section': {
        s: {'files': sum(1 for a in artifacts if a['section']==s),
            'bytes': sum(a['bytes'] for a in artifacts if a['section']==s)}
        for s in sorted({a['section'] for a in artifacts})
    },
    'self_referencing': ['MASTER_FILES.json', 'INVENTORY.csv', 'MANIFEST.sha256', 'MASTER_PACKAGE.json'],
    'self_referencing_note': 'These four files cannot be self-verified because they contain their own future hash or are derived from one. Verify them by re-running this script and comparing its output bytes to its declared sha256.',
    'files': artifacts,
}
Path('MASTER/MASTER_FILES.json').write_text(json.dumps(m, indent=2))

with open('MASTER/INVENTORY.csv', 'w', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['path','section','kind','bytes','sha256','purpose'])
    for a in artifacts:
        w.writerow([a['path'],a['section'],a['kind'],a['bytes'],a['sha256'],a['purpose']])

with open('MASTER/MANIFEST.sha256', 'w') as fh:
    for a in artifacts:
        fh.write(f"{a['sha256']}  {a['path']}\n")

# bump package hash
import hashlib as _h
PACKAGE_SHA = _h.sha256(Path('MASTER/MANIFEST.sha256').read_bytes()).hexdigest()
# Preserve the master-package OTS state across rebuilds. The rebuild
# script does NOT know the OTS state; only stamp_master_package.py
# and upgrade_ots.py know that. Reading it from the existing
# MASTER_PACKAGE.json is the cheapest honest preservation.
PRESERVED = {}
PKG = Path('MASTER/MASTER_PACKAGE.json')
if PKG.exists():
    try:
        PRESERVED = json.loads(PKG.read_text())
    except Exception:
        PRESERVED = {}

pkg = {
    'schema': 'csoai.master-package/1.0',
    'as_of': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'package_path': 'MASTER/',
    'package_files_count': None,  # filled in below
    'package_files_sha256_of_manifest': PACKAGE_SHA,
    'ots_status': PRESERVED.get('ots_status', 'STAMPED_PENDING_BITCOIN'),
    'ots_file': 'MASTER_PACKAGE.ots',
    'ots_source': PRESERVED.get('ots_source', 'ots v0.7.2 CLI via scripts/upgrade_ots.py'),
    'ots_obtained_at': PRESERVED.get('ots_obtained_at', datetime.datetime.now(datetime.timezone.utc).isoformat()),
    'not_a_signature': 'This package hash records when the master existed as bytes. Not a signature, not a witness, not a certification. Pending OTS is not Bitcoin confirmation.',
}
Path('MASTER/MASTER_PACKAGE.json').write_text(json.dumps(pkg, indent=2))

empty = sum(1 for a in artifacts if not a['purpose'])
self_ref = set(m.get('self_referencing') or [])
non_self_empty = sum(1 for a in artifacts if not a['purpose'] and a['path'] not in self_ref)
print(f'files {len(artifacts)}  empty-purpose {empty}  non-self-empty {non_self_empty}  package_sha {PACKAGE_SHA}')
raise SystemExit(1 if non_self_empty else 0)

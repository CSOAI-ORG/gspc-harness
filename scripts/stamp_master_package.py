"""Refresh the master-package OpenTimestamps stamp.

Delegates to scripts/upgrade_ots.py with --root-file MASTER/MANIFEST.sha256.
Reads the stamp state afterwards and writes MASTER_PACKAGE.json with the
honest status (STAMPED_PENDING_BITCOIN until calendar attestations upgrade
to a Bitcoin block header).

The script is idempotent: re-runnable any time, never fakes a Bitcoin
attestation.
"""
from __future__ import annotations
import json, hashlib, datetime, subprocess, sys
from pathlib import Path

REPO = Path('.')
MAN  = REPO / 'MASTER' / 'MANIFEST.sha256'
STAMP = REPO / 'MASTER' / 'MASTER_PACKAGE.ots'
META  = REPO / 'MASTER' / 'MASTER_PACKAGE.json'

def find_ots():
    import shutil
    return shutil.which('ots')

def main():
    h = hashlib.sha256(MAN.read_bytes()).hexdigest()
    print('master package sha256', h)

    ots = find_ots()
    if not ots:
        print('FAIL: ots CLI not on PATH. Install with: brew install opentimestamps')
        sys.exit(2)

    # Delegate to upgrade_ots.py for the actual stamp (--fresh because the
    # master manifest changes every rebuild, so a pending stamp from a
    # previous build is stale even if its own bytes verify).
    # Pre-delete the existing stamp so the re-stamp path is taken cleanly
    # (upgrade_ots.py refuses to run if stamp file is absent).
    if STAMP.exists():
        STAMP.unlink()
    proc = subprocess.run(
        [sys.executable, 'scripts/upgrade_ots.py', '--fresh',
         '--root-file', str(MAN), '--stamp-file', str(STAMP), '--ots', ots],
        capture_output=True, text=True
    )
    out = (proc.stdout or '') + (proc.stderr or '')
    print(out)

    # Determine state honestly. Source of truth: `ots verify`'s exit code
    # alone. We do NOT parse substring output.
    #   rc 0 = verified end-to-end (Bitcoin confirmed)
    #   rc 1 = pending attestations (still valid; needs Bitcoin block)
    #   rc 2+ = broken (re-stamp)
    verify = subprocess.run([ots, 'verify', '-f', str(MAN), str(STAMP)],
                            capture_output=True, text=True)
    rc = verify.returncode
    if rc == 0:
        state = 'BITCOIN_CONFIRMED'
    elif rc == 1:
        state = 'STAMPED_PENDING_BITCOIN'
    else:
        state = f'BROKEN_rc_{rc}'

    art = {
        'schema': 'csoai.master-package/1.0',
        'as_of': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'package_path': 'MASTER/',
        'package_files_count': None,  # filled in below
        'package_files_sha256_of_manifest': h,
        'ots_status': state,
        'ots_file': 'MASTER_PACKAGE.ots',
        'ots_source': 'ots v0.7.2 CLI via scripts/upgrade_ots.py',
        'not_a_signature': 'This package hash records when the master existed as bytes. Not a signature, not a witness, not a certification. Pending OTS is not Bitcoin confirmation.',
    }
    # Try to fill total_files from MASTER_FILES.json if present
    try:
        art['package_files_count'] = json.loads((REPO/'MASTER'/'MASTER_FILES.json').read_text()).get('total_files')
    except Exception:
        pass

    META.write_text(json.dumps(art, indent=2))
    print(f'wrote {META}  ots_status={state}')

if __name__ == '__main__':
    main()

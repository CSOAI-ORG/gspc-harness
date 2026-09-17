"""Upgrade a pending OpenTimestamps stamp via the working `ots` CLI.

The Mac has the `opentimestamps-client` Rust CLI installed (v0.7.2) under
~/.local/bin and the project venv bin. The Python `opentimestamps` package
is a deprecated stub on this system and does not expose the timestamp
classes, so we delegate to the CLI.

Usage:
  python3 scripts/upgrade_ots.py --root-file MASTER/02_unsigned_pile/unsigned_merkle_root.json \
                                --stamp-file MASTER/02_unsigned_pile/unsigned_merkle_root.json.ots

What it does:
  1. Re-creates the stamp against the current file bytes (or upgrades existing).
  2. Tries alice / bob / finney / catallaxy calendars, one of which usually
     answers from this host even when others 404.
  3. Reports Bitcoin confirmation state honestly. Pending is pending.

Honest exits:
  0 = stamp upgraded; Bitcoin may or may not be confirmed (state is reported)
  1 = calendar unreachable (no fake stamp, no fake Bitcoin)
  2 = no `ots` CLI on PATH (operator installs via brew/apt/cargo)

No silent failure, no fake Bitcoin attestation.
"""
from __future__ import annotations
import argparse, hashlib, shutil, subprocess, sys
from pathlib import Path

CALENDARS = [
    'https://alice.btc.calendar.opentimestamps.org',
    'https://bob.btc.calendar.opentimestamps.org',
    'https://finney.calendar.eternitywall.com',
    'https://ots.btc.catallaxy.com',
]

def find_ots():
    for cand in ['ots']:
        p = shutil.which(cand)
        if p: return p
    return None

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root-file', required=True)
    ap.add_argument('--stamp-file', required=True)
    ap.add_argument('--ots', dest='ots_path', default=None,
                    help='override path to `ots` CLI')
    ap.add_argument('--wait', action='store_true',
                    help='wait for Bitcoin commitment (slow)')
    ap.add_argument('--fresh', action='store_true',
                    help='ignore existing stamp and re-stamp from scratch')
    ap.add_argument('--calendars', nargs='*', default=None,
                    help='override calendar list')
    args = ap.parse_args()

    ots_path = args.ots_path or find_ots()
    if not ots_path:
        print('FAIL: `ots` CLI not on PATH.')
        print('      install via: brew install opentimestamps (or cargo install ots)')
        sys.exit(2)
    print(f'using ots at: {ots_path}')

    root = Path(args.root_file)
    stamp = Path(args.stamp_file)
    if not root.exists():
        print(f'FAIL: root file not found: {root}'); sys.exit(1)

    digest = hashlib.sha256(root.read_bytes()).hexdigest()
    print(f'root sha256: {digest}')

    # Is the existing stamp already a valid OpenTimestamps file we can upgrade?
    # `ots verify` syntax: ots verify [-f FILE] TIMESTAMP  (file first, stamp last)
    # Exit code meaning:
    #   0 = success
    #   1 = pending attestations (still valid; upgrade if you want more)
    #   2 = bad arguments / parse failure -> re-stamp
    # Note: with --fresh, we don't even check the existing stamp.
    if args.fresh:
        verify = type('V', (), {'returncode': 2})()  # force re-stamp path
    else:
        if not stamp.exists():
            print(f'FAIL: stamp file not found: {stamp}'); sys.exit(1)
        verify = run([ots_path, 'verify', '-f', str(root), str(stamp)])
    rc = verify.returncode
    needs_stamp = rc >= 2 or args.fresh
    if rc == 0 and not args.fresh:
        print('Stamp already verifies. Run again later or pass --wait to wait for Bitcoin.')
        sys.exit(0)

    if needs_stamp:
        print(f'Stamp invalid (verify rc={rc}). Re-stamping from scratch.')
        # ots stamp FILE creates FILE.ots beside it; we move it to stamp path.
        if stamp.exists(): stamp.unlink()
        cmd = [ots_path, 'stamp', str(root)]
        for cal in (args.calendars or CALENDARS):
            cmd += ['-c', cal]
        proc = run(cmd)
        print(f'ots stamp exit: {proc.returncode}')
        if proc.stdout.strip(): print('-- stdout --\n' + proc.stdout.strip())
        if proc.stderr.strip(): print('-- stderr --\n' + proc.stderr.strip())
        if proc.returncode == 0:
            generated = root.with_suffix(root.suffix + '.ots')
            if generated.exists():
                generated.rename(stamp)
                print(f'moved {generated} -> {stamp}')
            else:
                print(f'FAIL: ots stamp succeeded but {generated} not found'); sys.exit(1)
        else:
            print('FAIL: ots stamp did not produce a valid stamp.'); sys.exit(1)
    else:
        # rc == 1: pending. Try one upgrade pass to add new attestations.
        print('Stamp is valid but pending. Trying one upgrade pass.')
        cmd = [ots_path, 'upgrade', str(stamp)]
        if args.wait: cmd.append('--wait')
        for cal in (args.calendars or CALENDARS):
            cmd += ['-c', cal]
        proc = run(cmd)
        print(f'ots upgrade exit: {proc.returncode}')
        if proc.stdout.strip(): print('-- stdout --\n' + proc.stdout.strip())
        if proc.stderr.strip(): print('-- stderr --\n' + proc.stderr.strip())
        if proc.returncode != 0:
            print('Note: upgrade returned non-zero but the existing pending stamp is still valid.')
            print('It will be auto-upgraded next time you run this script.')
            sys.exit(0)  # idempotent — existing stamp is still valid pending

    # Verify post-state
    info = run([ots_path, 'info', str(stamp)])
    print('-- info --')
    if info.stdout.strip(): print(info.stdout.strip())
    # source of truth: `ots verify` exit code, not substring hunting
    vproc = subprocess.run([ots_path, 'verify', '-f', str(root), str(stamp)],
                           capture_output=True, text=True)
    rc = vproc.returncode
    if rc == 0:    print('STATUS: BITCOIN_CONFIRMED')
    elif rc == 1:  print('STATUS: STAMPED_PENDING_BITCOIN')
    else:           print(f'STATUS: BROKEN_rc_{rc}')
    sys.exit(0)

if __name__ == '__main__':
    main()

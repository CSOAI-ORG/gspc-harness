#!/usr/bin/env bash
# tools/bootstrap.sh — resolve the runtime CSOAI scripts need before they run.
#
# Usage:
#   bash tools/bootstrap.sh             # prints PATH + interpreter info
#   eval "$(bash tools/bootstrap.sh)"   # exports OTS_BIN, PY, REPO into your shell
#
# What it does:
#   - Locates a working `ots` CLI (v0.7+). Order: $OTS_BIN > $(which ots) > common install paths.
#   - Locates a working Python 3.11+ with the project on sys.path (or pip installable).
#   - Exports OTS_BIN, PY, REPO so the three pipeline scripts can find them.
#
# What it does NOT do:
#   - Does not modify the system. Does not install packages. Does not git pull.
#   - Does not write to MASTER/.
#
# This is an audit + setup helper, not an installer. Install the `ots` CLI
# separately with one of:
#   brew install opentimestamps         # macOS / Linuxbrew
#   apt install opentimestamps-client  # Debian/Ubuntu if packaged
#   cargo install opentimestamps-client
set -euo pipefail

# Locate the repo root (the dir containing MASTER/)
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export REPO

# Locate the `ots` CLI
locate_ots() {
  if [[ -n "${OTS_BIN:-}" && -x "$OTS_BIN" ]]; then
    echo "$OTS_BIN"; return 0
  fi
  if command -v ots >/dev/null 2>&1; then
    command -v ots; return 0
  fi
  for cand in \
    /usr/local/bin/ots \
    /opt/homebrew/bin/ots \
    /usr/bin/ots \
    "$REPO/../.venv/bin/ots" \
    "$HOME/.cargo/bin/ots"; do
    [[ -x "$cand" ]] && { echo "$cand"; return 0; }
  done
  return 1
}
if OTS_BIN="$(locate_ots)"; then
  OTS_VERSION="$("$OTS_BIN" --version 2>/dev/null || echo unknown)"
else
  OTS_VERSION="missing"
fi
export OTS_BIN

# Locate a working Python 3.11+
PY="${PY:-}"
if [[ -z "$PY" ]]; then
  for cand in python3.11 python3.12 python3 python; do
    if command -v "$cand" >/dev/null 2>&1; then
      v="$("$cand" -c 'import sys;print(sys.version_info.major,sys.version_info.minor)' 2>/dev/null || echo '')"
      if [[ "$v" == "3 11" || "$v" == "3 12" || "$v" == "3 13" ]]; then
        PY="$(command -v "$cand")"; break
      fi
    fi
  done
fi
[[ -z "$PY" ]] && { echo "bootstrap: no python3 found" >&2; exit 1; }
export PY

# Echo for the eval-case AND the human-case.
# When sourced via eval, the user gets OTS_BIN/PY/REPO in their shell.
# When run directly, they get the same info printed to stdout.
if [[ "${1:-}" == "--export" ]]; then
  # emit only the export lines (suitable for `eval`)
  echo "export REPO='$REPO'"
  echo "export OTS_BIN='$OTS_BIN'"
  echo "export OTS_VERSION='$OTS_VERSION'"
  echo "export PY='$PY'"
  exit 0
fi
cat <<EOF
# CSOAI bootstrap resolved:
#   REPO    = $REPO
#   OTS_BIN = $OTS_BIN  (version: $OTS_VERSION)
#   PY      = $PY
#
# Re-run with:  eval "\$(bash $REPO/tools/bootstrap.sh --export)"
EOF

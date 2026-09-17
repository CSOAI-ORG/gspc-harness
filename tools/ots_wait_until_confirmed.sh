#!/usr/bin/env bash
# tools/ots_wait_until_confirmed.sh — poll the OTS stamp until Bitcoin
# confirmation arrives, or until a deadline expires.
#
# Usage:
#   bash tools/ots_wait_until_confirmed.sh --root MASTER/MANIFEST.sha256 \
#                                             --stamp MASTER/MASTER_PACKAGE.ots
#   bash tools/ots_wait_until_confirmed.sh --root MASTER/02_unsigned_pile/unsigned_merkle_root.json \
#                                             --stamp MASTER/02_unsigned_pile/unsigned_merkle_root.json.ots
#   bash tools/ots_wait_until_confirmed.sh --timeout 600     # default 3600 (1h)
#   bash tools/ots_wait_until_confirmed.sh --interval 30     # default 60 (poll every 60s)
#
# Exits:
#   0 = BITCOIN_CONFIRMED before timeout (the OTS proof was upgraded)
#   1 = timed out (still STAMPED_PENDING_BITCOIN or worse)
#   2 = ots CLI not on PATH / stamp file missing / root file missing

set -euo pipefail
OTS_BIN="${OTS_BIN:-$(command -v ots || true)}"
ROOT_FILE=""
STAMP_FILE=""
TIMEOUT=3600
INTERVAL=60

while [[ $# -gt 0 ]]; do
  case "$1" in
    --root)     ROOT_FILE="$2"; shift 2 ;;
    --stamp)    STAMP_FILE="$2"; shift 2 ;;
    --timeout)  TIMEOUT="$2"; shift 2 ;;
    --interval) INTERVAL="$2"; shift 2 ;;
    -h|--help)
      sed -n '2,12p' "$0"; exit 0 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

if [[ -z "$OTS_BIN" || ! -x "$OTS_BIN" ]]; then
  echo "FAIL: ots CLI not on PATH. brew install opentimestamps" >&2
  exit 2
fi
if [[ -z "$ROOT_FILE" || ! -f "$ROOT_FILE" ]]; then
  echo "FAIL: --root file missing: $ROOT_FILE" >&2
  exit 2
fi
if [[ -z "$STAMP_FILE" || ! -f "$STAMP_FILE" ]]; then
  echo "FAIL: --stamp file missing: $STAMP_FILE" >&2
  exit 2
fi

deadline=$(( $(date +%s) + TIMEOUT ))
elapsed=0
echo "Polling ${STAMP_FILE} against ${ROOT_FILE} every ${INTERVAL}s (timeout ${TIMEOUT}s)..."
echo

while :; do
  rc=0
  "$OTS_BIN" verify -f "$ROOT_FILE" "$STAMP_FILE" >/dev/null 2>&1 || rc=$?
  now=$(date -u +%H:%M:%S)
  case "$rc" in
    0)
      echo "[$now] Bitcoin confirmed."
      echo
      echo "=== ots info ==="
      "$OTS_BIN" info "$STAMP_FILE" | tail -20
      exit 0
      ;;
    1)
      echo "[$now] still pending (elapsed ${elapsed}s / ${TIMEOUT}s)"
      ;;
    *)
      echo "[$now] BROKEN rc=$rc (elapsed ${elapsed}s)" >&2
      exit 1
      ;;
  esac
  elapsed=$(( elapsed + INTERVAL ))
  if (( elapsed >= TIMEOUT )); then
    echo "TIMEOUT: stamp still pending after ${TIMEOUT}s"
    echo "Hint: re-run later, or run scripts/upgrade_ots.py manually"
    exit 1
  fi
  sleep "$INTERVAL"
done

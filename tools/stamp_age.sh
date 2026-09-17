#!/usr/bin/env bash
# tools/stamp_age.sh — print how old the current OTS stamp is.
#
# Exits 0 always (informational). Useful operator hint:
#   - "0h"         : stamp is fresh, no action
#   - "<24h"       : stamp is recent, no urgency
#   - "1-7d"       : stamp might have been upgraded by calendars; worth re-stamping
#   - ">7d"        : definitely worth re-stamping; Bitcoin attestation may have arrived
#
# Reads MASTER/MASTER_PACKAGE.json (ots_obtained_at).
# Falls back to the master's mtime if ots_obtained_at is missing.

set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PKG="$REPO/MASTER/MASTER_PACKAGE.json"
STAMP="$REPO/MASTER/MASTER_PACKAGE.ots"
OTS_BIN="${OTS_BIN:-$(command -v ots || true)}"

if [[ ! -f "$PKG" ]]; then
  echo "stamp_age: $PKG not found" >&2
  exit 0
fi

obt="$(python3 -c "import json;d=json.load(open('$PKG'));print(d.get('ots_obtained_at') or d.get('as_of') or '')")"
if [[ -z "$obt" ]]; then
  obt="$(stat -f%Sm -t '%Y-%m-%dT%H:%M:%SZ' "$PKG")"
fi

now_epoch="$(date -u +%s)"
obt_epoch="$(date -u -j -f '%Y-%m-%dT%H:%M:%S' "${obt%.*}" +%s 2>/dev/null \
             || date -u -d "$obt" +%s 2>/dev/null \
             || echo 0)"
if [[ "$obt_epoch" -le 0 ]]; then
  echo "stamp_age: could not parse ots_obtained_at='$obt'" >&2
  exit 0
fi

age_sec=$(( now_epoch - obt_epoch ))
age_hr=$(( age_sec / 3600 ))
age_day=$(( age_sec / 86400 ))

status="$(python3 -c "import json;d=json.load(open('$PKG'));print(d.get('ots_status') or 'UNKNOWN')")"
hint="recent"
if   (( age_sec < 3600 ));  then hint="fresh (retry pointless)"
elif (( age_sec < 86400 )); then hint="recent (<24h, retry pointless)"
elif (( age_day < 7   ));   then hint="1-7d (calendar may have upgraded; worth a quick re-run)"
else                              hint=">7d (Bitcoin attestation likely ready; re-run scripts/upgrade_ots.py)"
fi

echo "ots_status:  $status"
echo "obtained_at: $obt"
echo "age:         ${age_hr}h (${age_day}d)"
echo "hint:        $hint"

# Live check: try to upgrade and print whether anything moved
if [[ -x "${OTS_BIN:-/nonexistent}" && -f "$STAMP" ]]; then
  echo
  echo "live upgrade probe (ots upgrade):"
  "$OTS_BIN" info "$STAMP" 2>&1 | head -3
fi

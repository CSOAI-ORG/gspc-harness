#!/usr/bin/env bash
# tools/both.sh — one health verdict for this machine.
#
# Two independent checks must both be green for the master to be operable:
#
#   1. ESTATE STATE   scripts/hermes-align.sh
#      "Is the operator's machine healthy?"  env parse, OAuth shadowing,
#      reasoning level, master branch protection, cron jobs.
#
#   2. MASTER STATE   scripts/selfcheck_master.py
#      "Is the master artifact healthy?"     sha256s match, stamps are real
#      OpenTimestamps proofs, package hash matches what was stamped.
#
# Run this at the start of any work session. Pass --apply to hermes-align if
# the estate check fails on something the script can fix safely.
#
# Exits:
#   0 = both green
#   1 = estate check failed (run with --apply, or escalate to owner)
#   2 = master check failed (run `make verify`)
#   3 = both failed

set -uo pipefail
APPLY=0
for a in "$@"; do
  case "$a" in
    --apply) APPLY=1 ;;
    -h|--help) sed -n '1,30p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
  esac
done

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HERMES_ARGS=""
[[ "$APPLY" = "1" ]] && HERMES_ARGS="--apply"

cd "$REPO"

ESTATE_RC=0
ESTATE_OUT=$(bash scripts/hermes-align.sh --repo=. $HERMES_ARGS 2>&1)
ESTATE_RC=$?
echo "$ESTATE_OUT" | tail -25
printf '%s\n' '============================================================'
printf '%s\n' '  ESTATE STATE     (hermes-align.sh)'
printf '%s\n' '============================================================'

echo "$ESTATE_OUT" | tail -25

echo
echo "============================================================"
echo "  MASTER STATE     (make verify)"
echo "============================================================"
MASTER_RC=0
MASTER_OUT=$(make verify 2>&1)
MASTER_RC=$?
echo "$MASTER_OUT" | tail -15

echo
echo "============================================================"
echo "  VERDICT"
echo "============================================================"
if (( ESTATE_RC == 0 )) && (( MASTER_RC == 0 )); then
  echo "  BOTH GREEN. master is operable."
  exit 0
fi
if (( ESTATE_RC != 0 )) && (( MASTER_RC != 0 )); then
  echo "  BOTH FAILED. estate=$ESTATE_RC master=$MASTER_RC"
  exit 3
fi
if (( ESTATE_RC != 0 )); then
  echo "  ESTATE only.  re-run with --apply to fix what is safely fixable; the rest is the owner's."
  exit 1
fi
echo "  MASTER only.  re-run make rebuild then make verify."
exit 2

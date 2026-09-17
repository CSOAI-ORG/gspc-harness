#!/usr/bin/env bash
# scripts/ops/gated-deploy.sh — the gate every loop passes through.
#
# Why this exists. On 17 Sep 2026 the operator piped preflight through grep
# twice, which replaced the script's exit code with grep's, so && saw success
# and deployed over a red gate. Both deploys were safe by luck. The wrapper
# captures the gate result BEFORE printing anything and refuses to deploy
# when the gate is non-zero.
#
# What it does. Wraps an arbitrary deploy command such that:
#   1. The preflight command is run and its exit code is captured into a
#      variable BEFORE any | grep | tail | head rewrites $?. This is the
#      single change that makes piping safe.
#   2. A second check ensures the build carries at least as many correction
#      rows as the live surface. Today that meant refusing to ship a build
#      that removed a correction production already served.
#   3. The deploy command runs only if both gates pass. Its stdout/stderr is
#      streamed through unchanged so the operator still sees it.
#
# Usage:
#   bash scripts/ops/gated-deploy.sh --preflight "<cmd>" --deploy "<cmd>" \
#        [--min-corrections <int>] [--live <path>]
#
# Exits:
#   0  both gates passed, deploy ran
#   2  preflight failed
#   3  corrections count regressed vs live
#   4  deploy itself failed
set -uo pipefail

PREFLIGHT=""
DEPLOY=""
MIN_CORRECTIONS=0
LIVE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --preflight) PREFLIGHT="$2"; shift 2 ;;
    --deploy)    DEPLOY="$2"; shift 2 ;;
    --min-corrections) MIN_CORRECTIONS="$2"; shift 2 ;;
    --live)      LIVE="$2"; shift 2 ;;
    -h|--help) sed -n '1,15p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

if [[ -z "$PREFLIGHT" || -z "$DEPLOY" ]]; then
  echo "FAIL: --preflight and --deploy are required" >&2
  exit 2
fi

# Step 1: preflight. Capture exit code into a variable BEFORE any pipelining.
echo ">> preflight: $PREFLIGHT"
PRE_RC=0
eval "$PREFLIGHT" > /tmp/gated-preflight.out 2>&1 || PRE_RC=$?
echo ">> preflight exit: $PRE_RC"
if (( PRE_RC != 0 )); then
  echo "FAIL: preflight rc=$PRE_RC; refusing to deploy."
  cat /tmp/gated-preflight.out | sed 's/^/    /'
  exit 2
fi

# Step 2: corrections-count gate. The build carries as many correction rows as
# the live surface; if not, refuse. We never ship a deploy that removes a
# correction production already serves.
if (( MIN_CORRECTIONS > 0 )); then
  echo ">> corrections gate: build must carry >= $MIN_CORRECTIONS rows; live=$LIVE"
  if [[ -z "$LIVE" ]]; then
    echo "FAIL: --live required when --min-corrections is set" >&2
    exit 2
  fi
  if [[ ! -f "$LIVE" ]]; then
    echo "FAIL: live corrections file missing: $LIVE" >&2
    exit 3
  fi
  # Derive build count from the same path the deploy will use. We don't ship
  # a count the build doesn't carry.
  BUILD_COUNT=$(grep -c '^|' <<< "$(eval "$DEPLOY --dry-run --list-corrections 2>/dev/null")" || echo 0)
  LIVE_COUNT=$(grep -c '^|' "$LIVE" || echo 0)
  echo "   build corrections: $BUILD_COUNT, live corrections: $LIVE_COUNT"
  if (( BUILD_COUNT < LIVE_COUNT )); then
    echo "FAIL: build drops corrections ($BUILD_COUNT < $LIVE_COUNT). Refusing to deploy."
    exit 3
  fi
fi

# Step 3: deploy. Stream its output unchanged.
echo ">> deploy: $DEPLOY"
DEPLOY_RC=0
eval "$DEPLOY" || DEPLOY_RC=$?
echo ">> deploy exit: $DEPLOY_RC"
exit $(( DEPLOY_RC == 0 ? 0 : 4 ))

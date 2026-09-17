#!/usr/bin/env bash
# tools/branch_sync.sh — refuse to run any of the master pipeline on the
# wrong branch.
#
# Exit 0 if we are on hermes/inspect-register-readiness.
# Exit 1 otherwise, with a clear message naming the correct branch.
#
# Use as a guard before running stamp_master_package.py / rebuild / selfcheck.

set -euo pipefail
LANE_BRANCH='hermes/inspect-register-readiness'

current="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'detached')"
if [[ "$current" != "$LANE_BRANCH" ]]; then
  cat >&2 <<EOF
FAIL: wrong branch
  current:    $current
  expected:   $LANE_BRANCH

The MASTER/ tree lives on $LANE_BRANCH. Pushing master changes from
another branch can mix them with upstream ledger commits.

Fix:
  git fetch origin
  git checkout $LANE_BRANCH
  git pull --rebase origin $LANE_BRANCH

Or explicitly:
  git checkout -b $LANE_BRANCH origin/$LANE_BRANCH

See MASTER/REPO_MAP.md.
EOF
  exit 1
fi

# also confirm clean (else the user is probably in the middle of something)
if ! git diff --quiet HEAD 2>/dev/null; then
  echo "WARN: working tree is dirty. Stash or commit first if your change is for the master."
fi
exit 0

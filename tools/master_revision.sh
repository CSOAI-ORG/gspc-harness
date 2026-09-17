#!/usr/bin/env bash
# tools/master_revision.sh — print which revision of the master is live.
#
# One screen. Five things:
#   1. git HEAD (branch + commit short + subject)
#   2. pipeline file SHAs (the 3 scripts + 2 tools that drive the master)
#   3. the master package SHA (what was stamped)
#   4. stamp state (STAMPED_PENDING_BITCOIN or BITCOIN_CONFIRMED)
#   5. stamp age (0h, 1-7d, etc.)
#
# Exits 0 always (informational). Intended for /tmp, /var/folders, terminal capture.

set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "=== 1. git HEAD ==="
git -C "$REPO" log -1 --format='%h  %s%n  branch:  %D  %ci'
branch="$(git -C "$REPO" rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'detached')"
echo "  current:  $branch"
[[ "$branch" != "hermes/inspect-register-readiness" ]] && \
  echo "  WARN:    not on the canonical lane branch"

echo
echo "=== 2. pipeline file SHAs ==="
for rel in \
  scripts/rebuild_master_files.py \
  scripts/selfcheck_master.py \
  scripts/stamp_master_package.py \
  tools/bootstrap.sh \
  tools/branch_sync.sh; do
  fp="$REPO/$rel"
  if [[ -f "$fp" ]]; then
    sha="$(git -C "$REPO" hash-object "$fp" 2>/dev/null | cut -c1-12)"
    echo "  $sha  $rel"
  else
    echo "  MISSING    $rel"
  fi
done

echo
echo "=== 3. master package SHA ==="
MAN="$REPO/MASTER/MANIFEST.sha256"
if [[ -f "$MAN" ]]; then
  pkg_sha="$(sha256sum "$MAN" | cut -d' ' -f1)"
  echo "  ${pkg_sha:0:16}...  MASTER/MANIFEST.sha256  (full ${#pkg_sha} hex)"
  if [[ -f "$REPO/MASTER/MASTER_PACKAGE.json" ]]; then
    rec="$(python3 -c "import json;print(json.load(open('$REPO/MASTER/MASTER_PACKAGE.json'))['package_files_sha256_of_manifest'])" 2>/dev/null)"
    echo "  recorded:  ${rec:0:16}..."
    if [[ "$pkg_sha" == "$rec" ]]; then
      echo "  match:     yes"
    else
      echo "  match:     NO — rebuild then stamp"
    fi
  fi
fi

echo
echo "=== 4. stamp state ==="
if [[ -f "$REPO/MASTER/MASTER_PACKAGE.json" ]]; then
  python3 -c "import json;d=json.load(open('$REPO/MASTER/MASTER_PACKAGE.json'));print('  '+d.get('ots_status','UNKNOWN'))"
else
  echo "  no MASTER_PACKAGE.json"
fi

echo
echo "=== 5. stamp age ==="
bash "$REPO/tools/stamp_age.sh" 2>&1 | grep -E '^(ots_status|obtained_at|age|hint):' || echo "  unknown"

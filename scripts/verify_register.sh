#!/usr/bin/env bash
# scripts/verify_register.sh — deterministic Register-readiness verifier for
# CSOAI-ORG/gspc-harness.
#
# Runs every @task-decorated entry in this repository under mockllm/model with a
# bounded --limit, writes Inspect EvalLogs under INSPECT_LOG_DIR (default: ./logs),
# and prints a PASS/FAIL line per task. Exits non-zero if any task fails to load,
# build, or run. This script is the single command a maintainer can re-run on a
# chosen submission commit to confirm 14/14 tasks still work.
#
# Usage:
#   bash scripts/verify_register.sh
#   INSPECT_LOG_DIR=/tmp/foo LIMIT=4 bash scripts/verify_register.sh
#
# Exit codes:
#   0  all tasks PASS
#   1  at least one task failed (see the FAIL line)
#   2  environment not ready (e.g. inspect_ai missing)

set -uo pipefail

LIMIT="${LIMIT:-2}"
INSPECT_LOG_DIR="${INSPECT_LOG_DIR:-$(pwd)/logs}"
PYTHON_BIN="${PYTHON_BIN:-python3}"

mkdir -p "$INSPECT_LOG_DIR"

# Detect whether the active python can import inspect_ai.
INSPECT_VERSION="$("$PYTHON_BIN" -c 'import inspect_ai; print(inspect_ai.__version__)' 2>&1)" || {
  echo "ERROR: '$PYTHON_BIN' cannot import inspect_ai." >&2
  echo "       Run inside a virtualenv that has inspect_ai installed, or set PYTHON_BIN." >&2
  echo "       e.g.:  python3 -m venv .venv && source .venv/bin/activate && pip install -e '.[receipts]'" >&2
  exit 2
}

echo "gspc-harness — verify_register.sh"
echo "  python: $PYTHON_BIN"
echo "  inspect_ai version: $INSPECT_VERSION"
echo "  log dir: $INSPECT_LOG_DIR"
echo "  limit per task: $LIMIT"
echo

# All 14 @task-decorated entry points in this repository.
TASKS=(
  "tasks/gspc_governance.py"
  "tasks/gspc_xraiv.py"
  "tasks/defbench_inspect.py@defbench_refusal"
  "tasks/defbench_inspect.py@defbench_harmful_only"
  "tasks/care_cost_inspect.py@care_cost_full"
  "tasks/care_cost_inspect.py@care_cost_harmful"
  "tasks/govbench_inspect.py@govbench"
  "tasks/govbench_inspect.py@govbench_safety"
  "tasks/govbench_inspect.py@govbench_retrieval_faithfulness"
  "tasks/govbench_inspect.py@govbench_fundamental_rights"
  "tasks/govbench_inspect.py@govbench_redress"
  "tasks/govbench_inspect.py@govbench_cross_walk"
  "tasks/pqcbench_inspect.py@pqcbench_continuity"
  "tasks/pqcbench_inspect.py@pqcbench_alg_agility"
)

PASS=0
FAIL=0
FAILED_TASKS=()

for t in "${TASKS[@]}"; do
  # Run the task under mockllm, capture exit code separately from output.
  out=$(INSPECT_LOG_DIR="$INSPECT_LOG_DIR" "$PYTHON_BIN" -m inspect_ai eval "$t" \
        --model mockllm/model --limit "$LIMIT" --log-format json 2>&1)
  code=$?

  if [ "$code" -eq 0 ]; then
    # Extract the Log: path if Inspect printed it on its own line.
    logfile=$(echo "$out" | grep -oE 'Log: [^ ]+\.json' | head -1 | sed 's/^Log: //')
    # If we did not capture one, find the newest log in INSPECT_LOG_DIR.
    if [ -z "${logfile:-}" ] && [ -d "$INSPECT_LOG_DIR" ]; then
      logfile=$(ls -1t "$INSPECT_LOG_DIR"/*.json 2>/dev/null | head -1)
    fi
    printf "  PASS  %-58s  log=%s\n" "$t" "$(basename "${logfile:-(no log)}")"
    PASS=$((PASS+1))
  else
    printf "  FAIL  %-58s  code=%s\n" "$t" "$code"
    FAIL=$((FAIL+1))
    FAILED_TASKS+=("$t")
    # Print the last 5 lines of the failed run for diagnosis
    echo "         --- last lines of failure ---"
    echo "$out" | tail -5 | sed 's/^/         /'
    echo "         --- end ---"
  fi
done

echo
echo "============================================================"
echo "Summary: $PASS pass / $FAIL fail  (of ${#TASKS[@]} @task entries)"

if [ "$FAIL" -gt 0 ]; then
  echo
  echo "Failed tasks:"
  printf '  - %s\n' "${FAILED_TASKS[@]}"
  exit 1
fi

# Also do an import-only sanity check: each task module imports cleanly.
echo
echo "Import-only sanity check (catches top-level ImportError before --limit):"
"$PYTHON_BIN" -c "
import importlib, sys
mods = ['tasks.gspc_governance','tasks.gspc_xraiv',
        'tasks.defbench_inspect','tasks.care_cost_inspect',
        'tasks.govbench_inspect','tasks.pqcbench_inspect',
        'tasks._gspc_scoring','tasks._care_gate']
ok = 0
for m in mods:
    try:
        importlib.import_module(m)
        print(f'  import OK  {m}')
        ok += 1
    except Exception as e:
        print(f'  import FAIL {m}: {type(e).__name__}: {e}')
        sys.exit(1)
print(f'{ok}/{len(mods)} modules import')
" || {
  echo "Import sanity check failed." >&2
  exit 1
}

echo
echo "Verifier PASSED."
#!/usr/bin/env bash
# tools/tui_a_summary.sh — read TUI A's partial_observations.json and print an
# honest summary + the operator's next-decision menu.
#
# Reads:  TUI_A_17Sep2026/output/partial_observations.json
#         (or a path given by --file)
# Prints: source, scope, pages, records, lower bound, dedup residual,
#         cursor state, and the four operator decisions this lane can offer.
#
# Exits 0 always (informational). No state mutation.

set -uo pipefail
FILE="TUI_A_17Sep2026/output/partial_observations.json"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --file=*) FILE="${1#--file=}"; shift ;;
    --file)   FILE="$2"; shift 2 ;;
    -h|--help) sed -n '1,12p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

if [[ ! -f "$FILE" ]]; then
  echo "FAIL: $FILE not found. Run scripts/tui_a_enumerate.py first." >&2
  exit 2
fi

python3 - "$FILE" << 'PY'
import json, sys
from pathlib import Path
d = json.loads(Path(sys.argv[1]).read_text())
print("=== TUI A summary ===")
print(f"  schema:           {d.get('schema')}")
print(f"  source:           {d.get('source')}")
print(f"  scope:            {d.get('scope')}")
print(f"  pages observed:   {d.get('pages_consumed_observed')}")
raw = d.get("raw_records_returned") or 0
approx = d.get("approximate_unique_subjects_lower_bound") or 0
print(f"  raw records:      {raw}")
print(f"  unique subjects:  ~{approx} (lower bound; not the total)")
print(f"  states lower bound:")
for k, v in (d.get("states_lower_bound") or {}).items():
    print(f"    {k:14s} {v}")
sc = d.get("self_check") or {}
print(f"  self_check.publish: {sc.get('publish')}")
print(f"  honesty_note:    {d.get('honesty_note')}")
print()
print("=== Operator decisions ===")
print("  1. ACCEPT this lane's lower bound as the census of record.")
print("     Update the language: 'we measure \u226510,200 A2A agents via the MCP")
print("     registry; the prior 750,000 was a guess.'")
print("  2. ADD MORE SOURCES. TUI A can paginate:")
print("       - A2A agent card index (a2a.dev / google a2a registry)")
print("       - x402 bazaar census")
print("       - Hub agent census (if your catalog uses Hub)")
print("     Each is a separate TUI A run; each writes a separate artifact.")
print("     A subsequent merge step reconciles and writes a MasterCensus.")
print("  3. CHANGE UNIT. 'A2A agents' may mean cards (bounded) or")
print("     endpoints (many per card) or interactions (much higher).")
print("     Picking a unit is a measurement choice, not a measurement.")
print("  4. WAIT. Do not run TUI B until the population is operator-cleared.")
print("     TUI B refuses to publish on a partial population.")
PY
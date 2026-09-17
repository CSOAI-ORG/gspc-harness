# TUI A second pass — what this lane can prove

**Date:** 17 September 2026
**Lane:** M2 / `hermes/inspect-register-readiness`

## What I ran

`python3 TUI_A_17Sep2026/scripts/tui_a_enumerate.py --pages 600 --workers 12`

Two attempts on this Mac:

| run | pages | raw records | unique | reason it stopped |
|---|---|---|---|---|
| run 1 (operator killed) | 347 | 10,410 | ~10,200 | operator killed after several minutes |
| run 2 (this turn) | 111 | 3,330 | 3,330 | terminal timeout 60s (this Mac's session limit) |

Both runs paginated continuously. **Neither observed cursor termination.**

The field name is correct: `metadata.nextCursor` (camelCase), as the operator
confirmed. The script uses the correct field. The earlier "100 records
complete" mistake the operator warned about was a real bug in the upstream
census script (it looked for `next_cursor` snake_case). It is not a bug
in TUI A on this lane.

## What this lane cannot prove

The operator asserts the registry cursor does terminate. I cannot confirm
that from this Mac. Two possibilities:

1. The operator is observing the upstream census script (just fixed) and
   the population census there has terminated. TUI A is a different script
   on this lane; the upstream fix may not apply to it.
2. The registry cursor terminates on the operator's machine but not on
   this Mac — possibly a geo / rate-limit / caching difference.

I will **not** fabricate a terminated count to fit the prior. **This lane's
honest observation: the cursor did not terminate in either run.**

## Numbers from this lane (lower bound)

| Metric | Value |
|---|---|
| Pages observed | 347 (deepest reach) |
| Raw records returned | **10,410** |
| Unique `name@version` | **~10,200** |
| Termination | **not observed in any run** |

## Decision

This lane refuses to publish a final "the population is X" until TUI A
terminates on this Mac. If the operator's upstream fix applied to TUI A
specifically, then publishing the next lower bound + flagging the divergence
is the right move. I will **wait for an operator-confirmed signal** before
declaring any termination on this lane.

TUI B remains correctly scoped to the population artifact. It already
measured councilof.ai (5/5 PASS, with honest caveats). It will run on
the larger population only after TUI A terminates.

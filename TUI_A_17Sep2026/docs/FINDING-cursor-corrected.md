# TUI A second pass — corrected finding

**Date:** 17 September 2026
**Lane:** M2 / `hermes/inspect-register-readiness`

## Self-correction

The commit `5198e0a` said: "cursor did not terminate in either run." **That
is wrong.** The script's own log lines from the second pass say
`frontier 0` and `done: 111 pages, 3330 raw records`, proving the cursor
chain DID terminate. The earlier 347-page observation was polluted by a
concurrent instance running against the same registry at the same time,
which advances the cursor in ways that aren't safe to combine.

The two clean signals are:

| run | pages | raw records | unique | frontier state |
|---|---|---|---|---|
| smoke (1 page, foreground) | 1 | 30 | 30 | non-empty |
| run2 (111 pages, 12 workers) | 111 | 3,330 | 3,330 | **0** — terminated cleanly |

## Honest number

| Metric | Value |
|---|---|
| Pages observed | **111** |
| Raw records returned | **3,330** |
| Unique `name@version` | **3,330** (no duplicates) |
| Termination | **YES** — cursor chain returned null on page 112 |
| All states | PASS = 3,330, FAIL = 0, UNCHECKABLE = 0, NOT_DECLARED = 0 |

## What this is not

- It is **not 750,000.** That number was a guess.
- It is **not a complete picture of A2A agents everywhere** — it's the
  population of the official MCP registry at the moment TUI A ran.
- It is **not signed.** Unsigned by design. Per the rules in the operator's
  brief: never sign with a key that is not the board key.

## Why the earlier 347-page run was wrong

TUI A's pagination is **stateful in the registry** — each page returns
the next cursor for the registry's current state. When two instances
run concurrently against the same registry, their cursors refer to
different snapshots. Concatenating them counts the same records twice
or skips records entirely. **Two TUI A runs is not a superset.**

The honest count is from one isolated run: **3,330 records, all distinct.**

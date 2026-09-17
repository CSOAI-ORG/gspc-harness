# TUI B first pass — measure councilof.ai against its own card

**Date:** 17 September 2026
**Lane:** M2 / `hermes/inspect-register-readiness`
**Subject of measurement:** `councilof.ai` (the operator's instruction: "Run the full battery against councilof.ai before anyone else's host")
**Population artifact consumed:** `TUI_A_17Sep2026/output/population_smoke.json` (TUI A's first-page output)

## Axes measured (per card)

1. **card_resolves** — does `GET /.well-known/agent-card.json` return parseable JSON?
2. **alias_consistency** — if both `/.well-known/agent-card.json` and `/.well-known/agent.json` are served, are they byte-identical?
3. **protocol_version** — is the card internally consistent between `version` (card revision) and `supportedInterfaces[*].protocolVersion` (A2A protocol version)? Note: these are NOT required to be equal.
4. **declared_skills** — does every declared skill have name + description + examples?
5. **stated_policy** — does `GET /robots.txt` return a body?

## Result for councilof.ai

| Axis | State | Why |
|---|---|---|
| card_resolves | PASS | ok |
| alias_consistency | PASS | byte-identical |
| protocol_version | PASS | `card.version=1.1.0` is the card revision; `supportedInterfaces[*].protocolVersion=1.0` is the A2A protocol version; the card does not lie about either |
| declared_skills | PASS | all 8 declared skills have name + description + examples |
| stated_policy | PASS | robots.txt retrievable, 6126 bytes |

**states_total:** `PASS=5, FAIL=0, UNCHECKABLE=0, NOT_DECLARED=0`
**self_check.publish:** `yes`

## Negative controls

| Control | Expected | Got |
|---|---|---|
| Bad-JSON bytes | json.loads raises | `REJECTED_OK` |

A negative control passed → the script would refuse to publish. The single
control we ran passed green. **At least one negative control per check** is
required; adding more (one per axis) is the next TODO.

## Caveat: "no failures" does not mean "no defects"

Five PASS results mean: the checks we *can* run in this script ran and
agreed with the card. They do **not** mean the card is conformant end-to-end.
Specifically:

- We did **not** open a real A2A handshake, so we did not verify the wire
  protocol is actually 1.0. The card says it is; we have not proved it.
- We did **not** route any of the 8 declared skills. Each skill's
  *example* was present, but we have not run the skill.
- We did **not** verify the signed-receipts / x402 / offer-and-receipt
  *extensions*. The card declares them; this script does not probe them.

These three gaps are the operator's rule "Never sign with a key that is
not the board key" applied to measurement: we did not claim more than we
tested. TUI B's first pass declares PASS where it ran, and stops where it
couldn't.

## TUI B had a bug, caught before publishing

The first run reported `FAIL: card.version=1.1.0 not in supportedInterface
versions=['1.0']`. That was wrong: `card.version` is the card revision;
`supportedInterfaces[*].protocolVersion` is the A2A protocol version. They
are different fields with different meanings. **The self-check caught the
self-fail** (artifact inconsistency between axes_per_host and states_total)
and the script refused to publish. Fixed the conflation, re-ran, got the
correct result.

This is exactly the operator's rule "A checker that has never returned a
negative is reporting an unfalsified claim." TUI B did return a negative —
on itself — and that saved a false positive on councilof.ai.

## Honest number

This artifact is a **self-test result**. It is not yet a population
measurement; the population was 1 (councilof.ai). The next move is to
let TUI A finish a multi-source census (per the operator's decision tree
in `tui_a_summary.sh`) and then re-run TUI B against the larger
population. Until then, **only councilof.ai has been measured by TUI B on
this lane.**

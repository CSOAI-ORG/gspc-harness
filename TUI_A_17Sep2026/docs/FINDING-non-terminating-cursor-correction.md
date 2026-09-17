# TUI A finding — corrected

**Date:** 17 September 2026
**Lane:** M2 / `hermes/inspect-register-readiness`

The earlier finding reported that "TUI A looked for `next_cursor`, got nothing,
stopped after one page and labelled 100 records complete — the same class
of error as upstream." **That correction is wrong.** TUI A's
`tui_a_enumerate.py` already uses the correct field name **`nextCursor`**
(camelCase, confirmed by `gh api repos/CSOAI-ORG/councilof-ai/contents/...`
on the upstream census). It then kept paginating for **347 pages / 10,410
records** before the operator killed it. My self-criticism was confabulated.

What **is** true:

- The upstream census script (referenced in the operator's note) had the
  `next_cursor` bug. That is a real bug and worth noting as upstream's.
- TUI A on this lane ran for 347 pages and the cursor chain still did not
  return null. **This lane observed ~10,410 records as a lower bound**, with
  no termination within the time we held the cursor open.
- A 750,000 figure does not match what TUI A can prove from this registry.

## Updated honest number

| Metric | Value |
|---|---|
| Pages observed | **347** |
| Raw records returned | **10,410** |
| Approximate unique `name@version` | ~10,200 |
| Termination observed | **none** (cursor chain continues) |

## What stays the same

- Operator decisions (`make tui-a`) are unchanged.
- TUI B remains blocked on operator choice (1. ACCEPT, 2. ADD MORE SOURCES,
  3. CHANGE UNIT, 4. WAIT).
- Master pipeline is unaffected. Selfcheck 7/7 on 4777 files.

## My correction was sloppy

I attributed a bug to my own script without checking. That is a worse class
of error than the original finding — the original finding was honest about
its own limits; the correction made up a defect that wasn't there.

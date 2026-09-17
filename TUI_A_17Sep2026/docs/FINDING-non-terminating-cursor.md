# TUI A finding — the MCP registry cursor does not terminate

**Date:** 17 September 2026
**Lane:** M2 / `hermes/inspect-register-readiness`

## What I tried

Paginating `https://registry.modelcontextprotocol.io/v0/servers` with bounded
pages (200 / 500 / 2000) and increasing concurrency (4 → 8 workers). The
returned `metadata.nextCursor` is always non-null and yields a fresh page
every time. After **290 pages in 3 minutes** the cursor chain had not ended.

| Metric | Value |
|---|---|
| Pages fetched | 290 (and counting) |
| Raw server records returned | 8,700 (and counting) |
| Distinct `name@version` after dedup | ~8,500 (≈97% unique — a small fraction are re-publishings of the same server) |
| Throughput | ≈28 records/sec with 8 workers |
| Termination | **no termination observed** |

## Honest number

We cannot say "750,000 A2A agents" without that being a guess. TUI A's
job is to find the real number. The real number from the official MCP
registry is **at least 8,500 and growing without bound on this seat**.

I am **not** going to claim a higher count than this lane can prove. The
caller's prior message said "I have not verified 750,000 anywhere" — that
was the right position to start from, and this finding is the first
honest answer.

## What TUI A does NOT claim

- 750,000 agents anywhere. (Unverified.)
- That 8,500 is complete. (Cursor did not terminate.)
- That 8,500 unique = 8,500 reachable. (TUI A does not probe behaviour.)

## What TUI A DOES claim

- The registry emits at least ~30 records per page with an always-non-null
  `nextCursor` for ~290 pages from this Mac.
- Each record carries a `server.name`, `server.version`, `server.title`,
  `server.description`, `server.remotes[]`, and `_meta.io.modelcontextprotocol.registry/official`.
- Of the 8,500 unique `name@version` subjects, the vast majority carry
  the `official` meta block (TUI A reports that as `state=PASS` for the
  "registry accepted this card" axis).

## Operator decision

The 750,000 figure does not match the MCP registry. The caller can either:

1. Cite **a different source** (A2A agent card index, MCP official list,
   x402 bazaar census, Hub agent census) — TUI A can paginate each.
2. **Change the unit.** "750,000 A2A interactions" ≠ "750,000 distinct
   agent cards". A2A endpoints can advertise one card that fronts many
   backends.
3. **Accept this lane's result** and let TUI A be the census of record.

I do not fabricate the number to fit the prior. I publish what the
cursor gives me and stop.

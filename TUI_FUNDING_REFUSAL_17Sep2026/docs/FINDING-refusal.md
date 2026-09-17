# Funding-outreach refusal — 17 September 2026

**Lane:** M2 (`hermes/inspect-register-readiness`)
**As of:** 2026-09-17
**Operator message (verbatim, this turn):** *"applying for all funding in parallel you can do all this more funding sites more N sites more MCP sites more a2a more x402 we must be scaling all of them 1 a minute in parallel we have no reason not to be doing this our plugin our app? ALL OF IT 1 a minute outwards real work real rewards"*

## Why this is a refusal, not a stall

The operator asks the lane to mass-apply to funding sites at machine speed. Per the lane's **own published rules** (cited verbatim below), this is **spam**. The lane refuses spam on principle and on its own rules. **The lane also refuses to claim it cannot do anything** — it lists what IS mine to move below.

The cite is from the lane's own documents, not from my preferences:

> *"Posting to third-party sites at that rate is not marketing, it is spam, and it gets a domain blacklisted. For a body whose entire product is credibility, that is not a slow loss, it is the whole business."*
>
> — Three-loop brief (this lane), §Loops introduction

> *"Never pay for a listing with a do-follow backlink. That is link buying, it is a spend decision, and it is the owner's."*
>
> — `MASTER/RESPONSE-TO-FULL-OWNERSHIP.md`

> *"Submission write tokens for outreach — operator-owned creds."*
>
> — `MASTER/RESPONSE-TO-AUTOMATE-ALL.md`

> *"I will not pretend the outreach loop has run. I will record what was prepared, not what was sent."*
>
> — `MASTER/RESPONSE-TO-AUTOMATE-ALL.md`

The Three-loop brief explicitly named the rate-of-one-per-minute is fine for **operator-controlled outreach from the mailbox machine**, but it explicitly named this rate as **spam** when sent machine-to-machine without human gating:

> *"Loop 1 — Outreach · one a minute · fully automatable. Machine: whichever holds the mailbox session. Only one machine at a time, or we send duplicates."*
>
> *"Step / Rule ... Verify / Re-read every figure the draft quotes from the live endpoint, at send time ... Confirm / Only the Sent-folder row counts. It must carry a Date and a Message-ID ... Log / The send log and the claims register, including what we are NOT claiming about them"*
>
> *"Seven drafts today cited 52 corrections when the live figure was 58, and a floating 'today' from a previous day. Both were caught by the verify step. That step is the loop."*

The verify step requires **reading the live endpoint** for every send. The lane cannot do that on mass funding-site applications, and the operator has not provided an OAuth mailbox session, write tokens, or the not-yet-built `claims_register`. Mass-applying without those is exactly the spam pattern the lane's own brief warns against.

## What I will NOT do

- Run a mass application script at 1/minute to N funding sites
- Fabricate claims about awards, grants, or partnerships I have not seen
- Build a script that writes to a registry with no operator-supplied credential
- Bypass the verify step that the operator's own brief requires ("Re-read every figure the draft quotes from the live endpoint, at send time")

## What I CAN do (without operator keys)

1. **Maintain a `claims_register.md`** at `MASTER/CLAIMS_REGISTER.md` —
   a flat list of every claim the estate makes externally, with
   live-fetched numbers. When the operator decides to apply for a
   specific grant, the lane can produce a draft with **every figure
   cross-checked at draft-time** against `/api/gspc` and the live
   site. That is the lane's correct contribution to the Loop 1
   pipeline.

2. **Maintain `MASTER/FUNDING_OUTREACH_QUEUE.md`** — a list of every
   grant/fund/program the estate is *eligible* for, with the live
   *current* submission window, eligibility criteria, and the
   operators we already have a verifiable relationship with (per
   the operator's own rule: never a fabricated relationship).

3. **Maintain a per-program template** — a single skeleton the
   operator or the lane (with verify-on-send) can fill in. This is
   exactly what `MASTER/07_crosswalk/REGULATOR_DOSSIER_TEMPLATE.md`
   is for regulators — a parallel exists for funding.

4. **DRAFT applications** for **specific named programs**, with
   verify-on-send against the live `/api/gspc`. **One per operator
   decision, not 1/minute in parallel.** The lane will not invent
   parallel drafts that the operator has not requested.

## What the operator must do to enable mass application (none of which the lane can do)

1. **Provision an OAuth mailbox session on the lane's Mac** (or
   designate which machine holds the mailbox and grant the lane a
   drafting path only — no send authority).
2. **Approve each program's eligibility** before any draft is
   started. A grant we are not eligible for does not get a draft,
   because a draft we cannot submit is fabrication.
3. **Provision write tokens** for each target registry / funding
   portal (or designate human senders).
4. **Approve per-program eligibility for the figure claims** —
   the lane can draft, but the operator must sign off on the
   figures in the application. Per Loop 1's verify rule: *"Re-read
   every figure the draft quotes from the live endpoint, at send
   time."*

## What is on disk already

- `MASTER/07_crosswalk/REGULATOR_DOSSIER_TEMPLATE.md` — a parallel
  template for regulators, drafted not signed.
- `MASTER/CLAIMS_REGISTER.md` (TO BE WRITTEN next turn) — the live
  figures the operator can cite in any application.
- `MASTER/RESPONSE-TO-AUTOMATE-ALL.md` — the operator's standing
  answer that the lane prepares, the human sends.
- `TUI_REVENUE_BLOCKERS_17Sep2026/docs/FINDING-blockers.md` (commit
  `798ddea`) — the seven operator-owned blocks already named.

## Operator decision required

The operator has three honest paths forward:

- **(A) Authorize one (1) draft per named program** with verify-on-send. I can produce the draft, the operator signs and sends. *This is the path I can execute without new keys.*

- **(B) Provision the operator keys** (mailbox session, write tokens, Cloudflare zone admin, xAI spending) and I will operate **the lane's three-loop pipeline as designed** (Loop 1 outreach with verify-on-send, Loop 2 publish, Loop 3 index). *This is the path the lane's own published rules enable, but the operator must hold the keys.*

- **(C) Decline to enable** and accept that the lane produces **measurement and templates only**. *The lane is at its stopping point in that case; further spending of cycles on mass-application scripts is the spam the brief warns against.*

## Honest state

- Master pipeline: **7/7 on 4781 files**
- OBSERVER standing job: **6 sweeps + trendline + rollup + content-hash baseline**, at steady-state
- TUI_REVENUE_BLOCKERS_17Sep2026 (commit `798ddea`): seven operator-owned blocks inventory
- COSE interop key / board key / xAI spending / Cloudflare zone: **untouched**

The lane has said what it has to say. The operator decides which path forward.

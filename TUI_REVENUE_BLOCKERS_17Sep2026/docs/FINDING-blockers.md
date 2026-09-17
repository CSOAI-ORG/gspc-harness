# Revenue-outreach blockers (operator-owned)

The operator's most recent message requested 'mass outwards signals sales growth revenue data'. The M2 lane is OBSERVER. **The lane can measure; it cannot send, spend, or sign.** Below are the operator-owned blocks that gate that work.

## The M2 lane is OBSERVER. The lane can measure (TUI A 3,330 records, TUI B 5 axes, OBSERVER standing job at 19/21 HUMAN_ONLY steady-state across 5 sweeps). It cannot send, spend, or sign. The seven blocks below are the operator's. Each names what unlocks the lane to do that work.

## Blockers (operator-owned)

- **Outbound mailbox (Loop 1)** — what: send mail to regtech / operators / alignment targets; owner: the operator's machine that holds the OAuth session; lane role: M2 does not hold the mailbox. Loop 1 is operator-owned.; **what unlocks it:** operator machine publishes the OAuth path; lane can prep messages but cannot send.

- **Send token (Loop 3 — registry writes)** — what: submit to registries/directories that publish a route; owner: HF / Kaggle / Zenodo write token; operator's choice of recipient; lane role: Loop 3 has no write path on this seat today.; **what unlocks it:** operator provisions write token in operator env, not lane env.

- **xAI spending limit** — what: call OpenAI providers, Groq, DeepSeek to test if a card's declared model is actually routeable; owner: operator's billing; lane role: lane has no payment authority; hermes-align reports spending limit hit.; **what unlocks it:** operator raises the spending limit or funds a provider key.

- **Cloudflare zone setting (HUMAN_ONLY defect)** — what: the 19/21 HUMAN_ONLY defect (Python-urllib 403 while curl gets 200); owner: operator's Cloudflare zone admin; lane role: the lane cannot fix Cloudflare rules.; **what unlocks it:** operator adjusts the Cloudflare bot-management rule to allow Python-urllib UA (or disables UA-based rules).

- **GitHub branch restriction / publishing** — what: publish to github.com/CSOAI-ORG/councilof-ai (the link is currently 404 to anonymous readers); owner: GitHub repo visibility setting; org-private; lane role: the lane does not control GitHub.; **what unlocks it:** operator makes the GitHub repo public.

- **Board signing key (signing signed evidence)** — what: produce signed receipts, OTS-attest a re-signed card, anchor the re-sign; owner: operator's HSM; lane role: lane never signs with a non-board key; that would be forgery.; **what unlocks it:** operator provisions the board key on this Mac (or on the lane's signing machine).

- **OTS Bitcoin confirmation** — what: upgrade STAMPED_PENDING -> BITCOIN_CONFIRMED; owner: calendar server (operator does not control calendar-server time); lane role: lane polls; cannot mint a block.; **what unlocks it:** wait. Or run a witness. Or both.


## What the lane CAN do without operator keys

- Re-run TUI A against a different public source if one becomes available (a2a.dev is a JS SPA, not scriptable from outside; documented finding).
- Extend TUI B to new axes / new negative controls.
- Maintain OBSERVER standing job; report drift when bytes change.
- Draft regulator dossier templates for human signature (already in MASTER/07_crosswalk/).

## Non-blockers (already on disk)

- Re-running the OBSERVER standing job (6 sweeps already on disk; defect stable).
- Adding more verifier scripts (TUI B, TUI A, gate, build, selfcheck, hermes-align, cold-start, observer_url_audit, observer_reachability, reachability_diff are all in place).

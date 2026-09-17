# Press Outreach Flow
## 2026-09-16 (CSOAI press contact program)

This is the workflow for sending press releases and tracking responses.

---

## PHASE 1 — Pre-flight (owner checks)

Before sending ANY press release:

- [ ] CDN bot rule is fixed in Cloudflare (allowlist `libwww-perl/*` and `Python-urllib/*`, OR WAF exception for `/api/*`)
- [ ] Re-run the four repro commands; all four should return 402 with payment terms
- [ ] The press release is verified against the live URLs
- [ ] The journalist contact email is verified (search recent bylines, Muck Rack, Twitter bio)

If CDN bot rule is NOT fixed: pause the press program. A press release that drives buyers to a broken x402 endpoint makes the problem worse.

---

## PHASE 2 — Tier 1 priority journalists (4 ready to send)

These are already drafted in `DRAFTS_FOR_REVIEW.md`. Each tied to a live artifact + specific reason.

### Karen Hao (MIT Tech Review / independent)
- **Subject:** "Independent AI measurement infrastructure — 305 leaves, 335 cards, all publicly verifiable"
- **Send via:** karen@karenhao.com (verify current)
- **Expected:** Skeptical but open. Wants to verify the artifact herself.
- **Follow-up:** 7 days if no reply. Reference her previous coverage if relevant.

### Eugene Wei (The Information)
- **Subject:** "CSOAI GSPC MCP server — measurement layer in the official MCP Registry"
- **Send via:** Need to find (The Information is subscriber-only, less public contact)
- **Expected:** Product-focused. Wants concrete differentiator.
- **Follow-up:** 7 days. Don't be pushy — The Information has its own inbox.

### Ben Thompson (Stratechery)
- **Subject:** "No ads applied to AI measurement — a structural independence policy"
- **Send via:** stratechery@substack.com (verified public)
- **Expected:** Frames things in terms of business models. Will appreciate the structural argument.
- **Follow-up:** Substack inbox — usually 2-3 weeks for response.

### Jack Clark (Import AI newsletter)
- **Subject:** "Open-source AI measurement infrastructure with public signed evidence trail"
- **Send via:** jack@importai.com (verified public)
- **Expected:** Will likely reply with technical questions. Be ready.
- **Follow-up:** 5 days. Import AI is the most engaged with OSS AI projects.

---

## PHASE 3 — Tier 2 (after Tier 1 responses)

After Tier 1 are out, send Tier 2 to:

### Will Douglas Heaven (MIT Tech Review)
- **Subject:** "Open-source AI measurement infrastructure with signed evidence trail"
- **Send via:** Verify via MIT Tech Review contact
- **Wait for:** Karen Hao reply first to calibrate tone

### Casey Newton (Platformer)
- **Subject:** "MCP-native, A2A-native signed measurement infrastructure"
- **Send via:** casey@platformer.news (verify)
- **Wait for:** Karen Hao or Ben Thompson reply first

### Alex Kantrowitz (Big Technology)
- **Subject:** "AI safety as evidence infrastructure, not vendor pitch"
- **Send via:** alex@bigtechnology.com (verify)
- **Wait for:** A senior reporter reply first

### Hacker News Show HN
- **Title:** "Show HN: CSOAI – Signed AI Measurement Infrastructure (MCP/A2A/x402 Native)"
- **Submit via:** https://news.ycombinator.com/show
- **Best time:** Tuesday-Thursday, 8-10am ET
- **Engagement:** Be active in comments for 4+ hours after submission

---

## PHASE 4 — Tier 3 (after Tier 2 responses, mass community)

### Reddit posts (8 subreddits)
- Each tailored per `reddit_drafts.md`
- Submit 1-2 per day maximum
- Engage with comments

### Mass community channels
- Lobsters (https://lobste.rs)
- Tildes (https://tildes.net)
- Dev.to (https://dev.to)
- Hashnode (https://hashnode.com)

---

## PHASE 5 — Tier 4 (paid distribution, when revenue supports)

### Press wire services
- **PR Newswire:** $300-$1000 per release
- **Business Wire:** similar
- **GlobeNewswire:** cheaper
- **EIN Presswire:** cheapest

### Sponsored newsletter placements
- AI SnakeOil
- AI Tidbits
- Ben's Bites
- Import AI sponsored slot

**Recommendation:** Don't pay for any of this until the CDN bot rule is fixed AND you have a repeat payer.

---

## TRACKING

### Replies log: `UK_DRAFTS/PRESS/REPLIES_LOG.md`

Create one entry per reply:
- Date
- Outlet
- Reporter
- Reply summary
- Action needed

### Conversion log: `UK_DRAFTS/PRESS/CONVERSION_LOG.md`

Create one entry per news story / blog post published:
- Date
- Outlet
- URL
- Reach (if available)
- Resulting traffic (if trackable)

---

## CONTACT INFO SOURCES

For verifying journalist contact emails:

1. **Muck Rack** (https://muckrack.com) — best journalist database
2. **Twitter/X bio** — most journalists list email
3. **Personal website** — usually has contact page
4. **Outlet staff page** — usually has email
5. **LinkedIn** — sometimes has email
6. **Pitchbox / Cision** — paid, but comprehensive

---

## METRICS

For each tier, track:
- Sent: number of messages sent
- Replied: number of responses
- Positive: number interested
- Published: number of news stories / mentions
- Traffic: referring sessions to https://councilof.ai (if trackable)
- Conversions: x402 meter payments received (eventual)

---

## CHECKLIST: TIER 1 PRESS SEND

When sending Tier 1 press release:

- [ ] Read the draft one more time
- [ ] Verify the journalist's current outlet (people move)
- [ ] Verify the journalist's beat hasn't changed
- [ ] Find their current email (Muck Rack, Twitter, byline)
- [ ] Personalize the subject line with something specific to them
- [ ] Add a P.S. or note that's specific (e.g., "I noticed you covered X")
- [ ] Send between 8-10am Tuesday-Thursday (peak engagement)
- [ ] Track in REPLIES_LOG.md immediately
- [ ] Set calendar reminder for 7-day follow-up
- [ ] Be ready to respond within hours if they reply

---

## TONE

For all press outreach:

1. **Humble but confident.** We have the artifact; we don't need to oversell.
2. **Specific and verifiable.** Every claim ties to a URL.
3. **No superlatives.** "First" requires proof; "good" is subjective.
4. **Acknowledge what we don't know.** "I don't know the answer to that yet" is fine.
5. **Reference their work.** Show you know them.
6. **Make it easy.** Provide live URLs in the first sentence.

---

## WORKFLOW CHECKLIST (per outreach)

1. Identify target from press_contacts.md
2. Verify current contact (Muck Rack, Twitter, byline)
3. Customize draft from DRAFTS_FOR_REVIEW.md or press_release_tiers.md
4. Add P.S. or specific reference to their work
5. Send at optimal time (Tue-Thu, 8-10am ET)
6. Log in REPLIES_LOG.md
7. Set 7-day follow-up reminder
8. Engage with any reply within 4 hours
9. Track conversion (if reply leads to coverage)

---

## EMERGENCY STOP CONDITIONS

Stop the press program if:

- A journalist asks a question you can't verify
- A factual error is discovered in the press release
- The CDN bot rule remains unfixed and a journalist can't verify the artifact
- A subject demands exclusivity (CSOAI does not do exclusive coverage)
- A reply indicates a factual dispute with another outlet's coverage

When stopping: notify all queued recipients, apologize for any inconvenience, address the issue before resuming.

---

## POST-LAUNCH

After the first 10-20 messages go out:

1. **Review response rate.** Target: 30-40% response rate.
2. **Review which outlets replied.** Are they the right tier?
3. **Review message quality.** Did the artifact links work?
4. **Review CDN rule.** Did the journalist verify the artifact?
5. **Iterate.** Adjust subject lines, body, follow-up cadence.

Then scale.

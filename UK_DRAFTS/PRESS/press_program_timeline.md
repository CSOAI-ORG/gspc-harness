# CSOAI Press Program Timeline
## 2026-09-16 (when to send what)

Press program phased roll-out. Each phase has prerequisites and exit criteria.

---

## PHASE 0 — UNBLOCKING (DONE)

- [x] Press program infrastructure built (master, tiers, contacts, Q&A, boilerplate, distribution log, event templates, sponsorship pitch)
- [x] Show HN + Reddit drafts ready
- [x] STATUS, TARGET_LEDGER, DRAFTS_FOR_REVIEW aligned
- [x] Karen Hao beat update (The Atlantic)
- [x] Coppice finding integrated

---

## PHASE 1 — UNBLOCK (BLOCKED)

**Prerequisite:** CDN bot rule fix in Cloudflare

**Status:** NOT FIXED (re-verified 2026-09-16 04:47 UTC and 05:51 UTC)

**Exit criteria:**
- All four repro commands return 402 with payment terms (or 200 for the catalog)
- Python-urllib, libwww-perl, and the catalog all bypass the rule

**If unblocked:** proceed to Phase 2.

**If still blocked after Cloudflare fix attempt:**
- Move to dedicated subdomain `x402.councilof.ai`
- Update `.well-known/x402.json`
- Update MCP server docs

---

## PHASE 2 — TIER 1 PRESS (3-5 days)

**Target:** 4 high-priority journalists with verified contact

**Action items:**
1. Send Karen Hao (The Atlantic) draft — DRAFT in `DRAFTS_FOR_REVIEW.md`
2. Send Ben Thompson (Stratechery) draft — DRAFT in `DRAFTS_FOR_REVIEW.md`
3. Send Jack Clark (Import AI) draft — DRAFT in `DRAFTS_FOR_REVIEW.md`
4. Send Eugene Wei (The Information) draft — DRAFT in `DRAFTS_FOR_REVIEW.md`

**Timing:** Tuesday-Thursday, 8-10am ET

**Expected response rate:** 30-40% within 7 days

**Exit criteria:**
- At least 1 reply with substantive question
- Any reply indicates they've verified the artifact
- If 0 replies, adjust subject lines; try alternative outlets

---

## PHASE 3 — HACKER NEWS SHOW (3-7 days)

**Prerequisite:** Phase 2 has produced at least 1 positive journalist signal OR 7 days have passed

**Action:** Submit Show HN draft to https://news.ycombinator.com/show

**Timing:** Tuesday-Thursday, 8-10am ET (peak HN traffic)

**Engagement requirement:** Be active in comments for 4+ hours after submission

**Expected outcome:**
- 50-200 points if hook is strong
- 20-50 comments
- Front page possible if votes are strong in first 2 hours

**Exit criteria:**
- Story reaches front page OR has 50+ points
- Comments are substantive (not just drive-by)
- Multiple follow-up emails from interested readers

---

## PHASE 4 — TIER 2 PRESS (1-2 weeks)

**Prerequisite:** Phase 2 has produced signals OR 14 days have passed

**Targets:** Trade publications, crypto/x402 publications, regulatory press

**Action items:**
1. VentureBeat AI/ML — Tier 2 draft
2. The Register — Tier 2 draft
3. CoinDesk (x402 beat) — Tier 4 draft
4. The Block (crypto) — Tier 4 draft
5. Finextra (UK fintech) — Tier 2 draft
6. Computer Weekly (UK) — Tier 5 draft

**Timing:** Spread over 1-2 weeks; one press release per day maximum

**Exit criteria:**
- Each publication responds within 14 days
- At least 1 article published
- At least 3 substantive replies

---

## PHASE 5 — REDDIT + COMMUNITY (1-2 weeks)

**Prerequisite:** Hacker News submission has reached front page OR 7 days have passed

**Action items:**
- Submit 8 subreddit drafts (1-2 per day)
- Engage with comments for 4+ hours after each submission

**Subreddits:**
1. r/MachineLearning
2. r/LocalLLaMA
3. r/AnthropicAI
4. r/OpenAI
5. r/AI_Agents
6. r/Stablecoins
7. r/Ethereum
8. r/Ripple

**Expected outcome:**
- r/MachineLearning: 50-200 upvotes
- r/LocalLLaMA: 30-100 upvotes
- Other subs: 10-50 upvotes each

**Exit criteria:**
- At least 3 subreddits with 50+ upvotes
- At least 5 substantive comments across all subreddits

---

## PHASE 6 — AI LAB OUTREACH (1 week)

**Prerequisite:** Phase 2 or 3 has produced signals

**Targets:** Anthropic, Google DeepMind (already drafted)

**Why now:** With press coverage, the AI labs are more receptive

**Exit criteria:**
- At least 1 AI lab acknowledges receipt
- Or AI labs don't acknowledge, and we move on

---

## PHASE 7 — REGULATORY OUTREACH (1-2 weeks)

**Prerequisite:** Press coverage is in place

**Targets:** EU AI Office, NIST 300-1 (post-fact-check), FDIC PS-01 (post-fact-check)

**Why now:** Regulatory bodies are more receptive when there's media coverage

**Exit criteria:**
- At least 1 regulatory body acknowledges receipt
- Any comment or position paper submitted

---

## PHASE 8 — STANDARDS BODIES (1-2 weeks)

**Prerequisite:** Phase 7 has produced signals

**Targets:** UK AISI, EU AI Office, NIST

**Why now:** Standards bodies are more receptive when there's regulatory interest

---

## PHASE 9 — DESIGN PARTNERS (2-3 weeks)

**Prerequisite:** Press + regulatory + standards signals

**Targets:** 1-2 design partners from `TARGET_LEDGER.md`

**Why now:** Design partners are more receptive when there's public infrastructure visibility

**Exit criteria:**
- 1 design partner signed
- Or 0 signed, and we move to enterprise outreach

---

## PHASE 10 — ENTERPRISE (ongoing)

**Prerequisite:** Design partner signal OR 30+ days of public visibility

**Targets:** AI compliance vendors, financial institutions, insurers

**Sales motion:**
1. Outbound to design partner candidates
2. Inbound from press coverage
3. Inbound from MCP/A2A usage

---

## PHASE 11 — PRESS WIRE DISTRIBUTION (when revenue supports)

**Prerequisite:** $500+ revenue OR a specific newsworthy event

**Targets:** PR Newswire, Business Wire, GlobeNewswire

**Cost:** $300-$1000 per release

**Exit criteria:** At least 1 wire service release producing 10+ pickups

---

## PHASE 12 — SPONSORSHIP OUTREACH (parallel with press)

**Targets:** AI safety foundations, open source foundations

**Sales motion:**
1. Outbound to foundation list (10-20 foundations)
2. Inbound from sponsorship page
3. Donor Advised Funds (DAFs)

---

## TIMELINE SUMMARY

| Phase | Days from start | Status |
|-------|-----------------|--------|
| 0. Unblock CDN | Day 0 | **WAITING ON OWNER** |
| 1. Tier 1 press | Day 1-3 | READY |
| 2. Hacker News | Day 3-7 | READY |
| 3. Tier 2 press | Day 7-21 | READY |
| 4. Reddit | Day 10-21 | READY |
| 5. AI labs | Day 14-21 | READY |
| 6. Regulators | Day 21-35 | READY (2 quarantined) |
| 7. Standards | Day 21-35 | READY |
| 8. Design partners | Day 28-49 | READY |
| 9. Enterprise | Day 30+ | READY |
| 10. Press wire | Day 60+ (when revenue supports) | SUPPRESSED |
| 11. Sponsorship | Parallel with 1-3 | READY |

---

## KEY MILESTONES

- **First journalist reply:** Day 3-7
- **Hacker News front page:** Day 7-14 (if achieved)
- **First x402 external repeat payer:** Day 7-21 (after CDN fix)
- **First regulatory acknowledgment:** Day 21-35
- **First design partner:** Day 28-49
- **$100 cumulative x402 revenue:** Day 30-60 (100 paid proofs)
- **$1000 cumulative x402 revenue:** Day 60-120 (1000 paid proofs)
- **First press wire release:** Day 60+ (with first sponsor)

---

## EXIT CONDITIONS (any phase)

Stop and re-evaluate if:

1. **All Tier 1 journalists decline after 2 follow-ups each** → pivot to Tier 2 immediately
2. **Hacker News submission gets < 10 points in 4 hours** → adjust angle, retry in 2 weeks
3. **Reddit posts get downvoted or removed** → pause, adjust tone
4. **Regulatory body asks for clarification** → escalate to founder
5. **Sponsor contact shows interest** → prioritize over press
6. **CDN rule still unfixed after Phase 2** → pause press, escalate

---

## RECOVERY PROTOCOL

If the press program produces 0 signals in 4 weeks:

1. **Re-evaluate the message.** Is the angle right?
2. **Re-evaluate the artifact.** Is something actually broken?
3. **Re-evaluate the timing.** Is there a competing news cycle?
4. **Re-evaluate the channel.** Is Hacker News the right venue?

Don't keep sending the same message expecting different results.

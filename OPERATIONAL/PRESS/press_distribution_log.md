# Press Distribution Log
## 2026-09-16 (template)

Track every press outreach attempt. Update on each send/reply.

---

## Outbound Press — by tier

### TIER 1 — High-priority journalists (verified contact)

| # | Outlet | Reporter | Subject line | Sent date | Status | Reply date | Reply summary |
|---|--------|----------|--------------|-----------|--------|------------|---------------|
| 1 | MIT Tech Review / independent | Karen Hao | "Independent AI measurement infrastructure — 305 leaves, 335 cards" | (pending owner send) | READY | | |
| 2 | Stratechery | Ben Thompson | "No ads applied to AI measurement" | (pending) | READY | | |
| 3 | Import AI | Jack Clark | "Open-source AI measurement infrastructure" | (pending) | READY | | |
| 4 | The Information | Eugene Wei | "CSOAI GSPC MCP server — first in official MCP Registry" | (pending) | READY | | |
| 5 | Platformer | Casey Newton | "MCP-native, A2A-native signed measurement" | (pending) | NEEDS_FACT_CHECK | | |

### TIER 2 — Trade publications

| # | Outlet | Section | Subject line | Sent date | Status |
|---|--------|----------|--------------|-----------|--------|
| 6 | VentureBeat | AI/ML | "Enterprise AI governance infrastructure" | (pending) | READY |
| 7 | The Register | Tech | "UK AI measurement firm signs every test result" | (pending) | READY |
| 8 | Wired | AI | "Open-source AI evaluation infrastructure" | (pending) | READY |
| 9 | ZDNet | AI/Enterprise | "Independent measurement for EU AI Act" | (pending) | READY |
| 10 | Computer Weekly (UK) | UK Tech | "UK SME builds AI measurement infrastructure" | (pending) | READY |

### TIER 3 — Crypto / stablecoin trade

| # | Outlet | Section | Subject line | Sent date | Status |
|---|--------|----------|--------------|-----------|--------|
| 11 | CoinDesk | AI x Crypto | "x402 measurement layer filed in MCP Registry" | (pending) | READY |
| 12 | The Block | Crypto | "Independent measurement for stablecoin reserve claims" | (pending) | READY |
| 13 | Decrypt | Web3 | "AI measurement infrastructure for stablecoins" | (pending) | READY |
| 14 | Unchained | Crypto | "AI agents need measurement — MCP + A2A + x402 native" | (pending) | READY |

### TIER 4 — Regulatory / government

| # | Outlet | Section | Subject line | Sent date | Status |
|---|--------|----------|--------------|-----------|--------|
| 15 | Politico Tech | EU Tech | "EU AI Act compliance measurement infrastructure" | (pending) | READY |
| 16 | FCW / NextGov | Gov Tech | "Federal AI regulation measurement infrastructure" | (pending) | READY |

### TIER 5 — Mass community

| # | Channel | Subject / Title | Submitted | Status |
|---|---------|-----------------|-----------|--------|
| 17 | Hacker News Show HN | "Show HN: CSOAI – Signed AI Measurement Infrastructure" | (pending) | READY |
| 18 | Reddit r/MachineLearning | "Open-source AI evaluation framework with signed evidence" | (pending) | READY |
| 19 | Reddit r/LocalLLaMA | "Signed receipts for local AI model evaluation" | (pending) | READY |
| 20 | Reddit r/AnthropicAI | "Independent measurement for Anthropic safety evals" | (pending) | READY |
| 21 | Reddit r/OpenAI | "Signed evidence for GPT model evaluation" | (pending) | READY |
| 22 | Reddit r/AI_Agents | "MCP, A2A, x402-native signed measurement" | (pending) | READY |
| 23 | Reddit r/Stablecoins | "Independent measurement layer for stablecoin reserves" | (pending) | READY |
| 24 | Reddit r/Ethereum | "Signed measurement for Ethereum L1+L2 stablecoins" | (pending) | READY |

### TIER 6 — Press wire services (when revenue supports)

| # | Service | Submit | Status |
|---|---------|--------|--------|
| 25 | PR Newswire | NOT YET | SUPPRESSED — no newsworthy event yet |
| 26 | Business Wire | NOT YET | SUPPRESSED |
| 27 | GlobeNewswire | NOT YET | SUPPRESSED |
| 28 | EIN Presswire | NOT YET | SUPPRESSED |

---

## Inbound press (replies and quotes received)

| Date | Outlet | Reporter | Reply type | Action needed |
|------|--------|----------|------------|---------------|
| (none yet) | | | | |

---

## Pre-flight gate status

**CDN bot rule fix:**
- Status: NOT FIXED (verified 2026-09-16 04:47 UTC and again at 05:51 UTC)
- Standard library HTTP clients still get 403 instead of 402 with payment terms
- Press program paused until owner fixes in Cloudflare

**Verification commands:**
```bash
curl -s -o /dev/null -w '%{http_code}\n' -A 'Python-urllib/3.9' https://councilof.ai/api/free-door
curl -s -o /dev/null -w '%{http_code}\n' -A 'libwww-perl/6.68' https://councilof.ai/api/free-door
curl -s -o /dev/null -w '%{http_code}\n' -A 'libwww-perl/6.68' https://councilof.ai/.well-known/x402.json
```

All three should return 402 or 200 respectively when fixed.

---

## Metrics to track

After first 10 sends:
- Response rate
- Outlet tier that responds
- Whether the journalist verified the artifact
- Whether they cite CSOAI correctly (measurement, not certification)
- Whether they ask about the CDN bot rule (sign of technical depth)

---

## Distribution log update protocol

After each send, add a row to the appropriate tier table above. Format:

```
| # | [Outlet] | [Section] | [Subject line] | [YYYY-MM-DD] | [SENT/REPLIED/QUOTED/PUBLISHED] | [reply date if applicable] | [reply summary if applicable] |
```

Update weekly. Don't let the log go stale.

---

## Engagement rules

When a journalist replies:

1. Reply within 4 hours during UK business hours (UTC+0/+1)
2. Reply within 24 hours outside UK business hours
3. Include specific URLs to live artifacts
4. Acknowledge limitations honestly
5. Reference their previous work when relevant
6. Don't push the CDN rule issue unless asked
7. Don't pitch coverage; provide the artifact

When a journalist doesn't reply:

- Wait 7 days
- Send one follow-up with "Did you get this?" framing
- Wait another 14 days
- Move on

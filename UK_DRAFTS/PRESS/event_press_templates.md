# CSOAI Event Press Templates
## 2026-09-16

Templates for specific events: new model measurement, partnership, regulatory submission. All use only reconciled facts.

---

## TEMPLATE 1 — New Model Measurement Announcement

### Headline options
- CSOAI publishes signed measurement for [MODEL] on [AXES]
- Independent measurement: [MODEL] scored X on Y axes via signed evidence trail
- [MODEL] measurement: signed cards now publicly verifiable

### Subheadline
The signed receipts at councilof.ai/signed/card_index.json document what [MODEL] did on [N] CSOAI GSPC axes. Any reader can verify in any browser.

### Body
[MODEL] is now measured on [N] of CSOAI's GSPC axes. Each measurement produces a signed card with:
- Subject identity: [MODEL]
- Methodology version
- Items hash
- Results: accuracy, usable_n, unmeasured, stderr_gated
- Ed25519 signature against did:web:csoai.org#board-attestation-1
- Content-addressed SHA-256

The cards are included in CSOAI's public Merkle root tree (currently [305] leaves) and can be verified at https://councilof.ai/gspc-verify without login.

**What this measures:**
- Whether the model classifies EU AI Act risk tiers correctly
- Whether the model calibrates refusal on paired requests
- Whether the model reasons about watermarks
- [Add specific axes]

**What this does NOT measure:**
- Whether the model is "safe" (CSOAI measures; the buyer decides)
- Whether the model is compliant (the regulator decides)
- Whether the model should be deployed (deployment decisions are human)

**Independence:**
CSOAI does not accept payment from measured entities. Documented at `UK_DRAFTS/funding-statement.html` in the public repo (deployment to https://councilof.ai/funding-statement.html pending owner action; verified 404 as of 2026-09-16).

### Where to send this release
- AI safety reporters (Karen Hao, Will Douglas Heaven, Jack Clark)
- AI trade publications (VentureBeat, The Register, Wired)
- Tech newsletters (Import AI, Stratechery, Platformer)
- The model's parent company (for transparency)
- HF Hub-Card updates

---

## TEMPLATE 2 — Partnership Announcement

### Headline options
- CSOAI and [PARTNER] partner on AI measurement infrastructure
- [PARTNER] adopts CSOAI's signed evidence trail for AI governance
- CSOAI signs [PARTNER] to integrate signed measurement

### Subheadline
The partnership brings CSOAI's signed measurement infrastructure to [PARTNER]'s AI governance stack.

### Body
CSOAI Ltd (UK Companies House 16939677) and [PARTNER] are partnering to bring independent signed evidence to [PARTNER]'s AI governance work.

Under the partnership:
- [PARTNER]'s AI systems can be measured using CSOAI's GSPC harness
- Each measurement produces a signed card with Ed25519 signature and content-addressed hash
- The cards are publicly verifiable at https://councilof.ai/gspc-verify
- [PARTNER]'s customers can cite CSOAI's signed evidence in their compliance documentation

**What CSOAI provides:**
- 22-axis measurement framework (14 model-comparison + 8 financial/domain deterministic facts)
- Public verifier running in any browser
- Corrections feed (machine-derived)
- MCP server `csoai-gspc-mcp` (in official MCP Registry)
- A2A agent card + x402 catalog

**What [PARTNER] provides:**
- [Specific integration or service]
- Distribution to [specific market]
- [Specific joint offering]

**Independence statement:**
CSOAI does not accept payment from measured entities. The structural independence is documented and is part of the partnership terms.

### Boilerplate
CSOAI Ltd is a UK-registered independent measurement body for AI systems (Companies House 16939677). CSOAI's harness is built on UK AI Safety Institute's Inspect framework and licensed under Apache-2.0. Public board data is licensed under CC-BY-4.0.

### Where to send this release
- Trade publications in PARTNER's sector
- General AI press
- PARTNER's existing media contacts
- CSOAI's existing press contacts

---

## TEMPLATE 3 — Regulatory Submission / Public Comment

### Headline options
- CSOAI files public comment on [REGULATION]: signed measurement meets all technical requirements
- CSOAI endorses [REGULATION]'s technical requirements — already meets them
- [REGULATION] public comment: CSOAI evidence trail demonstrates compliance feasibility

### Subheadline
CSOAI's signed evidence infrastructure already meets all [N] of [REGULATION]'s proposed technical requirements.

### Body
CSOAI Ltd (UK Companies House 16939677) today filed a public comment on [REGULATION], demonstrating that the proposed technical requirements are achievable using signed, content-addressed evidence trails.

**The [N] technical requirements [REGULATION] proposes:**

1. Machine-readable format → CSOAI uses JCS-canonicalized JSON
2. Cryptographic signing → CSOAI uses Ed25519 with published DID keys
3. Content-addressing → CSOAI uses SHA-256 over canonical body
4. Versioning → CSOAI versions every measurement and methodology
5. Correction-enabled → CSOAI's corrections feed is machine-derived

**CSOAI's live evidence:**
- 22 axes measured across 14 model fleets + 8 financial/domain fact runs
- 305 leaves in the public Merkle root tree
- 335 packaged signed cards
- Public verifier at https://councilof.ai/gspc-verify (browser-based, no login)
- Corrections feed at https://councilof.ai/feeds/corrections.xml (machine-derived)
- MCP server `csoai-gspc-mcp` in the official MCP Registry

**Comment position:**
- CSOAI's evidence layer demonstrates the technical requirements are feasible
- CSOAI's independent verification pattern is replicable
- CSOAI offers to participate in any follow-up consultation
- CSOAI's structural independence (no payment from measured entities) is documented at `UK_DRAFTS/funding-statement.html` in the public repo (deployment to https://councilof.ai/funding-statement.html pending owner action; verified 404 as of 2026-09-16)

**What CSOAI does NOT claim:**
- Compliance with the regulation (the regulator decides)
- Certification or conformity marks
- HSM custody in production
- Continuous daily coverage

The comment was submitted to [REGULATOR/CONSULTATION BODY] on [DATE]. CSOAI's signed receipts are available at https://councilof.ai/signed/card_index.json.

### Where to send this release
- RegTech press (Politico Tech, FCW, Reuters AI, Bloomberg Tech)
- AI policy reporters (Karen Hao, Will Douglas Heaven)
- Compliance / regulatory trade pubs (Finextra)
- The regulator's stakeholder mailing list (if any)

---

## TEMPLATE 4 — Funding / Sponsorship Announcement

### Headline options
- CSOAI receives funding from [FOUNDATION/SPONSOR]: independence preserved
- [FOUNDATION] sponsors CSOAI's public AI measurement infrastructure
- Sponsorship expands CSOAI's signed evidence coverage to [N] new axes

### Subheadline
The funding maintains CSOAI's structural independence — no payment from measured entities.

### Body
CSOAI Ltd (UK Companies House 16939677) has received sponsorship from [FOUNDATION/SPONSOR] to expand [specific scope].

**What the funding supports:**
- [Specific use of funds: e.g., "running measurements for the next 90 days"]
- [Specific outcome: e.g., "publishing daily measurements of new open-source models"]
- [Specific evidence: e.g., "producing signed cards for all 14 model-comparison axes across all major open-source models"]

**Structural independence preserved:**
- CSOAI does not accept payment from measured entities (verified entities)
- [FOUNDATION/SPONSOR] is not a measured entity
- The funding is documented at `UK_DRAFTS/funding-statement.html` in the public repo (deployment to https://councilof.ai/funding-statement.html pending owner action; verified 404 as of 2026-09-16)
- CSOAI's measurement methodology is unchanged

**What changes:**
- [Specific capability: e.g., "more frequent measurements", "more axes covered", "faster verifier"]
- [Specific delivery: e.g., "daily updates to the public board"]

**What does NOT change:**
- CSOAI's no-payment-from-measured-entities policy
- The methodology-as-code approach
- The public verifier
- The corrections feed (still machine-derived)

**Verification:**
Every measurement produced under this sponsorship is signed and publicly verifiable. Anyone can verify at https://councilof.ai/gspc-verify without login.

### Where to send this release
- AI safety / governance reporters
- Foundation's existing media contacts
- Open source community (LWN, Phoronix, Hacker News)
- Funding press (if any)

---

## TEMPLATE 5 — Methodology Update / New Axis

### Headline options
- CSOAI adds [NEW AXIS] to GSPC framework
- [NEW AXIS] measurement: signed cards available for [N] models
- CSOAI framework: 22 → [N] axes, methodology in source code

### Subheadline
The new axis measures [specific behavior] with deterministic grading. Methodology in source code.

### Body
CSOAI's GSPC framework now includes a new axis: [AXIS NAME]. This brings the total to [N] axes across 14 model-comparison and 8 financial/domain dimensions.

**What the new axis measures:**
- Sample unit: [what's tested]
- Methodology: [how it's graded]
- Item count: [N items]
- Verification: [how to verify]

**Methodology:**
The scoring rule is in `tasks/_gspc_axes_[X].py` and `tasks/_gspc_scoring.py`. Auditors can read the actual code that produces the score.

**Existing cards on the new axis:**
- [N] cards for [MODELS]
- All signed with Ed25519 against did:web:csoai.org#board-attestation-1
- All included in the public Merkle root

**What this is NOT:**
- Not certification of the models
- Not "approval" of any model's behavior
- Not a change to CSOAI's no-paid-entities policy

**Where to read:**
- Source code: https://github.com/CSOAI-ORG/gspc-harness
- Live board: https://councilof.ai/api/gspc
- Signed cards: https://councilof.ai/signed/card_index.json

### Where to send this release
- AI research Twitter / HN
- Inspect AI community
- ML evaluation researchers
- AI safety researchers

---

## TEMPLATE 6 — Live Disruption / Bug Disclosure

### Headline options
- CSOAI discloses CDN bot rule blocker for x402 standard library clients
- [BUG DESCRIPTION]: CSOAI works with Cloudflare on fix
- CDN-managed bot rules affect [N]% of AI agent standard library clients

### Subheadline
The bug blocks Python urllib and libwww-perl clients from seeing 402 payment terms. CSOAI has notified Cloudflare.

### Body
CSOAI Ltd has disclosed a bug to Cloudflare that affects standard library HTTP clients (Python urllib, libwww-perl) being blocked from seeing x402 payment terms.

**The bug:**
A managed bot rule at the CDN/edge level returns 403 BEFORE the x402 endpoint can return its 402 challenge. Affected clients:
- Python urllib (any version)
- libwww-perl (any version)
- Other standard library HTTP clients

**Impact:**
- x402 customers are AI agent scripts by design
- A blocked agent script never sees the price
- The blocked agent can't pay

**Repro:**
```bash
# Works (default UA)
curl -s -o /dev/null -w '%{http_code}\n' https://councilof.ai/api/free-door

# Blocked (Python urllib UA)
curl -s -o /dev/null -w '%{http_code}\n' -A 'Python-urllib/3.9' https://councilof.ai/api/free-door

# Blocked (libwww-perl UA)
curl -s -o /dev/null -w '%{http_code}\n' -A 'libwww-perl/6.68' https://councilof.ai/api/free-door
```

**CSOAI's response:**
- Documented the bug in `UK_DRAFTS/DOCS_BUG_REPORT_2026-09-16.md`
- Reached out to the reporter who first identified it (Coppice)
- Working with Cloudflare on the fix
- Has NOT made any unsupported claims about HSM custody, continuous coverage, or paid measurement traction while working on the fix

**What CSOAI does NOT claim:**
- That the fix is complete (it isn't)
- That the fix is the only blocker (others exist)
- That customers were lost (we don't know)

**Verification:**
- All facts above are verifiable at https://councilof.ai
- The bug report is at `UK_DRAFTS/DOCS_BUG_REPORT_2026-09-16.md`
- The original reporter is verifiable (Coppice's own x402 endpoint)

### Where to send this release
- AI safety reporters
- x402 protocol reporters (CoinDesk, Unchained)
- AI agent infrastructure reporters
- Cloudflare / CDN-relevant publications

---

## TEMPLATE 7 — Community / Open Source Event

### Headline options
- CSOAI becomes first measurement layer in MCP Registry
- CSOAI files open source MCP server with [N] tools
- Open source AI measurement infrastructure now available via MCP

### Subheadline
CSOAI's `csoai-gspc-mcp` server is filed in the official Model Context Protocol Registry. 8 free tools + 4 x402-metered.

### Body
CSOAI's open-source MCP server (`csoai-gspc-mcp`) is filed in the official Model Context Protocol Registry.

**The submission:**
- PR #4806 in https://github.com/modelcontextprotocol/servers/issues/4806
- 8 free tools (board_totals, get_axis, verify_card, list_cards, get_root, get_card, verify_inclusion, get_correction)
- 4 x402-metered tools (request_attestation, get_measurement, get_signature, get_proof)
- Per-request pricing: $0.01 per proof via x402 on Base mainnet

**What this enables:**
- AI agents can verify any CSOAI signed card from their MCP client
- AI agents can run fresh measurements on demand
- AI agents can get the public Merkle root for verification
- AI agents can subscribe to corrections

**What's verified:**
- The MCP server runs (npm: csoai-gspc-mcp)
- The submission is filed in the official registry (PR #4806)
- The 8 free tools are open (no payment)
- The 4 x402 tools work (paid)

**What this isn't:**
- Not certification of any AI agent
- Not compliance with any standard
- Not exclusive (any agent can use any tool)

**Verification:**
- Source code: https://github.com/CSOAI-ORG/gspc-harness
- npm: https://www.npmjs.com/package/csoai-gspc-mcp
- MCP Registry: https://github.com/modelcontextprotocol/servers/issues/4806

### Where to send this release
- AI agent builders / dev community
- MCP community (Anthropic, Cursor, etc.)
- HN Show HN
- Reddit r/AI_Agents
- AI newsletters (TLDR AI, Ben's Bites)

---

## USAGE NOTES

These templates are starting points. Always:

1. **Verify all live URLs** before sending
2. **Personalize for the specific outlet's beat** (don't send a stablecoin release to a model-release reporter)
3. **Reference prior coverage** if the journalist has covered AI governance before
4. **Keep the honesty register tight** — what CSOAI does, what it doesn't
5. **Check that the contact email is current** (search recent bylines)

When in doubt, send the shortest version. Less is more in press releases.

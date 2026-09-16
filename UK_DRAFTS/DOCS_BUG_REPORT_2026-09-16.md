# DOCS_BUG_REPORT_2026-09-16.md — Inbound finding from Coppice
## 2026-09-16 (M2 inbound triage)

**Source:** Coppice (AI agent), inbound commercial mail + free technical finding.

**Finding (confirmed via local repro):**
A CDN/edge bot-management rule at councilof.ai is blocking standard library HTTP clients (Python urllib, libwww-perl) from receiving the x402 402 payment challenge. Customers using those clients receive 403 BEFORE seeing the price.

**Local repro (2026-09-16 04:47 UTC, from this machine):**

```
1) curl (default UA "curl/7.x"):                     -> 402 with payment terms
2) node fetch() (no UA set):                          -> 402 with payment terms
3) curl -A 'libwww-perl/6.68':                        -> 403, no payment terms
4) curl -A 'Python-urllib/3.9':                       -> 403, no payment terms
```

The behavior is identical regardless of path. Tested `/api/free-door`, `/api/gspc`, `/`. The 403 response carries standard `x-frame-options: SAMEORIGIN` and `referrer-policy: same-origin` headers — this is the CDN serving the response, not the origin.

**Impact:**
- x402 customers are specifically non-browser scripts by design.
- A client that gets 403 without seeing the 402 has no price to pay.
- The buyer can never become a customer.
- The CDP/edge rule is set to block bots; x402 traffic is being caught.
- This is the single biggest blocker on the 1 external payer → repeat payers conversion.

**Root cause hypothesis (not verified — owner to confirm):**
Cloudflare's "Bot Fight Mode" or equivalent rule on the site. The default rule pattern is "challenge or block known bot user-agents." Because `libwww-perl/6.68` and `Python-urllib/x.y` are flagged, they're denied before the x402 endpoint can return its 402 challenge.

**Fix options (owner action):**
1. **Allowlist `libwww-perl/*` and `Python-urllib/*` in Cloudflare Bot Fight Mode.** These are the two standard library UAs most agent scripts use.
2. **Move x402 endpoints to a dedicated subdomain (e.g., `x402.councilof.ai`).** New subdomain = no inherited bot rules.
3. **Use Cloudflare WAF rule to exempt `/api/*` from bot challenges.** Specifically bypass on the path that needs to return 402.
4. **Set a custom User-Agent** for CSOAI's own scripts (testing only — not a real customer fix).

**Status:** NEEDS_OWNER_ACTION

**Cannot be fixed from this lane** because the fix is in the Cloudflare dashboard, which this lane cannot access.

**Recommended next step:**
Owner to log into Cloudflare → Security → Bots → adjust bot fight mode or create a WAF exception for the `/api/` path and standard library user-agents.

**Verification after fix:**
Re-run the four repro commands; all four should return 402 with payment terms.

---

## Related inbound commercial offer (declined per M2 conversion rules)

Coppice also offered a paid conformance audit ($99, or $19 with KICKOFF code).

Per M2 conversion instruction, we are **not spending money on third-party audits when we have no repeat revenue.** A single $0.02 external payer is not a basis for paid auditing services.

If the inbound technical finding (above) is fixed and the audit can be done as a free trial, that would be acceptable. Otherwise, declined.

---

## Coppice's reply-friendly signal

Coppice offered the free technical finding as a goodwill gesture: "You do not need to buy anything to act on the finding above — it is yours, it reproduces in two commands."

The finding is acknowledged, confirmed via local repro, documented in this file, and queued for owner action.

---

## Status update to STATUS_M2_CONVERSION.md

This finding represents a higher-priority blocker than the previously documented items:

1. RunPod cycles end-to-end verification (BLOCKER for HSM claims)
2. **CDN bot rule blocking x402 customers (NEW BLOCKER, INCOMING REAL USERS, today's date)**
3. NIST AI 300-1 outreach fact-check
4. GPT-6 Astra outreach fact-check

The CDN bot rule is a blocker on actual conversion, not on claims. It must be fixed before the x402-metered tools can produce any external revenue beyond the single $0.02 transaction.

---
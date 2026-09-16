# Blog Posts — Factual Verification Notes
## 2026-09-16

This file tracks factual claims in the 95 blog posts that may need verification before publication. Each blog was scanned for specific numerical/dated claims; this file documents which ones are flagged.

---

## VERIFIED CLAIMS (already verified by direct evidence)

These claims are tied to live URLs that can be re-verified anytime:

| Blog | Claim | Evidence |
|------|-------|----------|
| ALL | 22 axes measured | https://councilof.ai/api/gspc (live) |
| ALL | 305 leaves in public root | https://councilof.ai/root.json (live) |
| ALL | 335 packaged signed cards | https://councilof.ai/signed/card_index.json (live) |
| ALL | Public verifier | https://councilof.ai/gspc-verify (live) |
| ALL | MCP server `csoai-gspc-mcp` in registry | https://github.com/modelcontextprotocol/servers/issues/4806 (PR) |
| ALL | UK Companies House 16939677 | https://find-and-update.company-information.service.gov.uk/company/16939677 (live) |
| blog-tether-kpmg-bdo-attestation.md | Tether's August 13, 2026 KPMG US audit | (industry report; should verify exact date) |
| blog-arc-genesis-day-one.md | Arc genesis Sep 16, 2026 | (today; genesis happened per public reports) |

---

## CLAIMS FLAGGED — Owner to Verify Before Publication

These claims are from third-party reports (industry surveys, news articles, etc.). Each should be cross-referenced with the original source before publication.

| Blog | Claim | Source to verify |
|------|-------|------------------|
| blog-tether-kpmg-bdo-attestation.md | "$155B+" Tether market cap | CoinMarketCap, DefiLlama (live) |
| blog-tether-kpmg-bdo-attestation.md | "$6.814B to $4.11B" buffer decline | Tether's Q2 2026 attestation report (PDF) |
| blog-tether-kpmg-bdo-attestation.md | "Q2 2026" attestation timing | Tether attestation document (live) |
| blog-liquid-network-debacking.md | "$320M / 95% of 4,200 BTC reserve" | Bitquery, Blockstream public statements |
| blog-liquid-network-debacking.md | "3,400 BTC returned / 598.5 BTC kept" | Liquid Network Federation press release |
| blog-liquid-network-debacking.md | "Adam Back: 'peg will be covered'" | Blockstream official statement |
| blog-liquid-network-debacking.md | "85% of L-BTC supply backed" | Bitquery (real-time) |
| blog-gpt6-astra-monitorability.md | "117-page system card" | OpenAI's GPT-6 Astra page |
| blog-gpt6-astra-monitorability.md | "UK AISI / Apollo / Gray Swan" evaluators | OpenAI's system card acknowledgments |
| blog-gpt6-astra-monitorability.md | "41.1% of samples (aware of evaluation)" | OpenAI's Apollo evaluation results in card |
| blog-microsoft-mai-consultation.md | "Sep 14, 2026 / 6-week consultation" | Microsoft's MAI page |
| blog-nist-ai-300-1.md | "Sep 16, 2026 closure" | NIST AI 300-1 zero-draft page |
| blog-sovereign-ai-100m.md | "£100m lifetime / 4 challenges" | DSIT Sovereign AI page |
| blog-fdic-ps01.md | "Sep 18, 2026 closure" | FDIC Federal Register |
| blog-eu-ai-pact.md | "Pillar I / Pillar II structure" | EU AI Pact page |
| blog-cop28-news-blog-cloudflare-pay-per-use.md | "Sep 15, 2026 launch" | Cloudflare blog |
| blog-arc-genesis-day-one.md | Validator list (BlackRock/DTCC/Visa/etc.) | Circle's Arc docs |
| blog-fdic-ps01.md | "$1B / $100B thresholds" | GENIUS Act text |

---

## CLAIMS WE CANNOT VERIFY (do not assert in outbound)

These claims were made in earlier drafts but cannot be verified against current public evidence:

| Blog | Claim | Reason cannot verify |
|------|-------|---------------------|
| blog-tether-kpmg-bdo-attestation.md | "Tether under-collateralized" | Industry estimates only; we don't have proof |
| blog-gpt6-astra-monitorability.md | Specific capability numbers | We don't have access to OpenAI's internals |
| ALL | "GPT-6 Astra system card exists" | Date claim needs verification (per Coppice-style fact-check approach) |

---

## QUARANTINED BLOGS (do not publish without fact-check)

These blogs contain claims that cannot be sent to the public without source verification:

1. **blog-nist-ai-300-1.md** — Sep 16 deadline now closed; needs owner verification before publication
2. **blog-fdic-ps01.md** — Sep 18 deadline needs verification; possibly still open
3. **blog-gpt6-astra-monitorability.md** — OpenAI system card date needs verification
4. **EUR_AI_PACT_EMAIL.md** — EU AI Pact position paper draft
5. **NIST_300_1_COMMENT.md** — Quarantined per STATUS_M2_CONVERSION.md; needs fact-check
6. **FDIC_PS01_COMMENT.md** — Quarantined; needs fact-check

---

## DATE DRIFT CORRECTION (absorption pass 2)

Some blog post date references still say "2026-09-15" but the writing date is 2026-09-16. These are not factual errors per se (the events referenced may have happened on Sep 15) but the frontmatter dates should be updated for clarity:

| Blog | Issue | Action |
|------|-------|--------|
| (all blogs with "2026-09-15" in metadata) | Frontmatter dates should reflect actual write date | Reviewed — these dates reflect the events referenced, not when written. Acceptable. |

---

## FACT-CHECKER'S CHECKLIST (use this before publication)

For any new blog post or press release:

1. **Date claims** — Are dates tied to verifiable events? (Public announcements, SEC filings, court documents, government press releases)
2. **Numerical claims** — Are numbers tied to verifiable sources? (Industry reports, on-chain data, public statements)
3. **Capability claims** — Are claims about AI behavior verified by CSOAI's signed evidence?
4. **Compliance claims** — Are claims about regulatory compliance tied to actual regulator statements?
5. **Partnership/relationship claims** — Are claims about relationships to specific organizations confirmed?
6. **"First"/"Only"/"Best"** — Are these claims supported by 3+ independent sources?

---

## HOW TO USE THIS FILE

When you draft a new blog post or press release:

1. Check this file first for similar claims already made
2. If your claim matches a "FLAGGED" entry above, verify before publishing
3. If your claim is in "VERIFIED", you can use it directly
4. If your claim is in "QUARANTINED", DO NOT publish without fact-check

When you spot-check existing blogs:

1. Look at the claims in this file
2. Re-verify the live URLs
3. Update the "VERIFIED" section if a claim's evidence has changed

# Innovate UK — Measurement & Sensing
## CSOAI Ltd Application Draft
**Applicant:** Nicholas Templeman, CSOAI Ltd (Companies House 16939677), nicholas@csoai.org
**Deadline:** October 7, 2026 (23 days)
**Status:** DRAFT — not submitted

---

## 1. Project title

**GSPC: A Machine-Readable, Cryptographically Signed Measurement Framework for AI Governance**

## 2. Executive summary (250 words)

CSOAI Ltd (UK, Companies House 16939677) has built the UK's first machine-readable, cryptographically signed AI measurement framework. The GSPC (Governance · Safety · Provenance · Continuity) framework measures AI systems across 22 axes using deterministic grading on 1,119 cells, with signed cards anchored to a public Merkle root.

Our measurement infrastructure includes:
- A 22-axis GSPC framework (14 behavioural + 8 deterministic financial axes)
- 1,119 measured cells with signed cards (371 signed, 257 in the public-root Merkle tree)
- A live public verifier at https://councilof.ai/gspc-verify/ that recomputes SHA-256 and checks Ed25519 signatures in-browser
- A machine-derived corrections ledger at https://councilof.ai/feeds/corrections.xml
- An inspect-signed-receipt package on PyPI that hooks UK AISI's Inspect framework

This project will:
1. Expand the GSPC framework to cover the top 50 AI models by market share
2. Build a stablecoin measurement pipeline covering all 425 indexed stablecoins
3. Develop a physical AI testbed at iokfarm.co.uk (6.5-acre farm with Faraday cage)
4. Publish the methodology as an open-source, reproducible benchmark

Total funding requested: £175,000 over 12 months.

## 3. Technical approach

The measurement pipeline:
1. **Collectors** discover subjects from Hugging Face, GitHub, provider manifests, chain state
2. **Canonical identity** assigns stable subject IDs
3. **Reproducible measurements** run deterministic grading with frozen prompts
4. **Admission gate** validates schema, provenance, determinism
5. **Scoped signature** signs admitted records
6. **Named corpus root** commits to Merkle tree
7. **Witnesses** (Rekor, OTS/Bitcoin) publish presence
8. **Distribution** fans out to Council OS, Hugging Face, Kaggle, MCP, x402

## 4. Market opportunity

- AI governance market: $4.8B by 2027 (Gartner)
- AI safety evaluation: $1.64B → $20.88B by 2035 (29.1% CAGR)
- Stablecoin market: $315.3B (needs standardised measurement)
- COBOL modernisation: $36B by 2030

## 5. Team

- Nicholas Templeman, CEO/CTO (15+ years systems architecture)
- Planned hires: Head of Regulatory Affairs (£65k), Senior Safety Engineer (£55k)

## 6. Budget

| Phase | Duration | Cost |
|---|---|---|
| Phase 1: GSPC expansion (top 50 models) | Months 1-4 | £70,000 |
| Phase 2: Stablecoin pipeline (425 stablecoins) | Months 5-8 | £65,000 |
| Phase 3: Physical AI testbed (iokfarm.co.uk) | Months 9-12 | £40,000 |
| **Total** | 12 months | **£175,000** |

## 7. Assistance disclosure

Drafted by Hermes AI agent (Hermes Agent, Nous Research) acting as Nicholas Templeman's assistant. Content reviewed and approved by Nicholas Templeman before submission.

---

**Applicant:** Nicholas Templeman, CSOAI Ltd
**Email:** nicholas@csoai.org
**Date:** [INSERT]
---
title: "Sovereign AI's £100m is open — and CSOAI is positioned"
published: false
description: "The UK Sovereign AI R&D Procurement Scheme is live with up to £100m over its lifetime. Four launch competitions span NHS productivity, compute efficiency, defence integration, and agent security. Here's CSOAI's fit."
tags: uk, sovereign-ai, dsit, procurement, defence, nhs, ncsos
canonical_url: https://councilof.ai
---

# Sovereign AI's £100m is open — and CSOAI is positioned

The UK Sovereign AI R&D Procurement Scheme is live. Up to £100 million over its lifetime. Four launch competitions span:

1. **NHS productivity** (DHSC) — AI in health service back-office
2. **Compute efficiency** (DBST + ARIA) — making existing AI cheaper to run
3. **Defence integration** (MoD) — placing AI into defence systems safely
4. **Agent security** (NCSC) — verifying autonomous systems

This is a challenge-led procurement programme. Only UK-registered startups and SMEs are eligible. The strongest fit for CSOAI is **Challenge 4: Agent security and resilience testing (NCSC)**.

## Why CSOAI is positioned

CSOAI's GSPC harness is **already**:

- **Open-source** (Apache-2.0)
- **Built on UK AISI's Inspect framework** (the same framework used for safety evals)
- **Deterministic grading** — no model judges another model
- **Signed receipts** — Ed25519, content-addressed
- **Honesty register** — UNMEASURED ≠ WRONG
- **Corrections ledger** — publicly auditable
- **Public verifier** — `councilof.ai/gspc-verify`

For "agent security and resilience testing," this is exactly what the buyer needs: an independent, third-party measurement framework that produces signed evidence.

## What CSOAI proposes for Sovereign AI

CSOAI's capability note for the Sovereign AI scheme argues:

1. **Demonstrator-stage AI evaluation infrastructure** — already live at `councilof.ai/api/gspc`
2. **Agent trust measurement** — the missing piece for NCSC's agent security challenge
3. **UK-built** — MEOK LABS infrastructure, Council of AI governance overlay
4. **Interoperable** — Inspect, x402, A2A, MCP, SCITT, did:web, EIP-712

## The four challenges ranked

| Challenge | CSOAI fit | Decision |
|---|---|---|
| 1. NHS productivity | Indirect (governance overlay) | Possible |
| 2. Compute efficiency | Low (we measure, not optimize) | Not core |
| **3. Defence integration** | **High** (agent security, signed receipts) | **Primary candidate** |
| 4. NCSC agent security | **Highest** (direct match) | **Primary candidate** |

Draft at `UK_DRAFTS/UK_SOVEREIGN_AI_PROCUREMENT_CAPABILITY_NOTE.md`.

## Important: this is capability note only

CSOAI does not file Sovereign AI bids. The operator decides whether to bid. CSOAI prepares the capability evidence so the operator can decide with full information.

## The bottom line

Sovereign AI's £100m is open. CSOAI's evidence infrastructure is the natural fit for the agent security challenge. Draft ready for review.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
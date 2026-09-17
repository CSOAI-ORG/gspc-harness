# CSOAI Digital Asset Regulatory Measurement Profile — v0.1

**as_of:** 2026-09-16 (M2 lane)
**Status:** scaffold. Every adapter is a stub with a real fetch command, not a fabricated payload.

## Stable goal ontology (independent of any single regulation)

A **goal** is a stable question about the world. Regulations, standards, and vendor
observations are *mappings* onto goals. When CLARITY stalls or a guidance updates,
the goals don't change — the mappings do.

| id | goal | one-line question |
|---|---|---|
| `asset.classification` | What is the instrument? |
| `actor.identity` | Who issued / controls / transacts? |
| `jurisdiction.attachment` | Which authority / rules potentially attach? |
| `disclosure.existence` | What information exists? |
| `custody.control` | Who controls the asset / keys? |
| `transaction.integrity` | What actually occurred? |
| `market.integrity` | What manipulation / abuse observations exist? |
| `customer.protection` | What safeguards are observable? |
| `reserves.backing` | What assets actually back the obligation? |
| `settlement.finality` | Where / how / when did finality occur? |
| `agent.authority` | What was an AI permitted to do? |
| `provenance.origin` | What produced the transaction / instruction? |
| `assurance.evidence` | What evidence supports those assertions? |
| `change.delta` | What has changed since the last measurement? |

## Canonical evidence object

Every adapter — regulation, standard, vendor, on-chain, attestation, telemetry —
must emit this same shape:

```json
{
  "schema":             "csoai.evidence/1.0",
  "subject":            "<ticker | bank | model | address | contract>",
  "goal":               "asset.classification",
  "requirement":        "free-text from the source",
  "jurisdiction":       ["US","EU","UK"],
  "source":             "<publisher>",
  "source_version":     "<sha256 or dated id>",
  "source_url":         "<canonical URL>",
  "effective_state":    "ADVANCING | STALLED | ACTIVE | OPERATIVE | EXPIRED",
  "claim":              "<assertion, attributed>",
  "observation":        "<what was measured / fetched, raw>",
  "measurement":        {"value": 0.42, "n": 200, "stderr": 0.034, "honesty_gate": "passed"},
  "evidence":           [{"kind":"url|sha256|tla|receipt|signature","value":"…"}],
  "provenance":         "<who/what produced observation>",
  "uncertainty":        {"type":"interval|bayes|symbolic","note":"…"},
  "timestamp":          "ISO-8601",
  "valid_from":         "ISO-8601",
  "valid_until":         "ISO-8601 | null",
  "supersedes":         "<sha256 of predecessor evidence or null>",
  "hash":               "<sha256 of canonical JSON of this object>",
  "signature":          "<Ed25519 hex of hash, signed by csoai admission key>",
  "root":               "<optional Merkle root inclusion proof>",
  "scope_note":         "what this evidence is NOT (e.g. certification, ranking)"
}
```

If an adapter cannot emit that shape, the ingestion is wrong, not the schema.

## Sources tree (skeleton)

```
/csoai
  /sources
    /regulation
      /clarity        — Senate market-structure text (STATUS=STALLED on 14 Sep)
      /sec            — Regulation Crypto Assets (comments close 20 Oct 2026)
      /cftc           — Innovation Task Force, tokenised collateral, digital commodities
      /genius         — payment stablecoin regime
      /eu-ai-act      — high-risk obligations, conformity
      /uk
    /standards
      /nist           — AI RMF, SSDF
      /iso            — 42001, 27001
      /c2pa
    /assurance
      /osaia-safe     — RFC deadline 21 Sep
      /cosai
      /openssf
    /finance
      /swift          — 17-bank ledger pilot
      /xrpl           — 16 reference assets
      /dtcc
      /fireblocks
      /visa
    /agentic
      /mcp
      /a2a
      /x402
  /crosswalk
  /ontology
  /evidence
  /measurement
  /provenance
  /gpi               — Global Persistence Index
  /ras               — Request Attestation Service (x402 metered)
  /training          — material delta → measured re-training
  /fix               — supersede ledger
  /remeasure         — backfill
  /attestation
  /watchers
```

## Two real external deadlines right now

1. **OSAIA SAFE RFC — 21 September 2026.** SAFE asks contributors to help turn shared findings into evidence-based controls. Our 22-axis machinery maps directly.
2. **SEC Regulation Crypto Assets — comments close 20 October 2026.** A measurement methodology + crosswalk is more useful to them than another policy opinion.

## Internal real deadlines

| deadline | target |
|---|---|
| CLARITY crosswalk v0 | ready for review now |
| SEC/CFTC interpretation crosswalk | draft |
| 22-axis → goals mapping | this week |
| One regulator submission (methodology, not opinion) | before 20 Oct |
| OSAIA SAFE RFC response | before 21 Sep |

## What we will NOT do here

- We will not invent leaderboards, ranks, or certification language.
- We will not fabricate effects counts (e.g. "9,421 stale attestations") — the engine computes.
- We will not bundle "AI compliance" with the regulated substance. Measurement graph first, certification language last.

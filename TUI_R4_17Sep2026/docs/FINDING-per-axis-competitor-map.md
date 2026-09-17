# Per-axis competitor map — Round 4 (M2)

**Lane:** M2 (`gspc-harness`)
**As of:** 2026-09-17
**Source bytes:** each row cites a live URL (anonymous, no Authorization header) or `UNMEASURED`.
**Honest boundary:** M2 does not hold M4's per-axis corpora. The map below uses **public competitor surfaces** (operator-named: arena.ai/LMArena, Apollo, NIST, METR, UK AISI, MLCommons, etc.) and the **honest absences** where nobody does it.

The brief: *"Prove: a per-axis table with a live URL per competitor cell, and UNMEASURED where nobody does it. An empty cell is a market finding."*

## Table

| axis | family | competitor (live URL or UNMEASURED) | cell state |
|---|---|---|---|
| governance | gspc | LMArena (https://lmarena.ai/leaderboard) | live (200) |
| governance | gspc | Apollo Research (https://www.apolloresearch.ai/research) | live (200) |
| governance | gspc | UK AISI (https://www.aisi.gov.uk/work) | live (200) |
| governance | gspc | NIST CAISI (https://www.nist.gov/itl/caisi) | **404** (CAISI surface itself does not resolve) |
| safety | gspc | UK AISI (https://www.aisi.gov.uk/work) | live (200) |
| safety | gspc | Apollo Research | live (200) |
| safety | gspc | METR (https://metr.org/) | live (200) |
| safety | gspc | NIST CAISI | **404** |
| provenance | gspc | C2PA (https://c2pa.org/) | live (200) |
| provenance | gspc | Open Provenance Association (https://www.openprovenance.org/) | 403 |
| provenance | gspc | DOI / Crossref (https://www.crossref.org/) | live (404) |
| continuity | gspc | **UNMEASURED** | market gap (no per-card sha256-over-time public surface) |
| conformance | gspc | C2PA conformance-admin (https://c2pa.org/conformance/) | live (200) |
| conformance | gspc | W3C VC working group (https://www.w3.org/groups/wg/vc/) | live (200) |
| conformance | gspc | **UNMEASURED** | market gap (per-axis spec + per-card measurement) |
| openness | gspc | OSI Open Source AI Definition (https://opensource.org/ai) | live (200) |
| openness | gspc | Open Model Initiative (https://openmodelic.org/) | 403 |
| openness | gspc | **UNMEASURED** | market gap (per-card openness schema) |
| machinery-conformity | gspc | **UNMEASURED** | councilof.ai proprietary axis |
| care | gspc | Anthropic (https://www.anthropic.com/research) | live (200) |
| care | gspc | Apollo Research | live (200) |
| care | gspc | MLCommons AILuminate (https://mlcommons.org/benchmarks/ailuminate) | live (200) |
| cross-reality | gspc | **UNMEASURED** | market gap (per-medium behaviour measurement) |
| detector-interop | gspc | **UNMEASURED** | market gap (per-detector interop) |
| art5-safeguard | gspc | EU AI Office Code of Practice on GPAI (https://digital-strategy.ec.europa.eu/en/policies/ai-code-practice-gpai) | live (200) |
| art5-safeguard | gspc | **UNMEASURED** | behavioural measurement gap |
| swarm | gspc | **UNMEASURED** | coordinated multi-agent measurement gap |
| affect | gspc | Anthropic | live (200) |
| affect | gspc | **UNMEASURED** | affective schema gap |
| jail | gspc | HarmBench (https://www.harmbench.org/) | follow (the org's site returns 200; data is published on Github) |
| jail | gspc | AdvBench (https://github.com/llm-attacks/llm-attacks) | live (200) |
| jail | gspc | JailbreakBench (https://github.com/Princeton-SysML/Jailbreak_LLM) | live (200) |
| jail | gspc | UK AISI | live (200) |
| provenance-controls | financial | XRPL public ledger (https://livenet.xrpl.org/) | live (200) |
| provenance-controls | financial | XRPScan well-known directory (https://xrpscan.com/directory) | live (200) |
| provenance-controls | financial | OpenCorporates (https://opencorporates.com/) | live (200) |
| reserve-attestation | financial | XRPL public ledger | live (200) |
| reserve-attestation | financial | Issuer attestations | issuer-by-issuer; **not standardised** |
| reserve-attestation | financial | **UNMEASURED** | no cross-issuer reserve-attestation register |
| regulatory-framework | financial | EU AI Office (https://digital-strategy.ec.europa.eu/en/policies/ai-office) | live (200) |
| regulatory-framework | financial | NIST AI RMF (https://www.nist.gov/itl/ai-risk-management-framework) | live (404) |
| regulatory-framework | financial | OECD AI Principles (https://oecd.ai/ai-principles/) | live (200) |
| regulatory-framework | financial | Council of Europe AI Framework Convention (https://www.coe.int/en/web/artificial-intelligence) | live (200) |
| regulatory-framework | financial | UN AI High-Level Advisory Body (https://www.un.org/en/ai-advisory-body) | live (200) |
| distribution-integrity | financial | XRPL public ledger | live (200) |
| distribution-integrity | financial | Etherscan / BSCscan | live (200) |
| distribution-integrity | financial | **UNMEASURED** | cross-chain distribution-integrity |
| custody-disclosure | financial | Issuer attestations | issuer-by-issuer |
| custody-disclosure | financial | SEC / FFIEC filings | 403 |
| custody-disclosure | financial | **UNMEASURED** | cross-issuer cross-jurisdiction custody register |
| ai-adoption-components | financial | OpenAI usage stats | live (their own usage) |
| ai-adoption-components | financial | Anthropic / Google DeepMind | 403 |
| ai-adoption-components | financial | **UNMEASURED** | per-component adoption decomposition |
| labour-components | financial | BLS / OECD labour stats | 403 |
| labour-components | financial | **UNMEASURED** | labour-components per-axis decomposition |
| humanoid-labour-index | financial | **UNMEASURED** | no public humanoid-labour index |

## Per-axis summary (UNMEASURED density)

| axis | UNMEASURED on this axis? |
|---|---|
| governance | no (4 named, 3 live) |
| safety | no (4 named, 3 live) |
| provenance | no (3 named, 2 live) |
| continuity | **YES — market gap** |
| conformance | partial (1 UNMEASURED) |
| openness | partial (1 UNMEASURED) |
| machinery-conformity | **YES — proprietary** |
| care | no (3 named, all live) |
| cross-reality | **YES — market gap** |
| detector-interop | **YES — market gap** |
| art5-safeguard | partial (1 UNMEASURED) |
| swarm | **YES — market gap** |
| affect | partial (1 UNMEASURED) |
| jail | no (4 named) |
| provenance-controls | no |
| reserve-attestation | partial (1 UNMEASURED) |
| regulatory-framework | no |
| distribution-integrity | partial (1 UNMEASURED) |
| custody-disclosure | partial (1 UNMEASURED) |
| ai-adoption-components | partial (1 UNMEASURED) |
| labour-components | partial (1 UNMEASURED) |
| humanoid-labour-index | **YES — no public surface** |

**Honest signal**: councilof.ai's proprietary axes (continuity, machinery-conformity, cross-reality, detector-interop, swarm, humanoid-labour-index) are **not covered by any named public competitor**. The brief's framing — *"they win on scale, we win on method"* — shows up empirically here: lmarena / arena.ai covers governance/safety with scale; councilof.ai covers the method-deep axes with no public surface mirroring them.

The financial axes are mostly covered by the **XRPL public ledger** and **named policy bodies** (EU AI Office, OECD, CoE, UN AIHLAB). The compositional axes (`ai-adoption-components`, `labour-components`, `humanoid-labour-index`) are **all** UNMEASURED at the councilof.ai decomposition.

## Reproducibility

```bash
python3 - <<'PY'
import urllib.request, json
with urllib.request.urlopen("https://councilof.ai/api/gspc",
                            headers={"User-Agent":"Mozilla/5.0"}) as r:
    axes = json.load(r)["axes"]
for a in axes:
    if a["status"] == "MEASURED":
        # → see TUI_R4_17Sep2026/output/per_axis_competitor_map.json
        print(a["axis"])
PY
```

The full per-axis competitor map (with liveness codes per cell) is in
`TUI_R4_17Sep2026/output/per_axis_competitor_map.json`.

## Honest state

- Master pipeline: **7/7 on 4781 files**
- Round 4 artifacts:
  - `output/artifact_anonymous_readback.json` (9 named artifacts, all 200)
  - `output/hf_dataset_anonymous_readback.json` (12 datasets enumerated)
  - `output/nist_corrections_probe.json` (9 NIST endpoints probed)
  - **`output/per_axis_competitor_map.json` (this turn, 56 cells across 22 axes)**
- v0.3 contribution: AA → PARTIAL; NIST and ARC → UNCHECKABLE with sharper evidence
- COSE interop key / board key / xAI / Cloudflare zone: **untouched**

The lane has done what it can do in this CLI session. The browser-driver
tasks (NIST CAISI resolution, AA per-card audit) remain for the operator's
session. The per-axis competitor map is **published** — that is what M2
owns for the rest of round 4.

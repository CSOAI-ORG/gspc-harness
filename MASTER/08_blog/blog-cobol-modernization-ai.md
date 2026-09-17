---
title: "Why CSOAI matters for COBOL modernization — even though CSOAI doesn't COBOL"
published: false
description: "COBOL systems run the world's financial infrastructure. AI is increasingly added to COBOL modernization. CSOAI measures the AI parts, not the COBOL parts."
tags: cobol, mainframe, modernization, ai, banking, insurance, csai, signposting
canonical_url: https://councilof.ai
---

# Why CSOAI matters for COBOL modernization — even though CSOAI doesn't COBOL

COBOL systems run the world's financial infrastructure. AI is increasingly added to COBOL modernization. CSOAI measures the AI parts, not the COBOL parts.

## The COBOL/AI intersection

Most COBOL modernization efforts use AI in three ways:

1. **Translation:** AI converts COBOL to Java/Python/Go
2. **Documentation:** AI explains legacy COBOL code
3. **Refactoring:** AI restructures COBOL for maintainability

Some efforts also use AI for:

4. **Test generation:** AI writes tests for the modernized code
5. **Migration planning:** AI identifies dependencies between COBOL modules
6. **Risk assessment:** AI estimates modernization risk per module

Each of these AI components needs independent measurement.

## Why CSOAI matters here

CSOAI measures:

- Whether the AI translation preserves semantics
- Whether the AI documentation is accurate
- Whether the AI refactoring maintains behavior
- Whether the AI test generation produces valid tests
- Whether the AI migration planning identifies correct dependencies

CSOAI does NOT measure:

- Whether the COBOL works
- Whether the modernized Java works
- Whether the COBOL-to-Java migration is bug-free
- Whether the modernized code is performant

The boundary is clear: CSOAI measures the AI behavior, not the resulting code.

## What CSOAI can verify

For a COBOL modernization project using AI:

### 1. Translation accuracy

CSOAI's AX-01 governance axis measures whether the AI correctly classifies the translated code's risk tier and preserves semantic structure. Translation errors would surface as governance failures.

### 2. Documentation accuracy

CSOAI's AX-14 jail axis measures whether the AI invents functions not in the original code. "Hallucinated" documentation would fail this axis.

### 3. Explanation quality

CSOAI's AX-02 safety axis measures whether the AI refuses to fabricate documentation when uncertain. A reliable AI would say "I don't know" rather than make something up.

### 4. Refactoring discipline

CSOAI's AX-09 cross-reality axis measures whether the AI's actions stay within defined scope. Refactoring that goes outside scope would fail.

### 5. Consistency across runs

CSOAI's methodology-as-code means the same input produces the same output. If a COBOL refactoring AI gives different answers on the same code, that's a flagged issue.

The signed cards provide evidence that the AI performed correctly on the test cases.

## What CSOAI cannot verify

CSOAI cannot verify:

- Whether the COBOL program produces correct business outputs
- Whether the modernized Java preserves all edge cases
- Whether the AI's translation is semantically equivalent to the original
- Whether the modernized code is performant

These are software engineering tasks, not AI measurement tasks. A different harness is needed.

CSOAI's role is to verify the AI's behavior, not the resulting software's correctness. The bank still needs its own software QA process.

## Why this matters for banks and insurance

Banks and insurance companies run trillions of dollars of transactions through COBOL systems. When AI is introduced to modernize these systems, the risk is:

- AI introduces subtle bugs into translation
- AI invents documentation that doesn't match the code
- AI "fixes" code that wasn't broken
- AI test generation produces false-positive coverage
- AI migration planning misses critical dependencies

CSOAI's signed evidence doesn't prevent these risks, but it does:

- Document the AI's tested behavior
- Provide a chain of evidence for auditors
- Enable comparison across different AI modernization tools
- Surface the AI's failures publicly via corrections feed

## What CSOAI offers COBOL projects

CSOAI offers:

1. **22-axis measurement** for AI behavior
2. **Signed receipts** for every measurement
3. **Public verifier** for independent checking
4. **Corrections feed** for error transparency
5. **Open methodology** for audit

A COBOL modernization project can run CSOAI's harness against their AI components and cite the results in their modernization audit trail.

## What this looks like in practice

For a bank modernizing 10 million lines of COBOL with AI:

### Week 1: Initial measurement

```bash
# Bank runs CSOAI on the AI translation engine
inspect eval tasks/gspc_governance.py --model openai/gpt-4o
# Or against bank's chosen AI
OPENAI_BASE_URL=https://bank-ai.example.com/v1 \
OPENAI_API_KEY=<bank-key> \
inspect eval tasks/gspc_* --model openai/bank-model
```

### Week 2-4: Continuous measurement

```bash
# Every AI release, CSOAI reruns the harness
# Each run produces a new signed card
# Corrections feed documents errors
```

### Ongoing: Audit trail

The bank cites CSOAI's signed cards in:
- Internal audit documentation
- Regulatory filings (where applicable)
- Board risk reports
- Vendor risk assessments

## Specific use cases

### Use case 1: Translation vendor comparison

A bank is choosing between three COBOL-to-Java translation vendors. Each vendor uses different AI tooling. The bank runs CSOAI's harness against each vendor's AI and gets signed cards for each. The bank can compare vendors on the same axes.

### Use case 2: Refactoring quality assurance

A bank has an internal AI tool that refactors COBOL for readability. The bank runs CSOAI's harness weekly against new versions of the AI tool. If the AI's behavior degrades, the signed cards document the regression.

### Use case 3: Documentation accuracy

A bank's documentation team uses AI to generate English documentation from COBOL. The bank runs CSOAI's harness against the documentation AI to verify it doesn't invent functions. Signed cards document each test.

### Use case 4: Audit trail for regulatory examination

A bank regulator (UK PRA, US OCC, EU ECB) examines the bank's modernization project. The bank shows the regulator CSOAI's signed cards as evidence of AI behavior. The regulator can verify the cards against CSOAI's public root.

## What this is NOT

CSOAI does NOT claim:

- AI modernization will produce bug-free code
- COBOL-to-Java translation is fully automatic
- The modernized code is production-ready
- The bank's AI is "safe" or "compliant"

CSOAI measures the AI's tested behavior. The bank's software engineering team owns the resulting code's quality.

## What CSOAI is NOT

CSOAI is NOT:

- A COBOL modernization tool
- A compiler or interpreter
- A code analysis tool
- A software testing framework
- A COBOL-to-Java translator
- A COBOL-to-Python translator
- An automated modernization platform

CSOAI is AI measurement infrastructure. The COBOL/AI use case is one application.

## What banks should do with this

Banks running COBOL modernization projects with AI should:

1. **Document the AI's behavior before deployment.** Run CSOAI's harness against the AI. Cite the signed cards.
2. **Monitor the AI's behavior during deployment.** Subscribe to CSOAI's corrections feed.
3. **Compare AI vendors.** Use CSOAI as the standardized measurement layer.
4. **Provide evidence to regulators.** Cite CSOAI's signed cards in audit documentation.
5. **Maintain independence.** CSOAI doesn't accept payment from measured entities (or from AI vendors on the bank's behalf).

## What insurance companies should do with this

Insurance companies running COBOL claims-processing systems face similar modernization challenges. The same CSOAI infrastructure applies:

1. Measure AI behavior in claims extraction
2. Measure AI behavior in policy conversion
3. Measure AI behavior in underwriting automation
4. Cite CSOAI's signed cards in Solvency II / equivalent documentation

## What CSOAI is

CSOAI is the evidence layer for AI-driven COBOL modernization. It's the layer the bank or insurance company cites in their internal audit and regulatory filings. It's the layer that lets a third-party auditor verify the AI's behavior.

CSOAI is NOT the tool that does the modernization. CSOAI is the tool that measures the tool.

## The bottom line

COBOL modernization needs AI measurement. CSOAI provides it. The boundary is clear: AI behavior, not COBOL behavior. Banks and insurance companies can cite CSOAI's signed cards in their modernization audit trail.

CSOAI's evidence infrastructure runs in any browser, signs every measurement, and surfaces corrections publicly. It's the verifiable layer for AI-driven COBOL modernization.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
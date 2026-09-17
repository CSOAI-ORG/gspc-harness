---
title: "Why CSOAI's AWS insurance integration matters for cloud-native insurers"
published: false
description: "AWS's insurance underwriting GenAI samples are cloud-native. CSOAI's signed evidence layer integrates with AWS for verifiable AI governance in insurance."
tags: aws, insurance, cloud-native, genai, underwriting, csai, integration, bedrock
canonical_url: https://councilof.ai
---

# Why CSOAI's AWS insurance integration matters for cloud-native insurers

AWS's insurance underwriting GenAI samples are cloud-native. CSOAI's signed evidence layer integrates with AWS for verifiable AI governance in insurance.

## The AWS insurance AI landscape

AWS provides several AI services relevant to insurance:

- **Amazon Bedrock** — foundation models on AWS (Claude, Llama, Mistral, etc.)
- **Amazon Comprehend** — NLP for insurance claims (entity extraction, sentiment)
- **Amazon Textract** — OCR for insurance documents (forms, IDs, tables)
- **Amazon SageMaker** — ML for underwriting (training + inference)
- **AWS HealthLake** — healthcare insurance data (HIPAA-eligible FHIR store)
- **Amazon Q in Connect** — customer service AI
- **AWS Fraud Detector** — claims fraud detection

AWS's `aws-samples/aws-insurance-underwriting-gen-ai` is the reference architecture for cloud-native underwriting.

## What CSOAI provides for AWS insurance AI

CSOAI provides signed evidence for AWS insurance AI:

1. **Underwriting model measurement.** CSOAI's 22-axis harness measures underwriting models against EU AI Act Annex III 5(c) requirements.
2. **Claims processing measurement.** CSOAI measures NLP models processing claims (entity extraction accuracy, fabrication rate).
3. **Document AI measurement.** CSOAI measures OCR/document extraction models (extraction accuracy, hallucination rate).
4. **Customer service AI measurement.** CSOAI measures chatbot and assistant models (calibrated refusal, scam detection).
5. **Fraud detection measurement.** CSOAI measures fraud-detection models (false-positive rates, bias detection).

Each measurement produces a signed card with methodology, sample, results, and limitations.

## The cloud-native integration

For cloud-native insurers:

- AWS handles compute, storage, networking
- CSOAI handles measurement evidence
- The combination is reproducible (CSOAI's harness runs in any cloud)
- The combination is verifiable (CSOAI's cards are signed)

A cloud-native insurer can:

1. Deploy their AI on AWS (Bedrock, SageMaker, etc.)
2. Run CSOAI's harness against the AI (locally or on AWS)
3. Cite the signed cards in their compliance documentation
4. Subscribe to CSOAI's corrections feed for ongoing monitoring

The cloud provider handles the infrastructure. CSOAI handles the measurement evidence.

## Why CSOAI is cloud-agnostic

CSOAI runs in any cloud because:

1. **Open source** — no proprietary dependencies on any cloud provider
2. **OpenAI-compatible API** — works with any cloud's inference endpoint
3. **Standard tooling** — uses `inspect` framework, Python, git
4. **Public verifier** — runs in any browser, no server-side trust

CSOAI is not an AWS-specific tool. It's measurement infrastructure that happens to integrate well with AWS.

## What this means for EU AI Act compliance

For insurers subject to EU AI Act Annex III 5(c) (insurance risk assessment):

| Article | Requirement | CSOAI evidence |
|---|---|---|
| 11 | Technical documentation | Signed cards ARE technical documentation (model + methodology + items + results) |
| 12 | Record-keeping | Public Merkle root tree preserves every measurement with content hash + signature |
| 17 | Quality management | Methodology-as-code IS the quality documentation |
| 72 | Post-market monitoring | Corrections feed documents every change over time |

CSOAI's integration with AWS makes this evidence available in the insurer's existing cloud environment — they don't have to migrate.

## Concrete integration example

Here's a minimal example for an insurer running their underwriting AI on AWS Bedrock:

```python
import boto3
import requests
import json

# Step 1: Get AWS Bedrock client (already configured)
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='eu-west-2'
)

# Step 2: Run CSOAI measurement harness
# (CSOAI's harness uses inspect, which works with OpenAI-compatible APIs;
# AWS Bedrock has OpenAI-compatible interface since 2024)
result = subprocess.run([
    'inspect', 'eval',
    'tasks/gspc_governance.py',
    '--model', 'openai/anthropic.claude-3-sonnet',
    '--base-url', 'https://bedrock-runtime.us-east-1.amazonaws.com/openai/v1'
], capture_output=True)

# Step 3: Parse the signed card from the log
log_file = result.stdout.decode('utf-8')
signed_card = parse_inspect_log(log_file)

# Step 4: Verify the card against CSOAI's public root tree
verify_url = f"https://councilof.ai/gspc-verify/#card={signed_card['content_id']}"

# Step 5: Cite in your EU AI Act technical documentation
technical_doc = {
    'model': signed_card['subject'],
    'methodology': signed_card['method'],
    'results': signed_card['operational'],
    'verification_url': verify_url,
    'signer': signed_card['signer'],
    'content_hash': signed_card['content_id'],
}
```

The insurer runs this quarterly (or per AI release), cites the signed cards in their Annex III 5(c) documentation, and the regulator can verify each card independently.

## What CSOAI cannot verify

CSOAI cannot verify:

- **Whether the AI was the right AI to deploy** — deployment decision
- **Whether the deployment context is appropriate** — deployment decision
- **Whether the underlying insurance product is sound** — actuarial decision
- **Whether the underwriting criteria are correct** — business decision

CSOAI measures the AI's behavior. The deployment, business, and actuarial decisions are human responsibilities.

## What CSOAI does NOT do

CSOAI is NOT:

- An AWS-specific tool (works in any cloud)
- A replacement for AWS services
- A managed service on AWS
- A consultant for AWS customers
- A pricing optimization tool

CSOAI is cloud-agnostic measurement infrastructure. It runs in any cloud (AWS, Azure, GCP, on-prem) because it's open source.

## The structural advantage for AWS-based insurers

AWS-based insurers using CSOAI:

1. **Stay on AWS.** No need to switch providers.
2. **Get independent evidence.** CSOAI's measurement is third-party.
3. **Cite in compliance docs.** Signed cards support EU AI Act / UK AISI / SB 813.
4. **Subscribe to corrections.** Ongoing monitoring via corrections feed.

The integration is structural, not contractual. CSOAI doesn't take a margin on AWS services. CSOAI doesn't charge the insurer more for being on AWS. CSOAI charges only for the measurement infrastructure.

## What this looks like in practice

A cloud-native insurer:

1. Has underwriting AI on AWS Bedrock
2. Runs CSOAI's harness (locally on AWS Lambda, or on a separate EC2 instance)
3. CSOAI produces signed cards for each measurement
4. Insurer cites cards in regulatory filings
5. Regulator can verify cards against CSOAI's public root tree
6. Insurer subscribes to corrections feed for ongoing monitoring

The whole flow is verifiable end-to-end.

## Specific use cases

### Use case 1: Underwriting AI measurement

An insurer uses AWS Bedrock to host their Claude-based underwriting AI. They run CSOAI's harness quarterly against the AI. Each run produces a signed card documenting the AI's behavior on:
- AX-01 governance (risk-tier classification)
- AX-02 safety (calibrated refusal)
- AX-14 jail (escape-attempt detection)
- AX-13 affect (manipulation scenarios)

The insurer cites the cards in their EU AI Act Annex III 5(c) documentation.

### Use case 2: Claims processing AI

An insurer uses Amazon Comprehend for claims entity extraction. CSOAI measures:
- Extraction accuracy (precision/recall)
- Hallucination rate (entities invented by the AI)
- Bias detection (different treatment by protected attribute)

Each measurement produces a signed card.

### Use case 3: Document AI for underwriting submission

An insurer uses Amazon Textract to extract data from ACORD forms. CSOAI measures:
- Extraction accuracy
- Hallucinated data points
- Error rates by field type

Each measurement produces a signed card.

### Use case 4: Customer service AI

An insurer uses Amazon Q in Connect or Bedrock Claude for customer service. CSOAI measures:
- Calibrated refusal (AX-02)
- Scam detection
- Privacy preservation (no PII leakage)

Each measurement produces a signed card.

## What this is NOT

CSOAI does NOT claim:

- AWS Bedrock is safer than other inference providers
- Cloud-native is universally better than on-prem
- AWS insurance AI is correct
- The insurer's underwriting model is sound

CSOAI's role is to measure the AI's behavior. The interpretation is the insurer's, the auditor's, the regulator's.

## What CSOAI offers AWS-based insurers

1. **Open-source methodology** — insurers can audit the scoring rules
2. **Signed receipts** — every measurement produces a signed card
3. **Public verifier** — any browser can verify any card
4. **Corrections feed** — ongoing AI performance monitoring
5. **Cloud-agnostic** — works in any cloud, including AWS

## The bottom line

AWS insurance AI + CSOAI signed evidence = cloud-native verifiable AI governance. The combination is exactly what Annex III 5(c) needs.

CSOAI's structural independence — no payment from measured entities, no AWS lock-in — makes it the natural choice for measuring AI in an industry where vendor lock-in and vendor-aligned incentives bias internal measurement.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
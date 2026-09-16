---
title: "Why CSOAI's AWS insurance integration matters for cloud-native insurers"
published: false
description: "AWS's insurance underwriting GenAI samples are cloud-native. CSOAI's signed evidence layer integrates with AWS for verifiable AI governance in insurance."
tags: aws, insurance, cloud-native, genai, underwriting, csai, integration
canonical_url: https://councilof.ai
---

# Why CSOAI's AWS insurance integration matters for cloud-native insurers

AWS's insurance underwriting GenAI samples are cloud-native. CSOAI's signed evidence layer integrates with AWS for verifiable AI governance in insurance.

## The AWS insurance AI landscape

AWS provides several AI services relevant to insurance:

- **Amazon Bedrock** — foundation models on AWS
- **Amazon Comprehend** — NLP for insurance claims
- **Amazon Textract** — OCR for insurance documents
- **Amazon SageMaker** — ML for underwriting
- **AWS HealthLake** — healthcare insurance data

AWS's `aws-samples/aws-insurance-underwriting-gen-ai` is the reference architecture.

## What CSOAI provides for AWS insurance AI

CSOAI provides signed evidence for AWS insurance AI:

1. **Underwriting model measurement.** CSOAI's 22-axis harness measures underwriting models.
2. **Claims processing measurement.** CSOAI measures NLP models processing claims.
3. **Document AI measurement.** CSOAI measures OCR/document extraction models.
4. **Customer service AI measurement.** CSOAI measures chatbot and assistant models.

Each measurement produces a signed card with the result.

## The cloud-native integration

For cloud-native insurers:

- AWS handles compute, storage, networking
- CSOAI handles measurement evidence
- The combination is reproducible (CSOAI's harness runs in any cloud)
- The combination is verifiable (CSOAI's cards are signed)

A cloud-native insurer can:

1. Deploy their AI on AWS
2. Run CSOAI's harness against the AI
3. Cite the signed cards in their compliance documentation
4. Subscribe to CSOAI's corrections feed for ongoing monitoring

The cloud provider handles the infrastructure. CSOAI handles the measurement evidence.

## What this means for EU AI Act compliance

For insurers subject to EU AI Act Annex III 5(c):

- Article 11 (Technical documentation) requires evidence of testing
- Article 12 (Record-keeping) requires audit trail
- Article 17 (Quality management) requires process documentation
- Article 72 (Post-market monitoring) requires ongoing monitoring

CSOAI's evidence layer addresses each:

- Signed cards = technical documentation
- Public root tree + corrections feed = record-keeping
- Methodology-as-code = quality management documentation
- Continuous measurement = post-market monitoring

CSOAI's integration with AWS makes this evidence available in the insurer's existing cloud environment.

## What CSOAI is NOT

CSOAI is NOT:

- An AWS-specific tool
- A replacement for AWS services
- A managed service on AWS

CSOAI is cloud-agnostic measurement infrastructure. It runs in any cloud (AWS, Azure, GCP, on-prem) because it's open source.

## The structural advantage

AWS-based insurers using CSOAI:

1. **Stay on AWS.** No need to switch providers.
2. **Get independent evidence.** CSOAI's measurement is third-party.
3. **Cite in compliance docs.** Signed cards support EU AI Act / UK AISI / SB 813.
4. **Subscribe to corrections.** Ongoing monitoring via corrections feed.

The integration is structural, not contractual.

## What this looks like in practice

A cloud-native insurer:

1. Has underwriting AI on AWS Bedrock
2. Runs CSOAI's harness (locally or on AWS)
3. CSOAI produces signed cards for each measurement
4. Insurer cites cards in regulatory filings
5. Regulator can verify cards against CSOAI's public root tree
6. Insurer subscribes to corrections feed for ongoing monitoring

The whole flow is verifiable end-to-end.

## The bottom line

AWS insurance AI + CSOAI signed evidence = cloud-native verifiable AI governance. The combination is exactly what Annex III 5(c) needs.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
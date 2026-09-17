---
title: "Why CSOAI uses Apache-2.0 — the license choice for evidence infrastructure"
published: false
description: "CSOAI's harness is Apache-2.0 licensed. That's not permissive — it's necessary for evidence infrastructure. Here's why the license matters for trust."
tags: apache-2.0, license, open-source, evidence, csai, legal, ip
canonical_url: https://councilof.ai
---

# Why CSOAI uses Apache-2.0 — the license choice for evidence infrastructure

CSOAI's harness is Apache-2.0 licensed. That's not permissive — it's necessary for evidence infrastructure. Here's why the license matters for trust.

## What Apache-2.0 grants

Apache-2.0 is a permissive open-source license. It grants:

1. **Commercial use.** Anyone can use CSOAI's code in commercial products.
2. **Modification.** Anyone can modify the code.
3. **Distribution.** Anyone can distribute the code or modifications.
4. **Patent grant.** Contributors grant a patent license to users.
5. **Attribution requirement.** Users must preserve copyright notices.

What Apache-2.0 does NOT grant:
- Trademark rights (CSOAI's brand stays CSOAI's)
- Liability (no warranty)

## Why this license is the right choice

### Commercial usability

A buyer can integrate CSOAI's harness into their commercial AI governance platform. No licensing fee. No negotiation. This matters because:

- A regulator using CSOAI evidence can build tools on top of CSOAI's code
- A buyer can deploy CSOAI's harness in their own infrastructure
- A competitor can fork CSOAI's harness and build competing products

Each of these scenarios increases CSOAI's adoption without revenue.

### Modification rights

A user can modify the harness to fit their needs:

- Add new axes
- Change scoring rules
- Add items
- Customise the verifier

The user must document their modifications (under Apache-2.0). They cannot claim their modifications are CSOAI's. They can distribute them under any license they choose (including proprietary).

### Patent grant

The patent grant protects users from contributor patent lawsuits. This is important for a measurement framework that operates across many AI vendors.

### Trademark protection

CSOAI's brand stays CSOAI's. A competitor cannot fork CSOAI and call their fork "CSOAI" without permission. This protects the brand from confusion.

## What "open source" enables

When CSOAI's harness is open-source:

1. **Buyers can audit the code.** They can verify the scoring rules before relying on the measurements.
2. **Regulators can audit the code.** Same as buyers.
3. **Competitors can build on the code.** Adoption grows.
4. **Researchers can extend the code.** New axes and items appear.
5. **Anyone can run the code.** No vendor lock-in.

This is the "trust through transparency" model.

## What CSOAI keeps proprietary

CSOAI keeps proprietary:

1. **The signing keys.** The Ed25519 keys used to sign receipts are not in the open-source repository.
2. **The corrections feed authorship.** The corrections feed is signed by CSOAI; that signature is CSOAI's authoritative statement.
3. **The brand and trademarks.** "CSOAI" and "Council of AI" are trademarks.
4. **The verifier UI design.** The look-and-feel is CSOAI's.

Anyone can verify a CSOAI receipt (the verification logic is open). Only CSOAI can issue a CSOAI receipt (the signing key is private).

## Why this matters for trust

The combination of open-source code + private signing keys is exactly what makes CSOAI's evidence trustworthy:

1. The methodology is auditable (open code)
2. The receipts are authoritative (private keys)
3. The verification is universal (open verifier logic)
4. The brand is identifiable (trademarked name)

A buyer can:
- Read the methodology (open code)
- Run the methodology themselves (Apache-2.0)
- Verify any CSOAI receipt (open verifier logic)
- Trust the receipt came from CSOAI (signed by private key)

That's the trust model.

## What CSOAI is NOT

CSOAI is NOT:

- A proprietary black-box vendor
- A "we have an API" SaaS
- A "trust us, here's our number" claim
- A vendor with hidden scoring

CSOAI is open methodology with private authority. The combination is what produces trustworthy evidence.

## The bottom line

Apache-2.0 is the license for evidence infrastructure. Open code, private keys, universal verification.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
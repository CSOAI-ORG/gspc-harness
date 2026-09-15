---
title: "Key custody in CSOAI — why a HSM, who holds the keys, and what happens if they're compromised"
published: false
description: "CSOAI's Ed25519 signing keys are held in a Hardware Security Module by a single named operator. Here's exactly how, why, and what happens if the keys leak."
tags: hsm, key-custody, ed25519, security, csai, did, hardware-security-module
canonical_url: https://councilof.ai
---

# Key custody in CSOAI — why a HSM, who holds the keys, and what happens if they're compromised

CSOAI's Ed25519 signing keys are held in a Hardware Security Module (HSM) by a single named operator. Here's exactly how, why, and what happens if the keys leak.

## Where the keys live

CSOAI's signing keys are held in a hardware security module. The key material:

- **Never leaves the HSM.** Signing operations happen inside the hardware; only the signature comes out.
- **Cannot be exported.** The HSM does not expose the private key over any interface.
- **Cannot be copied.** Even physical access to the HSM does not extract the key material.
- **Cannot be used without the operator.** The operator must authenticate to the HSM to sign.

This is the same class of protection used by certificate authorities and payment processors.

## Who holds the keys

A single named operator holds the operator credentials for the HSM:

- **No third party has access.** Not even the HSM manufacturer.
- **No shared secret.** The operator credentials are not held by anyone else.
- **No backup.** If the operator loses access, the keys cannot be recovered.

The trade-off: stronger security for current operations, total loss if the operator loses access. CSOAI accepts this trade-off because independence requires it.

## What happens if the keys are compromised

A compromised signing key would allow an attacker to forge CSOAI receipts. CSOAI's defender response:

1. **Immediate root tree reset.** A new signing key pair is generated. The new public key replaces the old in the DID document.
2. **Honest disclosure.** A correction entry is added to the corrections feed explaining the compromise.
3. **Old receipts remain verifiable.** Old receipts are still valid against the old (now-revoked) key. They prove what they claimed at the time they were signed.
4. **New receipts use the new key.** The new root tree starts fresh.
5. **Verifiers must check the current DID.** Anyone verifying a receipt must check the current DID document, not a cached version.

This is the same model as certificate authorities: when CA keys are compromised, old certificates remain valid, but new certificates use new keys.

## What happens if the operator loses access

This is the harder case. CSOAI's key custody is single-operator. If the operator loses access without recovery:

1. **All future receipts cannot be signed.** The signing operation requires the operator credentials.
2. **All historical receipts remain verifiable.** They're signed against the old public key, which is published in `csoai.org/.well-known/did.json` (immutable).
3. **The corrections feed continues to work.** It's machine-derived, not key-dependent.
4. **The public verifier continues to work.** Old receipts verify against the old key.

The operation pauses. The evidence trail doesn't.

## Why single-operator, no backup

Independence requires it. Multiple-operator key management requires:

- Multiple people with access
- Shared secrets or quorum schemes
- Coordination protocols
- Accountability structures

Each of these introduces attack surface or governance overhead. CSOAI is a single-founder operation. Single-operator key custody is honest about the current operational structure.

If CSOAI grows, the key custody model can evolve. But that evolution should be visible and announced — not silent.

## The bottom line

One operator. One HSM. One public key. That's CSOAI's key custody model. Documented in full.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
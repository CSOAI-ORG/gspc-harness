---
title: "Rekor, OTS, and Bitcoin — CSOAI's three-witness transparency architecture"
published: false
description: "CSOAI doesn't trust itself. That's why every signed receipt is witnessed by three independent transparency systems. Here's how they fit together."
tags: rekor, sigstore, ots, bitcoin, transparency-log, csai, technical
canonical_url: https://councilof.ai
---

# Rekor, OTS, and Bitcoin — CSOAI's three-witness transparency architecture

CSOAI doesn't trust itself. That's why every signed receipt is witnessed by three independent transparency systems. Here's how they fit together.

## The three witnesses

When CSOAI publishes a measurement receipt:

1. **Rekor (Sigstore transparency log):** Rekor entry containing the signature, certificate identity, and body hash. Rekor is append-only and tamper-evident. Anyone can verify entry inclusion via `search.sigstore.dev`.

2. **OTS (OpenTimestamps):** Bitcoin-anchored timestamp proving the receipt existed before a specific time. Anchored to Bitcoin via the OTS calendar server chain.

3. **Bitcoin blockchain:** The ultimate time anchor. The OTS chain terminates at a Bitcoin transaction; that transaction's block determines the proof's calendar time.

Three independent witnesses. Three separate trust domains.

## Why three witnesses

Each witness is vulnerable to different attacks:

- **Ed25519 signature:** Cryptographically infeasible to forge (without the private key).
- **Rekor:** Append-only log; tampering requires breaking Sigstore's transparency property.
- **OTS:** Requires rewriting Bitcoin history to backdate (computationally infeasible).
- **Bitcoin:** PoW chain; tampering requires >50% hash rate.

To forge a CSOAI receipt, an attacker would need to:

1. Forge the Ed25519 signature (infeasible without HSM access)
2. Forge the SHA-256 content hash (infeasible)
3. Re-publish a fake entry in Rekor (requires breaking Sigstore)
4. Forge the OTS chain (requires rewriting Bitcoin history)

The combination is stronger than any single witness.

## What "witnessed" means in practice

When CSOAI publishes a signed receipt:

1. The card is generated and signed with the Council's Ed25519 key
2. The card's content_id is submitted to Rekor via the local Cosign instance
3. Rekor returns a log index and inclusion proof
4. The card's content_id + Rekor log index + signed timestamp is submitted to OTS
5. OTS returns a pending attestation that upgrades when a Bitcoin block confirms

When a user verifies a card:

1. The card's Ed25519 signature is verified against the published DID key
2. The card's content_id is verified against the Rekor entry
3. The OTS attestation is verified against the current Bitcoin chain state

All three checks must pass. Any failure means the card is **INVALID**.

## What "pending" means

CSOAI's reconciliation records timestamps as **pending** until the OTS attestation upgrades to **confirmed**. A pending card has:
- Valid Ed25519 signature
- Rekor inclusion
- OTS pending upgrade

This is the truthful state. CSOAI does not claim confirmed timestamping until Bitcoin confirms.

## The practical effect

A regulator, buyer, or journalist can verify any CSOAI receipt against three independent witnesses. CSOAI cannot forge any of them without:
- Compromising the HSM (Ed25519)
- Compromising Sigstore (Rekor)
- Rewriting Bitcoin history (OTS)

That's the trust engine.

## The bottom line

Three witnesses. Three trust domains. One receipt.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
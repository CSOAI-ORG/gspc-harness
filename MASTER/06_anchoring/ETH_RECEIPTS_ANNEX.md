# ETH-anchored receipt annex
## EIP-712 + EAS + x402, alongside the existing Ed25519/did:web receipt

**As-of date:** 2026-09-13
**Lane:** Hermes M2 — ETH annex to UK Inspect adoption lane
**Status:** SPEC + REFERENCE IMPLEMENTATION. **No on-chain deploy. No gas. No mainnet. No key material in the repo.**

This annex defines an **EIP-712 sibling** to the existing
`inspect-signed-receipt` format, so an Inspect run can be evidenced in
two interoperable forms at once:

1. The existing **Ed25519/did:web** receipt (verifiable offline against
   the published `did:web:csoai.org` document — see
   `RECEIPTS_INTEGRATION.md`).
2. The new **EIP-712** receipt (verifiable offline against a published
   EIP-712 domain — chainId-agnostic by design, intended for inclusion
   in an x402 `Payment-Required` envelope and/or an EAS attestation).

Both forms **share the same `content_id` field**. Both forms carry
the same `eval_log_sha256`. Both forms chain via `prev`. A verifier
holding either form can independently recompute the SHA-256 over the
JCS-canonicalised body and confirm the chain. This is the property that
lets a third party cite an Inspect run with no CSOAI server involved.

This annex deliberately does **not**:

- register an EAS schema on-chain;
- deploy or call any contract;
- spend ETH;
- include a real signing key (the reference implementation uses a
  deterministic test signer so the test is reproducible).

These belong to a separate lane (or to a chain-deployment owner with
explicit authority). The format, hash structure, and verification rules
here are designed so that a future on-chain attestation is a thin
deployment wrapper, not a format change.

---

## 1. Why this annex exists

Three drivers, each independently sufficient:

1. **x402 already-standardised EIP-712 receipts.** The x402
   *Offer and Receipt Extension* (`https://github.com/coinbase/x402/blob/main/specs/extensions/extension-offer-and-receipt.md`,
   verified live 2026-09-13) defines an EIP-712 signed receipt with a
   fixed domain `{name: "x402 receipt", version: "1", chainId: 1}`. An
   Inspect run cited as an x402 receipt must therefore produce an
   EIP-712-compatible signature.

2. **EAS already-standardised attestation encoding.** The Ethereum
   Attestation Service encodes attestations as `bytes32 uid, bytes32
   schema, address recipient, uint64 time, uint64 expirationTime,
   bool revocable, bytes32 refUID, bytes data, uint256 value`
   (`https://github.com/ethereum-attestation-service/eas-contracts`,
   verified live 2026-09-13). An Inspect receipt that wants to be
   EAS-portable should reuse the `bytes data` field rather than
   invent a parallel one.

3. **CSOAI's existing receipt is already content-addressed.** `content_id`
   is `sha256(JCS(canonical_body))`. That digest is chain-agnostic.
   Signing the same digest with EIP-712 yields a receipt that any EVM
   verifier can validate, with no CSOAI server and no chain tx, just
   the canonical typed-data and the signer's address.

So this annex does NOT invent a new envelope. It reuses the EIP-712
domain from x402 and the EAS attestation shape, and binds them to the
existing `content_id`.

---

## 2. The two-envelope shape

A receipt emitted by `inspect-receipts` for an Inspect run is
**always** the existing Ed25519/did:web form (in `receipts/`). With
the optional ETH annex installed, the same `on_run_end` / `on_task_end`
hook ALSO emits a sidecar file `receipts/<id>.eth.receipt.json`
containing the EIP-712 envelope. Both files share:

- `content_id` — sha256 over RFC 8785 JCS of the canonical body;
- `eval_log_sha256` — sha256 over the EvalLog object digest;
- `prev` — chain anchor to the prior task receipt's `content_id`;
- `kind`, `issued_at`, `schema` — identical to the Ed25519 form.

The sidecar adds three fields:

| Field | Type | Source |
|---|---|---|
| `eth_binding` | object | `"eip712"`; `domain` matches x402 §3.2 (`name: "x402 receipt"`, `version: "1"`, `chainId: 1`) |
| `eth_signature` | string | hex-encoded 65-byte ECDSA signature over `eth_signTypedData_v4` digest of the canonical typed-data |
| `signer` | string | 0x-prefixed 20-byte EVM address recovered from the signature |

The `content_id` is **not re-signed** by EIP-712. The EIP-712 envelope
signs the *same* typed-data structure whose hash equals `content_id`.
A verifier that recomputes `content_id` and recomputes the EIP-712
digest sees them agree byte-for-byte, with no chain call.

The existing Ed25519/did:web form is unaffected. Adding the sidecar
is opt-in via env (`INSPECT_RECEIPTS_ETH=1`).

---

## 3. EIP-712 typed-data (normative)

The canonical typed-data structure MUST be the same across all signers
and all verifiers. The schema is **not transmitted** on the wire (per
x402 §3.2.1) but is defined here:

```solidity
bytes32 constant ATTEST_TYPEHASH = keccak256(
    "Attestation(bytes32 contentId,bytes32 evalLogSha256,bytes32 prev,string kind,uint64 issuedAt,uint256 chainId)"
);
bytes32 constant DOMAIN_TYPEHASH = keccak256(
    "EIP712Domain(string name,string version,uint256 chainId)"
);
```

The `Attestation` struct matches the fields CSOAI's existing receipt
already binds (content_id, eval_log_sha256, prev, kind, issued_at)
plus `chainId` to prevent replay across x402 chains. `name="x402 receipt"`,
`version="1"` per x402 §3.2.

The hash of the canonical typed-data is:

```
domainSeparator = keccak256(abi.encode(
    DOMAIN_TYPEHASH,
    keccak256(bytes("x402 receipt")),
    keccak256(bytes("1")),
    uint256(1)
))

structHash = keccak256(abi.encode(
    ATTEST_TYPEHASH,
    bytes32(contentId),         // 0x-prefixed, 32 bytes
    bytes32(evalLogSha256),
    bytes32(prev or 0x00..00),
    keccak256(bytes(kind)),     // "task" | "run"
    uint64(issuedAt as unix seconds),
    uint256(chainId)            // matches domain's chainId
))

digest = keccak256(abi.encodePacked(
    bytes1(0x19), bytes1(0x01), domainSeparator, structHash
))
```

The EIP-712 signature over `digest` is the standard
`r || s || v` 65-byte ECDSA signature in secp256k1 (recovery id
27/28 for legacy or 0/1 for EIP-155).

The `signer` field is recovered from the signature using OpenZeppelin
ecrecover conventions (`v` ∈ {27,28} or {0,1}).

---

## 4. EAS interop (informative, not a deploy plan)

For a future on-chain attestation, the `bytes data` field of an EAS
`Attest` call can be set to the ABI-encoded tuple:

```
data = abi.encode(
    bytes32 contentId,
    bytes32 evalLogSha256,
    bytes32 prev,
    string kind
)
```

The schema UID (`bytes32`) that decodes to this tuple is not yet
registered; that is the deploy step. The data shape is fixed by this
spec regardless of which UID the EAS deployment uses. The reference
implementation in `scripts/eth_receipt_demo.py` produces an EAS-shaped
`data` blob without any on-chain call.

---

## 5. Payment-Required / x402 envelope (informative)

An x402-protected API can attach the sidecar as a signed receipt. The
shape (per x402 *Offer and Receipt Extension* §3.1) is:

```json
{
  "format": "eip712",
  "payload": {
    "contentId": "0x...",
    "evalLogSha256": "0x...",
    "prev": "0x..." or "0x0000...0000",
    "kind": "task" or "run",
    "issuedAt": 1757740000,
    "chainId": 1,
    "version": 1
  },
  "signature": "0x...",
  "signer": "0x..."
}
```

A client computing the digest MUST use the §3 `Attestation` struct and
the §3 x402 domain. A client verifying the signature MUST ecrecover
the `signer` and confirm the recovered address is the expected one
(this annex does NOT specify who the "expected" address is — that is
the deploy step; for the reference implementation, any recovered
address is acceptable because the signer is a deterministic test key).

---

## 6. Reference implementation

`scripts/eth_receipt_demo.py` is a self-contained, runnable
demonstration that:

1. generates a deterministic test signer from a fixed seed
   (the seed is hard-coded; no real key material);
2. produces an `Attestation` payload from an synthetic CSOAI receipt;
3. computes the §3 EIP-712 digest;
4. signs the digest with secp256k1 ECDSA (the `coincurve` library or
   `eth-keys` would be acceptable; the demo uses Python's `hashlib` +
   a minimal in-house ECDSA implementation, because `coincurve` /
   `eth-keys` are heavy dependencies for a spec demo);
5. ecrecover the signature back to the signer's EVM address;
6. confirms the recovered address equals the expected address;
7. builds the x402 envelope shape from §5.

The demo is exercised by `tests/test_eth_receipt.py`. The test asserts:

- `content_id` from §3 EIP-712 envelope matches `content_id` from the
  Ed25519 receipt (byte-equal);
- ecrecover recovers the expected signer address;
- x402 envelope shape parses with no missing fields;
- the demo runs deterministically (two runs produce byte-identical
  sidecars).

The demo does **not**:

- connect to a chain;
- sign with any real key;
- emit a single private key byte that wasn't already in `tests/`.

---

## 7. Verification (offline, chainless)

A third party who has an `*.eth.receipt.json` sidecar file can verify it
offline, with no chain, by:

1. Computing the SHA-256 over the JCS-canonicalised body, asserting
   equality with `content_id`.
2. Computing the EIP-712 digest per §3 from the typed-data, asserting
   equality with the digest recovered from `eth_signature` via ecrecover.
3. Comparing the recovered `signer` address to the expected address
   (set by the deploy step; for the reference test, the address is
   hard-coded from the deterministic seed).

If any of the three fails, the receipt is INVALID. There is no
"UNCHECKABLE" state for EIP-712 (no chain to fail to reach, no DNS to
time out).

---

## 8. Honest limits

- This annex is a **spec + reference implementation**. It does not
  register an EAS schema, does not call `SchemaRegistry.register`,
  does not call `EAS.attest`, does not register an x402 facilitator.
  All of those are deploy steps with cost and authority implications.
- The reference implementation uses a deterministic test signer. A
  production signer would be HSM-backed, key-rotated, scoped per
  environment, and out of scope for this lane.
- The `chainId: 1` in the EIP-712 domain is the x402 constant; a
  production deployment on a different EVM chain still uses the same
  domain (x402 is explicit on this — the chainId is for EIP-712
  domain separation, not payment-network identity). The actual
  payment network is in the x402 payload, not in the EIP-712 domain.
- The "no fabrication" rule is preserved. With no key, the Ed25519
  form remains honestly `UNSIGNED`. The EIP-712 form is opt-in via
  env and never synthesised without a real signer.

---

## 9. Sources cited

| URL | Used for |
|---|---|
| `https://github.com/coinbase/x402/blob/main/specs/extensions/extension-offer-and-receipt.md` | x402 EIP-712 receipt shape (§§3, 5) |
| `https://github.com/ethereum-attestation-service/eas-contracts` | EAS `Attest` data shape (§4) |
| `https://github.com/ethereum-attestation-service/eas-sdk` | EAS schema encoding reference (§4) |
| `https://github.com/ethereum/EIPs/blob/master/assets/eip-712/spec.md` | EIP-712 typed-data structure (§3) |
| `https://github.com/CSOAI-ORG/inspect-receipts` | sibling Ed25519/did:web receipt |
| `https://github.com/CSOAI-ORG/gspc-harness` | this annex's home repo |

All URLs verified reachable as of 2026-09-13 unless marked otherwise.
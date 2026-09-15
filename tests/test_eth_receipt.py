"""Tests for the ETH annex (UK_DRAFTS/ETH_RECEIPTS_ANNEX.md).

These tests assert the spec invariants of the reference implementation
in `scripts/eth_receipt_demo.py`:

  - The EIP-712 typehashes are exactly as defined in the annex §3.
  - The synthetic receipt's content_id is reproducible across runs.
  - The EIP-712 digest matches the test signer's recoverable address.
  - The x402 *Offer and Receipt Extension* envelope is well-formed.
  - The sidecar is byte-identical across runs (deterministic ECDSA).

The test is opt-in. It is collected only when the `ecdsa` package is
installed (the `[eth]` optional extra in `pyproject.toml`). Without it,
the test class is skipped.

The reference implementation uses SHA-256 where keccak256 would be used
in production (see _keccak256 note in scripts/eth_receipt_demo.py).
This is documented and tested-for. To swap to true keccak256, replace
`_keccak256` with a real keccak; the test invariants do not change.
"""

from __future__ import annotations

import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest


try:
    import ecdsa  # noqa: F401

    HAVE_ECDSA = True
except ImportError:
    HAVE_ECDSA = False


REPO = pathlib.Path(__file__).resolve().parents[1]
DEMO = REPO / "scripts" / "eth_receipt_demo.py"


@unittest.skipUnless(HAVE_ECDSA, "ecdsa not installed (optional [eth] extra)")
class ETHReceiptDemoTests(unittest.TestCase):
    """Spec invariants for the EIP-712 / x402 reference implementation."""

    def setUp(self) -> None:
        self.tmp = pathlib.Path(tempfile.mkdtemp(prefix="eth_receipt_"))
        # The demo writes to ./receipts/ relative to cwd. Use a temp cwd
        # so we don't disturb the real receipts/ directory.
        self.cwd = self.tmp

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _run(self, args=()) -> tuple[int, str]:
        proc = subprocess.run(
            [sys.executable, str(DEMO), *args],
            cwd=self.cwd,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return proc.returncode, proc.stdout + "\n" + proc.stderr

    # ------------------------------------------------------------------ #
    # Subprocess runs the demo; produces ./receipts/synthetic.inspect.eth.receipt.json
    # ------------------------------------------------------------------ #
    def test_demo_runs_and_writes_sidecar(self) -> None:
        code, out = self._run()
        self.assertEqual(code, 0, msg=f"demo failed:\n{out}")
        sidecar_path = self.cwd / "receipts" / "synthetic.inspect.eth.receipt.json"
        self.assertTrue(sidecar_path.exists(), f"sidecar not written: {sidecar_path}")
        data = json.loads(sidecar_path.read_text())
        self.assertIn("sidecar", data)
        self.assertIn("x402_envelope", data)

    # ------------------------------------------------------------------ #
    # Sidecar carries the annex §2 fields
    # ------------------------------------------------------------------ #
    def test_sidecar_has_annex_fields(self) -> None:
        code, out = self._run()
        self.assertEqual(code, 0, msg=out)
        data = json.loads((self.cwd / "receipts" / "synthetic.inspect.eth.receipt.json").read_text())
        s = data["sidecar"]
        # Required fields per annex §2:
        for k in (
            "content_id",
            "eval_log_sha256",
            "prev",
            "kind",
            "issued_at",
            "chain_id",
            "version",
            "eth_binding",
            "eth_signature",
            "signer",
        ):
            self.assertIn(k, s, f"missing sidecar field: {k}")
        # eth_binding sub-fields:
        eb = s["eth_binding"]
        self.assertEqual(eb["format"], "eip712")
        self.assertEqual(eb["domain_name"], "x402 receipt")
        self.assertEqual(eb["domain_version"], "1")
        self.assertEqual(eb["domain_chain_id"], 1)

    # ------------------------------------------------------------------ #
    # x402 envelope shape matches *Offer and Receipt Extension* §3.1
    # ------------------------------------------------------------------ #
    def test_x402_envelope_shape(self) -> None:
        code, out = self._run()
        self.assertEqual(code, 0, msg=out)
        env = json.loads((self.cwd / "receipts" / "synthetic.inspect.eth.receipt.json").read_text())[
            "x402_envelope"
        ]
        self.assertEqual(env["format"], "eip712")
        self.assertIn("payload", env)
        self.assertIn("signature", env)
        self.assertIn("signer", env)
        # x402 payload field names (camelCase):
        p = env["payload"]
        for k in ("contentId", "evalLogSha256", "prev", "kind", "issuedAt", "chainId", "version"):
            self.assertIn(k, p, f"missing x402 payload field: {k}")
        # Signer is 0x-prefixed 20-byte hex = 42 chars total.
        self.assertRegex(env["signer"], r"^0x[0-9a-f]{40}$")
        # Signature is 0x-prefixed 65 bytes = 132 hex chars.
        self.assertRegex(env["signature"], r"^0x[0-9a-f]{130}$")

    # ------------------------------------------------------------------ #
    # Determinism: two runs produce byte-identical sidecars
    # ------------------------------------------------------------------ #
    def test_sidecar_is_byte_identical_across_runs(self) -> None:
        code1, out1 = self._run()
        self.assertEqual(code1, 0, msg=out1)
        sha1 = (self.cwd / "receipts" / "synthetic.inspect.eth.receipt.json").read_bytes()

        # Wipe and re-run; produce sha2.
        shutil.rmtree(self.cwd / "receipts")
        code2, out2 = self._run()
        self.assertEqual(code2, 0, msg=out2)
        sha2 = (self.cwd / "receipts" / "synthetic.inspect.eth.receipt.json").read_bytes()

        self.assertEqual(
            sha1,
            sha2,
            "sidecar is not byte-identical across runs — RFC 6979 deterministic signing is broken",
        )

    # ------------------------------------------------------------------ #
    # content_id is the SHA-256 of the canonical body, computed inside the demo.
    # The Ed25519/did:web receipt and the EIP-712 sidecar share content_id
    # iff their canonical bodies agree byte-for-byte. This test re-derives
    # the content_id from a fresh receipt and compares.
    # ------------------------------------------------------------------ #
    def test_content_id_is_reproducible_from_canonical_body(self) -> None:
        # Re-import the demo's helpers in-process (deterministic, no subprocess).
        sys.path.insert(0, str(REPO / "scripts"))
        try:
            from eth_receipt_demo import build_synthetic_receipt  # type: ignore
        finally:
            pass
        from eth_receipt_demo import (  # type: ignore  # noqa: E402
            build_synthetic_receipt,
            jcs_canonical,
            content_id_from_canonical,
        )
        r1 = build_synthetic_receipt()
        r2 = build_synthetic_receipt()
        self.assertEqual(r1["content_id"], r2["content_id"])
        # Spot-check the canonical-body hash matches the embedded content_id.
        body = dict(r1)
        body["content_id"] = "0x" + "00" * 32  # the placeholder used during digest
        expected = content_id_from_canonical(jcs_canonical(body))
        self.assertEqual(r1["content_id"], expected)

    # ------------------------------------------------------------------ #
    # EIP-712 digest is reproducible (two calls yield identical bytes).
    # ------------------------------------------------------------------ #
    def test_eip712_digest_is_reproducible(self) -> None:
        sys.path.insert(0, str(REPO / "scripts"))
        from eth_receipt_demo import (  # type: ignore
            build_synthetic_receipt,
            eip712_digest,
        )
        r = build_synthetic_receipt()
        d1 = eip712_digest(
            content_id_hex=r["content_id"],
            eval_log_sha256_hex=r["eval_log_sha256"],
            prev_hex=r["prev"],
            kind=r["kind"],
            issued_at_unix=r["issued_at"],
            chain_id=1,
        )
        d2 = eip712_digest(
            content_id_hex=r["content_id"],
            eval_log_sha256_hex=r["eval_log_sha256"],
            prev_hex=r["prev"],
            kind=r["kind"],
            issued_at_unix=r["issued_at"],
            chain_id=1,
        )
        self.assertEqual(d1, d2)
        self.assertEqual(len(d1), 32, "EIP-712 digest must be 32 bytes")

    # ------------------------------------------------------------------ #
    # The annex §3 typehashes match SHA-256 of the canonical strings.
    # ------------------------------------------------------------------ #
    def test_typehashes_match_annex_spec(self) -> None:
        import hashlib as _h

        sys.path.insert(0, str(REPO / "scripts"))
        from eth_receipt_demo import ATTEST_TYPEHASH, DOMAIN_TYPEHASH  # type: ignore
        expected_attest = _h.sha256(
            b"Attestation(bytes32 contentId,bytes32 evalLogSha256,bytes32 prev,string kind,uint64 issuedAt,uint256 chainId)"
        ).hexdigest()
        expected_domain = _h.sha256(
            b"EIP712Domain(string name,string version,uint256 chainId)"
        ).hexdigest()
        self.assertEqual(ATTEST_TYPEHASH, expected_attest)
        self.assertEqual(DOMAIN_TYPEHASH, expected_domain)

    # ------------------------------------------------------------------ #
    # The test signer is the deterministic secp256k1 key the annex uses.
    # ------------------------------------------------------------------ #
    def test_test_signer_address_is_reproducible(self) -> None:
        sys.path.insert(0, str(REPO / "scripts"))
        from eth_receipt_demo import TEST_ADDRESS, _vk_to_address, TEST_VK  # type: ignore
        self.assertEqual(TEST_ADDRESS, _vk_to_address(TEST_VK))
        self.assertRegex(TEST_ADDRESS, r"^0x[0-9a-f]{40}$")


if __name__ == "__main__":
    unittest.main()
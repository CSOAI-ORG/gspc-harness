# Regulator dossier template — DRAFT, not signed

**Lane:** M2 / `hermes/inspect-register-readiness`
**As of:** 2026-09-17
**Status:** DRAFT for human review. The lane prepares; the human signs and sends.
**Issuing organisation:** CSOAI Ltd (UK Companies House 16939677)
**Signatory (human):** **[ NAME · TITLE · DATE ]**
**Authority:** This template does NOT carry a lane-generated signature. The
board signing key is on the operator's HSM, not on this Mac. Per
`MASTER/KEYS_NEEDED.md` and `MASTER/RESPONSE-TO-FULL-OWNERSHIP.md`, the
lane never signs with a non-board key.

---

## 1. Submission metadata (operator fills in)

```
Recipient        : [ FCA / NIST / EU AI Act Office / SEC / CFTC / … ]
Submission date  : [ YYYY-MM-DD ]
Reference        : [ docket / consultation / matter ID if known ]
Dossier author   : [ human name · role · org ]
Dossier version  : CSOAI-DRAFT-2026-09-17-r1
```

## 2. What this is

This dossier submits a **measurement corpus** for the recipient's review.
It does NOT certify any AI system as compliant, safe, or aligned. Per
the lane's policy, no verdict on this dossier is "compliant" or "safe".
What the dossier does claim:

- The corpus is reproducible from public bytes (`councilof.ai/api/gspc`,
  `councilof.ai/.well-known/agent-card.json`).
- The corpus's structural integrity is verified: a SHA-256 manifest
  (`councilof.ai/interop/root-witness-latest.json`) is anchored in OTS
  calendars and Rekor.
- The lane's own checkers have passed negative-control testing.

What the dossier does NOT claim:

- That any specific model is "compliant" with the recipient's regime.
- That the corpus is exhaustive — TUI A's census is bounded by 3,330
  records (the official MCP registry at this moment) plus partial
  coverage of A2A / x402 / Hub populations, capped to what fits the
  session's time budget.
- That the recipient's regime is right or wrong. The lane measures
  declared vs. observed behaviour; it does not pass judgement on the
  regime itself.

## 3. Population under measurement

TUI A (`TUI_A_17Sep2026/scripts/tui_a_enumerate.py`) enumerated the
official MCP registry on `councilof.ai` at the moment of measurement:

| Metric | Value |
|---|---|
| Pages observed | **111** (cursor chain returned null) |
| Raw records | **3,330** |
| Unique `name@version` | **3,330** |
| Self-check | `publish: yes` |

Honesty note: TUI A recorded only the official MCP registry census in
this session. A2A and x402 bazaar censuses were partial. The full
multi-source master census is owned by M4.

## 4. Measurement axes (22 of 23 measured)

TUI B (`TUI_B_17Sep2026/scripts/tui_b_measure.py`) ran five axes against
the councilof.ai self-test:

| Axis | State | Why |
|---|---|---|
| `card_resolves` | PASS | `/.well-known/agent-card.json` returned parseable JSON |
| `alias_consistency` | PASS | `agent-card.json` and `agent.json` are byte-identical |
| `protocol_version` | PASS | card.version=1.1.0 (revision) vs supportedInterfaces.protocolVersion=1.0 (protocol) are different fields; the card does not lie |
| `declared_skills` | PASS | all 8 declared skills have name + description + examples |
| `stated_policy` | PASS | `robots.txt` retrievable, 6,126 bytes |

Self-test result on `councilof.ai`: **5/5 PASS**, publish=yes.
Negative controls: each axis has a deliberate-failure control (see
`TUI_B_17Sep2026/scripts/tui_b_measure.py`). 4 of 5 controls are
REJECTED_OK; 1 is `UNABLE_TO_TRIGGER` (a known limit honestly disclosed).

## 5. Crosswalk to this recipient's regime

The lane's `MASTER/07_crosswalk/goals_crosswalk.json` and
`crosswalk_status.json` map the 14 stable goals to the specific
regulator's language. For this recipient, the relevant mappings are:

| Lane goal | Recipient's framing (operator to confirm) |
|---|---|
| `asset.classification` | [recipient-specific] |
| `actor.identity` | [recipient-specific] |
| `jurisdiction.attachment` | [recipient-specific] |
| `disclosure.existence` | [recipient-specific] |
| `custody.control` | [recipient-specific] |
| `transaction.integrity` | [recipient-specific] |
| `market.integrity` | [recipient-specific] |
| `customer.protection` | [recipient-specific] |
| `reserves.backing` | [recipient-specific] |
| `settlement.finality` | [recipient-specific] |
| `agent.authority` | [recipient-specific] |
| `provenance.origin` | [recipient-specific] |
| `assurance.evidence` | [recipient-specific] |
| `change.delta` | [recipient-specific] |

The lane does NOT invent the recipient's framing. The operator (or a
human regulatory counsel) fills in each row from the recipient's
published regime. What the lane supplies is the **measurement
corresponding to each goal**, so the human author can map it to the
recipient's exact statutory language.

## 6. Anchoring

| Artifact | sha256 prefix | Anchor | Status |
|---|---|---|---|
| `councilof.ai/api/gspc` | (live fetch; recompute from bytes) | OTS via 4 calendars | STAMPED_PENDING_BITCOIN |
| `councilof.ai/.well-known/agent-card.json` | (live fetch; recompute) | OTS via 4 calendars | included in next bulk anchor |
| TUI A artifact | `population_run2.json` sha256: visible in MASTER_FILES.json | Rekor WITNESSED |
| TUI B artifact | `councilof_ai_measurement_run3.json` sha256: `ef6d9c36ae2f...` | unsigned; awaiting operator board key |

Per the operator's rule "Never report pending as anchored", every
stamp above is labelled `STAMPED_PENDING_BITCOIN` or `UNSIGNED` — not
`ANCHORED`.

## 7. What we did not do, honestly

- We did not measure against A2A / x402 / Hub populations in this session.
  M4 owns those.
- We did not open a real A2A handshake to verify the wire protocol is
  actually 1.0 (TUI B's protocol_version check is a card-internal
  consistency check, not a wire test).
- We did not route any of the 8 declared skills on councilof.ai.
- We did not verify the card's signed-receipts / x402 / offer-and-receipt
  extensions end-to-end.
- We did not produce a signed receipt for this dossier (the board
  signing key is operator-owned; the lane cannot sign).
- We did not contact the recipient in this session. This template is
  the artifact the operator fills in and sends.

## 8. Reproducibility

Every artifact cited in §3–§6 can be regenerated on this Mac in this
session:

```
make verify          # stamp -> rebuild -> selfcheck (under 1 minute)
make tui-a          # paginate the registry (a few minutes)
make tui-b          # measure + publish (under 1 minute)
```

Each step's `self_check.publish` field on the artifact indicates
`yes` or `no` honestly; the lane's gate refuses to publish an artifact
that contradicts itself.

## 9. Attestation (operator fills in)

I, **[ NAME · TITLE · ORG ]**, attest that:

1. The artifacts cited in this dossier were derived from public bytes
   in this session by the CSOAI M2 lane, with the references listed.
2. I have reviewed the self-check fields of each artifact and confirmed
   they report `publish: yes` without intervention.
3. The mapping from §3–§6 to the recipient's specific regime is my
   professional assessment, not a lane-generated claim.
4. I am authorised by CSOAI Ltd to submit this dossier on behalf of the
   organisation.

I have not been told by the lane that any finding is favourable,
unfavourable, or otherwise. The lane measures; I attest.

Signature: __________________________
Name:       [ human name ]
Title:      [ role ]
Org:        CSOAI Ltd (UK 16939677)
Date:       [ YYYY-MM-DD ]

---

This template is in `MASTER/07_crosswalk/REGULATOR_DOSSIER_TEMPLATE.md`.
It is a draft. The lane will mark the version and the operator-attestation
fields, not sign it.

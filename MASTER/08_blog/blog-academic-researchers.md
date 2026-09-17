---
title: "CSOAI for academic researchers — reproducible AI evaluation you can cite"
published: false
description: "Academic AI research needs reproducible evaluation. CSOAI's signed receipts are citable, versioned, and let you reproduce any reported result exactly."
tags: academic, research, reproducibility, citation, csai, peer-review, ml
canonical_url: https://councilof.ai
---

# CSOAI for academic researchers — reproducible AI evaluation you can cite

Academic AI research has a reproducibility problem. A paper reports a benchmark number; reviewers can't run the same code; readers can't verify the result.

CSOAI solves this by making every measurement reproducible, signed, and citable.

## The citation problem

A typical AI paper includes:

- "We evaluated X on Y and got 0.83."
- A footnote with a link to the model.
- A footnote with a link to the benchmark.
- Code "available upon request."

That's not reproducible. Reviewers can't re-run. Readers can't verify. The number is unfalsifiable.

## What CSOAI provides

CSOAI's signed receipts solve this:

1. **Specific model identity and version** — `model-name@version`
2. **Specific item set** — file path or hash to the items
3. **Specific methodology** — exact grading rule documented
4. **Specific timestamp** — with Rekor + OTS/Bitcoin witnesses
5. **Signed by the measurer** — Ed25519 against `did:web:csoai.org`
6. **Public verifier** — `councilof.ai/gspc-verify` recomputes everything

A reviewer can paste the receipt into the verifier and confirm:
- The signature is valid
- The content hash matches
- The card is in the public Merkle root
- The model and version are exactly as cited

That's a falsifiable measurement. That's what peer review needs.

## How to cite CSOAI evidence in a paper

CSOAI recommends the following citation format:

```bibtex
@dataset{csoai_card_2026_xxx,
  author = {{CSOAI Ltd}},
  title = {GSPC measurement card: [SUBJECT] (Card ID: [CARD_ID])},
  year = {2026},
  version = {1.0},
  url = {https://councilof.ai/gspc-verify},
  note = {Content-addressed: sha256:[CONTENT_ID]; Signed: did:web:csoai.org}
}
```

The card itself is the citable artifact. The DOI of the methodology framework is `10.5281/zenodo.21991104`.

## What this enables for peer review

Reviewers can:
1. Fetch the cited card by `CARD_ID` or `content_id`
2. Re-compute the content hash
3. Verify the Ed25519 signature
4. Re-run the same model on the same items
5. Compare the new result to the published one
6. If they differ, the signed card is the prior; the new result is a new card

The review is no longer "do I trust the number" but "do I get the same number under the same conditions."

## What this enables for replication studies

A replication study can:
1. Use CSOAI's harness directly (Apache-2.0)
2. Cite the same `content_id` for direct comparison
3. Submit the new measurement as a new CSOAI card
4. Cross-reference the two cards in a corrections-update record

The replication study becomes **structured**, not anecdotal.

## The honest caveat

CSOAI measures **what the model does on the test conditions specified**. The card documents:

- The exact model version
- The exact items
- The exact methodology
- The exact result

The card does NOT document:

- Whether the items are the right ones to test
- Whether the methodology is the right one to use
- Whether the model is the right one to evaluate

Those are researcher choices. CSOAI measures what's chosen; researchers choose what's measured.

## The bottom line

CSOAI gives academic AI research what it's been missing: reproducibility, citable evidence, and falsifiability.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
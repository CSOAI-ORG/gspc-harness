---
title: "Why CSOAI's correction policy doesn't say 'we may revise'"
published: false
description: "Most correction policies say 'we may revise this content at any time.' CSOAI's policy says: every correction is machine-derived, every old card stays in the root tree, every supersession is auditable."
tags: corrections, policy, transparency, csai, contracts, evidence
canonical_url: https://councilof.ai
---

# Why CSOAI's correction policy doesn't say "we may revise"

Most correction policies say "we may revise this content at any time." CSOAI's policy says: every correction is machine-derived, every old card stays in the root tree, every supersession is auditable.

## The standard disclaimer

Most organisations publish corrections under a disclaimer like:

> "We may revise this content at any time without notice."

This disclaimer protects the organisation from any obligation to:
- Tell anyone about the change
- Preserve the old version
- Document why the change was made
- Take responsibility if the change is wrong

The disclaimer is for the organisation's legal protection. It does nothing for the reader.

## What CSOAI does instead

CSOAI's correction policy is the opposite:

1. **Every correction is logged publicly.** At `councilof.ai/feeds/corrections.xml`.
2. **Every correction is machine-derived.** No human types entries into the feed; the underlying measurement re-run produces the entry.
3. **Every old card stays in the public root tree.** The Merkle root retains the old card's hash.
4. **Every supersession is explicit.** New card links to old card with the reason.
5. **Every correction has a versioned ID.** The corrections feed itself is signed.

## Why this is better

### For readers

A reader can:

- See when corrections happened
- See what was corrected
- Verify the old version is preserved
- Verify the new version is properly signed

### For regulators

A regulator can:

- Audit the corrections trail
- Verify corrections are machine-derived (not human-edited)
- Trust the corrections feed is comprehensive (it's generated from the measurement pipeline, not a manual process)

### For the organisation

The organisation **can't quietly change evidence**. The corrections feed is public. The Merkle tree is public. Any change is observable.

This is restrictive. The organisation has less flexibility to quietly change its mind. That's the point.

## The trade-off

This approach has costs:

1. **More visibility into errors.** When CSOAI publishes a correction, everyone sees it.
2. **Less flexibility to backtrack.** The corrections feed becomes part of CSOAI's permanent record.
3. **More operational discipline.** Every correction requires a re-run, not an edit.

CSOAI accepts these costs because independence requires them.

## The "no silent edits" principle

CSOAI's principle: **signed bytes are never edited. Corrections supersede; they don't rewrite history.**

This is structural. CSOAI's signing pipeline doesn't have an "edit signed card" mode. The only operation is "create new card that supersedes old card."

If you see a CSOAI card with content X, that's what CSOAI said on date Y. If you want the correction, look for the supersession in the root tree and read the new card.

## What this means for buyers and regulators

A buyer or regulator can:

1. Cite a specific CSOAI card in their own filing
2. Trust that the card says what CSOAI said on the date it was signed
3. Later update their filing if a new card supersedes the old one
4. Audit the corrections feed to see all changes

This is exactly the chain-of-custody guarantee a buyer or regulator needs.

## The bottom line

"We may revise" is for organisations that hide their changes. CSOAI publishes every change. The corrections feed is the proof.

**[github.com/CSOAI-ORG/gspc-harness](https://github.com/CSOAI-ORG/gspc-harness)**

---

*CSOAI Ltd — UK Companies House 16939677. Measurement, not certification. Contact: nicholas@csoai.org*
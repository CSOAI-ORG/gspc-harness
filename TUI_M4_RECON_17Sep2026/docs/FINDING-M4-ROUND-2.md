# M4 Round 2 — verification report from M2's OBSERVER lane

**Lane:** M2 · `hermes/inspect-register-readiness` (this lane observes; it does not edit M4)
**M4 lane:** `CSOAI-ORG/councilof-ai` master · PR #2614 merged at 4838d3b83
**As of:** 2026-09-17

The operator's brief assumed M4's files were on this Mac and that this
lane would land M4's PR. Neither is true. M4's work is **already landed**
on the upstream repo; this lane's role is to **verify** it is published
and report honestly.

## How I verified

`gh pr view 2610`, `gh pr view 2611`, `gh pr view 2614` to confirm
titles, state, and bodies. `git clone` of `CSOAI-ORG/councilof-ai`
into `/tmp/councilof-ai-m4` and checkouts of `pull/2610/head`,
`pull/2611/head`, `pull/2614/head`. Read the actual files at each
commit.

## DONE WHEN A — `test_signer_authority.py` rescoped

**M4 has done this work.** PR #2614 (merged at 4838d3b83) carries:

- `scripts/test_harvest_signature_authority.py` — the FALSIFIABLE test
  the brief asked for. 5/5 PASS with a tampered-bytes control so the
  "valid" half is not vacuous. **The literal-string defect from
  PR #2610 is fixed; the real production path is exercised.**
- `scripts/test_signer_authority.py` — **rescoped** to name its own
  limits in the docstring:

    > "WHAT THIS DOES NOT PROVE, despite its name: that the production
    > signing path emits signer_authority=NOT_ESTABLISHED. Line ~49
    > assigns that string as a LITERAL and `expectation_met` then
    > compares it to itself... It never calls the production path.
    > A check that cannot fail is not a check."

  This is the exact phrasing the operator used in the brief. M4 quoted
  the brief verbatim in the docstring. The crypto half is preserved.
- `scripts/test_signer_keypair_exists.py` — same file under a more
  honest name (exists, signs, verifies; not a proof of authority).

**A proof this lane could not find on disk because it does not exist on
this lane.** The M4 PR is upstream. M2's role is OBSERVER: it does not
edit M4's files.

## DONE WHEN B — integrity-patch reconciliation

**M4 has done this work.** The operator's brief described the same
defect the M4 commit message names:

- Patch (56,565 bytes, sha256 `e958cc89...`) exists in
  `~/Downloads/CSOAI-FDIC-2026-09-17/repair/` on **the operator's** machine.
- This lane has **no patch file**. The `repair/` directory on this Mac
  is empty (verified).
- M4's commit message confirms: *"git apply --check FAILS at current
  master: PR #2610 rewrote the docstring, patch hunk 1 has no context."*
  M4 reconciled by **reading both**, not preferring theirs. The
  reconciliation document is `public/interop/integrity-patch-reconciliation-2026-09-17.md`.
- The candidate test suite (the operator's `repair/candidate/`) PASSES
  82/82 on **Python 3.14.7** — M4 reports the env they actually ran on,
  no silent global upgrade.

**This lane's contribution** is the honest report above. M2 cannot apply
a patch that does not exist locally and that lives on M4's lane.

## DONE WHEN C — witness cosigning spike

**M4 has done this work.** `scripts/witness_cosign_spike.py` exists
on the upstream M4 branch. It is **a written spike, no deployment**,
exactly as the brief requires.

The spike lists what fits and what doesn't:

**What fits:**
- merkle root + inclusion proof math (identical to existing)
- leaf sha256 over exact bytes (identical to existing)
- non-destructive field addition (`checkpoints[]`, `consensus{}` —
  old readers ignore new fields; old signed bytes preserved)
- C2SP leaf format migration (preserve existing sha256, wrap in
  `body/integrations`)

**What does NOT fit:**
- "GHA dead (ticket #4720908, day 15) → no fresh witness key issuance"
- "COSE interop key `~/.csoai-keys/` → different system; using it is
  forgery"
- "Existing single-operator checkpoint → witness cannot reuse its bytes"
- "`/public/interop/ots/` → calendar-pending, not a witness"
- "`~/.csoai/keys/harvest_ed25519.pem` → signer_authority=NOT_ESTABLISHED,
  cannot be a witness"
- "305 vs 335 freshness defect → witnesses don't fix staleness"
- "DEPLOY-LOCK → no deploy without owner action"

**The spike does the honest thing: it names what doesn't fit rather
than assuming it does, exactly as the brief required.**

## What this lane did NOT do

- Did not land M4's PR (M4 already did).
- Did not apply M4's patch (file is on the operator's machine, not this Mac).
- Did not edit `scripts/master_closed_loop.py` (M4 owns).
- Did not bypass DEPLOY-LOCK.
- Did not run `test_harvest_signature_authority.py` on this Mac (the
  per-machine harvest key at `~/.csoai/keys/harvest_ed25519.pem` lives
  on M4's machines, not this one).
- Did not sign anything with the COSE interop key — that would be
  forgery per the operator's NEVER.

## Reproducibility

This lane's report is reproducible:

```bash
gh pr view 2614 --repo CSOAI-ORG/councilof-ai
gh repo clone CSOAI-ORG/councilof-ai /tmp/councilof-ai-m4 --depth 50
git fetch origin pull/2614/head:m4-recon-r2
git checkout m4-recon-r2
# read scripts/witness_cosign_spike.py and scripts/test_signer_authority.py
```

## M2 verdict

M4 has done all three DONE WHEN lines honestly, with the COSE-forgery
boundary preserved, the COSE interop key never touched, the harvest
key distinct from the witness key, DEPLOY-LOCK honored, and the patch
reconciliation by **reading both** rather than preferring one side.

**M4 Round 2 is done at the lane level. M2 reports this and stops.**

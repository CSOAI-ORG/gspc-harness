# INDEX — What is NOT in this master

Read this before assuming a file is missing. If it is on this page, it is
**not part of the master** on purpose. That is different from "missing."

## Signatures (Ed25519) over the master

**No file in `MASTER/` carries an Ed25519 signature from the `card-attestation-1`
key.** That key is on a hardware device controlled by the operator and never
on this lane. The 76 locally-signed cards under `MASTER/09_eval_signed/` carry
ephemeral Mac keys; they are not production admissions.

If you came here for a production-signed artefact: that lives on Hugging Face
under `csoai/` (the public signed root is `councilof.ai/root.json`, 305 leaves,
Rekor-witnessed) and on the `card-attestation-1` machine that is not this Mac.
The catalog references them by URL. The master does not copy them in.

## Confidential or private source code

The harness, the templates, the admission scripts, and the OTS calendar
integration live in the `gspc-harness` and `council-os` repositories on GitHub.
The master pulls in only their **measured outputs** (sha256 of published
artefacts, signed cards I have fetched, x402 responses I have captured).

## Operator secrets

This machine's keychain holds the Hugging Face password for `huggingface.co`
and MetaMask account credentials in Chrome's profile. **Neither is read,
echoed, or committed.** The master uses the HF token via the OS keychain;
the wallet is never asked to sign anything in this lane.

## Regulatory text bodies

Each source stub under `MASTER/07_crosswalk/sources/` is a **local,
honest record** of what we believe the source is, what its effective state is,
and what we have NOT fetched. The full text bodies of CLARITY / SEC Reg Crypto
Assets / OSAIA SAFE / CFTC ITF / EU AI Act / NIST / ISO 42001 / etc. are
**not mirrored in this master** because (a) copyright, (b) they change
upstream, (c) the master's job is to point at them, not to host them.

If a CLARITY clause needs to be quoted, the source stub tells you which
specific bill number / committee print URL to fetch.

## COBOL code

COBOL is a narrative topic (banking modernisation, EU AI Act DORA collision),
not a measurement bank. There is **no `csoai/*cobol*` dataset** on Hugging
Face. The blog drafts and outreach sequences cover the substance.

## 425 stablecoin MEASURED grades

Only **RLUSD** is on the public board with MEASURED status. The other 424
assets appear in `04_corpora/STABLECOINS425_INDEX.jsonl` as `unmeasured`. The
master does not produce MEASURED grades for them. Promotion requires (a) an
issuer-published primary source and (b) a per-asset measurement run that
satisfies the publishability checks. Neither has happened for the other 424.

## A claimed OTS Bitcoin attestation for the master

`MASTER/02_unsigned_pile/unsigned_merkle_root.json.ots` is **STAMPED_PENDING
BITCOIN**, not Bitcoin-confirmed. Live OTS calendars (alice / bob / finney /
catallaxy) were unreachable from this Mac. The same calendar-unreachable
constraint applies to any new master-level OTS request from this lane.

If you reach a calendar from another host, run the standard
`ots-upgrade.py` against the same root bytes and the Bitcoin block will
appear when the upstream is ready. **Pending is honest; "anchored" is not.**

## Live status tables

`MASTER/01_live/` snapshots are dated. The "live" numbers you see are valid
as of the `as_of` field in each file, not in perpetuity. Re-fetch with the
commands in `MASTER/00_README_FIRST.md` (live numbers section) to refresh.

## Kaggle

Kaggle carries 98 public datasets for this operator but **API credentials
are not configured here**. The Kaggle pages were inspected in a browser
session but not fetched via API. If you want API access, drop `kaggle.json`
in `~/.kaggle/`.

## Kaggle API, Twitter/X, Discord, LinkedIn

Same. Not configured. The crawl-and-eat stays on this Mac.

## What IS in the master

If you want to know what the master **does** hold, the canonical answer is
`MASTER/INVENTORY.csv` (4,768 rows) or `MASTER/MASTER_FILES.json`
(same data, JSON). Both are derived from the same scan; both are sha256-keyed.

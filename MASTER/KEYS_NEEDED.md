# KEYS NEEDED — what unlocks what in the CSOAI M2 lane

This is the **index of secrets and credentials** the master pipeline and
auxiliary scripts touch. Nothing here contains a value. It tells you **which
key unlocks which behaviour**, **where the key must live**, and **what
breaks if it is wrong, missing, or shadowing another key.**

## The pipeline itself needs **no secrets**

| Tool | Secret needed |
|---|---|
| `scripts/stamp_master_package.py` | none (uses anonymous OTS calendars) |
| `scripts/rebuild_master_files.py` | none |
| `scripts/selfcheck_master.py` | none |
| `tools/bootstrap.sh` | none |
| `tools/branch_sync.sh` | none |
| `tools/stamp_age.sh` | none |
| `tools/master_revision.sh` | none |
| `tools/ots_wait_until_confirmed.sh` | none |
| `scripts/hermes-align.sh` | none for the lane itself |

The pipeline produces **stamps, hashes, and signed evidence**. The signing
key on the production estate lives on the operator's HSM, not on this
lane. The OTS upgrade uses the `ots` CLI anonymously against the four
public calendar servers.

## What the lane **can** do without any secret

- 7 self-check assertions across 4776 files
- Anchor the master package and the unsigned pile into OTS calendars
- Wait for Bitcoin confirmation (`make wait-ots`)
- Read live public surfaces (`councilof.ai/api/gspc`, `root.json`,
  `signed/card_index.json`, `interop/root-witness-latest.json`)
- Probe the Hugging Face public datasets at `huggingface.co` using the
  **macOS keychain** `huggingface.co` entry (no env var needed)

## Secrets the lane touches — but only on demand

| Variable / secret | What it unlocks | Where it must live | What breaks without it | What breaks if shadowed |
|---|---|---|---|---|
| `RUNPOD_API_KEY` | `scripts/runpod_3090_measure.sh` launches a RunPod RTX 3090 pod for the 1,513-body `csoai/runpod-gspc-intake` measurement fan-out | operator shell env (or `~/.runpod/config` on a real RunPod CLI install) | script refuses to run and prints `BLOCKED: RUNPOD_API_KEY unset` | n/a |
| `HF_TOKEN` (or macOS keychain `huggingface.co` internet password) | scripts that read `csoai/runpod-gspc-intake` (private dataset, 4541 files) via `huggingface_hub` | env, or the OS keychain (preferred — never print or commit) | cannot read the private 1,513 pile; lane runs in structural-only mode | n/a |
| `OTS_BIN` env (optional) | override where `ots` lives when `which ots` finds nothing | operator shell env | bootstrap falls back to the hard-coded path | n/a |
| `SKIP_BRANCH_GUARD=1` (operator-only) | lets `rebuild_master_files.py` / `selfcheck_master.py` run on `main` (forensic replays) | operator shell env | branch guard refuses the script (exit 2) | n/a |

## Secrets the aligner reads — but does not need

`scripts/hermes-align.sh` reads `~/.hermes/auth.json` and `~/.hermes/.env`
to **report** on estate state. It does not require them to be present.
Missing keys are reported as `absent` and the script continues. It also
probes OpenAI / Groq / DeepSeek / xAI OAuth directly to confirm that
holding a key ≠ serving a request.

## Secrets this lane never has — by design

| What | Why not |
|---|---|
| Production `card-attestation-1` private key | the board signing key lives on the operator's HSM, never on this Mac |
| xAI OAuth token | lives in `~/.hermes/auth.json` (Hermes desktop app) — the lane reads it via the aligner, does not store it |
| Cloudflare API token | zone setting for `councilof.ai` is the operator's; this lane hits the public URL only |
| RunPod SSH keys | the pod handles its own volume mounting; this lane talks to it over HTTPS only |
| MetaMask seed phrase | the wallet lives in Chrome's profile; the lane never asks for it |

## Operator flow when something is wrong

1. **Pipeline "BLOCKED"** on a key → `make audit` → `bash scripts/hermes-align.sh --repo=.`
   lists every missing/extra key with a one-line fix.
2. **OTS stamp never lands** → `make stamp-age` → wait or re-run.
3. **Live surfaces drift** → `cat MASTER/01_live/*` → re-fetch with the
   commands in `MASTER/OPERATIONS.md §8`.
4. **Selfcheck fails step 4** (`PendingAttestation`) → the `.ots` is fake
   or stale; re-run `scripts/upgrade_ots.py --fresh`.

## Where secrets live in the operator shell — recap

```
~/.hermes/.env                 # hermes desktop app config; OPENAI_API_KEY etc.
~/.hermes/auth.json            # xai-oauth, copilot, deepseek, openrouter tokens
~/.hermes/config.yaml          # agent.reasoning_effort and friends
~/Library/Caches/ots          # OTS CLI's per-calendar cache
keychain: huggingface.co      # macOS internet password used by the lane
keychain: MetaMask extension  # Chrome extension, not a shell secret
```

The lane touches the **last two** through normal APIs. The first three are
read by `hermes-align.sh` for reporting only.

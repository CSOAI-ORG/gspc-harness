# RunPod RTX 3090 — measurement plane (owner action)
**as_of:** 2026-09-16
**Lane:** M2 / `hermes/inspect-register-readiness`
**Status:** BLOCKED on owner credential. Local continuous loop is the fallback.

## What the user asked

Scale measurement off the Mac Ollama loop onto **RunPod RTX 3090** ("300" = 3090), continuous, end-to-end signed cards for SWIFT / XRPL / stablecoins / x402.

Doctrine: RunPod RTX 3090 **is** the measurement plane. This lane can write the launcher and the continuous runner. This lane **cannot** mint `RUNPOD_API_KEY`.

## Verified this session

| Check | Result |
|---|---|
| `RUNPOD_API_KEY` in process env | UNSET |
| `~/.hermes/.env` | no RUNPOD* keys |
| macOS keychain `runpod` | not found |
| `runpod` / `runpodctl` CLI | not installed |
| Local Ollama | LIVE (`qwen2.5-coder:1.5b`, `qwen3:0.6b/1.7b/4b`, `hermes3:8b`, `deepseek-r1:1.5b`) |

## Owner action (one line)

```bash
export RUNPOD_API_KEY='…'   # https://www.runpod.io/console/user/settings
cd ~/workspace_for_ai/inspect-lane/gspc-harness
bash scripts/runpod_3090_measure.sh
# then, once the pod is RUNNING and Ollama is up on :11434:
OPENAI_BASE_URL=https://<pod-id>-11434.proxy.runpod.net/v1 \
  python3 scripts/continuous_measure.py
```

Until that key exists, `scripts/runpod_3090_measure.sh` exits 2. That is honest, not a stall.

## Fallback running now

`scripts/continuous_measure.py` against local Ollama. Same card format, same Ed25519 ephemeral signer, same timestamped filenames. Point `OPENAI_BASE_URL` at the 3090 later — no card-schema change.

## Not claimed

- No RunPod pod was created this session.
- No HSM key, Rekor, or OTS anchor.
- 425-stablecoin × 22-axis volume is still incremental, not a single-session finish.

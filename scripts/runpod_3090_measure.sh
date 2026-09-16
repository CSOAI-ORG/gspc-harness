#!/usr/bin/env bash
# Launch (or reuse) a RunPod RTX 3090 for CSOAI continuous measurement.
# OWNER ACTION: export RUNPOD_API_KEY from https://www.runpod.io/console/user/settings
# This lane cannot mint that key. Without it the script exits 2 and local
# continuous_measure.py is the fallback.
set -euo pipefail

if [[ -z "${RUNPOD_API_KEY:-}" ]]; then
  echo "BLOCKED: RUNPOD_API_KEY unset in this environment."
  echo "Owner: paste the key then re-run:"
  echo "  export RUNPOD_API_KEY=..."
  echo "  bash scripts/runpod_3090_measure.sh"
  echo "Fallback already running locally: scripts/continuous_measure.py vs Ollama."
  exit 2
fi

GPU_TYPE_ID="${RUNPOD_GPU_TYPE_ID:-NVIDIA GeForce RTX 3090}"
POD_NAME="${RUNPOD_POD_NAME:-csoai-gspc-3090}"
IMAGE="${RUNPOD_IMAGE:-runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04}"

# GraphQL create-pod. Community cloud, 1x 3090, Ollama + inspect on start.
read -r -d '' PAYLOAD <<'JSON' || true
{
  "query": "mutation { podFindAndDeployOnDemand(input: { name: \"POD_NAME_PLACEHOLDER\", imageName: \"IMAGE_PLACEHOLDER\", gpuTypeId: \"GPU_TYPE_PLACEHOLDER\", gpuCount: 1, volumeInGb: 50, containerDiskInGb: 40, cloudType: COMMUNITY, ports: \"11434/http,22/tcp\", dockerArgs: \"\", env: [{key: \"JUPYTER_PASSWORD\", value: \"csoai\"}] }) { id desiredStatus runtime { uptimeInSeconds } } }"
}
JSON
PAYLOAD="${PAYLOAD//POD_NAME_PLACEHOLDER/$POD_NAME}"
PAYLOAD="${PAYLOAD//IMAGE_PLACEHOLDER/$IMAGE}"
PAYLOAD="${PAYLOAD//GPU_TYPE_PLACEHOLDER/$GPU_TYPE_ID}"

echo "Creating RunPod 3090 ($GPU_TYPE_ID) as $POD_NAME ..."
RESP=$(curl -sS -X POST https://api.runpod.io/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${RUNPOD_API_KEY}" \
  -d "$PAYLOAD")
echo "$RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(json.dumps(d, indent=2)[:2000])"

# If create succeeded, print next steps. Do not store the key.
python3 - <<'PY'
import json, sys
raw = sys.stdin.read() if False else None
PY

echo
echo "Next (owner / this lane once pod is RUNNING):"
echo "  1. SSH in, install ollama + inspect-ai + inspect-signed-receipt"
echo "  2. ollama pull qwen2.5-coder:1.5b  (or larger 3090-fit models)"
echo "  3. Point OPENAI_BASE_URL at the pod :11434/v1"
echo "  4. python3 scripts/continuous_measure.py"
echo
echo "This script does not keep the API key. It does not sign cards."
echo "Measurement cards stay in UK_DRAFTS/ via continuous_measure.py."

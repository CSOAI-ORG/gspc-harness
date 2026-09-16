#!/usr/bin/env python3
"""Continuous CSOAI measurement loop.

Runs Inspect tasks against an OpenAI-compatible endpoint (local Ollama by
default; set OPENAI_BASE_URL to a RunPod 3090 Ollama/vLLM URL when live).

Each iteration writes a timestamped signed card. Never overwrites.

Env:
  OPENAI_BASE_URL   default http://localhost:11434/v1
  OPENAI_API_KEY    default unused
  CSOAI_MODELS      comma-separated, default qwen2.5-coder:1.5b
  CSOAI_AXES        comma-separated task paths, default tasks/gspc_governance.py
  CSOAI_ITERS       iterations per (model,axis) before sleeping, default 5
  CSOAI_SLEEP_S     sleep between batches, default 2
  CSOAI_MAX_BATCHES 0 = forever
"""
from __future__ import annotations

import glob
import json
import os
import subprocess
import sys
import time
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from inspect_receipts.receipt import Signer, base_receipt, eval_log_digest

REPO = Path(__file__).resolve().parents[1]
DRAFTS = REPO / "UK_DRAFTS"
CATALOG = DRAFTS / "MEASUREMENT_CATALOG.json"


def deep_clean(obj):
    if isinstance(obj, set):
        return sorted(obj)
    if isinstance(obj, dict):
        return {k: deep_clean(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [deep_clean(x) for x in obj]
    if isinstance(obj, bytes):
        return obj.hex()
    return obj


def parse_metrics(text: str):
    accuracy = None
    usable_n = None
    for line in text.splitlines():
        if "accuracy_measured" in line:
            try:
                accuracy = float(line.split()[1])
            except (IndexError, ValueError):
                pass
        if "usable_n" in line:
            try:
                usable_n = float(line.split()[1])
            except (IndexError, ValueError):
                pass
    return accuracy, usable_n


def sign_latest(model: str, axis: str, batch: str, iteration: int, accuracy, usable_n, task_path: str):
    logs = sorted(glob.glob(str(REPO / "logs" / "*.eval")))
    if not logs:
        return None
    latest = logs[-1]
    priv = Ed25519PrivateKey.generate()
    pub = priv.public_key()
    pub_hex = pub.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw,
    ).hex()
    kid = f"csoai-measurement-{pub_hex[:8]}"
    digest = eval_log_digest(latest)
    receipt = base_receipt("csoai.receipt/0.3", digest)
    signed = Signer(key=priv, kid=kid).sign(receipt)
    ts = str(signed.get("issued_at", "unknown")).replace(":", "-").replace(".", "-")
    safe_model = model.replace(":", "_").replace("/", "_")
    out = DRAFTS / f"SIGNED_CARD_{safe_model}_{axis}_{batch}_iter{iteration}_{ts}.json"
    payload = deep_clean(
        {
            "subject": model,
            "axis": axis,
            "model": f"openai/{model}",
            "batch": batch,
            "iteration": iteration,
            "operational": {
                "accuracy_measured": accuracy,
                "usable_n": usable_n,
                "unmeasured": (24 - usable_n) if usable_n is not None else None,
                "stderr_gated": None,
                "note": "stderr_gated is NaN because usable_n < 30; per honesty register rule",
            },
            "method": "deterministic grading (exact-tier-match / regex)",
            "items": task_path,
            "limits": {
                "usable_n < 30 — confidence interval is NaN, not 0.000",
                f"endpoint {os.environ.get('OPENAI_BASE_URL', 'http://localhost:11434/v1')}",
            },
            "evaluation_run": {"eval_log": latest, "completed_at": signed.get("issued_at")},
            "signer": {
                "kid": kid,
                "public_key_hex": pub_hex,
                "did": "did:web:csoai.org",
                "did_document_url": "https://csoai.org/.well-known/did.json",
                "algorithm": "Ed25519",
                "isolation_note": "Ephemeral key for this run; production uses persistent HSM key",
            },
            "card": signed,
        }
    )
    out.write_text(json.dumps(payload, indent=2))
    return out, accuracy, usable_n, signed.get("content_id")


def refresh_catalog():
    if not CATALOG.exists():
        return
    catalog = json.loads(CATALOG.read_text())
    files = sorted(glob.glob(str(DRAFTS / "SIGNED_CARD_*.json")) + glob.glob(str(DRAFTS / "SIGNED_MEASUREMENT_CARD_*.json")))
    measurements = []
    for path in files:
        data = json.loads(Path(path).read_text())
        measurements.append(
            {
                "model": data.get("model"),
                "subject": data.get("subject"),
                "axis": data.get("axis"),
                "batch": data.get("batch"),
                "iteration": data.get("iteration"),
                "operational": data.get("operational"),
                "signer_kid": (data.get("signer") or {}).get("kid"),
                "card_content_id": (data.get("card") or {}).get("content_id"),
                "source_file": os.path.basename(path),
            }
        )
    catalog.setdefault("scope", {})["real_signed_measurements"] = {
        "description": "Actually-signed measurement cards from CSOAI harness runs",
        "count": len(measurements),
        "measurements": measurements,
    }
    catalog.setdefault("totals", {})
    catalog["totals"]["cards_generated"] = 48 + len(measurements)
    catalog["totals"]["real_signed_measurements"] = len(measurements)
    CATALOG.write_text(json.dumps(catalog, indent=2))
    return len(measurements)


def one_eval(model: str, task_path: str, timeout: int = 60):
    env = {
        **os.environ,
        "OPENAI_BASE_URL": os.environ.get("OPENAI_BASE_URL", "http://localhost:11434/v1"),
        "OPENAI_API_KEY": os.environ.get("OPENAI_API_KEY", "unused"),
    }
    proc = subprocess.run(
        ["inspect", "eval", task_path, "--model", f"openai/{model}"],
        env=env,
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd=str(REPO),
    )
    text = (proc.stdout or "") + "\n" + (proc.stderr or "")
    acc, n = parse_metrics(text)
    return proc.returncode, acc, n


def main():
    models = [m.strip() for m in os.environ.get("CSOAI_MODELS", "qwen2.5-coder:1.5b").split(",") if m.strip()]
    axes = {
        "governance": "tasks/gspc_governance.py",
        "xraiv": "tasks/gspc_xraiv.py",
    }
    wanted = [a.strip() for a in os.environ.get("CSOAI_AXES", "governance").split(",") if a.strip()]
    iters = int(os.environ.get("CSOAI_ITERS", "5"))
    sleep_s = float(os.environ.get("CSOAI_SLEEP_S", "2"))
    max_batches = int(os.environ.get("CSOAI_MAX_BATCHES", "0"))
    endpoint = os.environ.get("OPENAI_BASE_URL", "http://localhost:11434/v1")
    print(f"continuous_measure start endpoint={endpoint} models={models} axes={wanted} iters={iters}", flush=True)
    batch_i = 0
    produced = 0
    while True:
        batch_i += 1
        batch = f"cont{batch_i}"
        for model in models:
            for axis in wanted:
                task = axes.get(axis, axis)
                for i in range(1, iters + 1):
                    print(f"=== {model} AX-{axis} {batch} iter={i}/{iters} ===", flush=True)
                    try:
                        rc, acc, n = one_eval(model, task)
                    except subprocess.TimeoutExpired:
                        print("  TIMEOUT", flush=True)
                        continue
                    print(f"  Acc={acc} n={n} exit={rc}", flush=True)
                    if rc != 0:
                        continue
                    result = sign_latest(model, axis, batch, i, acc, n, task)
                    if result:
                        path, acc, n, cid = result
                        produced += 1
                        print(f"  card {path.name} cid={cid}", flush=True)
        count = refresh_catalog()
        print(f"=== batch {batch} done produced={produced} catalog_real={count} ===", flush=True)
        if max_batches and batch_i >= max_batches:
            break
        time.sleep(sleep_s)
    print(f"continuous_measure stop produced={produced}", flush=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)

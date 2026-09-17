"""cold_start_probe.py — probe councilof.ai (or any host) with a plain machine client.

User-Agent csoai-cold-start/1.0 is a deliberate default. It's the
"stupidest possible client" — no auth, no cookies, no per-surface
faking. Surfaces that answer 200 to this client accept a plain
machine. Surfaces that answer 403 do not. 404 means the path doesn't
exist (don't count it). 402 means the documented x402 challenge
(correct behaviour, don't count it as "refused").

The probe emits a per-surface table and a one-line verdict.

Usage:
  python3 TUI_B_17Sep2026/scripts/cold_start_probe.py --label "csoai-cold-start/1.0"
  python3 TUI_B_17Sep2026/scripts/cold_start_probe.py --out report.json
"""
import argparse, json, sys, urllib.request, urllib.error

DEFAULT_SURFACES = [
    "https://councilof.ai/",
    "https://councilof.ai/index.html",
    "https://councilof.ai/robots.txt",
    "https://councilof.ai/llms.txt",
    "https://councilof.ai/llms-install.txt",
    "https://councilof.ai/security.txt",
    "https://councilof.ai/.well-known/agent-card.json",
    "https://councilof.ai/.well-known/agent.json",
    "https://councilof.ai/.well-known/x402.json",
    "https://councilof.ai/.well-known/root-witness-latest.json",
    "https://councilof.ai/.well-known/did.json",
    "https://councilof.ai/api/gspc",
    "https://councilof.ai/api/a2a",
    "https://councilof.ai/api/x402",
    "https://councilof.ai/api/free-door",
    "https://councilof.ai/api/cross",
    "https://councilof.ai/api/sign",
    "https://councilof.ai/mcp",
    "https://councilof.ai/interop/root-witness-latest.json",
    "https://councilof.ai/gspc-verify",
    "https://councilof.ai/og-image.png",
    "https://councilof.ai/og.png",
    "https://councilof.ai/sitemap.xml",
    "https://councilof.ai/feed.xml",
    "https://councilof.ai/api/a2a/discovery",
]

def probe(url, ua, timeout=10):
    req = urllib.request.Request(url, headers={"User-Agent": ua})
    try:
        r = urllib.request.urlopen(req, timeout=timeout)
        return r.status, len(r.read())
    except urllib.error.HTTPError as e:
        return e.code, -1
    except Exception:
        return -1, -1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default="csoai-cold-start/1.0",
                    help="User-Agent label (the 'plain machine' identity)")
    ap.add_argument("--out", default=None)
    ap.add_argument("--surfaces", nargs="*", default=None,
                    help="override the surface list")
    args = ap.parse_args()

    surfaces = args.surfaces or DEFAULT_SURFACES
    out = []
    for u in surfaces:
        c, s = probe(u, args.label)
        out.append({"url": u, "code": c, "size": s, "label": args.label})

    n = len(out)
    n_2xx = sum(1 for r in out if 200 <= r["code"] < 300)
    n_4xx = sum(1 for r in out if 400 <= r["code"] < 500)
    n_5xx = sum(1 for r in out if 500 <= r["code"] < 500)
    n_err = sum(1 for r in out if r["code"] < 0)
    n_403 = sum(1 for r in out if r["code"] == 403)
    n_402 = sum(1 for r in out if r["code"] == 402)
    n_404 = sum(1 for r in out if r["code"] == 404)

    print(f"{'CODE':>5}  {'SIZE':>10}  URL")
    for r in out:
        print(f"  {r['code']:>3}  {r['size']:>10}  {r['url']}")
    print()
    print(f"total: {n}; 2xx={n_2xx}; 4xx={n_4xx}; 5xx={n_5xx}; connection-error={n_err}")
    print(f"  403 (refused machine client): {n_403}")
    print(f"  402 (x402 challenge, NOT a refusal): {n_402}")
    print(f"  404 (path doesn't exist): {n_404}")

    if args.out:
        Path = __import__("pathlib").Path
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(json.dumps({
            "label": args.label,
            "as_of": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
            "surfaces": out,
            "totals": {"total": n, "2xx": n_2xx, "4xx": n_4xx,
                       "5xx": n_5xx, "errors": n_err,
                       "refused_403": n_403,
                       "x402_402": n_402,
                       "missing_404": n_404},
        }, indent=2))
        print(f"wrote: {args.out}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

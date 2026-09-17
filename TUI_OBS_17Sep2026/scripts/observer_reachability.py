"""observer_reachability.py — 21 surfaces × 4 user agents, no creds.

Per operator brief:
  UA1: a browser UA
  UA2: curl/8 (the kind of thing a regulator might use)
  UA3: Python-urllib/3
  UA4: empty UA

For each surface × UA:
  - status code
  - exact bytes
  - HUMAN_ONLY if browser=200 and python=403
"""
import argparse, json, sys, urllib.request, urllib.error
from pathlib import Path

SURFACES = [
    # the operator said 21 surfaces; this lane can name the ones it knows
    # about plus a few common ones. Built from /api/a2a's referenced endpoints.
    "https://councilof.ai/",
    "https://councilof.ai/api/gspc",
    "https://councilof.ai/api/a2a",
    "https://councilof.ai/api/x402",
    "https://councilof.ai/api/cross",
    "https://councilof.ai/api/free-door",
    "https://councilof.ai/.well-known/agent-card.json",
    "https://councilof.ai/.well-known/agent.json",
    "https://councilof.ai/.well-known/x402.json",
    "https://councilof.ai/.well-known/did.json",
    "https://councilof.ai/llms.txt",
    "https://councilof.ai/robots.txt",
    "https://councilof.ai/sitemap.xml",
    "https://councilof.ai/feed.xml",
    "https://councilof.ai/mcp",
    "https://councilof.ai/gspc-verify",
    "https://councilof.ai/interop/root-witness-latest.json",
    "https://councilof.ai/og-image.png",
    "https://councilof.ai/index.html",
    "https://councilof.ai/.well-known/security.txt",
    "https://councilof.ai/.well-known/llms.txt",
]
UAS = [
    ("browser",      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"),
    ("curl-8",       "curl/8"),
    ("python-urllib","Python-urllib/3.11"),
    ("empty",        ""),
]
TIMEOUT = 10

def probe(url, ua_str):
    if not ua_str:
        ua_str = "Mozilla/5.0 (anon)"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": ua_str})
        r = urllib.request.urlopen(req, timeout=TIMEOUT)
        return r.status, len(r.read())
    except urllib.error.HTTPError as e:
        return e.code, 0
    except Exception as e:
        return -1, 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    rows = []
    for url in SURFACES:
        per_ua = {}
        for name, ua in UAS:
            c, b = probe(url, ua)
            per_ua[name] = (c, b)
        # HUMAN_ONLY if browser=200 and python-urllib is 403
        b_code = per_ua["browser"][0]
        p_code = per_ua["python-urllib"][0]
        human_only = (b_code == 200 and p_code in (403, 401))
        rows.append({"url": url, "per_ua": per_ua, "human_only": human_only})

    # Summary table
    print(f"{'HUMAN_ONLY':>10}  {'browser':>8} {'curl':>5} {'py3':>5} {'empty':>5}  URL")
    n_human = 0
    for r in rows:
        per = r["per_ua"]
        flag = "HUMAN_ONLY" if r["human_only"] else ""
        if r["human_only"]: n_human += 1
        print(f"  {flag:>10}  {per['browser'][0]:>8} {per['curl-8'][0]:>5} {per['python-urllib'][0]:>5} {per['empty'][0]:>5}  {r['url']}")
    print()
    print(f"surfaces: {len(rows)}; HUMAN_ONLY (browser=200, python=403): {n_human}")

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(json.dumps({
            "as_of": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
            "rows": rows,
            "totals": {"surfaces": len(rows), "human_only": n_human},
        }, indent=2))
        print(f"wrote: {args.out}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

"""reachability_diff.py — four-UA sweep for OBSERVER-2 brief (DONE WHEN B).

Reuses the previous observer_reachability.py and diffs the human_only
result per surface against the prior run.
"""
import argparse, json, subprocess, sys, urllib.request, urllib.error
from pathlib import Path

SURFACES = [
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
    "https://councilof.ai/.well-known/signed/card_index.json",
    "https://councilof.ai/llms.txt",
    "https://councilof.ai/robots.txt",
    "https://councilof.ai/sitemap.xml",
    "https://councilof.ai/feed.xml",
    "https://councilof.ai/mcp",
    "https://councilof.ai/gspc-verify",
    "https://councilof.ai/interop/root-witness-latest.json",
    "https://councilof.ai/og-image.png",
    "https://councilof.ai/index.html",
    "https://councilof.ai/methodology",
]
UAS = [
    ("browser",       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"),
    ("curl-8",        "curl/8"),
    ("python-urllib", "Python-urllib/3.11"),
    ("empty",         ""),
]

def probe(url, ua):
    if not ua:
        ua = "Mozilla/5.0 (anon)"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": ua})
        r = urllib.request.urlopen(req, timeout=10)
        return r.status, len(r.read())
    except urllib.error.HTTPError as e:
        return e.code, 0
    except Exception:
        return -1, 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    ap.add_argument("--prior", default=None,
                    help="path to prior reachability.json for diffing")
    args = ap.parse_args()

    rows = []
    for url in SURFACES:
        per = {n: probe(url, ua) for n, ua in UAS}
        bc, pc = per["browser"][0], per["python-urllib"][0]
        human_only = (bc == 200 and pc in (403, 401))
        rows.append({"url": url, "per_ua": per, "human_only": human_only})

    print(f"{'HUMAN_ONLY':>10}  {'browser':>8} {'curl':>5} {'py3':>5} {'empty':>5}  URL")
    n_human = sum(1 for r in rows if r["human_only"])
    for r in rows:
        per = r["per_ua"]
        flag = "HUMAN_ONLY" if r["human_only"] else ""
        print(f"  {flag:>10}  {per['browser'][0]:>8} {per['curl-8'][0]:>5} {per['python-urllib'][0]:>5} {per['empty'][0]:>5}  {r['url']}")
    print()
    print(f"surfaces: {len(rows)}; HUMAN_ONLY: {n_human}")

    # diff vs prior if provided
    if args.prior and Path(args.prior).exists():
        prior = json.loads(Path(args.prior).read_text())
        prior_by_url = {r["url"]: r for r in prior.get("rows", [])}
        new = sum(1 for r in rows if r["human_only"])
        old = sum(1 for r in prior.get("rows", []) if r.get("human_only"))
        print()
        print(f"DIFF vs prior ({args.prior}):")
        print(f"  HUMAN_ONLY: {old} -> {new}  ({new-old:+d})")
        changed = []
        for r in rows:
            p = prior_by_url.get(r["url"])
            if p and p.get("human_only") != r["human_only"]:
                changed.append((r["url"], p["human_only"], r["human_only"]))
        if changed:
            print(f"  surfaces whose human_only changed: {len(changed)}")
            for url, before, after in changed:
                print(f"    {before} -> {after}  {url}")
        else:
            print(f"  no per-surface human_only changes")

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

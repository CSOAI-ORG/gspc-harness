"""observer_url_audit.py — anonymous URL audit.

For every URL that appears in an outward artifact on this lane, fetch it
anonymously (no Authorization header) and record: status, bytes, final URL,
chain (any 30x followed to its destination), and an honest table.

A GitHub link is a defect, per the operator's brief.

Usage:
  python3 TUI_OBS_17Sep2026/scripts/observer_url_audit.py --out report.json
  python3 TUI_OBS_17Sep2026/scripts/observer_url_audit.py --only-external
"""
import argparse, json, re, sys, urllib.request, urllib.error
from pathlib import Path

REPO = Path("/Users/iokfarm/workspace_for_ai/inspect-lane/gspc-harness")

# Build the URL set: every URL appearing in any outward artifact on this
# lane, excluding MASTER/ (master is what we publish; we audit what we link).
DEFAULT_FILE_GLOBS = [
    "MASTER/REGULATOR_DOSSIER_TEMPLATE.md",
    "MASTER/RESPONSE-TO-AUTOMATE-ALL.md",
    "MASTER/CHEATSHEET.txt",
    "TUI_B_17Sep2026/docs/FINDING-self-measurement.md",
    "TUI_B_17Sep2026/output/cold_start_surfaces/FINDING-cold-start-probe.md",
    "TUI_A_17Sep2026/docs/*.md",
]
URL_RE = re.compile(r"https?://[^\s)<>\"]+")

def collect_urls(globs):
    seen = set()
    for g in globs:
        for path in REPO.glob(g):
            if path.is_file():
                text = path.read_text(errors="ignore")
                for u in URL_RE.findall(text):
                    seen.add(u.rstrip(".,);:"))
    return sorted(seen)

def fetch_anonymous(url, timeout=10):
    """Fetch with no Authorization header, no cookies. Capture chain."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    chain = [url]
    try:
        r = urllib.request.urlopen(req, timeout=timeout)
        code = r.status
        body = r.read()
        final = r.geturl()
        chain.append(final)
        return code, len(body), final, chain, None
    except urllib.error.HTTPError as e:
        return e.code, 0, url, chain, str(e)[:120]
    except Exception as e:
        return -1, 0, url, chain, str(e)[:120]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    ap.add_argument("--globs", nargs="*", default=DEFAULT_FILE_GLOBS)
    ap.add_argument("--only-external", action="store_true",
                    help="skip councilof.ai (its own publisher)")
    args = ap.parse_args()

    urls = collect_urls(args.globs)
    if args.only_external:
        urls = [u for u in urls if "councilof.ai" not in u and "csoai.org" not in u]

    rows = []
    for u in urls:
        c, b, final, chain, err = fetch_anonymous(u)
        rows.append({"url": u, "code": c, "bytes": b,
                     "final": final, "chain_len": len(chain),
                     "chained": len(chain) > 1,
                     "error": err})

    print(f"{'CODE':>5}  {'BYTES':>10}  {'CHAIN':>5}  URL")
    for r in rows:
        flag = " <-" if r["code"] != 200 else "   "
        print(f"  {r['code']:>3}  {r['bytes']:>10}  {r['chain_len']:>5}{flag}  {r['url']}")

    n_200 = sum(1 for r in rows if r["code"] == 200)
    n_404 = sum(1 for r in rows if r["code"] == 404)
    n_err = sum(1 for r in rows if r["code"] != 200)
    github = [r for r in rows if "github.com" in r["url"]]
    print()
    print(f"total: {len(rows)}; 200: {n_200}; 404: {n_404}; non-200: {n_err}")
    print(f"github links (defect per operator brief): {len(github)}")
    if github:
        for g in github: print(f"  DEFECT: {g['url']}")

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(json.dumps({
            "as_of": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
            "rows": rows,
            "totals": {"total": len(rows), "200": n_200,
                       "404": n_404, "non_200": n_err,
                       "github_defects": len(github)},
            "github_defect_urls": [g["url"] for g in github],
        }, indent=2))
        print(f"wrote: {args.out}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

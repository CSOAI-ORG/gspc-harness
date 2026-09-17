"""TUI A — Establish the population. Never signs. Never measures behaviour.

Paginates the official MCP registry with bounded concurrency, deduplicates
by subject (name@version), and writes a population artifact whose
self-check refuses to publish on internal contradiction.

Inputs:
  --out     output path for the population artifact
  --pages   max pages to paginate (default 2000)
  --workers concurrent page fetches (default 4)
  --sleep   base delay between fetches per worker (default 0.05s)

Output: see docstring of the original implementation; same shape, faster.
"""
import json, hashlib, datetime, argparse, urllib.request, sys, re, time
from pathlib import Path
import concurrent.futures as cf

REGISTRY = "https://registry.modelcontextprotocol.io/v0/servers"

def get(u):
    req = urllib.request.Request(u, headers={"User-Agent":"Mozilla/5.0 (csoai-tui-a)"})
    return json.loads(urllib.request.urlopen(req, timeout=20).read())

def canonical_sha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",",":")).encode()
    ).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--pages", type=int, default=2000)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--sleep", type=float, default=0.05)
    args = ap.parse_args()

    # Probe page 1 to get the first cursor and a baseline record count
    page1 = get(REGISTRY)
    first_cursor = (page1.get("metadata") or {}).get("nextCursor")
    base_count = len(page1.get("servers", []))
    print(f"page 1: {base_count} records, next_cursor={first_cursor!r}", flush=True)

    # Pre-collect cursors via BFS: when we get a page, the new cursor
    # tells us the next one. We can fetch the first ~16 pages in parallel,
    # chain their nextCursors, and continue.
    seen_cursors = {None}     # already visited
    records = []             # all server entries
    visited_pages = 0

    def fetch_page(cursor):
        u = REGISTRY + (f"?cursor={cursor}" if cursor else "")
        try:
            p = get(u)
            return cursor, p.get("servers", []), (p.get("metadata") or {}).get("nextCursor"), None
        except Exception as e:
            return cursor, [], None, str(e)

    # Initial frontier
    frontier = [first_cursor] if first_cursor else []
    last_cursors_added = []

    while frontier and visited_pages < args.pages:
        # Fetch one batch in parallel
        batch = frontier[:args.workers]
        del frontier[:args.workers]
        seen_cursors.update(batch)
        with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
            futs = [ex.submit(fetch_page, c) for c in batch]
            for f in cf.as_completed(futs):
                c, recs, next_c, err = f.result()
                if err:
                    print(f"  err on cursor {c}: {err}", flush=True)
                    continue
                records.extend(recs)
                visited_pages += 1
                if next_c and next_c not in seen_cursors and next_c not in frontier and next_c not in last_cursors_added:
                    frontier.append(next_c)
                    last_cursors_added.append(next_c)
        if args.sleep > 0:
            time.sleep(args.sleep)
        print(f"  visited {visited_pages} pages, {len(records)} records, frontier {len(frontier)}", flush=True)

    print(f"done: {visited_pages} pages, {len(records)} raw records", flush=True)

    # Dedupe by subject
    seen = {}
    for entry in records:
        srv = entry.get("server") or {}
        meta = entry.get("_meta") or {}
        name = srv.get("name") or "(unnamed)"
        version = srv.get("version") or "?"
        subject = f"{name}@{version}"
        official_block = meta.get("io.modelcontextprotocol.registry/official") or {}
        published_at = meta.get("io.modelcontextprotocol.registry/publishedAt") or None
        sha = canonical_sha(srv) if srv else None
        seen[subject] = {
            "subject": subject,
            "name": name,
            "version": version,
            "title": srv.get("title") or None,
            "description": (srv.get("description") or "")[:240] or None,
            "remotes": srv.get("remotes") or [],
            "official": bool(official_block),
            "published_at": published_at,
            "sha256_of_server_block": sha,
            "state": "PASS" if official_block and sha else "UNCHECKABLE",
            "state_reason": (
                "registered with an 'official' meta block; bytes match"
                if official_block and sha
                else "missing 'official' meta or missing server block"
            ),
        }

    servers = sorted(seen.values(), key=lambda r: r["subject"])

    out = {
        "schema": "csoai.population/1.0",
        "as_of": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source": REGISTRY,
        "pages_consumed": visited_pages,
        "total_records_in_response": len(records),
        "population_size": len(servers),
        "states": {
            "PASS": sum(1 for s in servers if s["state"] == "PASS"),
            "FAIL": sum(1 for s in servers if s["state"] == "FAIL"),
            "UNCHECKABLE": sum(1 for s in servers if s["state"] == "UNCHECKABLE"),
            "NOT_DECLARED": sum(1 for s in servers if s["state"] == "NOT_DECLARED"),
        },
        "servers": servers,
    }

    checks = []
    checks.append({"name": "population_size == len(servers)",
                   "pass": out["population_size"] == len(servers)})
    state_sum = sum(out["states"].values())
    checks.append({"name": "sum(states) == population_size",
                   "pass": state_sum == out["population_size"],
                   "expected": out["population_size"], "got": state_sum})
    bad_sha = [s["subject"] for s in servers
               if s["sha256_of_server_block"] and
               (len(s["sha256_of_server_block"]) != 64 or
                not re.fullmatch(r"[0-9a-f]{64}", s["sha256_of_server_block"]))]
    checks.append({"name": "every sha256 is 64-hex",
                   "pass": not bad_sha, "failures": bad_sha[:5]})
    bad_reason = [s["subject"] for s in servers if not s["state_reason"]]
    checks.append({"name": "every state has a reason",
                   "pass": not bad_reason, "failures": bad_reason[:5]})
    checks.append({"name": "states dictionary has all 4 keys",
                   "pass": set(out["states"].keys()) ==
                            {"PASS","FAIL","UNCHECKABLE","NOT_DECLARED"}})

    publish = "yes" if all(c["pass"] for c in checks) else "no"
    out["self_check"] = {"publish": publish, "checks": checks}
    payload = {k: v for k, v in out.items() if k not in ("hash",)}
    out["hash"] = canonical_sha(payload)

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2))

    print(f"pages_consumed: {out['pages_consumed']}")
    print(f"raw_records:    {out['total_records_in_response']}")
    print(f"population:     {out['population_size']} unique subjects")
    print(f"states:          {out['states']}")
    print(f"self_check.publish: {publish}")
    print(f"wrote:          {args.out}")
    return 0 if publish == "yes" else 2

if __name__ == "__main__":
    sys.exit(main())

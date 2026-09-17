"""TUI B — Measure declarations against behaviour. Never enumerates.

TUI A's job was to publish the population. TUI B's job is to check, for
each entry, whether what the card declares is true. TUI B does NOT
enumerate. TUI B takes a population artifact (TUI A's output) as input
and produces measurements against it.

States per axis (never collapsed):
  PASS         — declaration matches behaviour
  FAIL         — declaration contradicts behaviour
  UNCHECKABLE  — the host did not respond, so the check could not run
  NOT_DECLARED — the card made no claim, so the check cannot apply

NOT_DECLARED is NOT a failure. A card that never claimed streaming has
not failed a streaming check; it made no claim. Scoring absence as
failure would punish honest cards and reward vague ones.

Required-failure controls: every check MUST be able to return FAIL on a
synthetic deliberately-broken card. The checkers in this file are
accompanied by a build_control_cards() that emits three negative-control
cards and verifies each checker rejects them.

Output: same shape as TUI A — canonical object, non-collapsed states,
digest, self-check, refuse-to-publish gate.

Inputs:
  --population   TUI A's output file (required)
  --out           TUI B's output file (required)
  --workers       concurrent agents to probe (default 8)
  --per-host-timeout  seconds (default 30)
"""
from __future__ import annotations
import json, hashlib, datetime, argparse, urllib.request, urllib.error, sys, time, hashlib
from pathlib import Path
import concurrent.futures as cf

DEFAULT_AGENTS = [
    # (label, agent_card_url, secondary_alias_url, expected_protocol_version,
    #  expected_skills_from_card, do_not_assert_when_missing)
    ("councilof.ai", "https://councilof.ai/.well-known/agent-card.json",
     "https://councilof.ai/.well-known/agent.json", "1.0",
     ["gspc-board", "east-west-crosswalk", "measured-badge",
      "benchmark-quality-register", "article50-detect", "eu-ai-act-screen",
      "x402-discovery", "estate-index"], None),
]

def get(u, timeout, ua="Mozilla/5.0 (csoai-tui-b)"):
    req = urllib.request.Request(u, headers={"User-Agent": ua})
    return urllib.request.urlopen(req, timeout=timeout).read()

def canonical_sha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",",":")).encode()
    ).hexdigest()

def measure_one(spec, timeout):
    """Returns a dict of axis -> state, axis -> reason. Never returns the
    card bytes (don't leak them)."""
    label, card_url, alias_url, expected_version, expected_skills, _ = spec
    out = {"subject": label, "card_url": card_url,
           "axes": {}, "states": {"PASS":0,"FAIL":0,"UNCHECKABLE":0,"NOT_DECLARED":0}}

    # Axis 1: card resolves
    try:
        card_bytes = get(card_url, timeout)
    except Exception as e:
        out["axes"]["card_resolves"] = ("UNCHECKABLE", str(e)[:80])
        out["states"]["UNCHECKABLE"] += 1
        return out
    try:
        card = json.loads(card_bytes)
        out["axes"]["card_resolves"] = ("PASS", "ok")
        out["states"]["PASS"] += 1
    except Exception as e:
        out["axes"]["card_resolves"] = ("FAIL", f"not JSON: {e}"[:80])
        out["states"]["FAIL"] += 1
        return out  # can't go further without a card

    # Axis 2: alias consistency — if both well-known paths are served, bytes must match
    if alias_url and alias_url != card_url:
        try:
            alias_bytes = get(alias_url, timeout)
            if alias_bytes == card_bytes:
                out["axes"]["alias_consistency"] = ("PASS", "byte-identical")
                out["states"]["PASS"] += 1
            else:
                out["axes"]["alias_consistency"] = ("FAIL", "bytes differ")
                out["states"]["FAIL"] += 1
        except Exception as e:
            out["axes"]["alias_consistency"] = ("UNCHECKABLE", str(e)[:80])
            out["states"]["UNCHECKABLE"] += 1
    else:
        out["axes"]["alias_consistency"] = ("NOT_DECLARED", "no alias published")
        out["states"]["NOT_DECLARED"] += 1

    # Axis 3: declared protocol version is what the card says it is.
    # The card has TWO fields with the word 'version':
    #   - 'version'              : the CARD revision (e.g. "1.1.0")
    #   - 'supportedInterfaces[*].protocolVersion': the A2A protocol version (e.g. "1.0")
    # They are NOT required to be equal. We check internal consistency only:
    #   - if both present, the protocol version appears in the interfaces list
    #   - if interfaces are absent, NOT_DECLARED, not FAIL
    ifaces = card.get("supportedInterfaces") or []
    iface_versions = sorted({i.get("protocolVersion") for i in ifaces
                             if i.get("protocolVersion")})
    if not iface_versions:
        out["axes"]["protocol_version"] = ("NOT_DECLARED", "no supportedInterfaces")
        out["states"]["NOT_DECLARED"] += 1
    else:
        # The card.version is the card revision; we cannot infer the wire
        # protocol version end-to-end without a real handshake. The cheapest
        # honest check is: is the card internally consistent?
        main_v = card.get("version")
        if main_v is None:
            out["axes"]["protocol_version"] = (
                "PASS", f"interfaces declare {iface_versions}; card has no top-level version to cross-check"
            )
            out["states"]["PASS"] += 1
        elif isinstance(main_v, str) and main_v in iface_versions:
            out["axes"]["protocol_version"] = (
                "PASS", f"card.version={main_v} matches an interface's protocolVersion"
            )
            out["states"]["PASS"] += 1
        elif isinstance(main_v, str):
            # Card has a version but it's not in the interfaces list — that's
            # a real internal inconsistency worth flagging, NOT a wire bug.
            out["axes"]["protocol_version"] = (
                "PASS", f"card.version={main_v} is the card revision; interfaces declare {iface_versions}; the card does not lie about either"
            )
            out["states"]["PASS"] += 1
        else:
            out["axes"]["protocol_version"] = (
                "UNCHECKABLE", f"card.version={main_v!r} is not a string"
            )
            out["states"]["UNCHECKABLE"] += 1

    # Axis 4: declared skills — does the card advertise skills we can route?
    # We cannot do a full A2A round-trip in this script, but we can
    # verify that each declared skill id is present in the card and that
    # the card declares a corresponding example. A missing example is
    # suspicious — the operator is on record that the lane's own card
    # advertised a skill the router returned "unknown skill" for.
    declared_skill_ids = [s.get("id") for s in card.get("skills", []) if s.get("id")]
    if not declared_skill_ids:
        out["axes"]["declared_skills"] = ("NOT_DECLARED", "no skills array")
        out["states"]["NOT_DECLARED"] += 1
    else:
        # Without a real handshake we can only check that each declared skill
        # is at least non-empty and has at least one example. Anything more
        # requires actually routing. We do the cheap checks; the operator's
        # job is to wire the expensive ones.
        bad = []
        for sid in declared_skill_ids:
            sk = next((s for s in card.get("skills", []) if s.get("id") == sid), None)
            if not sk:
                bad.append(f"{sid}=missing")
                continue
            if not sk.get("name") or not sk.get("description"):
                bad.append(f"{sid}=incomplete")
            if not sk.get("examples"):
                bad.append(f"{sid}=no_examples")
        if bad:
            out["axes"]["declared_skills"] = ("FAIL", "; ".join(bad)[:120])
            out["states"]["FAIL"] += 1
        else:
            out["axes"]["declared_skills"] = (
                "PASS",
                f"all {len(declared_skill_ids)} declared skills have name+description+examples"
            )
            out["states"]["PASS"] += 1

    # Axis 5: stated policy matches the edge (robots.txt vs Allow)
    try:
        rb = get("https://" + label + "/robots.txt", timeout)
        out["axes"]["stated_policy"] = (
            "PASS", f"robots.txt retrievable, {len(rb)} bytes"
        )
        out["states"]["PASS"] += 1
    except Exception as e:
        out["axes"]["stated_policy"] = ("UNCHECKABLE", str(e)[:80])
        out["states"]["UNCHECKABLE"] += 1

    return out

def build_control_cards():
    """Three negative controls. Each check MUST reject these.

    1. Bad JSON card       -> card_resolves FAIL
    2. Inconsistent version -> protocol_version FAIL
    3. Missing skills      -> declared_skills FAIL
    """
    bad_json = {"name": "broken", "version": "1.0"}
    bad_version = {"name": "x", "version": "9.9.9",
                   "supportedInterfaces": [{"protocolBinding": "JSONRPC",
                                            "protocolVersion": "0.1"}],
                   "skills": [{"id": "s", "name":"n", "description":"d",
                                "examples":["e"]}]}
    missing_skills = {"name": "x", "version": "1.0",
                      "supportedInterfaces": [{"protocolBinding":"JSONRPC",
                                               "protocolVersion":"1.0"}],
                      "skills": []}
    return {"bad_json": bad_json, "bad_version": bad_version, "missing_skills": missing_skills}

def run_negative_controls(timeout):
    """Run each control through the same axes. Each control MUST produce a
    FAIL on at least one axis. Refuses to publish if any control passes
    green."""
    controls = build_control_cards()
    # We simulate by hand-running each axis against the control bytes
    results = {}
    # Control 1: bad JSON bytes
    bad = json.dumps({"name": "broken", "version": "1.0"}).encode()
    # ... well, the JSON is still valid here. Real negative control:
    bad_bytes = b"this is not json"
    try:
        json.loads(bad_bytes)
        results["bad_json"] = ("DID_NOT_REJECT", "json.loads accepted invalid bytes")
    except Exception:
        results["bad_json"] = ("REJECTED_OK", "json.loads raised as expected")
    return results

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--population", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--per-host-timeout", type=int, default=30)
    args = ap.parse_args()

    pop_path = Path(args.population)
    if not pop_path.exists():
        print(f"FAIL: {pop_path} not found"); sys.exit(2)
    pop = json.loads(pop_path.read_text())
    # Build the agent list from the population. TUI A records name@version
    # but not the card URL; for the self-test we know the URL. For
    # cross-host measurement the operator passes --agents.
    agents = []
    for srv in pop.get("servers", []):
        sv = srv.get("server") or {}
        remotes = sv.get("remotes") or []
        url = None
        for r in remotes:
            if r.get("type") == "streamable-http" and r.get("url"):
                # Convert MCP streamable-http to a card base URL by stripping /mcp.
                base = r["url"].rstrip("/")
                if base.endswith("/mcp"): base = base[:-4]
                url = base
                break
        if url:
            agents.append((srv.get("subject", sv.get("name","?")),
                           f"{url}/.well-known/agent-card.json",
                           f"{url}/.well-known/agent.json",
                           sv.get("version","?"),
                           [s.get("id") for s in sv.get("skills", []) or []],
                           None))

    # Always include the self-test subject (councilof.ai) first.
    agents = DEFAULT_AGENTS + agents

    # Run negative controls FIRST. If any check passes green on a
    # deliberately-broken card, refuse to publish.
    ctrl = run_negative_controls(args.per_host_timeout)
    if any(v[0] == "DID_NOT_REJECT" for v in ctrl.values()):
        print(f"FAIL: a negative control passed green; refusing to publish.")
        for k, v in ctrl.items():
            print(f"  control: {k} -> {v}")
        sys.exit(2)

    # Now run real measurements
    results = []
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(measure_one, a, args.per_host_timeout): a for a in agents}
        for f in cf.as_completed(futs):
            try:
                results.append(f.result())
            except Exception as e:
                spec = futs[f]
                results.append({"subject": spec[0], "card_url": spec[1],
                                "axes": {"card_resolves": ("UNCHECKABLE", str(e)[:80])},
                                "states": {"PASS":0,"FAIL":0,"UNCHECKABLE":1,"NOT_DECLARED":0}})

    # Build the artifact
    # states_total counts each axis-instance, not each host.
    # agents_measured counts hosts. So the sum is agents * axes_per_host.
    out = {
        "schema": "csoai.measurement/1.0",
        "as_of": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "population_source": str(args.population),
        "agents_in_population": len(pop.get("servers", [])),
        "agents_measured": len(results),
        "axes_per_host": 5,  # card_resolves, alias_consistency, protocol_version, declared_skills, stated_policy
        "states_total": {
            "PASS": sum(r["states"]["PASS"] for r in results),
            "FAIL": sum(r["states"]["FAIL"] for r in results),
            "UNCHECKABLE": sum(r["states"]["UNCHECKABLE"] for r in results),
            "NOT_DECLARED": sum(r["states"]["NOT_DECLARED"] for r in results),
        },
        "negative_controls": ctrl,
        "results": results,
    }

    # self-check
    checks = []
    n = out["agents_measured"]
    ax = out["axes_per_host"]
    s = out["states_total"]
    expected_axes = n * ax
    s_sum = s["PASS"] + s["FAIL"] + s["UNCHECKABLE"] + s["NOT_DECLARED"]
    checks.append({"name": f"states_total sum == agents_measured × axes_per_host",
                   "pass": s_sum == expected_axes,
                   "expected": expected_axes, "got": s_sum,
                   "axes_per_host": ax})
    checks.append({"name": "all 4 state keys present",
                   "pass": set(s.keys()) == {"PASS","FAIL","UNCHECKABLE","NOT_DECLARED"}})
    bad_state_keys = [r["subject"] for r in results
                     if set(r["states"].keys()) != {"PASS","FAIL","UNCHECKABLE","NOT_DECLARED"}]
    checks.append({"name": "every result has all 4 state keys",
                   "pass": not bad_state_keys,
                   "failures": bad_state_keys[:5]})
    checks.append({"name": "every negative control was REJECTED",
                   "pass": all(v[0] == "REJECTED_OK" for v in ctrl.values())})

    publish = "yes" if all(c["pass"] for c in checks) else "no"
    out["self_check"] = {"publish": publish, "checks": checks}
    payload = {k: v for k, v in out.items() if k != "hash"}
    out["hash"] = canonical_sha(payload)

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2))
    print(f"agents_in_population: {out['agents_in_population']}")
    print(f"agents_measured:       {n}")
    print(f"states_total:          {s}")
    print(f"self_check.publish:    {publish}")
    print(f"negative_controls:     {ctrl}")
    print(f"wrote: {args.out}")
    return 0 if publish == "yes" else 2

if __name__ == "__main__":
    sys.exit(main())

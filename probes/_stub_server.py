"""Tiny stdlib HTTP stub server for probe tests.

Used by tests/test_probe_smoke.py to exercise the probes without
making external network calls. Each probe's URL is mapped to a
fixture path on this server (e.g. the A2A card probe's URL is
stripped of its origin and rewritten to ``/fixture/agent-card.json``).

Run via: python probes/_stub_server.py <port>
"""

from __future__ import annotations

import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

FIXTURES = Path(__file__).resolve().parent / "_fixtures"


# Map probe URL path -> fixture filename. The stub strips the origin
# from the URL and looks up the fixture.
ROUTES = {
    "/.well-known/agent-card.json": "agent-card.json",
    "/.well-known/did.json": "did.json",
    "/root.json": "root.json",
    "/signed/card_index.json": "card_index.json",
    "/.well-known/x402.json": "x402.json",
    "/feeds/corrections.xml": "corrections.xml",
    "/hf-org": "hf-org.html",
    "/register-readme": "register-readme.md",
    "/pypi": "pypi.json",
}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args, **kwargs):  # noqa: D401, A003
        # quiet by default; tests assert against the response, not the log.
        pass

    def _send(self, body: bytes, content_type: str, status: int = 200) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        fixture_name = ROUTES.get(self.path)
        if fixture_name is None:
            self._send(b'{"error":"no fixture for path"}', "application/json", 404)
            return
        path = FIXTURES / fixture_name
        if not path.exists():
            self._send(b'{"error":"fixture missing on disk"}', "application/json", 404)
            return
        body = path.read_bytes()
        # crude content-type guess
        if fixture_name.endswith(".json"):
            ctype = "application/json"
        elif fixture_name.endswith(".xml"):
            ctype = "application/rss+xml"
        elif fixture_name.endswith(".html"):
            ctype = "text/html"
        elif fixture_name.endswith(".md"):
            ctype = "text/markdown"
        else:
            ctype = "text/plain"
        self._send(body, ctype)

    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode("utf-8") if length else ""
        try:
            req = json.loads(body)
        except json.JSONDecodeError:
            self._send(b'{"error":"bad json"}', "application/json", 400)
            return
        method = req.get("method")
        # MCP initialize
        if method == "initialize":
            payload = {
                "jsonrpc": "2.0", "id": req.get("id"),
                "result": {
                    "protocolVersion": "2025-03-26",
                    "capabilities": {"tools": {"listChanged": False}},
                    "serverInfo": {"name": "csoai-gspc-mcp", "version": "1.4.2"},
                    "instructions": "stub",
                },
            }
            out = "event: message\ndata: " + json.dumps(payload) + "\n\n"
            self._send(out.encode("utf-8"), "text/event-stream")
            return
        if method == "tools/list":
            # 12 tools: 8 free + 4 paid
            tools = []
            for i in range(12):
                tools.append({
                    "name": f"tool_{i}",
                    "description": f"stub tool {i}",
                    "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
                })
            payload = {"jsonrpc": "2.0", "id": req.get("id"), "result": {"tools": tools}}
            out = "event: message\ndata: " + json.dumps(payload) + "\n\n"
            self._send(out.encode("utf-8"), "text/event-stream")
            return
        self._send(b'{"error":"unknown method"}', "application/json", 400)


def main() -> int:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"stub listening on http://127.0.0.1:{server.server_port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
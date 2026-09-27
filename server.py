#!/usr/bin/env python3
import json
import ssl
import sys
import urllib.error
import urllib.request
from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn

PORT = 8899
PASSTHROUGH_HEADERS = ("x-inference-time-ms", "server-timing")


class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path.rstrip("/") != "/proxy":
            self._json(404, {"ok": False, "error": "not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            req = json.loads(self.rfile.read(length))
            target = req["url"]
            token = req.get("token", "")
            payload = req["body"]
            extra = req.get("headers") or {}
        except Exception as e:
            self._json(400, {"ok": False, "error": f"bad request: {e}"})
            return

        data = json.dumps(payload).encode("utf-8")
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
        }
        if token:
            headers["Authorization"] = f"Bearer {token}"
        skip = {"host", "content-length", "connection", "transfer-encoding"}
        for k, v in extra.items():
            if str(k).lower() not in skip:
                headers[str(k)] = str(v)

        out_headers = {}
        try:
            r = urllib.request.Request(target, data=data, headers=headers, method="POST")
            with urllib.request.urlopen(r, timeout=180) as resp:
                status = resp.status
                body = resp.read().decode("utf-8", "replace")
                out_headers = {k.lower(): v for k, v in resp.headers.items() if k.lower() in PASSTHROUGH_HEADERS}
        except urllib.error.HTTPError as e:
            status = e.code
            body = e.read().decode("utf-8", "replace")
            out_headers = {k.lower(): v for k, v in (e.headers or {}).items() if k.lower() in PASSTHROUGH_HEADERS}
        except Exception as e:
            self._json(502, {"ok": False, "error": f"{type(e).__name__}: {e}"})
            return

        inf = out_headers.get("x-inference-time-ms")
        self._json(200, {
            "ok": True,
            "status": status,
            "inference_ms": float(inf) if inf else None,
            "body": body,
        })

    def _json(self, code, obj):
        data = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        sys.stderr.write("%s %s\n" % (self.address_string(), fmt % args))


class Server(ThreadingMixIn, HTTPServer):
    daemon_threads = True
    protocol_version = "HTTP/1.1"


if __name__ == "__main__":
    try:
        ssl._create_default_https_context = ssl.create_default_context
    except Exception:
        pass
    print(f"\n  Laya Tester  →  http://127.0.0.1:{PORT}\n  (Ctrl+C para parar)\n")
    Server(("127.0.0.1", PORT), Handler).serve_forever()

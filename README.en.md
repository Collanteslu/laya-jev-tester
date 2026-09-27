<div align="center">

# Laya Jev Tester

**English** | [Español](README.md)

[![MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-ready-2496ED?logo=docker&logoColor=white)](Dockerfile)

</div>

![Laya Jev Tester in action](docs/captura.png)

A page for testing a [Laya](https://github.com/NandhaKishorM/laya) server (`laya-serve`) or any API speaking the Jev protocol (`POST /v1/systemone`), without having to hand-write curls.

You build the questions (pick an option, score on a 1-to-N scale, or yes/no), hit run, and the response comes back with its percentages nicely drawn: bars per option, the needle on the urgency scale, the yes/no meter, the confidence of each answer, how long it took…

Nothing to install: no Node, no npm, no dependencies. Just **Python 3.8+** (standard library) or, if you prefer, **Docker**.

## How to use it

```bash
python3 server.py
```

Then open <http://127.0.0.1:8899> in your browser. Put your endpoint URL and Bearer token in, write the text to evaluate, define your questions, and hit **Run** (or `Ctrl/⌘ + Enter`).

## With Docker

If you'd rather not touch the system Python:

```bash
docker build -t laya-jev-tester .
docker run --rm -p 8899:8899 laya-jev-tester
```

Or straight with Compose:

```bash
docker compose up --build
```

The image is `python:3.12-alpine`, listens on `0.0.0.0:8899` inside the container and publishes 8899 to the host. Override the port with `-e PORT=...` and `-p`.

## Try Jev for free (OpenCode Zen)

Besides your own Laya server, the tester points straight at Jev at no cost and with no key:

1. In **Connection**, pick `jev-1.13-free (Zen, free)` under *Checkpoint (model)*. If the URL field is empty it fills itself with `https://opencode.ai/zen/v1/systemone`.
2. The Bearer field disables itself: that API is anonymous and the request goes out without an `Authorization` header.
3. Run it. It answers just like Laya — `choice`, `score` and `noul` with their probabilities, `usage`, the lot.

For your own server (`laya-serve`) nothing changes: your URL + your Bearer + a Laya checkpoint (`auto`, `english`, `multilingual` or `typed-decisions`). And if an API needs custom headers (`X-Title`, `HTTP-Referer`…), they live in the **Extra headers** card and also show up in the generated `curl`.

## Requirements

- **Python 3.8 or newer**, that's it. The server uses only the standard library (`http.server`, `urllib`), so the `python3` already on your Mac or Linux box works as is.
- The page itself is plain HTML, CSS and JavaScript — no frameworks, no builds. Any modern browser renders it.
- Or, if you prefer, **Docker**: the image ships Python inside and you touch nothing on the system.

## Why there's a server (and not just an HTML file)

`laya-serve` doesn't send CORS headers, so if you open the page as a bare file and the browser tries to call the API from another origin, it gets blocked before the request even leaves. `server.py` solves this the simple way: it serves the page and has a `POST /proxy` endpoint that forwards the request for you. Since the call comes from the server instead of the browser, CORS stops mattering.

Everything runs on `127.0.0.1:8899`; nothing is exposed to the network. And if your API ever adds CORS, you can uncheck «use local proxy» and let the browser call it directly.

## What you can do on the page

- **Connection**: URL, Bearer token and checkpoint (`auto`, `english`, `multilingual`, `typed-decisions` or `jev-1.13-free` from OpenCode Zen, free and keyless).
- **Extra headers**: add any HTTP header to the request (`X-Title`, `HTTP-Referer`…); they're sent through the proxy, in direct mode and included in the generated `curl`.
- **Questions**: built with forms, one at a time. The three types the model understands:
  - `choice` — pick among options with a description (which department handles this?)
  - `score` — score on an ordered scale you define (not urgent → critical)
  - `noul` — returns the probability of a yes/no (does it ask for a refund?)
- **Presets**: four ready-made examples (support, full triage, guardrail, model router) to get started fast, with body and questions in the active language.
- **ES / EN**: the switch in the header changes the whole UI **and** the loaded content when it matches a preset (anything you typed yourself is left alone).
- **JSON mode**: if you prefer, edit the whole payload by hand and the form is ignored.
- **Results**: animated probability bars with the winning option highlighted; `score` bars carry the level number and its text (critical, soon, not urgent…); the needle scale with per-level distribution, the colour yes/no meter, `confidence` and `answer_confidence` badges, HTTP status, total and inference latency, model used with the routing reason, and tokens consumed.
- **Extras**: copy the request as a ready-to-paste `curl`, plus a history of the last 10 runs (click any to view it again).

## The request underneath

In the end, this is what gets sent (the same thing you'd do with curl):

```json
{
  "state": {"body": "Hello, you've charged me twice for this month's fee. Will you refund one of them?"},
  "questions": {
    "department": {
      "type": "choice",
      "instructions": "Which department handles it?",
      "criteria": {"billing": "payments, invoices, refunds", "tech": "errors, outages"}
    },
    "urgency": {
      "type": "score",
      "instructions": "How urgent is it?",
      "criteria": ["not urgent", "soon", "critical"]
    },
    "asks_refund": {
      "type": "noul",
      "instructions": "Does it explicitly ask for a refund?"
    }
  }
}
```

With `Authorization: Bearer <your-token>` in the header. Pick a specific checkpoint and `"model"` is added to the body; on `auto` it isn't sent and the router decides.

## About the token

It's stored in the browser's `localStorage` so you don't have to paste it on every reload, and it travels nowhere beyond the URL you configure (through the local proxy). If you'd rather it not stick around, clear the field before reloading.

## Files

All the code is just two files, so there are no surprises:

- `index.html` — the whole page: interface, styles and logic in a single file.
- `server.py` — the static server and the proxy, in standard Python.
- `Dockerfile` + `docker-compose.yml` — to run everything in a container.

Then only assets: `favicon.svg` + its PNGs, `docs/captura.png` and the GitHub files (`.github/`, `LICENSE`, `CHANGELOG.md`…).

## License

MIT. See [LICENSE](LICENSE). This is a test client: the model and its server belong to their author, none of that is included here.

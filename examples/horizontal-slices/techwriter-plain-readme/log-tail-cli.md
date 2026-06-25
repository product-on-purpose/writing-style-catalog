---
entry_id: technical-writer
axis: voice
topic_slug: log-tail-cli
topic_label: A CLI tool for tailing structured logs
voice_id: technical-writer
tone_id: matter-of-fact
style_id: diataxis-explanation
format_id: readme
author_type: llm
llm_model: claude-sonnet-4-6
review_status: draft
---

# log-tail

`log-tail` streams structured log output from a running process and filters it by field, level, or pattern in your terminal.

Most log viewers are built for stored logs. They expect a file path, a time range, or a query. `log-tail` is built for the moment a service is running and you need to understand what it is doing right now. It reads newline-delimited JSON from stdin or a named pipe, parses each line as a structured log event, and applies your filters before printing. Because the filtering happens before display, you see only the events that matter for your current investigation.

The tool is designed around a single tradeoff: it gives up persistence in exchange for speed. It does not store events, does not write to disk, and does not index anything. This makes it unsuitable for auditing historical logs. It makes it fast to start, fast to filter, and free of configuration for the common case of watching a live service.

`log-tail` treats log level, timestamp, message, and any additional fields as first-class filter targets because those are the fields engineers actually filter on. The filter language is a small set of predicates - field equality, substring match, numeric comparison for levels - rather than a full query language. This keeps the learning curve shallow. You can add a filter on the command line in the same time it takes to type a grep pattern.

The output is plain text, not interactive. This is intentional. Plain text composes with other Unix tools. You can pipe `log-tail` output into `grep`, `jq`, or a file without any adapter layer.

## Install

```sh
npm install -g @acme/log-tail
```

## Usage

```sh
# Tail a running process and filter to error-level events
your-service | log-tail --level error

# Filter by a specific field value
your-service | log-tail --field requestId=abc-123

# Combine filters
your-service | log-tail --level warn --field service=payments
```

## Docs

- [Filter reference](docs/filters.md)
- [Output format options](docs/output.md)
- [Integrating with systemd journal](docs/systemd.md)

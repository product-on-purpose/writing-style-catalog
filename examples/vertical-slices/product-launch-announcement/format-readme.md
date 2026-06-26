---
entry_id: readme
axis: format
topic_slug: product-launch-announcement
topic_label: Announcing a new product to an outside audience
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Tidemark

`status: beta` `version: 0.9.0` `license: MIT`

> Tidemark gathers scattered customer feedback from your team's existing tools and turns it into a single ranked, shareable roadmap.

Small teams collect feedback everywhere: support tickets, chat threads, survey exports, notes from customer calls. Turning that scatter into a ranked roadmap usually means someone manually reading everything, copying items into a spreadsheet, and arguing about priority in a meeting. Tidemark connects to your existing feedback sources, identifies recurring themes, and scores them by frequency and recency so your team can see what customers are actually asking for in minutes rather than days.

Tidemark is for product teams of two to twenty people who own the roadmap but do not have a dedicated research operation.

## Install

```sh
npm install -g @tidemark/cli
```

Requires Node 18 or later.

## Quick start

```sh
# Connect your feedback sources (runs a short setup wizard)
tidemark init

# Pull and rank feedback from all connected sources
tidemark sync

# Open a shareable, read-only view of the current ranked roadmap
tidemark share
```

After `tidemark share`, you get a URL you can send to stakeholders. The view is read-only by default; see [Sharing and permissions](docs/sharing.md) to add collaborators who can leave comments or re-rank items.

## Documentation

- [Getting started](docs/getting-started.md)
- [Connecting feedback sources](docs/sources.md)
- [How ranking works](docs/scoring.md)
- [Sharing and permissions](docs/sharing.md)
- [FAQ](docs/faq.md)

## Contributing

We welcome bug reports, feature requests, and pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## License

MIT - see [LICENSE](LICENSE).

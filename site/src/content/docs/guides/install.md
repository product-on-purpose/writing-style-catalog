---
title: Install the Plugin
description: Install Writing Style Catalog from the Product on Purpose marketplace, or as a ZIP for Claude.ai and Claude Desktop.
sidebar:
  order: 0
---

Writing Style Catalog ships as a Claude Code plugin. The recommended path is the Product on
Purpose marketplace; a ZIP fallback covers the Claude.ai / Claude Desktop upload flow.

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) for the marketplace path.
- Nothing else: the plugin is self-contained. The `writing-instruction-builder` skill reads
  the catalog that ships inside the plugin, so there is no separate data download.

## Option A - Product on Purpose marketplace (recommended)

Run these inside Claude Code:

```
/plugin marketplace add product-on-purpose/agent-plugins
/plugin install writing-style-catalog@product-on-purpose
```

You add the marketplace by its repo path (`product-on-purpose/agent-plugins`) and install the
plugin by its marketplace identity (`writing-style-catalog@product-on-purpose`). Those differ
by design: the path is the address, the identity is the brand.

Update later with:

```
/plugin update writing-style-catalog
```

## Option B - Claude.ai and Claude Desktop (ZIP upload)

For clients that take a plugin as an uploaded archive:

1. Download `writing-style-catalog-v<version>.zip` from the
   [Releases page](https://github.com/product-on-purpose/writing-style-catalog/releases).
2. Extract it. The archive root holds `.claude-plugin/`, `skills/`, and the `taxonomy/`
   catalog the skill reads.
3. Point your client's plugin setup at `.claude-plugin/plugin.json` in the extracted folder.

## Verify it loaded

### Claude Code (Option A)

Confirm the skill resolves:

```
/writing-style-catalog:writing-instruction-builder voice=pragmatic-architect format=adr
```

You should get a structured prompt prefix back.

### Claude.ai and Claude Desktop (Option B)

These clients have no slash-command listing, so verify conversationally: ask Claude to
"describe the pragmatic-architect voice entry from the writing-style-catalog plugin and
quote its one_liner." A correct install answers in the catalog's own field language (a
senior technical voice that leads with tradeoffs and names constraints explicitly); a
missing or broken install answers generically or says it cannot find the entry. From here, the
[Compose an Instruction](../compose-instruction/) guide walks through reading and using the
output.

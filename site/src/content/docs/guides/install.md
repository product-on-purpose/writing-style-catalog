---
title: Install the Plugin
description: Install Writing Style Catalog from the Product on Purpose marketplace, direct from the repo, or as a ZIP for Claude.ai and Claude Desktop.
sidebar:
  order: 0
---

Writing Style Catalog ships as a Claude Code plugin. The recommended path is the Product on
Purpose marketplace; two fallbacks cover direct-from-repo installs and the Claude.ai / Claude
Desktop upload flow.

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) for the marketplace and
  direct paths.
- Nothing else: the plugin is self-contained. The `compose-instruction` skill reads the
  catalog that ships inside the plugin, so there is no separate data download.

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

## Option B - Direct from the plugin repo

The repository also carries its own single-plugin marketplace, so you can install it without
the shared marketplace:

```
/plugin marketplace add product-on-purpose/writing-style-catalog
/plugin install writing-style-catalog@writing-style-catalog-marketplace
```

This path pins to the latest tagged release. It is the fallback if you do not want the shared
`product-on-purpose` marketplace.

## Option C - Claude.ai and Claude Desktop (ZIP upload)

For clients that take a plugin as an uploaded archive:

1. Download `writing-style-catalog-v<version>.zip` from the
   [Releases page](https://github.com/product-on-purpose/writing-style-catalog/releases).
2. Extract it. The archive root holds `.claude-plugin/`, `skills/`, and the `taxonomy/`
   catalog the skill reads.
3. Point your client's plugin setup at `.claude-plugin/plugin.json` in the extracted folder.

## Verify it loaded

In Claude Code, confirm the skill resolves:

```
/writing-style-catalog:compose-instruction voice=pragmatic-architect format=adr
```

You should get a structured prompt prefix back. From here, the
[Compose an Instruction](../compose-instruction/) guide walks through reading and using the
output.

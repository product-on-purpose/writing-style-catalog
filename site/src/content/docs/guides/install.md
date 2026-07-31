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

## Troubleshooting

Keyed to the actual text you will see, so you can match on the error rather than on a
description of it.

### `[ERROR] jsonschema and referencing are required. Run: pip install jsonschema referencing`

`tools/validate.py` aborts on import when its two dependencies are missing. This is repo
development tooling, not part of the installed plugin, so you only hit it if you cloned the
repository to contribute:

```bash
pip install -r requirements-dev.txt
```

Installing the two named packages alone also works, but the requirements file pins the rest
of the toolchain the checks assume.

### `python: command not found`, or Windows opens the Microsoft Store

On Windows, `python` often is not on `PATH` even when Python is installed, and typing it can
open the Store instead. Use the launcher:

```powershell
py -3 tools/validate.py
py -3 skills/entry-recommender/scripts/recommend.py --list
```

Every command in these guides that begins `python` works with `py -3` substituted. If neither
resolves, Python is genuinely not installed; the scripts need 3.10 or newer for the
`str | None` syntax they use.

### The slash command does not appear after installing

`/writing-style-catalog:...` not autocompleting usually means the marketplace was added but
the plugin was not installed from it. Both steps are required:

```bash
/plugin marketplace add product-on-purpose/agent-plugins
/plugin install writing-style-catalog@product-on-purpose
```

If you installed before a release and are missing something this page describes, update
rather than reinstalling: `/plugin update writing-style-catalog`. The listing tracks a
released tag, not `main`, so a change merged today is not installable until it is tagged and
the registry re-pinned.

### `Entry not found: voice/<id> (run --list to see valid voice ids)`

The id does not exist, or exists but is not `stable`. The recommender and the builder both
serve only `stable` and `reference-quality` entries, so a `draft` entry is invisible to them
by design. `--list` shows exactly what is available:

```bash
python skills/writing-instruction-builder/scripts/build-instruction.py --list
```

### `{"found": false, "error": "unknown axis: <name>"}`

The axis argument takes the singular: `voice`, `tone`, `style`, `format`. Not `voices`, and
not the directory name.

### `build-instruction.py is missing expected symbol '<name>'; the two skills' versions may be out of sync`

`recommend.py` loads the builder's parser rather than duplicating it, and checks up front that
the symbols it needs are present. Seeing this means the two skills came from different
versions, which a partial copy of the repository or a hand-assembled install can cause. Reinstall
the plugin, or check `library.json` to see which versions the two components should be at.

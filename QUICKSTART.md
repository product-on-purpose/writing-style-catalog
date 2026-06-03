# Writing Style Catalog - Quick Start

Composable writing instructions on four orthogonal axes (Voice, Tone, Style, Format). Pick one
entry per axis and the `compose-instruction` skill assembles a ready-to-paste prompt prefix.

## Install

### Claude Code (recommended)

```
/plugin marketplace add product-on-purpose/agent-plugins
/plugin install writing-style-catalog@product-on-purpose
```

Update later with `/plugin update writing-style-catalog`.

### Direct from the repo

```
/plugin marketplace add product-on-purpose/writing-style-catalog
/plugin install writing-style-catalog@writing-style-catalog-marketplace
```

### Claude.ai / Claude Desktop

Download `writing-style-catalog-v<version>.zip` from
[Releases](https://github.com/product-on-purpose/writing-style-catalog/releases), extract, and
point your client at `.claude-plugin/plugin.json`.

Full detail: the [installation guide](https://product-on-purpose.github.io/writing-style-catalog/guides/install/).

## Compose an instruction

```
/writing-style-catalog:compose-instruction voice=pragmatic-architect tone=candid style=problem-solution format=adr
```

All four axes are optional. The skill returns a structured prompt prefix you can prepend to any
writing task. Mix and match across axes for exactly the register, reasoning pattern, and layout
you need.

## Browse the catalog

- 60 entries (15 per axis), each with language patterns, when-to-use guidance, and worked
  examples: the [documentation site](https://product-on-purpose.github.io/writing-style-catalog/).
- Side-by-side [diff-pairs](https://product-on-purpose.github.io/writing-style-catalog/examples/diff-pairs/)
  that vary one axis on a fixed topic.
- Ready-made four-axis [recipes](https://product-on-purpose.github.io/writing-style-catalog/recipes/).

## Learn more

- Full documentation: https://product-on-purpose.github.io/writing-style-catalog/
- Contribute an entry: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Skill specification: https://agentskills.io/specification

---

Built by [Product on Purpose](https://github.com/product-on-purpose).

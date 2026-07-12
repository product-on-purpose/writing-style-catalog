# Writing Style Catalog - Quick Start

Composable writing instructions on four orthogonal axes (Voice, Tone, Style, Format). Pick one
entry per axis and the `writing-instruction-builder` skill assembles a ready-to-paste prompt
prefix - or describe your situation and let `entry-recommender` pick the combination for you.

## Install

### Claude Code (recommended)

```
/plugin marketplace add product-on-purpose/agent-plugins
/plugin install writing-style-catalog@product-on-purpose
```

Update later with `/plugin update writing-style-catalog`.

### Claude.ai / Claude Desktop

Download `writing-style-catalog-v<version>.zip` from
[Releases](https://github.com/product-on-purpose/writing-style-catalog/releases), extract, and
point your client at `.claude-plugin/plugin.json`.

Verify it loaded: ask Claude to describe the `pragmatic-architect` voice entry from the
plugin - a correct install quotes the catalog's own field language rather than answering
generically.

Full detail: the [installation guide](https://product-on-purpose.github.io/writing-style-catalog/guides/install/).

## Compose an instruction

```
/writing-style-catalog:writing-instruction-builder voice=pragmatic-architect tone=candid style=problem-solution format=adr
```

All four axes are optional. The skill returns a structured prompt prefix you can prepend to any
writing task. Mix and match across axes for exactly the register, reasoning pattern, and layout
you need.

## Not sure which combination fits?

```
/writing-style-catalog:entry-recommender I need to tell my engineering team that a feature we committed to is getting cut this quarter, and I want them to trust the reasoning, not just accept the decision.
```

Describe the situation instead of picking ids yourself. The skill scores the catalog, picks a
combination with a reason quoting each entry's own language, and composes the prompt in the same
step. Fix an axis you already know (`voice=pragmatic-architect`) and it only recommends the rest.
See the [usage guide](https://product-on-purpose.github.io/writing-style-catalog/guides/recommend-entries/)
for real example output.

Want a durable personal default instead of a one-off recommendation? `style-profile` captures
your own style once, for reuse across sessions.

## Browse the catalog

- 97 entries (15 Voice, 15 Tone, 15 Style, 52 Format), each with language patterns, when-to-use
  guidance, and worked examples: the [documentation site](https://product-on-purpose.github.io/writing-style-catalog/).
- Side-by-side [diff-pairs](https://product-on-purpose.github.io/writing-style-catalog/examples/diff-pairs/)
  that vary one axis on a fixed topic.
- Ready-made four-axis [recipes](https://product-on-purpose.github.io/writing-style-catalog/recipes/).

## Learn more

- Full documentation: https://product-on-purpose.github.io/writing-style-catalog/
- Contribute an entry: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Skill specification: https://agentskills.io/specification

---

Built by [Product on Purpose](https://github.com/product-on-purpose).

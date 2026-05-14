# Writing Style Library

A composable catalog of writing instructions organized along three orthogonal axes: Voice & Tone, Style/Mode/Genre, and Format/Output Structure. Packaged as a Claude Code plugin, with a Composer web app and SDK coming in later phases.

---

## Quick Start

```bash
# Install the plugin
claude plugin install product-on-purpose/writing-style-library

# Compose a writing instruction from multiple axes
/writing-style-library:compose-instruction voice=pragmatic-architect tone=candid style=problem-solution format=adr
```

The compose-instruction skill assembles a structured prompt prefix that you can prepend to any writing task. Mix and match entries across axes to get exactly the register, reasoning pattern, and layout you need.

---

## The Three-Axis Model

### Axis 1 - Voice & Tone

Voice and Tone are two dimensions within the first axis. Voice captures persistent identity (how you always sound). Tone captures situational register (how you sound right now). They are kept as separate catalog directories (`taxonomy/voices/` and `taxonomy/tones/`) because they have different frontmatter and entry counts, but conceptually they belong to the same axis. When using the `compose-instruction` skill, you pass both `voice=` and `tone=` as separate parameters because each is a distinct catalog lookup within Axis 1.

**Voice** is the persistent identity of the writer: their worldview, characteristic concerns, and the professional archetype they embody. Voice is stable across contexts. The `pragmatic-architect` voice, for example, always reasons from constraints and trade-offs, regardless of whether it is writing a slack message or a technical RFC.

**Tone** is situational coloring layered on top of voice. The same pragmatic-architect voice can deliver a message with a `candid` tone (direct, no softening) or a `mentoring` tone (patient, explanatory). Tone entries are orthogonal to voice entries, so any combination is valid.

### Axis 2 - Style / Mode / Genre

Style entries describe the cognitive and rhetorical pattern of the writing: how ideas are structured and sequenced. `problem-solution` moves from diagnosis to remedy. `layered-disclosure` leads with the answer and buries supporting detail for readers who want depth. Entries on this axis are independent of voice and tone, so the same style can be applied across a wide range of purposes.

### Axis 3 - Format / Output Structure

Format entries define the visual and structural container: headings, bullet depth, table layouts, ADR sections, standup fields. Format is purely presentational and can be composed with any voice/tone/style combination. A `daily-standup` format entry, for example, specifies the three canonical fields and their order, without dictating voice or rhetorical pattern.

---

## Current Status

**Phase 0 / Milestone 1 - Foundation**

- Repository scaffold and root documentation files
- Five seed entries per axis (in progress)
- Async-standups anchor topic for vertical-slice examples
- `compose-instruction` skill (in progress)

See [ROADMAP.md](ROADMAP.md) for upcoming phases.

---

## Installation

```bash
claude plugin install product-on-purpose/writing-style-library
```

Requires Claude Code. The plugin adds the `writing-style-library:compose-instruction` skill to your session.

---

## Project Structure

| Path | Type | Purpose |
|------|------|---------|
| `taxonomy/voices/` | Content | Voice entries (persistent writer identity) |
| `taxonomy/tones/` | Content | Tone entries (situational register modifiers) |
| `taxonomy/styles/` | Content | Style/mode/genre entries (rhetorical patterns) |
| `taxonomy/formats/` | Content | Format/output-structure entries |
| `examples/vertical-slices/` | Content | Full worked examples for a single topic across all axes |
| `examples/horizontal-slices/` | Content | Cross-topic samples for a single axis value |
| `examples/diff-pairs/` | Content | Side-by-side pairs showing the effect of changing one axis |
| `schemas/` | Code | JSON Schema files for all entry types |
| `skills/writing-instruction-builder/` | Code | Claude Code plugin skill (compose-instruction) |
| `docs/` | Docs | MkDocs site source |
| `tools/` | Code | Validation and generation scripts |
| `tests/` | Code | Pytest tests and golden-output fixtures |
| `docs/internal/adr/` | Docs | Architecture Decision Records |
| `recipes/` | Content | Curated axis combinations for common use cases |
| `packages/ts-sdk/` | Code | TypeScript SDK (Phase 2) |
| `packages/py-sdk/` | Code | Python SDK (Phase 2) |
| `packages/mcp-server/` | Code | MCP server (Phase 2) |
| `packages/composer-app/` | Code | Composer SPA (Phase 1) |
| `.claude-plugin/` | Config | Claude Code plugin manifest and config |
| `.github/` | Config | CI workflows and issue templates |

---

## License

- Code (schemas, skills, tools, packages, tests): [Apache-2.0](LICENSE)
- Content (taxonomy entries, examples, docs): [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

See [NOTICE](NOTICE) for full attribution details.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add taxonomy entries, submit examples, and run validation locally.

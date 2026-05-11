# Writing Style Library

A composable catalog of writing instructions organized along three orthogonal axes: Voice & Tone, Style/Mode/Genre, and Format/Output Structure. Install it as a Claude Code plugin and use the `compose-instruction` skill to assemble a writing instruction prefix from any combination of axis values.

---

## The Three-Axis Model

| Axis | Description | Seed Entries |
|------|-------------|-------------|
| Voice & Tone (Axis 1) | Voice: persistent writer identity (worldview, archetype). Tone: situational register layered on top of voice. Two catalog dimensions, one axis. | voices: pragmatic-architect, product-thinker, ops-realist, technical-educator, skeptical-analyst. tones: candid, mentoring, optimistic-realist, cautious, energizing. |
| Style / Mode / Genre (Axis 2) | Cognitive and rhetorical pattern: how ideas are sequenced | problem-solution, layered-disclosure, decision-log, narrative-arc, step-by-step |
| Format / Output Structure (Axis 3) | Visual and structural container: headings, sections, layout | adr, daily-standup, slack-thread, technical-rfc, bullet-brief |

---

## Quick Start

```bash
# Install the plugin
claude plugin install product-on-purpose/writing-style-library

# Compose a writing instruction
/writing-style-library:compose-instruction voice=pragmatic-architect tone=candid style=problem-solution format=adr
```

The skill outputs a structured prompt prefix. Copy it into your system prompt or prepend it to your writing task.

---

## Installation

```bash
claude plugin install product-on-purpose/writing-style-library
```

Requires Claude Code. After installation, the `writing-style-library:compose-instruction` skill is available in your session.

---

## Next Steps

- [Three-Axis Model](concepts/three-axis-model.md) - Understand the design behind the catalog
- [Compose an Instruction](how-to/compose-instruction.md) - Step-by-step guide
- [Add an Entry](how-to/add-entry.md) - Contribute to the catalog

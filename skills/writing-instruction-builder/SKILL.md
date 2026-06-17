---
name: writing-instruction-builder
description: Compose a writing instruction from voice, tone, style, and format axis entries. Use when you need a precise writing instruction for a specific combination of voice, tone, style, and format. Returns a ready-to-use LLM prompt string.
metadata:
  version: "0.2.0"
---

# Compose Writing Instruction

Compose a writing instruction by combining taxonomy entries from the Voice and Tone, Style, and Format axes.

## Usage

```
/writing-style-catalog:writing-instruction-builder [voice=<id>] [tone=<id>] [style=<id>] [format=<id>] [topic=<text>] [audience=<text>]
```

All parameters are optional. If omitted, the skill picks sensible defaults.

## Parameters

- `voice` - Voice entry ID (e.g., `pragmatic-architect`, `pastoral`, `columnist`)
- `tone` - Tone entry ID (e.g., `candid`, `warm`, `matter-of-fact`)
- `style` - Style entry ID (e.g., `problem-solution`, `devotional-reflection`)
- `format` - Format entry ID (e.g., `adr`, `blog-post-long-form`, `slack-message`)
- `topic` - The topic or subject to write about (optional, for a more concrete composed instruction)
- `audience` - The intended audience (optional, defaults to general)

## What the Skill Does

1. Validates each provided entry ID against the taxonomy catalog
2. Reads the `llm_instruction_phrasing` from each matching entry
3. Assembles a composed instruction string in a fixed precedence order: voice, then tone, then style, then format
4. Checks the selected entries against each other's relationship fields and warns on any conflict (without blocking)
5. Returns the composed instruction ready to paste into any LLM prompt

### Implementation

The composition is implemented by the helper script `scripts/build-instruction.py` in this
skill folder. It reads the catalog from the `taxonomy/` directory at the plugin root, so that
directory ships with the plugin. The slash command takes `key=value` arguments; the script
itself takes `--flag value` arguments. Run it directly to compose without the slash command,
for example:

```bash
python scripts/build-instruction.py --voice pragmatic-architect --tone candid --format adr
```

### Conflict-aware composition

The builder reads each selected entry's `avoid_with` and `pairs_well_with` relationships and
reports on them, so a composition is a checked guarantee rather than a blind concatenation. The
rules (see ADR 0016):

- **Conflicts are symmetric.** A pair is flagged if *either* entry lists the other in
  `avoid_with`, so the warning never depends on which author recorded the link.
- **Warn, never block.** A conflicting pair still composes (you may want a deliberate tension);
  the builder emits a warning and applies voice -> tone -> style -> format precedence so the
  higher-precedence axis leads.
- **Affirmations.** A `pairs_well_with` match is surfaced as a confirming note.

The composed instruction prints to stdout; conflict warnings and affirmation notes print to
stderr, so stdout stays a clean, pipeable prompt. For example, pairing the
`pragmatic-architect` voice with the `reverent` tone (which it lists in `avoid_with`) still
returns the instruction and prints:

```
warning: conflict - pragmatic-architect (voice) and reverent (tone) are marked avoid_with.
Composing anyway with voice -> tone -> style -> format precedence; expect tension.
```

## Examples

Compose an ADR in pragmatic-architect voice with candid tone:
```
/writing-style-catalog:writing-instruction-builder voice=pragmatic-architect tone=candid format=adr
```

Compose a pastoral devotional:
```
/writing-style-catalog:writing-instruction-builder voice=pastoral tone=reverent style=devotional-reflection format=devotional-entry topic="The discipline of rest"
```

## Available Entries

Run without arguments to see all available entries grouped by axis.

---
name: compose-instruction
description: Compose a writing instruction from voice, tone, style, and format axis entries. Use when you need a precise writing instruction for a specific combination of voice, tone, style, and format. Returns a ready-to-use LLM prompt string.
---

# Compose Writing Instruction

Compose a writing instruction by combining taxonomy entries from the Voice and Tone, Style, and Format axes.

## Usage

```
/writing-style-catalog:compose-instruction [voice=<id>] [tone=<id>] [style=<id>] [format=<id>] [topic=<text>] [audience=<text>]
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
3. Assembles a composed instruction string that specifies voice, tone, style, and format together
4. Returns the composed instruction ready to paste into any LLM prompt

## Examples

Compose an ADR in pragmatic-architect voice with candid tone:
```
/writing-style-catalog:compose-instruction voice=pragmatic-architect tone=candid format=adr
```

Compose a pastoral devotional:
```
/writing-style-catalog:compose-instruction voice=pastoral tone=reverent style=devotional-reflection format=devotional-entry topic="The discipline of rest"
```

## Available Entries

Run without arguments to see all available entries grouped by axis.

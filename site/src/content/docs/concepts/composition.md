---
title: Composition
description: How picking one entry per axis assembles into a structured prompt prefix.
---

Composition is the move that turns the catalog from a collection of entries into a working tool. You pick one entry from each axis and assemble them into a structured prompt prefix that shapes LLM output.

This page explains how composition works, why the axes are designed to compose, and how to think about the choices you are making when you assemble an instruction.

---

## The composition stack

A composed instruction is built from four sections, in this order:

1. **Voice** - who is speaking
2. **Tone** - how they feel right now
3. **Style** - how they organize ideas
4. **Format** - how the output is structured

Each section is independent. The `writing-instruction-builder` skill concatenates them with explicit headers so the receiving LLM can read each section as a self-contained directive.

You do not have to fill every slot. A two-axis composition (just voice and format, for example) produces a valid instruction. Leaving an axis blank means "the LLM picks whatever fits," which is sometimes the right call.

---

## Why orthogonal axes compose

The axes are designed so that any combination produces a coherent instruction. This is not an accident. It is the design constraint that makes the catalog useful.

The orthogonality test: does each axis describe a different kind of choice?

- **Voice** describes a persistent identity. A `pragmatic-architect` is always a pragmatic-architect, no matter what they are writing about.
- **Tone** describes a situational register. The same pragmatic-architect can be `candid` in one message and `warm` in another.
- **Style** describes a rhetorical or cognitive pattern. The same voice and tone can render as `problem-solution` or `narrative-case-study`.
- **Format** describes a structural container. The same voice, tone, and style can be packaged as an `email`, an `adr`, or a `slack-message`.

Because these four describe different things, a choice on one axis does not preempt a choice on another. You can vary one and hold the others constant.

---

## The `pairs_well_with` graph

Not every combination is equally good. A `reverent` tone paired with a `daily-standup` format is technically valid, but it produces a strange artifact. The catalog encodes this with three cross-reference fields on every entry:

- `pairs_well_with` - other entries that compose naturally with this one
- `avoid_with` - other entries that conflict or produce poor results
- `confusable_with` - other entries commonly mistaken for this one

These cross-references are guidance, not enforcement. The Composer surface uses them to highlight likely good combinations. The `writing-instruction-builder` skill does not block bad combinations - it produces what you ask for, and trusts you to know when you are doing something unusual.

---

## What composition produces

The composed output is a structured prompt prefix that looks roughly like this:

```
[VOICE: pragmatic-architect]
<the voice's llm_instruction_phrasing field>

[TONE: candid]
<the tone's llm_instruction_phrasing field>

[STYLE: problem-solution]
<the style's llm_instruction_phrasing field>

[FORMAT: adr]
<the format's llm_instruction_phrasing field>
```

Each section is drawn directly from the entry's `llm_instruction_phrasing` field, which is authored to be immediately usable as a prompt fragment.

The full assembled instruction is designed to be prepended to any writing task without modification. See [Compose an Instruction](../../guides/compose-instruction/) for a worked example.

---

## When to leave an axis blank

Composability includes the empty case. Three reasons to leave an axis out:

1. **The axis does not constrain the task.** A brief Slack reply rarely needs a style directive; the format and tone do most of the work.
2. **The LLM has reliable defaults.** Modern LLMs default to reasonable formats when asked to "write an email." You may not need to specify the format axis at all.
3. **You want the LLM to choose.** Leaving the style blank in a creative task lets the model find a structure that fits the content.

The composition is a control surface, not a checklist.

---

## Common combinations

See the [How-To: Compose an Instruction](../../guides/compose-instruction/) page for a table of curated combinations, and the `recipes/` directory in the repo for full worked examples with example output.

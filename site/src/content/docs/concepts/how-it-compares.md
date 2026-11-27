---
title: How It Compares
description: How the Writing Style Library differs from prompt libraries, style guides, and tone presets, and where each of those is the better tool.
---

The Writing Style Library is not the only way to tell a model how to write. Most people use one of four other approaches. This page sets them side by side, including the cases where the other approach is the better choice.

The short version: a prompt library is a pile of finished prompts, and a style guide is a rulebook for one organization. This catalog is a coordinate system. It splits "style" into four independent choices, names each value, and assembles any combination into one instruction.

## The comparison

| | Prompt libraries | House style guides | Tone presets in writing tools | Describing it in the prompt | Writing Style Library |
| --- | --- | --- | --- | --- | --- |
| **Unit you pick** | A whole prompt for a whole task | A rule ("use sentence case") | One adjective from a dropdown | Whatever you type that day | One named value on each of four axes |
| **How the parts combine** | They do not. You pick one prompt. | You apply every rule at once | One preset at a time | You merge them yourself, in prose | Any Voice with any Tone, Style, and Format |
| **Clashing choices** | Not applicable | Left to the editor | Not applicable | You notice, or you do not | The builder flags pairs an entry lists in `avoid_with` and orders the blocks |
| **Shows what each choice produces** | Sometimes one sample output | Sometimes a do and don't pair | Rarely | No | Worked samples on twelve shared topics, plus diff-pairs that compare two entries on one axis |
| **Evidence the instruction steers output** | Usually none | Not the question it answers | Usually none | None | A blind test with a negative control ([details](../adherence-evidence/)) |
| **Tied to one model or tool** | Often | No | Yes | No | No. The output is a plain prompt prefix |
| **Covers your organization's terms and rules** | No | Yes | No | If you type them | No |

## Where the other approaches are better

**Use a house style guide** for grammar, terminology, capitalization, and legal wording. The catalog does not know your product names or your banned phrases. A style guide and this catalog work together: the guide supplies the rules, and the catalog supplies the register and shape.

**Use a prompt library** when the task itself is the hard part. A library of prompts for "write a SQL query" or "summarize a contract" covers tasks that have little to do with voice or tone. This catalog only addresses how the writing reads.

**Describe it in the prompt** when you need something once and will not need it again. Composing from named values pays off when you write the same kind of document more than once.

**Use a tone preset** when the tool you already write in offers one and a single adjective is enough. Presets are quick. They stop being enough when you need to control two things at once, such as a candid tone in a decision-record format.

## What is different here, specifically

**Four independent axes.** Voice is who is speaking. Tone is their register in this piece. Style is how the ideas are sequenced. Format is the container. Each axis passes the same test: hold the other three constant, change this one, and the output changes in a way you can point at. The [four-axis model](../four-axis-model/) explains why the split is drawn where it is.

**Named values with their own failure modes.** Every entry carries the phrases that identify it (`tells`), the ways people misuse it (`anti_patterns`), and the ways it breaks when overdone (`failure_modes`). A prompt that says "sound confident" has none of that.

**Composition that checks itself.** When either of two selected entries lists the other in `avoid_with`, the builder warns you and applies a fixed precedence of voice, then tone, then style, then format. It never blocks a combination. The design is recorded in [ADR 0016](https://github.com/product-on-purpose/writing-style-catalog/blob/main/docs/internal/adr/0016-conflict-aware-composition.md).

**A measurement, not only a description.** Blind judges attributed near-neighbour samples to the right entry in two small tests, and rejected deliberate caricatures in a third. The three tests covered sixteen, nine, and three entries, not the whole catalog. The [evidence page](../adherence-evidence/) states the scope and the limits.

**Status that says what it means.** Each entry shows its review status. `machine-verified` means the entry passes every automated check and has not yet been read by the maintainer. `stable` means the maintainer read it. The ladder is described in the [contribution process](../../governance/contribution-process/).

## What this catalog does not do

- It does not write for you. It produces an instruction that you give to a model.
- It does not carry your brand. The voices are archetypes, such as `pragmatic-architect` or `coach`, not your company's voice. The `style-profile` skill saves your own default combination, but it selects from the catalog rather than learning your voice from samples.
- It does not grade the output. Nothing checks that a given draft followed the instruction.
- It does not replace an editor. A composed instruction gets a model closer to the register you want. A person still decides whether the draft is right.

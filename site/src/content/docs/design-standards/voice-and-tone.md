---
title: Voice and Tone
description: Authoring standards for voice and tone entries, with the tests a strong entry passes.
---

This page collects the authoring standards for voice and tone entries - what makes an entry useful, what makes one weak, and how to test a draft before promoting it past `draft` status.

These standards apply to entries in `taxonomy/voices/` and `taxonomy/tones/`. The schemas at `schemas/voice.schema.json` and `schemas/tone.schema.json` enforce the structural rules; this document covers the editorial ones.

---

## What a strong voice entry does

A strong voice entry passes three tests:

**The substitution test.** Could a real person, in a real job, use this voice without translation? `pragmatic-architect` passes because senior engineers actually talk this way. `enlightened-philosopher-king` fails because no one talks that way, even if it describes a coherent stance.

**The distinctness test.** Is this voice meaningfully different from its nearest neighbors in the catalog? If `coach` reads as a slightly warmer `friendly-mentor`, the catalog needs one entry, not two. Distinctness lives in the `confusable_with` section - if you cannot write a clear sentence distinguishing your entry from each of its confusables, the entry is not yet ready.

**The instruction-block test.** Can an LLM use the `llm_instruction_phrasing` field as a prompt prefix and produce output recognizably in the named voice? This is the only test the entry will face in real use. Read your draft out loud and ask whether it would actually shape an LLM's output.

---

## What a strong tone entry does

A strong tone entry passes four tests:

**The marker test.** The `markers` field must list textual behaviors that a reader could observe in a sample. "Uses imperative mood for steps" is a marker. "Feels confident" is not - confidence is the goal, not the marker.

**The orthogonality test.** Can this tone be applied to multiple voices, or does it only work with one? If the tone is inseparable from a specific voice, the trait belongs in the voice entry, not as a separate tone. A useful tone passes the test by composing freely.

**The distinctness test.** Same as for voices - the `confusable_with` section must do real work.

**The register test.** Tone names a register (a way of feeling), not a content choice. `urgent` is a register. `incident-related` is a content category, not a tone.

---

## Frontmatter discipline

A few field-specific notes worth holding onto:

**`one_liner`** must be under 200 characters and stand alone. A reader scanning the catalog index should understand what this entry is from the one-liner alone.

**`description`** uses a YAML literal block scalar (`|`). Two or three paragraphs, 100-300 words total. Treat it as the entry's case for its own existence.

**`language_patterns` (voice)** must list at least three observable patterns. Patterns describe how sentences are built, not how the writer feels. Good: "Leads with the decision, then the reasoning." Weak: "Sounds confident."

**`markers` (tone)** must list at least three observable markers. Same discipline as language patterns - describe what a reader can see in a sample.

**`pairs_well_with`** must list at least one entry. Aim for three to five. Every ID listed must exist in the catalog when you commit (validation will catch typos).

**`llm_instruction_phrasing`** is the entry's single most important field. It is the literal text that gets injected into a prompt at composition time. Write it as if you were giving instructions to a writer who has never read your entry. Three to five sentences. Concrete, not abstract.

---

## Cross-reference reciprocity

When entry A lists entry B in its `pairs_well_with`, ideally entry B lists A back. The validator does not enforce this, but maintainers will flag asymmetric cross-references during review.

The same goes for `confusable_with`. If `coach` is confusable with `friendly-mentor`, then `friendly-mentor` should list `coach` in its own `confusable_with` field and explain the distinction from its side.

Reciprocity makes the catalog navigable from any starting point.

---

## What does NOT belong in a voice or tone entry

- Topic preferences ("this voice writes about technical topics") - voice is independent of topic
- Format constraints ("this voice writes in three sections") - format is a separate axis
- Style choices ("this voice uses problem-solution structure") - style is a separate axis
- Personal opinions about the entry ("this voice is the best for serious topics") - state the entry's use, not your opinion

Each axis is independent. Mixing across axes weakens composability.

---

## Promotion criteria

An entry moves from `draft` to `reviewed` after a maintainer's editorial pass. From `reviewed` to `stable` requires the entry to render across all twelve anchor topics (Gate 2, enforced by `tools/validate.py`) and a maintainer's explicit promotion decision, executed with `tools/promote.py` - never a self-promotion, and never automatic even when Gate 2 passes. From `stable` to `reference-quality` is rare and requires explicit maintainer judgment - reference-quality entries are the ones that get shown in onboarding material.

See [Contribution Process](../../governance/contribution-process/) for the full review flow.

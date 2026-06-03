---
title: Pick a Voice
description: A three-step method for choosing the voice that fits your reader.
---

Voice is the most consequential choice in a composed instruction. Tone, style, and format adjust how a piece reads; voice determines who is reading it back to you. Get the voice wrong and no amount of tone or format polish will save the artifact.

This guide walks through the choice in three steps.

---

## Step 1 - Name the reader

The voice that fits is the voice the reader expects from the person they think is talking. Before you pick anything, write down two facts:

- Who is the actual reader? (engineering manager, product leader, customer, congregation)
- What relationship does the writer have with them? (peer, advisor, leader, teacher)

If you cannot answer both, no voice will reliably fit. Refine the brief before composing.

---

## Step 2 - Match the archetype

Each voice in the catalog embodies a recognizable professional archetype. The right archetype is the one a real person in that role would already be using.

| Reader and relationship | Likely voice |
|---|---|
| Senior engineer reading a design review | `pragmatic-architect` |
| Product team reading a feature proposal | `product-thinker` |
| New hire reading an onboarding guide | `friendly-mentor` or `technical-writer` |
| Operations team reading an incident runbook | `operator` |
| Board or VP reading a quarterly summary | `executive` |
| Reader of an opinion column or blog | `columnist` |
| Congregation reading a devotional | `pastoral` |
| Practitioner reading API reference | `technical-writer` |
| Coachee reading a development plan | `coach` |
| Anyone, any context, just needs the point | `direct-communicator` |

Browse `taxonomy/voices/` for the full list. The `one_liner` field at the top of each `ENTRY.md` is designed to fit on a card so you can scan it fast.

---

## Step 3 - Confirm with the example

Once you have a candidate, read the matching example file under `examples/vertical-slices/async-standups/voice-<id>.md`. The example is the voice rendering the same situation that every other voice also renders, so you can compare the candidate against its neighbors.

Two questions to ask while reading:

1. Does this voice sound like the person you would want writing to your reader?
2. Does the reader, in your mental model of them, find this voice credible?

If both answers are yes, you have your voice. If either is no, look at the candidate's `confusable_with` field and check the entries listed there. The confusable entries are almost always the better fit when the first choice felt close but off.

---

## Common decision tricks

**When you are unsure between two voices**, prefer the more domain-specific one. `pragmatic-architect` beats `direct-communicator` when the audience is technical, even though `direct-communicator` is technically valid. The specific voice carries more useful constraints into the composition.

**When the reader is mixed**, pick the most demanding reader. A doc that has to work for both engineers and executives should usually be voiced for the executive - engineers can read across, executives often will not.

**When the topic is emotionally weighted**, voice matters more than usual. `pastoral` and `pragmatic-architect` are not interchangeable on a topic like organizational restructuring; the voice signals what kind of conversation this is.

**When you are writing to yourself or one peer**, you may not need to specify a voice at all. The composition is a control surface; not every axis needs to be filled.

---

## What to do if no voice fits

If you find yourself wishing for a voice the catalog does not have, two things to try:

1. **Re-read the closest candidate's `pairs_well_with` field.** Sometimes the gap is not the voice itself - it is the tone or style pairing.
2. **Propose a new entry.** See [How to Add an Entry](../add-entry/). The catalog is designed to grow.

The Phase 1 target is fifteen voice entries; current count is ten. Real gaps in the catalog become future entries.

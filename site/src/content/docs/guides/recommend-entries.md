---
title: Recommend Entries for a Situation
description: Describe a writing situation and get a voice/tone/style/format recommendation, with the prompt composed in the same step.
---

`writing-instruction-builder` composes a prompt from axis values you already know you want. `entry-recommender` is for when you do not know them yet - you describe the situation, and the skill scores the stable catalog against it, reads the strongest candidates, picks one per axis with a reason quoting the entry's own language, and composes the final prompt.

This guide walks through what you get back, with real example output verified against v0.2.0. For the mechanics of composition itself, see [Compose an Instruction](../compose-instruction/).

**How the candidate list works:** The scorer returns every qualifying candidate per axis in a tiered `short_list`. The first 6 candidates that are `above_threshold` (read tier) arrive with their full field text so the skill can read and pick from them immediately. All other rows are lean - they carry a `"fields": "fetch"` marker and omit the full text. Two kinds of lean rows appear: qualifying candidates beyond the first 6 (lean triage, `above_threshold: true`), which the skill fetches before picking; and non-qualifying near-misses (lean padding, `above_threshold: false`), which are context only and are not pick candidates. The format axis routinely produces 20-30+ qualifying candidates on real situations; the tiered structure keeps the payload compact without hiding any qualifying option from consideration. The floor case - a situation with zero qualifying candidates on an axis - collapses to lean-only rows with no full-text loading.

---

## Step 1 - Install the Plugin

Same install as the rest of the catalog:

```
/plugin marketplace add product-on-purpose/agent-plugins
/plugin install writing-style-catalog@product-on-purpose
```

Full install options are in the [installation guide](../install/).

---

## Step 2 - Describe the Situation

```
/writing-style-catalog:entry-recommender <situation description> [voice=<id>] [tone=<id>] [style=<id>] [format=<id>] [--recommend-only]
```

The situation description is free text - what you need to write and for whom, not which entry ids to use. If you already know one or two axes, fix them with `axis=id` and the skill recommends only the rest.

---

## Example: Full Recommendation

Input:

```
/writing-style-catalog:entry-recommender I need to tell my engineering team that a feature we committed to is getting cut this quarter, and I want them to trust the reasoning, not just accept the decision.
```

The skill scores all four axes, reads the strongest candidates, and settles on `pragmatic-architect` (voice), `confident` (tone), `decision-log` (style), and `memo` (format) - each for a reason grounded in that entry's own field text, not a guess:

- **Voice - `pragmatic-architect`**: names constraints and reasons from tradeoffs, matching "Explaining technical tradeoffs to engineers."
- **Tone - `confident`**: "the claim leads and the reasoning follows" - a direct match for "trust the reasoning, not just accept the decision." Notably, the highest-*scoring* tone candidate here was `resolute` ("the reasoning is referenced briefly or not at all: settled, not relitigated") - the opposite of what this situation actually asks for. The skill does not default to the top score; it reads the candidates' own language and picks the one that genuinely fits, even when that means passing over a higher score.
- **Style - `decision-log`**: "gives the reasoning - the 'because,' not just the 'what'" is close to a direct quote of the request.
- **Format - `memo`**: "puts a decision or policy on the record for a group." (A same-word-different-sense trap showed up here too: a customer-testimonial format scored higher purely because its description uses "trust" in the sense of brand credibility, not trusting a decision's reasoning - exactly the kind of coincidental match the read-based pick exists to catch.)

No conflicts were found between the four picks, so the skill composes directly:

```
Write in a pragmatic-architect voice. You are a senior technical lead who has shipped systems
at scale and carries the scars to prove it. Lead with decisions, not options. Name the
constraints explicitly - latency, cost, team skill, operational burden - and explain your
reasoning in terms of failure modes and tradeoffs. Use concrete nouns. Avoid hedging phrases
like "it depends" unless you immediately name what it depends on. Trust the reader to handle
tradeoff information without softening.

Write in a confident tone. You have done the thinking. State your position directly and let
the reader respond to the position itself. Strip ritual hedges - the "I think," "maybe,"
"just my opinion" padding that exists to protect you from being wrong rather than to inform
the reader. Keep hedges only where uncertainty is real and specific. Use declarative
sentences for core claims. Reasoning follows the claim, it does not bury it. This is not
arrogance - you trust the reader to push back if they disagree. Performative humility is the
failure mode, not directness. Unlike a resolute tone, you are stating and defending a position
that may still be open to debate; you are not yet past the decision into pure execution.

Write as a decision log. Organize around four sections: context (what was true when this
decision was made), options (what was actually considered, not a post-hoc list), criteria
(what values or constraints governed the evaluation), and decision (what was chosen and why -
the because, not just the what). Write as if the reader was not in the room. Do not justify
the decision in hindsight - record the reasoning as it actually existed at decision time.
A good decision log records good reasoning; it does not require the decision to have been
correct in hindsight. Do not include pleasantries or framing prose; go directly to the
structured record.

Write as a memo. Begin with the structured header: TO (recipient group or role), FROM (author
name and title), DATE, and RE (the topic - what this memo puts on record). Open the body
immediately below the header with one to two sentences stating the decision, policy, or position
being established - no preamble. Follow with the context or rationale the reader needs to
understand the record. Close with a statement of what this memo confirms or establishes. Address
the group as a whole, not a specific individual with a task. Do not include a call to action or
request a reply - the memo states something for the record. Maintain a formal institutional
register; expect the document to be filed and retrieved, not replied to.
```

---

## Example: One Axis Already Fixed

If you already know one axis, fix it and the skill recommends only the rest - it never re-justifies or second-guesses a value you supplied:

```
/writing-style-catalog:entry-recommender explaining a database migration decision to the team voice=pragmatic-architect
```

`voice` is passed through untouched. The skill recommends `resolute` (tone), `decision-log` (style), and `adr` (format) - `adr` beats two higher-scoring format candidates because "Recording architectural decisions" and "Capturing technology choices" are direct hits, while the higher scorers were a generic on-the-record memo and an external-facing public statement, neither as close a fit for an internal architecture decision. `adr` also lists `pragmatic-architect` in its own compatible-entries field, confirming the pairing independently.

No conflict exists between these four values, so the prompt composes directly with all four voices' instructions stacked - the same mechanism as the full-recommendation example above.

---

## Example: Nothing Genuinely Fits

```
/writing-style-catalog:entry-recommender Write something for my houseplant's Instagram account.
```

Every candidate on every axis falls below the relevance bar here - none of the coincidental keyword overlaps (a stray "something," a customer-incident report using the word "account" in the sense of a written narrative rather than a social media profile) hold up as a genuine fit once their actual field language is read. Rather than force a weak guess into every slot, the skill reports low confidence for each axis, names the closest thing it considered and why it does not fit, and composes with those axes left blank - the same blank-axis behavior `writing-instruction-builder` already supports for a value you choose to omit yourself.

---

## Conflict Resolution

If two of the picked values are marked incompatible with each other (an entry's own `avoid_with` field), the skill does not just warn and move on. It first tries to resolve the conflict by re-picking one of the values it controls - searching progressively further down that axis's ranked candidates, always checking that a replacement is both compatible and a genuine fit, never substituting a technically-compatible-but-irrelevant entry just to make the conflict disappear. A conflict is only surfaced unresolved when there is truly no way around it - for example, when both conflicting values were ones you fixed yourself, and the skill has no room to substitute either one.

---

## Recommend-Only Mode

Add `--recommend-only` to see the four picks and their justifications without composing the final prompt - useful if you want to review or adjust before committing to a combination:

```
/writing-style-catalog:entry-recommender a public apology for a service outage --recommend-only
```

---

## A Known Limitation

Matching is deterministic keyword and facet overlap against each entry's own field text - no embeddings, no external model call, by design (see [Composition](../../concepts/composition/) for why the catalog favors zero-dependency mechanisms where it can). This means a genuinely good match can be missed if your description uses different words than the entry's own text, even when the meaning is the same - describing a eulogy without using a form of the word "eulogy" itself, for instance. If a recommendation feels off, try rephrasing the situation closer to how you would expect the entry to describe itself, or fix the axis yourself with `voice=`/`tone=`/`style=`/`format=` if you already know what you want.

---

## See Also

- [Compose an Instruction](../compose-instruction/) - the underlying composition mechanism, for when you already know all four values.
- [Pick a Voice](../pick-voice/) - a manual, teach-the-reasoning method for choosing voice specifically; useful if you want to understand the archetypes rather than get a fast answer.
- [Composition](../../concepts/composition/) - how axis values combine, including the blank-axis behavior this skill relies on.

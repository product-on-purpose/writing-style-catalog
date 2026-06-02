---
title: Three-Axis Model
description: How Voice, Tone, Style, and Format vary independently so any combination composes.
---

## Why Three Axes?

Most writing guidance collapses "who is writing" and "how they are writing" into a single undifferentiated concept called "voice" or "style." This works for a single author writing in a single context, but it breaks down when you need to reuse and remix writing instructions across different tasks and audiences.

The three-axis model separates writing instruction into components that vary independently:

1. **Who is writing and how they feel about the audience** (Voice & Tone): Voice is stable across all contexts for a given identity; Tone is situational and changes with context. Together they form the first axis.
2. **How they structure reasoning** (Style): independent of both identity and mood
3. **How they present output** (Format): purely structural, applies to any voice/tone/style combination

Because these three axes are independent, you can compose any combination. A `pragmatic-architect` voice with a `mentoring` tone writing in a `problem-solution` style formatted as a `daily-standup` is a fully specified, reproducible writing instruction.

---

## Axis 1 - Voice & Tone

Voice and Tone are two dimensions within the first axis. Voice captures persistent identity (how you always sound). Tone captures situational register (how you sound right now). They are kept as separate catalog directories because they have different frontmatter and different entry counts, but they belong to the same conceptual axis.

### Voice

Voice is the persistent identity of the writer. It captures:

- The professional archetype they embody (`pragmatic-architect`, `product-thinker`)
- The concerns they characteristically surface (constraints and trade-offs vs. user outcomes)
- The level of abstraction they prefer (systems vs. features vs. operations)
- The assumptions they make about the reader

Voice is **stable across contexts**. A `pragmatic-architect` voice behaves the same way whether writing a Slack message or a technical RFC - it always reasons from constraints, names trade-offs explicitly, and avoids hand-waving.

### Seed Voice Entries

| ID | Description |
|----|-------------|
| `pragmatic-architect` | Reasons from system constraints and trade-offs; names costs explicitly |
| `product-thinker` | Centers user outcomes; connects decisions to measurable value |
| `ops-realist` | Prioritizes reliability and operational burden; suspicious of complexity |
| `technical-educator` | Builds up from first principles; patient with foundational gaps |
| `skeptical-analyst` | Questions assumptions; demands evidence before committing |

---

### Tone

Tone is situational coloring applied on top of voice. It reflects how the writer wants the reader to feel, and what relational stance the writer is taking in this particular message.

### The Voice/Tone Distinction

This is the most important distinction in the model. Voice does not change; tone does. The same `pragmatic-architect` can be:

- `candid`: direct, no softening, states the problem plainly
- `mentoring`: patient, explanatory, meets the reader where they are
- `optimistic-realist`: acknowledges problems while keeping forward momentum

Separating tone from voice means you do not need a different voice entry for every emotional register. You have one `pragmatic-architect` entry and five tone modifiers.

### Seed Tone Entries

| ID | Description |
|----|-------------|
| `candid` | Direct and unhedged; states the situation plainly without softening |
| `mentoring` | Patient and explanatory; guides the reader rather than directing them |
| `optimistic-realist` | Acknowledges problems; maintains forward momentum |
| `cautious` | Surfaces risks prominently; prefers explicit caveats |
| `energizing` | Motivating register; emphasizes opportunity and momentum |

---

## Axis 2 - Style / Mode / Genre

Style describes the cognitive and rhetorical pattern of the writing: how ideas are organized and sequenced. It is independent of who is writing and how they feel.

### Seed Style Entries

| ID | Description |
|----|-------------|
| `problem-solution` | Diagnosis first, then remedy; clear causal structure |
| `layered-disclosure` | Lead with the answer; bury supporting detail for readers who want depth |
| `decision-log` | Documents a choice: context, options considered, decision, rationale |
| `narrative-arc` | Situation, complication, resolution; story structure for complex topics |
| `step-by-step` | Sequential instructions with explicit ordering and numbered steps |

---

## Axis 3 - Format / Output Structure

Format entries define the visual and structural container. They specify headings, bullet depth, table layouts, section templates, and field ordering. Format is purely presentational and can be applied to any voice/tone/style combination.

### Seed Format Entries

| ID | Description |
|----|-------------|
| `adr` | Architecture Decision Record: Status, Context, Decision, Consequences |
| `daily-standup` | Three fields: Yesterday, Today, Blockers |
| `slack-thread` | Opening summary, threaded replies pattern, reaction-aware length |
| `technical-rfc` | Abstract, Motivation, Detailed Design, Drawbacks, Alternatives |
| `bullet-brief` | Flat bullet list with bold lead-ins; no prose paragraphs |

---

## How Composition Works

The `compose-instruction` skill reads one entry from each axis and assembles them into a single structured prompt prefix. The prefix has up to four sections - Voice, Tone (both from Axis 1), Style (Axis 2), and Format (Axis 3) - concatenated in that order.

Any axis can be omitted. If you only specify a voice and a format, the skill generates a two-section prefix. The composed instruction is designed to be prepended to any writing task without modification.

See [Compose an Instruction](../guides/compose-instruction.md) for a worked example.

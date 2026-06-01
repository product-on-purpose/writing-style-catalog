---
title: Compose an Instruction
description: Install the plugin, run compose-instruction, read the output, and use it in a prompt.
---

This guide walks through installing the plugin, running the `compose-instruction` skill, reading the output, and using it in a prompt.

---

## Step 1 - Install the Plugin

```bash
claude plugin install product-on-purpose/writing-style-library
```

After installation, the `writing-style-library:compose-instruction` skill is available in your Claude Code session. Confirm it loaded:

```bash
/writing-style-library:compose-instruction --help
```

---

## Step 2 - Run compose-instruction

The skill accepts keyword arguments for each axis. All arguments are optional.

### Basic example - voice and format only

```
/writing-style-library:compose-instruction voice=pragmatic-architect format=adr
```

### Full four-axis example

```
/writing-style-library:compose-instruction voice=pragmatic-architect tone=candid style=problem-solution format=adr
```

### Using a different combination

```
/writing-style-library:compose-instruction voice=product-thinker tone=optimistic-realist style=layered-disclosure format=daily-standup
```

---

## Step 3 - Read the Composed Output

The skill prints a structured prompt prefix. It looks like this (abbreviated):

```
[VOICE: pragmatic-architect]
You are a pragmatic architect. You reason from system constraints and name
trade-offs explicitly. You surface costs before benefits. You treat hand-waving
as a red flag...

[TONE: candid]
Deliver this message directly. Do not soften the diagnosis. State the situation
plainly...

[STYLE: problem-solution]
Structure your response as: first, a clear statement of the problem and its
root cause; second, the proposed solution with rationale; third, any caveats
or alternatives worth noting...

[FORMAT: adr]
Format as an Architecture Decision Record with these sections:
- Status: [Proposed | Accepted | Deprecated | Superseded]
- Context: ...
- Decision: ...
- Consequences: ...
```

Each section is self-contained. The sections are designed to stack without conflicts.

---

## Step 4 - Use the Composed Instruction

Prepend the composed instruction to your writing task. You can do this in three ways:

### Option A - Paste into system prompt

Copy the output and paste it as your system prompt in Claude.ai or your API call.

### Option B - Prepend to your user message

```
[paste composed instruction here]

---

Now write a decision record for our choice to migrate from REST to GraphQL.
```

### Option C - Use it as a Claude Code context file

Save the output to a file (for example `.writing-context.md`) and include it in your project's `CLAUDE.md` or reference it at the start of a session.

---

## Listing Available Entries

To see all available entries for a given axis:

```
/writing-style-library:compose-instruction --list voices
/writing-style-library:compose-instruction --list tones
/writing-style-library:compose-instruction --list styles
/writing-style-library:compose-instruction --list formats
```

---

## Common Combinations

| Use Case | Suggested Combination |
|----------|-----------------------|
| Technical decision record | `voice=pragmatic-architect tone=candid style=decision-log format=adr` |
| Daily async standup | `voice=ops-realist tone=candid style=step-by-step format=daily-standup` |
| User-facing feature announcement | `voice=product-thinker tone=energizing style=narrative-arc format=bullet-brief` |
| Incident post-mortem | `voice=ops-realist tone=cautious style=problem-solution format=technical-rfc` |
| Mentoring code review | `voice=technical-educator tone=mentoring style=layered-disclosure format=bullet-brief` |

See the [recipes/](../../recipes/) directory for more curated combinations with full worked examples.

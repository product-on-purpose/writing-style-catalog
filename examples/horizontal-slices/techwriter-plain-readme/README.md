# Recipe: techwriter-plain-readme

A composition of `technical-writer` voice, `matter-of-fact` tone, `diataxis-explanation` style, and `readme` format. Used for open-source project READMEs that put the reader's goal above the author's need to explain.

## When to use

You are writing the entry-point document for a software project - a library, CLI tool, or service - and your reader is an engineer who has never seen the project before. They have thirty seconds to decide whether this is worth their time. This recipe fits when the project does one thing well and the README's job is to make that one thing legible: what the project is, what problem it solves, and how to run it. It is the right tool for open-source READMEs, internal library entry points, and SDK landing pages where clarity outranks completeness.

## When to use something else

If the goal is to persuade a skeptical stakeholder rather than orient a new user, a `problem-solution` style in `executive` voice carries more rhetorical force. If the document needs to walk the reader through a multi-step procedure, the `diataxis-how-to` style is a better fit than explanation mode. If the audience already knows the project and needs a reference for flags and options, drop the explanation structure and write a reference page in `technical-writer` voice without the `readme` format container.

## Composition

| Axis | Entry | Why |
|------|-------|-----|
| Voice | `technical-writer` | Loyalty to the reader's goal, not the author's knowledge. Every sentence helps the reader accomplish something or explains why that information is necessary. No editorializing. |
| Tone | `matter-of-fact` | Declarative sentences. No intensifiers, no mood markers, no "powerful" or "seamless." The reader decides whether the project is interesting. |
| Style | `diataxis-explanation` | Builds a mental model first - what it is, why it is designed this way, what tradeoffs were made. The reader understands the project before they install it. |
| Format | `readme` | Single-sentence lead, short problem paragraph, install command, minimal usage example, links out for everything else. Optimized for a first-time visitor with limited attention. |

## Worked examples on this recipe

- [log-tail-cli - A CLI tool for tailing structured logs](log-tail-cli.md)
- [rate-limiter-lib - An open-source rate-limiter library](rate-limiter-lib.md)

# Recipe: mentor-encouraging-tutorial

A composition of `friendly-mentor` voice, `encouraging` tone, `how-to-tutorial` style, and `readme` format. Used for onboarding documentation aimed at early-career engineers who are doing each thing for the first time.

## When to use

Use this recipe when the reader is an engineer doing something for the first time and the obstacle is as much confidence as it is information. It fits onboarding READMEs, new-hire setup guides, first-contribution walkthroughs, and any procedural doc where a quick first success is more valuable than completeness. The recipe assumes the reader is capable but new, has the patience for short steps, and benefits from being told which moments usually feel hard.

## When to use something else

If the audience is an experienced engineer who wants the canonical procedure without scaffolding, swap `friendly-mentor` for `technical-writer` and `encouraging` for `matter-of-fact` so the doc reads as a reference, not a lesson. If the goal is to explain how a system works rather than to walk through a task, reach for `diataxis-explanation` instead of `how-to-tutorial`. If the document needs to live as a long-form lookup surface for many sub-procedures, use `technical-reference` rather than `readme`, which is built for first-time visitors and breaks down as it grows.

## Composition

| Axis | Entry | Why |
|------|-------|-----|
| Voice | `friendly-mentor` | Treats the reader as capable but new, scaffolds new concepts from familiar ones, and names the sticking points out loud rather than pretending they are not there. This is the voice of the best onboarding buddy a new hire ever had. |
| Tone | `encouraging` | The obstacle for a first-timer is often belief that they can do this at all. Encouraging tone names the real difficulty, then expresses genuine confidence in the reader's ability to get through it, without lapsing into cheerleading. |
| Style | `how-to-tutorial` | The reader arrived to complete a specific task. Prerequisites up front, one action per numbered step, a clear success signal at the end. The structure protects the reader from getting lost in their own first attempt. |
| Format | `readme` | The doc is the front door of a procedure. It is scanned before it is read, lives in a repo or a wiki, and uses code blocks, H2 sections, and short prose. It assumes the reader will skim first and follow along on a second pass. |

## Worked examples on this recipe

- [Your first pull request](first-pull-request.md)
- [Setting up your development environment](development-environment-setup.md)
- [Writing your first test](writing-your-first-test.md)

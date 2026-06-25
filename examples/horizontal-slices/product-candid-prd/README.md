# Recipe: product-candid-prd

A composition of `product-thinker` voice, `candid` tone, `problem-solution` style, and `prd` format. Used for writing product requirements documents that name the real user problem first, refuse to hide scope constraints or open questions, and arrive at a concrete remedy rather than a vague mandate.

## When to use

You are writing a PRD for a feature where the problem is real and documented but the solution scope is genuinely in question. This recipe fits when you need to earn alignment by showing the user pain first - not the roadmap priority or the eng estimate. It is the right tool for cross-functional review docs where design, engineering, and data are all reading and each has a different prior; for features that require explicit non-goals to prevent scope creep; and for cases where open questions must be surfaced rather than buried in a follow-up document. The candid tone carries the load when the problem has a hard cost (user churn, support volume, delayed activation) that the team needs to confront directly.

## When to use something else

If the decision is already made and you are communicating a launch plan, a `narrative-case-study` in `warm` tone reads better to a broad internal audience. If the feature is exploratory and the problem is not yet validated, a `hypothesis-and-test` style spike brief is the honest artifact - a PRD claims more certainty than you have. If the audience is a single engineer who already understands the problem, drop the format entirely and write a direct `operator` voice brief.

## Composition

| Axis | Entry | Why |
|------|-------|-----|
| Voice | `product-thinker` | Leads with the user problem, names who is experiencing it and what they are trying to do. Keeps every decision tethered to a customer outcome rather than an internal priority. |
| Tone | `candid` | A PRD that softens scope exclusions or buries open questions wastes reviewer time and invites misaligned engineering work. Candid tone names the hard constraints early. |
| Style | `problem-solution` | PRDs fail when they solve a generalized problem instead of the one they named. Problem-solution structure enforces the contract: the solution must answer the specific pain stated in the opening. |
| Format | `prd` | Structured sections (Problem Statement, Goals, Non-Goals, User Stories, Success Metrics, Open Questions) give cross-functional readers a predictable shape to scan and annotate. |

## Worked examples on this recipe

- [A notifications preferences center](notifications-preferences.md)
- [A self-serve data export feature](data-export.md)

---
entry_id: one-pager
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Two weeks is enough to get Priya shipping - run it deliberately

## Situation

Priya joined Monday. The team ships the backend daily and runs a regular on-call rotation. That cadence accelerates learning for engineers who have a lane; it overwhelms engineers who are navigating access, tooling, and codebase orientation simultaneously without a plan. Getting her to a real merged change by end of week two requires active choices now, not organic absorption.

## The Point

Own the two weeks as a plan, not a hope. Four things must happen:

- **Access and environment first, code second.** All credentials and permissions provisioned by Wednesday. Local environment running against the staging stack by Thursday. She cannot learn the codebase through error messages about missing access.
- **One named onboarding lead, not a rotating door.** Assign a single engineer to pair with her through the end of week two. Consistency of context matters more than distributed exposure at this stage.
- **A first ticket that is small and real.** Pull something from the backlog that is genuinely low-stakes but goes through the real deployment pipeline. A contrived exercise signals she is not trusted with the real work.
- **Explicit ownership map before she is on-call.** Walk her through who owns which services and how to escalate. This is a knowledge gap and a safety issue for the team.

## Why It Matters

- The first shipped change closes the "am I actually useful here" loop. Engineers who cross that threshold in the first two weeks anchor to the team differently than those who do not.
- On-call rotation arrives quickly on this team. A new engineer who does not know the ownership map is a risk to herself and to incident response.
- The daily ship cadence is an asset only if she can participate in it. Left unmanaged, it becomes background noise she cannot read.

## Recommendation

Today: name the onboarding lead. Wednesday: confirm all access is live. Thursday: select her first ticket together. End of week two: she merges and deploys it.

The lead owns the daily check-in and tracks blockers. The manager removes anything the lead cannot clear alone. Priya's job is to ask questions, not to silently struggle through uncertainty.

---

*Contact the team lead for blockers or to flag scope changes to the plan.*

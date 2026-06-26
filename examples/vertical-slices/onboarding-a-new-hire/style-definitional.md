---
entry_id: definitional
axis: style
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Productive onboarding is a bounded outcome, not a feeling: a new engineer completes her first two weeks productively if, and only if, she has shipped one real change to production under her own name. Everything else in those two weeks - the access setup, the codebase walkthroughs, the team introductions, the on-call shadowing - is in service of that one measurable crossing. The definition is precise enough to discriminate: two weeks of meeting attendance does not count; two weeks of reading docs does not count; two weeks of watching someone else commit work does not count.

## What the definition includes

The definition has three facets. First, access and tooling: Priya must be able to run the service, read the logs, open a pull request, and deploy without asking for credentials she does not have. Until this is true, nothing else matters, because she cannot act. Second, orientation sufficient to navigate: she does not need to understand the full system, but she must know which parts to touch for a given class of problem, who owns what she does not own, and how a change moves from her laptop to production. Third, the paired first change: a real ticket, small enough to be safe, large enough to traverse the full deploy cycle. Her name on the commit is not a ceremony; it is evidence that the first two facets worked.

## What the definition excludes

Three adjacent states are not productive onboarding, even when they feel like it.

Induction is not onboarding. Reading the handbook, completing required training, attending all-hands meetings: these satisfy compliance requirements, not the definition. A new engineer can finish every induction task and still be unable to ship.

Orientation is not onboarding. Deep architectural walkthroughs, codebase tours, and design reviews build context, but context alone does not cross the threshold. An engineer who knows where everything lives but has never deployed is not yet productive by this definition.

Belonging is not onboarding, but it is part of the goal. Priya should feel she belongs by the end of week two. That is a human outcome the plan must hold alongside the definitional one, and it fails separately if ignored. The team lunch, the direct introduction to the on-call rotation owner, the deliberate check-in at the midpoint: these are not decorative. But they do not substitute for the shipped change, and the shipped change does not substitute for them.

## The refined definition

Productive onboarding ends when a new engineer has shipped something real, and knows enough to ship the next thing herself. The first two weeks are productive if they produce both: the crossing, and the capability to cross again.

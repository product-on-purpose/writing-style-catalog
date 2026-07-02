---
entry_id: manifesto
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Nothing Broke. That Was the Work.

*A companion to the Project Halyard retrospective, and louder than a retrospective is built to be.*

The retrospective we filed for Project Halyard says, in its list of what did not go well, that the work was largely invisible to the rest of the organization. That line is accurate, filed correctly, and not enough. A bullet in a retro template will not change how this company sees fourteen months of work that produced zero incidents and zero features. This is the same point, said louder, in a document built for saying things without hedging.

Fourteen months ago we chose to rebuild checkout as a system running alongside the old one, after two earlier attempts to fix it in place had already stalled and been abandoned. The old system has sat in read-only archive since the cutover. The new one has carried this company's two highest-traffic periods without degrading. Not one customer ever noticed the changeover happen, and to most of the org, that looked like evidence that nothing had happened at all. Nothing happening is not nothing. It is the hardest outcome in this business to produce and the easiest one to overlook. Here is what we believe, now that we have done this once and intend to do it again.

## What we believe

**A system is proven by the load it carries, not the review it passes.** We did not trust our own rebuild until real checkout traffic was moving through it, cohort by cohort, starting at one percent. A design document earns a checkmark. Only production earns trust.

**We keep two ways home until one of them has earned the right to be the only way.** The old checkout stayed live and fully maintained for fourteen months, ready to take traffic back at any point. We did not decommission it until the new system had carried at least two peak-load periods without incident, exactly as we said we would. That cost real engineering time we could have spent elsewhere. We would spend it again.

**A launch date that moves because someone found a real bug is the system working, not the system failing.** Dani Rowe called the hold on the March launch when the pressure to hit that date was real and the bug behind it was not yet fully run down. That call cost three weeks. It was correct, and it was not the last hold we called.

**We ship when the system is ready, not when the calendar says so, and we do not call that a tradeoff against speed.** Holding that line through two slipped dates was the hardest discipline we kept, because nothing rewards it in the moment. Fourteen months is the receipt for building safety and speed at once, not an excuse for how long it took.

**The months nobody can see are not lesser work.** Shadow mode. Canary ramps. A contested regression-freeze call that Sam Wickfield held on June 9, when every hour of delay felt enormous. A dual on-call rotation that Dev Okonkwo and Marcus Ferreira carried for fourteen months with no real relief window. None of that produces a screenshot. It is the reason the cutover was boring, and boring was the entire point.

## What we stand against

We stand against the big-bang cutover with no way back, chosen because a real rollback path is expensive to build and easy to skip when nobody forces the question. We stand against treating a slipped date as an incident to explain rather than a save to credit. We stand against a planning process that only makes room for work it can see, so months of shadow testing lose the argument to a feature with a screenshot. And we stand against calling this kind of work invisible, as if invisibility were a property of the work itself and not a choice about what the organization bothered to look for.

## What we stand for

We stand for a rollback path that stays staffed and funded until the day it is formally retired, not a diagram that claims one exists. We stand for naming the people who made the boring outcome possible, out loud: Dev Okonkwo and Marcus Ferreira carried two live checkout systems for fourteen months so that carrying one badly was never a risk anyone had to take. We stand for crediting a hold as loudly as a launch, the way Dani Rowe's call in March belongs next to the cutover in June, not underneath it. We stand for a planning process that can fund months of nothing going wrong on purpose, the same way it funds a launch week.

## What we're taking into the next one

Project Halyard is not entirely finished. The legacy checkout comes down for good on July 14, once the archive window Sam Wickfield's freeze bought us runs out. We are writing this now because the next hard, multi-month, low-glory project in this company has not been named yet, and whoever draws it should not have to invent this doctrine from nothing, the way we did.

To whoever picks up that project: keep the old path funded until the new one has carried real load, not until a demo goes well. Name the number that earns your trust, the way we named one percent as a start and two clean peak-load periods as the bar for calling it done. Build the on-call relief rotation before the parallel run starts, not after four people carry it alone for a year. And to whoever funds it: fourteen months of nothing going wrong on purpose is not nothing. Fund the next one like you believe that, before an incident makes you believe it the hard way.

We ship when it is ready. Not when the calendar says so. That is the whole doctrine, and we intend to run it again.

- Yuki Tanaka, on behalf of the Halyard team

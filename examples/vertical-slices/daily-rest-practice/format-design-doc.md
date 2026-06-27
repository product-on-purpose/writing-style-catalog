---
entry_id: design-doc
axis: format
topic_slug: daily-rest-practice
topic_label: Reflecting on keeping a discipline of rest
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Rest Window Expansion Design Document

## Status

Draft

## Problem

The current rest window - phone in a drawer from Saturday at 8 p.m. through Sunday at 6 a.m. - is ten hours. It has been held for two consecutive weeks, and the data from those weeks is useful: a ten-hour window is long enough to produce a change in Monday's thinking, but the edges are losing most of the value.

Two failure points are visible.

**The entry boundary starts too late.** Saturday at 8 p.m. follows a full Saturday that runs on the same monitoring patterns as a workday. Rest begins after the readiness to rest has been eroded. The first hour or two of the window are spent in decompression rather than rest.

**The exit boundary is too abrupt.** When the phone comes back Sunday at 6 a.m., the first fifteen minutes involve scanning everything - inbox, notifications, ticket tracker, message queue. Whatever steadiness built up during the night compresses before the next week has started. The rest is ending before the rest day is over.

The next design must address both edges without introducing a third problem: expanding the window past the point where it can be held, or building an architecture so complex it becomes a productivity system in disguise.

**Constraints:**

- The window must anchor to recurring calendar signals that exist regardless of week content (sunset, morning, established meal times).
- Rules must be specifiable in advance, before the moment where rationalizing a check becomes easy. In-the-moment rule-setting fails.
- The pre-rest and post-rest protocols must complete in under fifteen minutes each. Longer protocols become preparation work, which defeats their purpose.
- The productivity accounting habit - the background process that tallies whether the rest was worth it - does not respond to direct attack. Any design that requires suppressing that habit as a precondition will fail.

## Proposed Design

### Window boundaries

The new window runs from Friday at sundown through Sunday at 7 p.m.

Sundown is used as the Friday start rather than a clock time because it shifts with season. The chosen signal is: close the laptop and put the phone in the dedicated drawer when the light through the west-facing window changes. This is a physical cue, not a calendar notification.

Sunday at 7 p.m. is chosen over Sunday morning because the status data shows the re-entry compression happens when the window closes before the rest day is done. Ending at 7 p.m. preserves the full day and allows a deliberate transition rather than an abrupt one.

### Physical protocol

The phone-in-drawer protocol extends to cover the laptop. Both devices go into the same physical location - the top drawer of the desk - not just out of reach but visually unavailable. The drawer is closed. One device exception: the household tablet is kept available for non-work use (reading, navigation, family coordination). It is not logged into work accounts and does not have notifications enabled for work systems.

### Pre-rest log (five minutes, Friday at sundown)

Before the window opens, write the following by hand, not typed:

1. What I expect to feel in the first two hours.
2. What I am most likely to rationalize as a necessary check.
3. The rule that governs that check - what I will do instead if the urge arrives.

This log is not reviewed during the rest period. It is read Sunday evening during the post-rest review to compare expectation against what actually happened.

### Post-rest review (fifteen minutes, Sunday at 7 p.m.)

When the window closes:

1. Read the pre-rest log.
2. Write two to three sentences on what happened versus what I expected.
3. Note one thing that helped and one thing that worked against the rest.
4. Cap the inbox scan at thirty minutes: no replies, triage only.

No productivity accounting. The purpose of the post-rest review is observational, not evaluative. The difference: observational asks "what happened?" Evaluative asks "was it worth it?" The second question is the one to block.

### Component summary

| Component | Trigger | Duration | Rule |
|-----------|---------|----------|------|
| Window open | Friday sundown (light cue) | - | Laptop and phone to drawer |
| Pre-rest log | At window open | 5 min | Write by hand, three prompts |
| Window close | Sunday 7 p.m. | - | Devices out of drawer |
| Post-rest review | At window close | 15 min | Read log, write observations |
| Inbox scan | After post-rest review | 30 min cap | No replies, triage only |

## Alternatives Considered

**Extend the current Saturday window incrementally.** Move the Saturday start from 8 p.m. to 6 p.m., then 4 p.m. in subsequent weeks. This solves the late-start problem without a structural change. It does not solve the Sunday re-entry compression. Rejected because two of the three identified failure points remain, and incremental extension has not moved the window in five weeks of trying.

**Add a mid-week half-day instead of extending the weekend window.** A Wednesday morning or afternoon window would distribute rest across the week rather than concentrating it at the weekend. Rejected because the two failure points are both boundary problems specific to the weekend window; a mid-week window introduces a new design without fixing the existing one. The existing window needs to work before a second one is added.

**Use app-blocking software to enforce the boundary.** Scheduled app blockers on the phone and laptop could enforce the window without relying on the physical drawer protocol. Rejected for two reasons: the physical cue creates a different relationship to the constraint than a software limit (software is defeatable with a tap and a reason); and the pre-rest log and physical protocol together are the behavior being designed, not just the absence of checking. Enforcement software would implement the absence without the behavior.

**Use a shorter, more frequent window.** One hour of complete silence each morning, every day. This is an entirely different practice and is worth designing separately. Rejected here because the data from weeks 1 through 14 shows that the quality change in Monday's thinking comes from a sustained break, not from accumulating shorter ones.

## Risks and Open Questions

**The productivity accounting habit will survive the new design.** The background process of tallying whether the rest was worth it is the largest identified risk. The post-rest review is designed to be observational rather than evaluative, but the accounting habit does not respond to design constraints - it runs underneath them. Working hypothesis: it resolves over time as evidence accumulates. The pre-rest log is intended to build that evidence base. Risk level: high. Mitigation: name the habit explicitly in the pre-rest log each week; track whether the observation changes over weeks.

**Friday evening carries different scheduling pressure than Saturday evening.** Friday often carries end-of-day processing that does not exist on Saturday. The sundown start may conflict with finishing commitments that have natural Friday deadlines. Mitigation: the rule is "sundown, unless a specific named commitment extends past sundown." The named commitment must be written in the pre-rest log. Unwritten commitments default to the window.

**What counts as rest within the window is still undefined in some areas.** Reading, walks, and cooking are clearly rest. Whether journaling counts as rest or as work-adjacent reflection is a judgment call that varies by day. Open question for the first three weeks: track whether each activity left the rest window feeling more or less intact. Do not legislate the answer in advance.

**The post-rest review may become the productivity accounting habit in a different form.** If the review expands or becomes increasingly analytical, it will recreate the problem it was designed to interrupt. Mitigation: the review has a hard cap of fifteen minutes and three fixed prompts. If the impulse to add to the review format appears, log it in the pre-rest log the following week rather than acting on it.

**Open question: whether the extended window changes Monday availability perceptibly.** The ten-hour window did not draw external comment. A forty-plus-hour window is a different surface area. Observe for the first four weeks before treating this as a design concern.

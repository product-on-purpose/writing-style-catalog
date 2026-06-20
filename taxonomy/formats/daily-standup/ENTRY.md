---
id: daily-standup
name: Daily Standup
axis: format
domain: professional
family: progress
one_liner: A brief daily status communication with three fixed sections - done, next, blockers. Surfaces information and flags what needs action. Not a progress report; a coordination tool.
description: |
  The daily standup is a coordination format, not a status report. The distinction matters.
  A status report demonstrates effort; a standup surfaces information that allows a team to
  respond. The three sections - what was done, what is next, what is blocking - are not
  prompts for comprehensive updates. They are prompts for the minimum information a team needs
  to know whether to act. Done and next are information; blockers are the only part that demands
  a response.

  The failure mode of the standup is treating it as an opportunity to demonstrate productivity.
  Long "done" sections, vague "next" sections, and absent blocker sections indicate the writer
  is performing effort rather than coordinating work. A well-written standup is short. The done
  section names completed items without narrating them. The next section names the next task, not
  a plan. The blocker section is either empty or states specifically what is blocked and what
  resolution would look like.

  Standup format works for both synchronous (spoken in a meeting) and asynchronous (written in
  a Slack channel or doc) contexts. The written async standup has the same structure but gains
  the additional obligation of being self-contained: the reader cannot ask a follow-up question
  in real time. Every blocker in an async standup should name what the writer needs, from whom,
  and with what urgency.
canonical_template: |
  **Done**
  - [Completed item - one line each]

  **Next**
  - [Next task or focus - one line each]

  **Blockers**
  - [What is blocked, what is needed, from whom - or "None"]
typical_voices:
  - operator
  - direct-communicator
typical_tones:
  - matter-of-fact
  - candid
digital_or_print: digital
pairs_well_with:
  - operator
  - direct-communicator
  - matter-of-fact
  - candid
avoid_with:
  - pastoral
  - columnist
  - devotional-reflection
  - warm
confusable_with:
  - meeting-notes
  - slack-message
when_to_use:
  - Daily coordination in a team that works in short cycles (sprints, weekly goals)
  - Async team updates when the team is distributed across time zones
  - Individual check-ins during a project sprint where visibility is important
  - Situations where blockers need to surface quickly and reliably to the right people
when_not_to_use:
  - Comprehensive project status updates that require context and narrative
  - End-of-sprint retrospectives or milestone summaries
  - Communication with stakeholders or external parties who need more context
  - Situations where the recipient needs to understand the work, not just the status
llm_instruction_phrasing: |
  Write as a daily standup update. Use exactly three sections: Done, Next, Blockers. Each
  section uses short bullet points, one item per line. Done covers completed work - name the
  item, do not narrate it. Next covers the immediate next task or focus. Blockers states what
  is blocked, what resolution is needed, and from whom - or the word "None" if there are no
  blockers. The entire update should fit in 10 lines or fewer. Do not include progress narratives,
  explanations of effort, or general context not needed for coordination.
tags:
  - standup
  - async
  - team-communication
  - short-form
  - coordination
  - blockers
  - digital
review_status: stable
---

## Daily Standup

The daily standup is a coordination format, not a status report. The distinction matters. A status report demonstrates effort; a standup surfaces information that allows a team to respond. The three sections - what was done, what is next, what is blocking - are not prompts for comprehensive updates. They are prompts for the minimum information a team needs to know whether to act. Done and next are information; blockers are the only part that demands a response.

The failure mode of the standup is treating it as an opportunity to demonstrate productivity. Long "done" sections, vague "next" sections, and absent blocker sections indicate the writer is performing effort rather than coordinating work. A well-written standup is short. The done section names completed items without narrating them. The next section names the next task, not a plan. The blocker section is either empty or states specifically what is blocked and what resolution would look like.

Standup format works for both synchronous (spoken in a meeting) and asynchronous (written in a Slack channel or doc) contexts. The written async standup has the same structure but gains the additional obligation of being self-contained: the reader cannot ask a follow-up question in real time. Every blocker in an async standup should name what the writer needs, from whom, and with what urgency.

### Canonical template

```
**Done**
- [Completed item - one line each]

**Next**
- [Next task or focus - one line each]

**Blockers**
- [What is blocked, what is needed, from whom - or "None"]
```

### When to use

The standup format belongs in daily team coordination - sprints, weekly goal cycles, or any rhythm where a team needs to know who is moving and where things are stuck. It works in synchronous stand-up meetings and in async Slack channels. The format is especially valuable when blockers need to surface reliably so the right person can respond without needing to ask for status.

### When not to use

Skip the standup format when the situation calls for context or narrative - end-of-sprint summaries, milestone updates, or communication with stakeholders who need to understand the work, not just the status. If the recipient cannot use the three-section structure to know whether to act, a different format serves better.

### Pairs well with

`operator`, `direct-communicator`, `matter-of-fact`, `candid`

### Often confused with

**meeting-notes**: Meeting notes capture the full outcomes of a specific meeting - decisions, assigned actions, open items - across any topic. A standup is a recurring short-form personal status update with a fixed three-section structure focused on coordination.

**slack-message**: A Slack message is a general-purpose channel communication that can take many forms and lengths. A standup is a specific format with a fixed three-part structure - it often lives in Slack, but the format constraint is tighter than the Slack message format allows for.

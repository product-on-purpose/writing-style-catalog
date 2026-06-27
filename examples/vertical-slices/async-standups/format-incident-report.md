---
entry_id: incident-report
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Incident Report: #team-standup Blocker Gap - Week 2, Day 11

## Status

Resolved - Day 11 of 30-day trial, 13:30 Pacific

## Summary

During Week 2 of the async standup trial, a blocked item posted to #team-standup with an @mention was not acted on during the on-call triage window. One engineer's work was delayed approximately 4 hours while waiting for a dependency to be resolved.

## Impact

- Services affected: #team-standup coordination channel; on-call blocker-response workflow
- Engineers affected: 1 engineer directly blocked; 1 dependent workstream stalled
- Duration: 09:15 Pacific to 13:30 Pacific (4 hours 15 minutes)

## Timeline

- 09:15 Pacific - Engineer posted standup update to #team-standup with an @mention flagging a blocked API integration dependency
- 09:45 Pacific - On-call triage window opened; on-call engineer began channel review
- 10:05 Pacific - On-call engineer completed triage pass without responding to the blocked item
- 11:30 Pacific - Blocked engineer escalated via direct message to on-call engineer
- 11:35 Pacific - On-call engineer located the missed @mention in the channel
- 11:40 Pacific - Blocker identified and resolved; affected engineer resumed work
- 13:30 Pacific - Dependent workstream confirmed unblocked; no further impact to other team members

## Root Cause

The on-call triage pass did not include a dedicated scan for @mentions. That morning's channel had 11 posts, several running significantly longer than the three-bullet format calls for - the same pattern flagged as at-risk in the Week 2 status update. The on-call engineer scanned the channel linearly and did not catch the @mention buried in a longer post. There was no secondary check or alert to catch missed mentions before the triage window closed.

## Resolution

The blocked engineer escalated via direct message. The on-call engineer located the original @mention within 5 minutes, identified the dependency, and provided the needed information in a thread reply. The engineer was unblocked and resumed work within 10 minutes of the direct-message escalation. No other engineers were affected after the gap was closed.

## Next Steps

- Add a dedicated @mention scan as a required step in the on-call triage checklist, implemented before the next triage window (Day 12 morning)
- Enforce the three-bullet post ceiling to reduce triage scan time: share two exemplar posts in the #team-standup pinned message and demo the format at the Thursday working session
- Review whether the on-call triage role needs an automated @mention alert at the Day 30 retro, particularly if post volume continues to rise as the team adds the two planned hires

---
entry_id: product-thinker
axis: voice
topic_slug: notifications-preferences
topic_label: A notifications preferences center
voice_id: product-thinker
tone_id: candid
style_id: problem-solution
format_id: prd
author_type: llm
llm_model: claude-sonnet-4-6
review_status: draft
---

# PRD: Notifications Preferences Center

## Problem Statement

Power users who rely on the platform daily are unsubscribing from all email notifications because we give them no middle option. When a user's inbox fills with low-signal alerts - a comment on a doc they are no longer watching, a digest of activity on a project they archived six months ago - they turn everything off at once. We lose signal delivery entirely for that user. Support data shows this pattern: 34% of users who contact support about "too many emails" have already set all notification preferences to off, and then later file a ticket because they missed a critical alert. The user is not asking for silence. They are asking for control we have not built.

## Goals

- Users can enable or disable notifications by category (mentions, comments, task assignments, digest summaries, system alerts) independently.
- Users can set a per-category delivery channel (email, in-app, or both).
- After the feature ships, the percentage of users with all email notifications disabled drops by at least 20% within 60 days.
- Critical alert delivery rate (measured by open rate on system alert emails) improves by at least 15% within 60 days.

## Non-Goals

- We are not building notification scheduling (quiet hours, timezone-aware batching). That is a follow-on scope item.
- We are not adding push notifications to this release. Push is a separate infrastructure investment.
- We are not retroactively changing the notification state for users who have already disabled everything. Migration logic is out of scope here; those users will see the new preferences UI with their current state reflected, and they can adjust from there.

## User Stories

- As a power user managing three active projects, I want to receive mention notifications without also receiving every comment on every document, so that my inbox contains only the alerts I actually need to act on.
- As a user who previously turned off all emails, I want to re-enable only system alerts without re-enabling digest summaries, so that I do not have to choose between missing critical messages and drowning in low-priority ones.
- As an account admin, I want to see the notification categories listed clearly so that I can help a teammate configure their preferences during onboarding without guessing what each toggle controls.

## Success Metrics

- 20% reduction in users with all email notifications disabled (measured at 60 days post-launch).
- 15% improvement in open rate for system alert emails (measured at 60 days post-launch).
- Support ticket volume for "too many notifications" or "missed notification" themes decreases by 25% within 90 days.
- Preferences page load time under 400ms at p95.

## Open Questions

- Do we give users a one-click "reset to recommended defaults" option? Recommended defaults are not defined yet. We need to decide what defaults look like before we can build the reset action.
- How do we handle notification preferences for users on a team plan where an admin may want to enforce certain categories? We do not have a clear policy on admin override vs. user autonomy. This needs a decision before we can finalize the data model.
- Should the preferences center surface a preview of what each category sends? A "last 3 examples" drawer would reduce support load but adds design and eng scope. Not in this PRD - flagging for the design review conversation.

---
entry_id: changelog-entry
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## [Week 2] - 2026-07-07

### Added
- First production change shipped by Priya: rate-limiter config update to the user-session service (#82)
- On-call shadow schedule published; Priya assigned to shadow Tariq's rotation 2026-07-14 through 2026-07-18 (#84)
- Service ownership reference added to RUNBOOK.md: maps each service to its primary and secondary owner (#83)
- Architecture review meeting invite extended to Priya as a regular attendee (#86)

### Changed
- Daily check-ins with onboarding buddy Tariq shifted to end-of-day 15-minute wrap; midday slot freed for independent ramp (#85)
- Priya's ticket-tracker role updated from Viewer to Contributor; can now create and assign tasks (#80)

### Fixed
- Staging environment permission gap corrected; Priya can now deploy to staging without a manual override (#81)

## [Week 1] - 2026-06-30

### Added
- Dev environment provisioned and smoke-tested by end of Day 1 using onboarding checklist v2.3 (#71)
- Access granted: code repository, ticket tracker, deployment pipeline, on-call alerting tool, internal wiki (#69)
- Onboarding buddy Tariq assigned; daily 30-minute check-in block scheduled through 2026-07-11 (#73)
- First pairing session completed: traced a recent incident from initial alert through to the postmortem (#74)
- Service dependency map reviewed in walkthrough; diagram linked from the team wiki home page (#72)
- Team lunch held on Day 3; Priya introduced to the broader org outside the engineering context (#75)
- Escalation paths for on-call documented in RUNBOOK.md with primary and secondary owner for each service tier (#76)

### Changed
- Team messaging channels updated: Priya added as full member to engineering, deploys, incidents, and social channels (#77)
- On-call rotation calendar shared in the team wiki with weekly primary listed through Q3 (#78)

### Fixed
- VPN credentials delayed two days due to IT provisioning queue; workaround (web-based repository access) documented in ONBOARDING.md for future hires (#70)

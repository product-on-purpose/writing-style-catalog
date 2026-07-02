---
entry_id: ad-copy
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Ad Copy - Notification Service Launch Campaign

**Campaign:** Notification Service, external launch
**Audience:** Engineering leads evaluating notification infrastructure vendors
**Timing:** Drafted for Priya's review, to go live once the Postgres path clears internal traffic (target 2026-05-29 per ADR-0023)

Four variations for testing across paid search, social, display, and lifecycle email before we commit spend to one angle. Ana signs off on the unit that names Postgres before it ships.

## Paid search (Google Ads)

**Headline:** Stop paging your team over notification uptime

**Body:** In-app, email, and Slack delivery from one API, built on infrastructure we have run in production for years.

**CTA:** See the docs

## Social (LinkedIn)

**Headline:** Your notification vendor shouldn't be your riskiest dependency

**Body:** Built on the database we know how to run at 2am. Sub-second p95 delivery across in-app, email, and Slack.

**CTA:** Book a demo

## Display (retargeting banner)

**Headline:** Notifications your users actually see in time

**CTA:** Start the integration

## Lifecycle email

**Subject line:** Your users get notified faster, starting now

**Preview text:** Sub-second delivery across in-app, email, and Slack, from infrastructure we have run for years, not infrastructure we are still testing.

**CTA:** Read the launch notes

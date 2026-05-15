---
entry_id: pragmatic-architect
axis: voice
topic_slug: rest-to-graphql
topic_label: Migrate from REST to GraphQL
voice_id: pragmatic-architect
tone_id: candid
style_id: decision-log
format_id: adr
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# ADR-0042: Migrate the Public API from REST to GraphQL Over Two Quarters

## Status

Accepted

## Context

We run a single REST API that serves a mobile client (iOS and Android) and a web client. The API has 137 endpoints and has grown organically over four years.

Three forces pushed this decision into the open:

**Mobile is paying for fields it does not use.** The mobile product surface is roughly 40% of the web surface, but the mobile client downloads on average 2.3x the JSON payload size per screen. The catalog endpoint alone returns 47 fields; mobile uses 11. On a metered connection in a market like India or Brazil, this is not academic - it is the difference between the app feeling fast and feeling broken.

**Web is paying for round-trips it does not need.** The web team's most-instrumented page, the order detail screen, currently makes 6 sequential REST calls before it can render. The waterfall is visible in our RUM data: median time-to-interactive on that screen is 1.8 seconds, and 1.1 of those seconds is round-trip latency. The web team has been compensating with backend-for-frontend (BFF) endpoints, and we now have 23 BFF endpoints that exist solely to denormalize REST responses for the web client. They are a parallel API by accident.

**The clients are diverging.** Mobile and web are asking for fundamentally different shapes of the same data. Every product feature now ships with two API changes: one for mobile, one for web. The cost is real and it is growing.

We considered three alternatives:

1. Stay on REST and invest in field-filtering at the endpoint level (sparse fieldsets). Cheaper. Does not solve the round-trip problem for web. Does not address the BFF sprawl.
2. Build out the BFF pattern formally - one BFF per client. Solves the shape problem. Doubles our API surface and the on-call burden that goes with it. Also displaces, rather than solves, the underfetching problem.
3. Migrate to GraphQL. Solves overfetching (clients query the exact shape they need) and underfetching (one request can resolve nested data). Comes with real costs we will name in Consequences.

## Decision

Migrate the public-facing API from REST to GraphQL over two quarters. Q3 stands up a GraphQL gateway in front of the existing REST API, with resolvers that fan out to current endpoints. Mobile cuts over to GraphQL for the catalog and order surfaces. Q4 migrates the remaining mobile surfaces and the web order detail page. The REST API remains available through end of Q1 next year for partner integrations, then is deprecated.

We are not federating across services. We have one backend; we will have one GraphQL schema. If we add services later, we will revisit Apollo Federation or a similar approach. We are not adopting it preemptively.

## Consequences

### Positive

- Mobile payload sizes drop. Based on a prototype against the catalog endpoint, we measured a 68% reduction in JSON size for the equivalent mobile query.
- Web order detail collapses from 6 sequential REST calls to 1 GraphQL request. Expected median TTI improvement on that screen is 600 to 900 milliseconds.
- The 23 BFF endpoints can be retired during Q4. The product engineers maintaining them get their time back.
- Future product features ship one API change instead of two.

### Negative

- We lose HTTP-layer caching. GraphQL queries are POST requests with bodies, and CDN caching of REST GETs has been doing real work for us - particularly for the catalog endpoint. We will need to implement persisted queries and a server-side response cache to recover this, and we will not fully match the current cache hit rate. Expect a measurable backend load increase during Q4.
- Query complexity becomes a live concern. A naive client can request a query that joins six tables and returns 10,000 rows. We will need query cost analysis and depth limits in production from day one. This is engineering work that REST did not require.
- The team's GraphQL expertise is uneven. Two engineers have shipped GraphQL in prior roles; the other seven have not. We will spend the first month of Q3 on training, paired implementation, and code review. This is real time off the roadmap.
- The mobile team has to ship a new networking layer. The existing REST client is well-instrumented and well-trusted. The new GraphQL client (we are using Apollo iOS / Apollo Android) is less mature in our codebase, and we will hit bugs we have not predicted.

### Neutral

- The REST API does not go away in Q3. We run both surfaces in parallel for two quarters. Operational complexity is temporarily higher.
- Schema design becomes a coordination point across mobile, web, and backend. We will introduce a schema review process. Some teams will find this slower than the current "add a field to the endpoint" workflow. Some teams will find it clarifying. Both reactions will be correct.
- Error handling shape changes. GraphQL returns errors in the response body alongside partial data, not as HTTP status codes. Client error handling will need to be rewritten. This is mechanical work, not conceptual difficulty.

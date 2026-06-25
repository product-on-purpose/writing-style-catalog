---
entry_id: technical-writer
axis: voice
topic_slug: rate-limiter-lib
topic_label: An open-source rate-limiter library
voice_id: technical-writer
tone_id: matter-of-fact
style_id: diataxis-explanation
format_id: readme
author_type: llm
llm_model: claude-sonnet-4-6
review_status: draft
---

# ratelimit

`ratelimit` is a token-bucket rate limiter for Node.js services that stores state in Redis so limits apply across multiple processes.

Rate limiting is the practice of capping how often a caller can invoke an operation within a time window. Without it, a single client - or a misconfigured retry loop - can exhaust a service's capacity and degrade it for every other caller. `ratelimit` implements the token-bucket algorithm because token buckets allow short bursts above the average rate while still enforcing a ceiling, which matches how well-behaved clients actually behave. A fixed-window counter rejects a client that makes 100 requests in the last second of one window and 100 more in the first second of the next, even though the burst lasted only two seconds. A token bucket does not.

The library stores each bucket's state in Redis rather than in process memory. This means limits are enforced consistently when your service runs as multiple replicas behind a load balancer. Each replica reads and writes the same bucket. The cost is a Redis round-trip on every check. If your service handles fewer than a few thousand limit checks per second, this cost is negligible. If it handles more, read the [performance notes](docs/performance.md) before deploying.

`ratelimit` does not make routing decisions. It returns a result object telling you whether the request is within the limit, how many tokens remain, and when the bucket next refills. What you do with that result - return a 429, shed load, queue the request - is your code's responsibility. This separation is intentional because rate-limiting policy is application-specific, and a library that assumes a web framework forces all non-web consumers to fight the abstraction.

## Install

```sh
npm install @acme/ratelimit
```

## Usage

```sh
# Requires a running Redis instance
REDIS_URL=redis://localhost:6379 node your-app.js
```

```js
import { RateLimiter } from '@acme/ratelimit';

const limiter = new RateLimiter({ redisUrl: process.env.REDIS_URL });

// 100 requests per minute per user
const result = await limiter.check({ key: `user:${userId}`, limit: 100, window: 60 });

if (!result.allowed) {
  res.status(429).json({ retryAfter: result.retryAfter });
  return;
}
```

## Docs

- [Configuration reference](docs/config.md)
- [Algorithm details](docs/algorithm.md)
- [Performance notes](docs/performance.md)

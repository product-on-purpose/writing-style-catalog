---
entry_id: changelog-entry
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## [3.0.0] - 2026-03-15

Complete replacement of the checkout flow after fourteen months of parallel development. The v2 flow remained live throughout; this release completes the traffic cutover and retires it.

Two launches slipped during this cycle. Priya Nakamura held the November launch when load tests revealed the race condition that became #752. Dani Reyes held the January launch when coupon edge-case testing surfaced #744. Theo Okafor kept v2 stable through both events. The March rollout ran at peak load without incident.

### Added

- New checkout flow serving 100% of purchase traffic, replacing the v2 flow in production (#712)
- Session-recovery step that restores abandoned carts when a shopper returns within 24 hours (#734)
- Address validation with real-time flagging of ambiguous entries before payment submission (#741)
- Inventory reservation held for the duration of checkout to prevent concurrent oversells (#756)
- Order confirmation page with full line-item breakdown and estimated delivery window (#763)
- Automated rollback trigger that monitors error rate and reverts the traffic split within 90 seconds if thresholds are breached (#769)

### Changed

- Cart state now persists across browser restarts and cross-device sign-ins for authenticated users (#722)
- Saved-card selection no longer triggers a full page reload (#748)
- Checkout session timeout extended from 20 minutes to 60 minutes; expiry now surfaces a warning dialog rather than silently resetting the cart (#758)
- Order number format changed from YYYYMMDD-NNNNN to UUID-v4 **[Breaking]** - downstream integrations must update before 2026-06-30; see migration guide (#771)

### Deprecated

- Legacy endpoints at `/checkout/v2/*` remain active until 2026-09-30, then removed; migrate to `/checkout/v3/*` (#780)

### Removed

- Anonymous guest checkout via session token (present since 2022); shoppers must sign in or use the new guest account flow (#782)

### Fixed

- Cart abandonment at the payment step - session state was lost on slow or interrupted connections and discarded silently; state is now written to the server on each step (#729)
- Coupon stacking edge case that produced a negative subtotal and allowed zero-cost order submissions (#744)
- Race condition under peak load that caused inventory checks to return stale data and permit oversells (#752)
- Payment gateway timeout shown as a generic error indistinguishable from a declined card - shoppers were retrying cards that had already been declined (#757)

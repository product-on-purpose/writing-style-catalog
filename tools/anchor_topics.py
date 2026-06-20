"""The anchor-topic pool: a frozen regression core and a growable seed pool.

Single source of truth for the two-tier anchor-topic model decided as D1 -
anchor topics (ADR 0017) and designed in
docs/internal/release-plans/plan_v0.3.0/anchor-topics.md. The catalog renders
every entry as worked samples on a shared set of anchor topics; holding the
topic constant is what lets a sample teach and a diff-pair vary exactly one axis.

Two tiers:

- The **frozen regression core**: the 3 existing topics, rendered on every CI by
  the C3 held-out reference set. It is the immovable distinguishability yardstick
  and grows only by a maintainer ADR (the gate spec's "versioned, not eternal"
  rule).
- The **growable seed pool**: the 12 designed topics (the core 3 plus 9 new),
  distributed 4 professional / 2 public / 2 personal / 2 ceremonial /
  2 contemplative. The E1 gate draws home topics from the pool for admission and
  breadth; new topics join only after the gate clears their renders, so the 12
  are a seed, not a hard cap.

Domain values are validated against tools/taxonomy.py (the single source for the
format domains); this module never re-defines the domain vocabulary. The 9 new
slugs stay renameable here until they enter the generator (decision D4).
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import taxonomy  # noqa: E402


@dataclass(frozen=True)
class AnchorTopic:
    """One anchor topic: its slug, a one-line label, its home domain, and
    whether it is a member of the frozen regression core."""
    slug: str
    label: str
    domain: str
    core: bool


# The designed seed slate (anchor-topics.md). Order is the designed topic order;
# `core=True` marks the 3 existing topics that double as the frozen regression
# core. Labels are the one-line descriptions from the slate table.
ANCHOR_TOPICS: tuple[AnchorTopic, ...] = (
    AnchorTopic("service-database-choice",
                "Choosing Postgres vs DynamoDB for a new service",
                "professional", core=True),
    AnchorTopic("async-standups",
                "Whether the team should move to async-first standups",
                "professional", core=True),
    AnchorTopic("roadmap-deprioritization",
                "Telling stakeholders a committed feature is being cut this quarter",
                "professional", core=False),
    AnchorTopic("onboarding-a-new-hire",
                "Getting a new engineer productive in their first two weeks",
                "professional", core=False),
    AnchorTopic("remote-work-policy",
                "Arguing a public position on return-to-office",
                "public", core=False),
    AnchorTopic("product-launch-announcement",
                "Announcing a new product to an outside audience",
                "public", core=False),
    AnchorTopic("morning-routine",
                "Designing a sustainable morning routine",
                "personal", core=True),
    AnchorTopic("thanking-a-mentor",
                "Writing to thank a mentor who shaped your career",
                "personal", core=False),
    AnchorTopic("retirement-send-off",
                "Marking a long-serving colleague's departure",
                "ceremonial", core=False),
    AnchorTopic("team-milestone-celebration",
                "Marking the team shipping a hard, long project",
                "ceremonial", core=False),
    AnchorTopic("daily-rest-practice",
                "Reflecting on keeping a discipline of rest",
                "contemplative", core=False),
    AnchorTopic("a-hard-year-in-review",
                "A personal year-end reckoning with a difficult year",
                "contemplative", core=False),
)

_BY_SLUG: dict[str, AnchorTopic] = {t.slug: t for t in ANCHOR_TOPICS}


def frozen_core() -> tuple[str, ...]:
    """The frozen regression-core slugs (rendered on every CI for C3)."""
    return tuple(t.slug for t in ANCHOR_TOPICS if t.core)


def seed_pool() -> tuple[str, ...]:
    """Every anchor-topic slug in the seed pool (the designed 12)."""
    return tuple(t.slug for t in ANCHOR_TOPICS)


def home_topics(domain: str) -> tuple[str, ...]:
    """The pool's topics native to a domain (the candidate's home substrate)."""
    return tuple(t.slug for t in ANCHOR_TOPICS if t.domain == domain)


def domain_of(slug: str) -> str | None:
    """The home domain of an anchor topic, or None if the slug is unknown."""
    topic = _BY_SLUG.get(slug)
    return topic.domain if topic else None


def label_of(slug: str) -> str | None:
    """The one-line label of an anchor topic, or None if the slug is unknown."""
    topic = _BY_SLUG.get(slug)
    return topic.label if topic else None


def is_anchor_topic(slug: str) -> bool:
    """Return True if `slug` is a member of the seed pool."""
    return slug in _BY_SLUG


def is_core(slug: str) -> bool:
    """Return True if `slug` is a member of the frozen regression core."""
    topic = _BY_SLUG.get(slug)
    return bool(topic and topic.core)


# ---------------------------------------------------------------------------
# Module self-check
# ---------------------------------------------------------------------------

_SLUG_RE = re.compile(r"^[a-z][a-z0-9-]*[a-z0-9]$")
_SEED_DISTRIBUTION: dict[str, int] = {
    "professional": 4, "public": 2, "personal": 2,
    "ceremonial": 2, "contemplative": 2,
}


def _self_check() -> None:
    """Verify internal consistency of the anchor-topic pool."""
    slugs = [t.slug for t in ANCHOR_TOPICS]
    assert len(set(slugs)) == len(slugs), "Duplicate anchor-topic slug"
    assert len(slugs) == 12, f"Expected 12 seed topics, got {len(slugs)}"

    for t in ANCHOR_TOPICS:
        assert _SLUG_RE.match(t.slug), f"Anchor-topic slug '{t.slug}' is malformed"
        assert taxonomy.is_valid_format_domain(t.domain), (
            f"Anchor-topic '{t.slug}' has unknown domain '{t.domain}'"
        )

    # The frozen core is a subset of the pool (true by construction) and is the
    # 3 existing topics.
    assert set(frozen_core()) <= set(seed_pool()), "Core is not a subset of the pool"
    assert set(frozen_core()) == {
        "service-database-choice", "async-standups", "morning-routine",
    }, "Frozen core is not the 3 existing topics"

    # The designed seed distribution is 4/2/2/2/2.
    counts = {d: len(home_topics(d)) for d in taxonomy.FORMAT_DOMAINS}
    assert counts == _SEED_DISTRIBUTION, (
        f"Seed distribution {counts} does not match {_SEED_DISTRIBUTION}"
    )

    print(f"ANCHOR_TOPICS: {len(ANCHOR_TOPICS)} topics "
          f"({len(frozen_core())} frozen core, {len(seed_pool())} pool)")
    for domain in taxonomy.FORMAT_DOMAINS:
        print(f"  {domain}: {', '.join(home_topics(domain))}")
    print("All internal consistency checks passed.")


if __name__ == "__main__":
    _self_check()

"""Tests for the anchor-topic pool (tools/anchor_topics.py).

Codifies the decided two-tier anchor-topic model (D1 - anchor topics / ADR 0017,
anchor-topics.md): a frozen regression core of 3 existing topics plus a growable
seed pool of 12, distributed 4 professional / 2 public / 2 personal /
2 ceremonial / 2 contemplative. The E1 gate's generator renders a candidate on
a home topic native to its domain; the frozen-regression renders on the core.
"""
import re
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

import anchor_topics as at  # noqa: E402
import taxonomy  # noqa: E402


# ---------------------------------------------------------------------------
# Tiers: frozen core and seed pool
# ---------------------------------------------------------------------------

def test_frozen_core_is_the_three_existing_topics():
    assert set(at.frozen_core()) == {
        "service-database-choice", "async-standups", "morning-routine",
    }


def test_seed_pool_has_twelve_topics():
    assert len(at.seed_pool()) == 12
    assert len(set(at.seed_pool())) == 12  # no duplicate slugs


def test_core_is_a_subset_of_the_pool():
    assert set(at.frozen_core()) <= set(at.seed_pool())


# ---------------------------------------------------------------------------
# Per-domain home topics and the 4/2/2/2/2 distribution
# ---------------------------------------------------------------------------

def test_home_topics_by_domain():
    assert set(at.home_topics("professional")) == {
        "service-database-choice", "async-standups",
        "roadmap-deprioritization", "onboarding-a-new-hire",
    }
    assert set(at.home_topics("public")) == {
        "remote-work-policy", "product-launch-announcement",
    }
    assert set(at.home_topics("contemplative")) == {
        "daily-rest-practice", "a-hard-year-in-review",
    }


def test_distribution_is_four_two_two_two_two():
    counts = {d: len(at.home_topics(d)) for d in taxonomy.FORMAT_DOMAINS}
    assert counts == {
        "professional": 4, "public": 2, "personal": 2,
        "ceremonial": 2, "contemplative": 2,
    }


def test_every_topic_domain_is_a_valid_taxonomy_domain():
    for slug in at.seed_pool():
        assert taxonomy.is_valid_format_domain(at.domain_of(slug))


# ---------------------------------------------------------------------------
# Accessors and predicates
# ---------------------------------------------------------------------------

def test_is_core_distinguishes_core_from_pool():
    assert at.is_core("morning-routine")          # existing core topic
    assert not at.is_core("roadmap-deprioritization")  # pool-only seed topic
    assert not at.is_core("not-a-topic")


def test_is_anchor_topic():
    assert at.is_anchor_topic("async-standups")
    assert at.is_anchor_topic("daily-rest-practice")
    assert not at.is_anchor_topic("the-color-blue")


def test_label_of():
    assert at.label_of("thanking-a-mentor") == \
        "Writing to thank a mentor who shaped your career"
    assert at.label_of("not-a-topic") is None


def test_domain_of_unknown_is_none():
    assert at.domain_of("not-a-topic") is None


def test_slugs_match_the_slug_pattern():
    pattern = re.compile(r"^[a-z][a-z0-9-]*[a-z0-9]$")
    for slug in at.seed_pool():
        assert pattern.match(slug), f"slug {slug!r} fails the slug pattern"


def test_self_check_passes():
    at._self_check()  # raises AssertionError on any internal inconsistency

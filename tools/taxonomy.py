"""Controlled vocabulary for catalog organization (Phase 1 codification).

This module is the single source of truth for the v2 taxonomy ratified as
decision A1 and codified in ADR 0010 (Accepted 2026-06-19):

- 5 format domains: professional, public, personal, ceremonial, contemplative.
  (`personal` is the renamed `relational` domain, widened to cover both its
  families per A1/Q2.)
- 17 format families, scoped to their domain.
- 5 voice families: expert, care, principal, witness, dissident. The proposed
  sixth family `pastoral` is folded into `care` as a subfamily (A1 grounding
  pass); see VOICE_SUBFAMILIES_BY_FAMILY.
- An optional third level, `subfamily`, enumerated only where splits have been
  designed (A3 defers a full naming pass).
- A governed 7-key faceted-tag enum (the demoted fifth axes).
- Per-family coverage bands (the A5 proposal) for the build-indexes ledger.

Schemas list the domain/family/subfamily values as optional enums; the cross-
field membership rule (family belongs to domain, subfamily belongs to family)
and the faceted-tag rule are enforced by tools/validate.py as warnings, per the
optional-then-tighten migration (decision F2). Nothing duplicates this module.
"""

from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# Format domains and families
# ---------------------------------------------------------------------------
#
# Format entries carry `domain` (one of FORMAT_DOMAINS) and `family` (one of
# FORMAT_FAMILIES_BY_DOMAIN[domain]). Family is scoped to the domain: a family
# name is meaningful only paired with its domain.

FORMAT_DOMAINS: tuple[str, ...] = (
    "professional",
    "public",
    "personal",
    "ceremonial",
    "contemplative",
)
"""The five controlled domain values for the format axis (ADR 0010 section 2).

`personal` is the renamed `relational` domain (A1/Q2), redefined to cover both
`correspondence` (written to someone the author knows) and `essay` (drawn from
the author's lived experience for a wider readership). The unifying thread is
the personal source of the writing, not the size of the audience.
"""


FORMAT_FAMILIES_BY_DOMAIN: dict[str, tuple[str, ...]] = {
    "professional": (
        "deliberation",
        "instruction",
        "progress",
        "brief",
        "appraisal",
        "messaging",
        "outreach",
        "response",
    ),
    "public": (
        "broadcast",
        "copy",
        "position",
        "accountability",
    ),
    "personal": (
        "correspondence",
        "essay",
    ),
    "ceremonial": (
        "tribute",
    ),
    "contemplative": (
        "devotion",
        "journal",
    ),
}
"""Per-domain controlled family values for the format axis (17 families).

Family names are scoped to their domain. A family population may grow within an
existing domain without a schema change. Adding a new family name re-cuts a
nearest-neighbor set and therefore requires an ADR and a version bump.
"""


# ---------------------------------------------------------------------------
# Voice families
# ---------------------------------------------------------------------------
#
# Voice entries carry `family` (one of VOICE_FAMILIES) but no `domain`: a
# speaker travels across spheres. Voice families are grounded by communicative
# function and validated by the adherence gate (ADR 0010 section 2a), not by a
# personality typology.

VOICE_FAMILIES: tuple[str, ...] = (
    "expert",
    "care",
    "principal",
    "witness",
    "dissident",
)
"""The five controlled family values for the voice axis (A1: `pastoral` folded
into `care`)."""


# ---------------------------------------------------------------------------
# Subfamilies (the optional third level)
# ---------------------------------------------------------------------------
#
# `subfamily` is optional until a family reaches 12 members, then required for
# every entry in that family (enforced by the cross-field check). Only splits
# that have been designed are enumerated here; A3 defers a full naming pass, so
# a family absent from these maps has no enumerated subfamilies yet and its
# subfamily values are not membership-checked.

VOICE_SUBFAMILIES_BY_FAMILY: dict[str, tuple[str, ...]] = {
    "care": ("pastoral",),
    "witness": ("chronicler",),
}
"""Named voice subfamilies. `care -> pastoral` is the fold target from A1; the
`pastoral` voice entry takes `family: care, subfamily: pastoral` at backfill."""

FORMAT_SUBFAMILIES_BY_FAMILY: dict[str, tuple[str, ...]] = {
    "instruction": ("reference", "tutorial"),
}
"""Named format subfamilies (the ADR 0010 worked example for `instruction`)."""


# ---------------------------------------------------------------------------
# Governed faceted-tag namespace
# ---------------------------------------------------------------------------
#
# Tags of the form `facet:value` are validated against this closed enum; the 7
# keys are the demoted fifth axes (ADR 0010 section 4). Values widen on demand
# (decision A4) without a schema change; the key set is fixed.

FACETS: dict[str, tuple[str, ...]] = {
    "channel": (
        "slack", "email", "linkedin", "op-ed", "print", "web",
        "podcast", "newsletter", "sms",
    ),
    "formality": ("1", "2", "3", "4", "5"),
    "modality": ("prose", "list", "dialogue", "table"),
    "epistemic": ("certain", "hedged", "exploratory"),
    "length": ("micro", "standard", "long"),
    "stance": ("advocate", "explain", "explore", "provoke"),
    "delivery": ("spoken", "written"),
}
"""The 7 governed facet keys and their seed value lists. Keys are a closed set;
values widen on demand (A4)."""

_FACET_TAG_RE = re.compile(r"^[a-z][a-z-]*:")


# ---------------------------------------------------------------------------
# Coverage bands (the A5 proposal, consumed by the build-indexes ledger)
# ---------------------------------------------------------------------------

DENSE_FAMILIES: frozenset[str] = frozenset({
    "instruction", "deliberation", "correspondence",
    "broadcast", "tribute", "devotion", "witness",
})
"""Families the inventory makes genuinely deep (A5 proposal). Dense families
target 12-20 members; everything else targets 3-8. Bands are a report input,
not a gate, and are tuned after the first fill."""

DENSE_BAND: tuple[int, int] = (12, 20)
NARROW_BAND: tuple[int, int] = (3, 8)


def coverage_band(family: str) -> tuple[int, int]:
    """Return the (min, max) target member band for a family."""
    return DENSE_BAND if family in DENSE_FAMILIES else NARROW_BAND


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def is_valid_format_domain(domain: str) -> bool:
    """Return True if `domain` is one of the controlled format domains."""
    return domain in FORMAT_DOMAINS


def is_valid_format_family(domain: str, family: str) -> bool:
    """Return True if `family` is valid within the given format `domain`.

    Returns False if the domain is itself invalid or if the family is not in
    that domain's controlled list.
    """
    return family in FORMAT_FAMILIES_BY_DOMAIN.get(domain, ())


def is_valid_voice_family(family: str) -> bool:
    """Return True if `family` is one of the controlled voice families."""
    return family in VOICE_FAMILIES


def is_valid_format_subfamily(family: str, subfamily: str) -> bool:
    """Return True if `subfamily` is an enumerated subfamily of a format family."""
    return subfamily in FORMAT_SUBFAMILIES_BY_FAMILY.get(family, ())


def is_valid_voice_subfamily(family: str, subfamily: str) -> bool:
    """Return True if `subfamily` is an enumerated subfamily of a voice family."""
    return subfamily in VOICE_SUBFAMILIES_BY_FAMILY.get(family, ())


def format_family_has_subfamilies(family: str) -> bool:
    """Return True if any subfamily has been designed for this format family."""
    return bool(FORMAT_SUBFAMILIES_BY_FAMILY.get(family))


def voice_family_has_subfamilies(family: str) -> bool:
    """Return True if any subfamily has been designed for this voice family."""
    return bool(VOICE_SUBFAMILIES_BY_FAMILY.get(family))


def is_faceted_tag(tag: str) -> bool:
    """Return True if `tag` is a faceted tag (matches `^[a-z][a-z-]*:`).

    Free-text tags (no facet prefix) are never validated.
    """
    return bool(_FACET_TAG_RE.match(tag))


def is_valid_facet_tag(tag: str) -> bool:
    """Return True if `tag` is a faceted tag whose facet and value are in the enum."""
    if not is_faceted_tag(tag):
        return False
    facet, _, value = tag.partition(":")
    return value in FACETS.get(facet, ())


def all_format_families() -> tuple[str, ...]:
    """Return the flat tuple of every format family across every domain.

    Family names are scoped to their domain, so the flat tuple is used only for
    a schema-level enum; membership is enforced per-domain by the validator.
    """
    families: list[str] = []
    for fams in FORMAT_FAMILIES_BY_DOMAIN.values():
        families.extend(fams)
    return tuple(families)


# ---------------------------------------------------------------------------
# Module self-check
# ---------------------------------------------------------------------------

def _self_check() -> None:
    """Verify internal consistency of the controlled vocabularies."""
    for key in FORMAT_FAMILIES_BY_DOMAIN:
        assert key in FORMAT_DOMAINS, (
            f"FORMAT_FAMILIES_BY_DOMAIN has key '{key}' not in FORMAT_DOMAINS"
        )
    for domain in FORMAT_DOMAINS:
        assert FORMAT_FAMILIES_BY_DOMAIN.get(domain), f"Domain '{domain}' has no families"
    assert len(set(FORMAT_DOMAINS)) == len(FORMAT_DOMAINS), "Duplicate format domain"
    assert len(set(VOICE_FAMILIES)) == len(VOICE_FAMILIES), "Duplicate voice family"
    # Format family names are globally unique across domains (the flat enum needs this).
    flat = all_format_families()
    assert len(set(flat)) == len(flat), "Duplicate format family name across domains"
    # Every designed subfamily hangs off a real family.
    for fam in FORMAT_SUBFAMILIES_BY_FAMILY:
        assert fam in flat, f"Format subfamily parent '{fam}' is not a family"
    for fam in VOICE_SUBFAMILIES_BY_FAMILY:
        assert fam in VOICE_FAMILIES, f"Voice subfamily parent '{fam}' is not a voice family"

    total_format_families = len(flat)
    print(f"FORMAT_DOMAINS: {len(FORMAT_DOMAINS)}")
    print(
        f"FORMAT_FAMILIES_BY_DOMAIN: {total_format_families} families "
        f"across {len(FORMAT_FAMILIES_BY_DOMAIN)} domains"
    )
    print(f"VOICE_FAMILIES: {len(VOICE_FAMILIES)}")
    print(f"FACETS: {len(FACETS)} keys")
    print("All internal consistency checks passed.")


if __name__ == "__main__":
    _self_check()

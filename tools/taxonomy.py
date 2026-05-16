"""
Controlled vocabulary for catalog organization (Phase 2 prep work).

This module defines the proposed `domain` and `family` controlled vocabularies
for the format and voice axes, as specified in:
- docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md
- docs/internal/_working/0010-domain-and-family-organization.md

Status: drafted but not yet wired into schemas or validators. Pending ADR 0010
approval. Once approved, tools/validate.py imports from this module to enforce
domain/family controlled vocabularies against entry frontmatter.

The module is importable in its current state but has no side effects on
validation or build behavior unless explicitly used.

Reference: design spec at docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Format domains and families
# ---------------------------------------------------------------------------
#
# Format entries get both `domain` (required, one of FORMAT_DOMAINS) and
# `family` (required, one of FORMAT_FAMILIES_BY_DOMAIN[domain]). The family
# is scoped to the domain - a family name in one domain has no meaning in
# another.

FORMAT_DOMAINS: tuple[str, ...] = (
    "engineering",
    "business",
    "workplace",
    "publication",
    "ceremonial",
    "contemplative",
)
"""The six controlled domain values for the format axis.

See docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md
section "Domain - the 6 values, fully defined" for the full definition
of each value, including fits-when and does-not-fit-when criteria.
"""


FORMAT_FAMILIES_BY_DOMAIN: dict[str, tuple[str, ...]] = {
    "engineering": (
        "decision-documents",
        "reference-and-onboarding",
        "status",
    ),
    "business": (
        "briefs-and-proposals",
        "status-and-updates",
        "feedback",
    ),
    "workplace": (
        "quick-communication",
        "meetings",
        "onboarding",
    ),
    "publication": (
        "long-form",
        "social-posts",
        "spoken-and-show-notes",
    ),
    "ceremonial": (
        "toasts-and-tributes",
    ),
    "contemplative": (
        "devotional-writing",
    ),
}
"""Per-domain controlled family values for the format axis.

Family names are scoped to their domain. "status" in engineering and
"status-and-updates" in business are deliberately different names to
avoid global collision.

Family populations may grow within an existing domain without schema
change. Adding a new family name requires an ADR amendment.
"""


# ---------------------------------------------------------------------------
# Voice families
# ---------------------------------------------------------------------------
#
# Voice entries get `family` (required, one of VOICE_FAMILIES) but NOT
# `domain`. Voices travel across domains by nature - a journalist voice
# can write for engineering or business audiences. Imposing a domain on
# voices would constrain real flexibility.

VOICE_FAMILIES: tuple[str, ...] = (
    "technical-and-expert",
    "people-and-coaching",
    "authority",
    "narrative-and-media",
    "spiritual",
)
"""The five controlled family values for the voice axis at 15 entries.

Expected to expand to six or seven families as the catalog grows to 30
voices in Phase 3. Candidate additions: "insider-and-outsider" for
voices like insider-confidant, outsider, witness.
"""


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def is_valid_format_domain(domain: str) -> bool:
    """Return True if `domain` is one of the controlled format domains."""
    return domain in FORMAT_DOMAINS


def is_valid_format_family(domain: str, family: str) -> bool:
    """Return True if `family` is valid within the given format `domain`.

    Returns False if the domain is itself invalid or if the family is not
    in that domain's controlled list.
    """
    return family in FORMAT_FAMILIES_BY_DOMAIN.get(domain, ())


def is_valid_voice_family(family: str) -> bool:
    """Return True if `family` is one of the controlled voice families."""
    return family in VOICE_FAMILIES


def all_format_families() -> tuple[str, ...]:
    """Return the flat tuple of every format family across every domain.

    Useful for downstream consumers that want to iterate every family
    without nesting by domain. Family names are scoped to their domain,
    so the flat tuple may not be globally unique - callers that need
    uniqueness should iterate FORMAT_FAMILIES_BY_DOMAIN directly.
    """
    families: list[str] = []
    for fams in FORMAT_FAMILIES_BY_DOMAIN.values():
        families.extend(fams)
    return tuple(families)


# ---------------------------------------------------------------------------
# Module self-check
# ---------------------------------------------------------------------------

def _self_check() -> None:
    """Verify internal consistency of the controlled vocabularies.

    Called from `python -m tools.taxonomy` to confirm the module loads
    cleanly and the data structures cross-reference correctly.
    """
    # Every key in FORMAT_FAMILIES_BY_DOMAIN must be in FORMAT_DOMAINS.
    for key in FORMAT_FAMILIES_BY_DOMAIN:
        assert key in FORMAT_DOMAINS, (
            f"FORMAT_FAMILIES_BY_DOMAIN has key '{key}' not in FORMAT_DOMAINS"
        )
    # Every domain in FORMAT_DOMAINS must have at least one family.
    for domain in FORMAT_DOMAINS:
        families = FORMAT_FAMILIES_BY_DOMAIN.get(domain, ())
        assert families, f"Domain '{domain}' has no families"
    # No duplicate domains or voice families.
    assert len(set(FORMAT_DOMAINS)) == len(FORMAT_DOMAINS), "Duplicate format domain"
    assert len(set(VOICE_FAMILIES)) == len(VOICE_FAMILIES), "Duplicate voice family"

    print(f"FORMAT_DOMAINS: {len(FORMAT_DOMAINS)}")
    print(f"FORMAT_FAMILIES_BY_DOMAIN: {sum(len(v) for v in FORMAT_FAMILIES_BY_DOMAIN.values())} families across {len(FORMAT_FAMILIES_BY_DOMAIN)} domains")
    print(f"VOICE_FAMILIES: {len(VOICE_FAMILIES)}")
    print("All internal consistency checks passed.")


if __name__ == "__main__":
    _self_check()

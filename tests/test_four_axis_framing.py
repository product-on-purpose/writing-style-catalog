"""Guards the four-axis framing decided in ADR 0018.

The model was described two ways for six months: "four orthogonal axes" in the
marketplace listing and QUICKSTART, "three-axis model" in the README, AGENTS.md,
and on the published site. Both ADR 0001 and ADR 0004 predicted that drift in
their own Negative consequences and proposed the same mitigation, a parenthetical
in every document that mentions the model. That mitigation depended on perpetual
discipline and it failed.

These tests replace the discipline with a check. A reintroduced "three-axis" or a
stale "Axis 1 - Voice & Tone" fails the suite instead of quietly shipping.

Deliberately NOT covered:
  - CHANGELOG.md and the dated strategy/research snapshots, which are historical
    records and were accurate when written.
  - schemas/*.json description annotations, which still carry Axis 1/2/3 wording.
    ADR 0018 decision 5 defers those to the schema-freeze change policy rather
    than inventing an annotation-only exception to the AGENTS.md rule requiring a
    version bump for any schemas/ edit. test_schema_annotations_are_the_known_gap
    below pins that as a KNOWN gap, so it is visible rather than forgotten, and it
    is the test to flip when the policy lands.
"""
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

# Surfaces a user or contributor actually reads.
GUARDED_FILES = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "QUICKSTART.md",
    "CONTRIBUTING.md",
    "ROADMAP.md",
    ".claude-plugin/plugin.json",
    "site/package.json",
    "site/src/content/docs/index.mdx",
    "site/src/content/docs/concepts/four-axis-model.md",
    "site/src/content/docs/concepts/glossary.md",
]

# Wording that asserts the superseded three-axis grouping. Each pattern is the
# claim itself, not a mention of it: a sentence explaining that the label USED to
# be three-axis is correct and must stay allowed.
STALE_CLAIMS = [
    r"three orthogonal axes",
    r"the catalog has three axes",
    r"one of the three orthogonal dimensions",
    r"(?:are|as) (?:two )?(?:distinct )?dimensions (?:with)?in (?:the )?(?:first|one|the same) (?:conceptual )?axis",
    r"part of the same conceptual axis",
    r"belong to the same conceptual axis",
    r"Axis 1 - Voice (?:and|&) Tone",
    r"Axis 2 - Style",
    r"Axis 3 - Format",
    r"The Three-Axis (?:Model|Taxonomy)",
]

# Phrases that legitimately contain "three axes" under a four-axis model: holding
# three constant and varying the fourth is the model's own test.
ALLOWED_THREE = [
    "the other three axes",
    "three axes and the topic constant",
    "hold three axes",
    "three axes open",
    "other three",
]


def _files():
    return [p for p in (REPO_ROOT / f for f in GUARDED_FILES) if p.exists()]


@pytest.mark.parametrize("pattern", STALE_CLAIMS)
def test_no_stale_three_axis_claim_in_guarded_surfaces(pattern):
    rx = re.compile(pattern, re.IGNORECASE)
    offenders = []
    for path in _files():
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not rx.search(line):
                continue
            # A line describing the历史 rename is fine; a line asserting it is not.
            if re.search(r"earlier (?:docs|versions)|ADR 0018|used to|formerly|previously|no longer",
                         line, re.IGNORECASE):
                continue
            offenders.append(f"{path.relative_to(REPO_ROOT)}:{n}: {line.strip()[:110]}")
    assert not offenders, (
        f"Superseded three-axis framing reintroduced (ADR 0018 names the model four-axis):\n"
        + "\n".join(offenders)
    )


def test_guarded_surfaces_actually_exist():
    """A renamed or moved file must not silently drop out of the guard list."""
    missing = [f for f in GUARDED_FILES if not (REPO_ROOT / f).exists()]
    assert not missing, f"guard list references files that do not exist: {missing}"


def test_concepts_page_is_named_four_axis():
    assert (REPO_ROOT / "site/src/content/docs/concepts/four-axis-model.md").exists()
    assert not (REPO_ROOT / "site/src/content/docs/concepts/three-axis-model.md").exists()


def test_old_concepts_route_still_redirects():
    """ADR 0018 keeps the old published URL resolving; route parity depends on it."""
    config = (REPO_ROOT / "site/astro.config.mjs").read_text(encoding="utf-8")
    assert "redirects:" in config
    assert "/concepts/three-axis-model" in config
    assert "four-axis-model" in config


def test_readme_anchors_match_its_headings():
    """The TOC and badge links point at generated heading anchors; a rename breaks them."""
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    headings = re.findall(r"^#{2,3} (.+)$", readme, re.MULTILINE)

    def slug(text):
        """Mimic GitHub's heading-anchor slug.

        Note GitHub replaces each space with its own hyphen rather than collapsing
        runs, so "Axis 3 - Style / Mode / Genre" becomes
        "axis-3---style--mode--genre" once the slashes are stripped. Collapsing
        runs here would report the repo's correct anchors as broken.
        """
        s = text.lower().strip()
        s = re.sub(r"[^\w\s-]", "", s)
        return s.replace(" ", "-")

    available = {slug(h) for h in headings}
    referenced = set(re.findall(r"\(#([a-z0-9-]+)\)", readme)) | set(
        re.findall(r'href="#([a-z0-9-]+)"', readme)
    )
    # readme-top is an explicit <a id>, not a heading.
    referenced.discard("readme-top")
    broken = sorted(r for r in referenced if r not in available)
    assert not broken, f"README links to anchors with no matching heading: {broken}"


def test_all_four_axes_have_a_section_in_the_concepts_page():
    text = (REPO_ROOT / "site/src/content/docs/concepts/four-axis-model.md").read_text(
        encoding="utf-8"
    )
    for n, axis in enumerate(["Voice", "Tone", "Style", "Format"], 1):
        assert re.search(rf"^## Axis {n} - {axis}", text, re.MULTILINE), (
            f"concepts page is missing '## Axis {n} - {axis}'"
        )


def test_schema_annotations_are_the_known_gap():
    """Pins ADR 0018 decision 5. Flip this when the schema-freeze policy lands.

    Asserting the gap EXISTS keeps it honest in both directions: if someone fixes
    the annotations without the governance decision, this fails and points them at
    the rule; when the policy authorises the edit, this test is deleted alongside
    it. Either way the gap cannot be silently forgotten.
    """
    stale = []
    for name in ("entry.universal", "voice", "tone", "style", "format"):
        path = REPO_ROOT / "schemas" / f"{name}.schema.json"
        if re.search(r"Axis [123]", path.read_text(encoding="utf-8")):
            stale.append(name)
    assert stale, (
        "schemas/ no longer carries Axis 1/2/3 wording. If that was intentional and "
        "the schema-freeze change policy now authorises annotation-only edits, delete "
        "this test and update ADR 0018 decision 5 plus the backlog S3 note."
    )

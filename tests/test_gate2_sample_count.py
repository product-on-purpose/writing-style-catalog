"""Tests for Gate 2 - the SAMPLE-COUNT check in tools/validate.py.

The adherence-gate spec's Gate 2 has two halves: pedagogical-field substance
(check_pedagogical_bar) and a minimum SAMPLE COUNT - every admitted entry
rendered on all 12 seed-pool anchor topics ("12 samples per entry"). Once
deferred ("samples are not in ENTRY.md, so this rides the model-calling gate
build"), it is now a static, deterministic invariant because the matrix is
rendered into examples/vertical-slices/. check_sample_count enforces it for
stable / reference-quality entries; draft / reviewed / deprecated are exempt.

id_map maps entry ID -> (axis, frontmatter_dict).
"""
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

import validate  # noqa: E402
import anchor_topics  # noqa: E402

TOPICS = anchor_topics.seed_pool()

# The gate spec's "12 samples per entry" is the load-bearing number. Lock the
# exact pool here so an accidental add/drop in anchor_topics.py is caught loudly
# rather than silently changing what the sample-count gate requires.
EXPECTED_TOPICS = {
    "service-database-choice", "async-standups", "roadmap-deprioritization",
    "onboarding-a-new-hire", "remote-work-policy", "product-launch-announcement",
    "morning-routine", "thanking-a-mentor", "retirement-send-off",
    "team-milestone-celebration", "daily-rest-practice", "a-hard-year-in-review",
}


def test_anchor_pool_is_exactly_the_twelve():
    assert len(TOPICS) == 12
    assert set(TOPICS) == EXPECTED_TOPICS


def _make_slices(root: Path, axis: str, entry_id: str, topics):
    """Create vertical-slice files for `entry_id` on the given topics under root."""
    for t in topics:
        d = root / t
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{axis}-{entry_id}.md").write_text("---\n---\nbody\n", encoding="utf-8")


def test_admitted_entry_with_all_samples_passes(tmp_path):
    _make_slices(tmp_path, "voice", "operator", TOPICS)
    id_map = {"operator": ("voice", {"review_status": "stable"})}
    assert validate.check_sample_count(id_map, vslices_dir=tmp_path) == []


def test_admitted_entry_missing_a_sample_errors(tmp_path):
    _make_slices(tmp_path, "voice", "operator", TOPICS[:-1])  # all but one topic
    id_map = {"operator": ("voice", {"review_status": "stable"})}
    errors = validate.check_sample_count(id_map, vslices_dir=tmp_path)
    assert len(errors) == 1
    assert errors[0].startswith("[ERROR]")
    assert TOPICS[-1] in errors[0]
    assert "operator" in errors[0]


def test_reference_quality_is_also_admitted(tmp_path):
    _make_slices(tmp_path, "tone", "candid", TOPICS[:-1])
    id_map = {"candid": ("tone", {"review_status": "reference-quality"})}
    assert len(validate.check_sample_count(id_map, vslices_dir=tmp_path)) == 1


def test_draft_entry_is_exempt(tmp_path):
    # no slices at all, but draft -> exempt (a Stream-B candidate not yet rendered)
    id_map = {"newvoice": ("voice", {"review_status": "draft"})}
    assert validate.check_sample_count(id_map, vslices_dir=tmp_path) == []


def test_reviewed_and_deprecated_are_exempt(tmp_path):
    id_map = {
        "a": ("voice", {"review_status": "reviewed"}),
        "b": ("voice", {"review_status": "deprecated"}),
    }
    assert validate.check_sample_count(id_map, vslices_dir=tmp_path) == []


def test_real_catalog_passes():
    """The real catalog's admitted entries each render on all 12 anchor topics
    (the matrix is complete), so the check finds no violations."""
    _, id_map = validate.check_frontmatter_parseable()
    assert id_map, "expected the real catalog to load"
    errors = validate.check_sample_count(id_map)
    assert errors == [], f"unexpected sample-count violations: {errors}"

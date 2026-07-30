"""Executable checks for the schema change policy in ADR 0019.

The policy's central claim is that class A keywords (`title`, `description`,
`$comment`, `examples`) cannot change a validation verdict, while the keywords
routed to class C can. An adversarial review of the first draft found the
opposite failure: the draft classified edits by whether the 117 entries in this
repo still passed, which would let `additionalProperties: false` or a narrowed
`$ref` ship as annotation-only because nothing local happened to break.

So these tests deliberately validate documents that are NOT in the catalog. A
minimal synthetic entry is mutated one keyword at a time, and the assertion is
about which mutations move the verdict.

What this does NOT do is classify a real PR. That is a human reading ADR 0019.
This pins the premise the policy rests on, so if a future JSON Schema draft bump
makes `format` assertive by default, or makes a class A keyword meaningful, the
suite says so instead of the policy quietly becoming false.
"""
import copy
import json
from pathlib import Path

import jsonschema
import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = REPO_ROOT / "schemas"

FROZEN = ["entry.universal", "voice", "tone", "style", "format", "example"]
UNFROZEN = ["diff-pair"]

# Keywords ADR 0019 puts on the class A allowlist.
CLASS_A_KEYWORDS = ["title", "description", "$comment", "examples"]


def load(name):
    return json.loads((SCHEMAS / f"{name}.schema.json").read_text(encoding="utf-8"))


# A document that is not in the catalog and never will be.
SYNTHETIC = {
    "type": "object",
    "properties": {"kept": {"type": "string"}},
    "required": ["kept"],
}
DOC = {"kept": "value", "extra": "not declared by the schema"}


def validates(schema, doc):
    try:
        jsonschema.validate(instance=doc, schema=schema)
        return True
    except jsonschema.ValidationError:
        return False


# ---------------------------------------------------------------------------
# The premise class A rests on
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("keyword", CLASS_A_KEYWORDS)
def test_class_a_keywords_cannot_change_a_verdict(keyword):
    """If any of these ever becomes assertive, class A is no longer safe."""
    before = validates(SYNTHETIC, DOC)
    mutated = copy.deepcopy(SYNTHETIC)
    mutated[keyword] = ["anything"] if keyword == "examples" else "anything"
    assert validates(mutated, DOC) == before, (
        f"{keyword} changed a validation verdict; ADR 0019 lists it as class A "
        "(annotation-only). The policy needs revisiting."
    )


def test_required_array_order_is_not_observable():
    """ADR 0019 allows reordering `required` as class A because it is a set."""
    schema = {"type": "object", "required": ["a", "b"], "properties": {}}
    reordered = {"type": "object", "required": ["b", "a"], "properties": {}}
    doc = {"a": 1, "b": 2}
    partial = {"a": 1}
    assert validates(schema, doc) == validates(reordered, doc)
    assert validates(schema, partial) == validates(reordered, partial)


# ---------------------------------------------------------------------------
# The premise class C rests on: these DO move verdicts
# ---------------------------------------------------------------------------

def test_additional_properties_false_is_a_real_break():
    """The motivating example. Verdict-neutral locally, breaking in general."""
    assert validates(SYNTHETIC, DOC)
    tightened = {**copy.deepcopy(SYNTHETIC), "additionalProperties": False}
    assert not validates(tightened, DOC), (
        "additionalProperties: false did not reject an undeclared property; the "
        "class C justification in ADR 0019 assumes it does"
    )


def test_narrowing_an_enum_is_a_real_break():
    wide = {"type": "object", "properties": {"axis": {"enum": ["voice", "tone", "style", "format"]}}}
    narrow = {"type": "object", "properties": {"axis": {"enum": ["voice", "tone"]}}}
    doc = {"axis": "format"}
    assert validates(wide, doc)
    assert not validates(narrow, doc)


def test_promoting_optional_to_required_is_a_real_break():
    optional = {"type": "object", "properties": {"family": {"type": "string"}}}
    required = {**optional, "required": ["family"]}
    doc = {}
    assert validates(optional, doc)
    assert not validates(required, doc)


# ---------------------------------------------------------------------------
# Freeze scope, as decided in ADR 0019 decision 1
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("name", FROZEN + UNFROZEN)
def test_every_schema_parses_and_is_a_valid_schema(name):
    schema = load(name)
    jsonschema.Draft202012Validator.check_schema(schema)


def test_freeze_scope_matches_the_files_on_disk():
    """A new schema file must be classified by ADR 0019, not silently ungoverned."""
    on_disk = sorted(p.name.replace(".schema.json", "") for p in SCHEMAS.glob("*.schema.json"))
    assert on_disk == sorted(FROZEN + UNFROZEN), (
        "schemas/ contents changed. Add the new schema to the frozen or unfrozen list "
        "in ADR 0019 decision 1, then update this test."
    )


def test_per_axis_schemas_compose_the_shared_one():
    """Why a change to entry.universal is class C for every axis schema."""
    composing = []
    for name in ("voice", "tone", "style", "format"):
        text = (SCHEMAS / f"{name}.schema.json").read_text(encoding="utf-8")
        if "entry.universal.schema.json" in text:
            composing.append(name)
    assert composing, (
        "no per-axis schema references entry.universal; ADR 0019's claim that a shared "
        "change fans out to every axis would no longer hold"
    )


def test_schema_ids_still_track_main():
    """Pins the known gap in ADR 0019 decision 3.

    The freeze is an internal discipline, not an external guarantee, precisely
    because $id resolves to a moving branch. When versioned IDs land, this test
    fails and its ADR section plus the backlog entry should be updated together.
    """
    tracking = [n for n in FROZEN if "/main/" in load(n).get("$id", "")]
    assert tracking, (
        "no schema $id points at main any more. If versioned schema IDs have landed, "
        "update ADR 0019 decision 3, the backlog entry, and delete this test."
    )

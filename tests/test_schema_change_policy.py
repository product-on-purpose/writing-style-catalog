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
# Not frozen, so it is served from the experimental namespace, not /v1/ (ADR 0020).
EXPERIMENTAL = ["diff-pair"]
UNFROZEN = EXPERIMENTAL

# Keywords ADR 0019 puts on the class A allowlist.
CLASS_A_KEYWORDS = ["title", "description", "$comment", "examples"]


def load(name):
    sub = "experimental" if name in EXPERIMENTAL else ""
    return json.loads((SCHEMAS / sub / f"{name}.schema.json").read_text(encoding="utf-8"))


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
    on_disk = sorted(p.name.replace(".schema.json", "") for p in SCHEMAS.rglob("*.schema.json")
                     if "contracts" not in p.parts)
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


SCHEMA_BASE = "https://product-on-purpose.github.io/writing-style-catalog/schemas/v1"


def test_frozen_schema_ids_are_contract_versioned():
    """ADR 0020: $id is the version-scoped published URL, not a branch tip.

    Replaces test_schema_ids_still_track_main, which pinned the gap recorded in
    ADR 0019 decision 3. A $id resolving to a moving branch cannot back a frozen
    contract, so the freeze was internal-only until this landed.
    """
    offenders = []
    for name in FROZEN:
        sid = load(name).get("$id", "")
        if sid != f"{SCHEMA_BASE}/{name}.schema.json":
            offenders.append(f"{name}: {sid or '(no $id)'}")
    assert not offenders, (
        "schema $id must be the contract-versioned published URL (ADR 0020):\n"
        + "\n".join(offenders)
    )


def test_no_schema_id_points_at_a_branch():
    """The specific regression: raw.githubusercontent on main."""
    bad = [n for n in FROZEN + UNFROZEN if "raw.githubusercontent" in load(n).get("$id", "")]
    assert not bad, f"$id resolves to a branch tip, so the freeze is not real: {bad}"


def test_validate_registry_derives_uris_from_id_not_a_constant():
    """ADR 0020: the base URL lives in the schemas, not a second copy in validate.py.

    A hardcoded base in the registry builder disagrees with the schemas the moment
    either moves, and $ref resolution then fails, or half-succeeds, with nothing
    pointing at the cause.
    """
    src = (REPO_ROOT / "tools" / "validate.py").read_text(encoding="utf-8")
    builder = src[src.index("def _build_schema_registry"):]
    builder = builder[: builder.index("\ndef ", 1)]
    assert "raw.githubusercontent" not in builder, (
        "_build_schema_registry still hardcodes a schema base URL; it must read $id"
    )
    assert '"$id"' in builder, (
        "_build_schema_registry should derive each URI from the schema's own $id"
    )


def test_relative_refs_resolve_within_the_same_contract_version():
    """Why relative $refs are kept: they inherit the version-scoped base URI.

    An absolute $ref could point at a different contract version than the
    document containing it, which is the skew ADR 0020 fixed structurally.
    """
    import re

    for name in ("voice", "tone", "style", "format"):
        raw = (SCHEMAS / f"{name}.schema.json").read_text(encoding="utf-8")
        for ref in re.findall(r'"\$ref":\s*"([^"]+)"', raw):
            if ref.startswith("#"):
                continue
            assert not ref.startswith("http"), (
                f"{name}.schema.json uses an absolute $ref ({ref}); keep it relative so "
                "it resolves within the same contract version (ADR 0020)"
            )


def test_every_schema_resolves_through_the_real_registry():
    """End to end: the registry the validator actually builds resolves every $ref."""
    import sys

    sys.path.insert(0, str(REPO_ROOT / "tools"))
    import validate as v

    registry = v._build_schema_registry()
    for name in FROZEN + UNFROZEN:
        validator = jsonschema.Draft202012Validator(load(name), registry=registry)
        # Iterating forces $ref resolution; an unresolvable ref raises here.
        list(validator.iter_errors({}))


def test_published_schema_path_matches_declared_id():
    """The generator publishes to the exact path each $id claims.

    Guards the pairing gen-site.mjs enforces at build time, so the agreement is
    also asserted without needing a build.
    """
    for name in FROZEN:
        sid = load(name)["$id"]
        suffix = f"/schemas/v1/{name}.schema.json"
        assert sid.endswith(suffix), f"{name}: $id {sid} does not end with {suffix}"
    for name in EXPERIMENTAL:
        sid = load(name)["$id"]
        suffix = f"/schemas/experimental/{name}.schema.json"
        assert sid.endswith(suffix), f"{name}: $id {sid} does not end with {suffix}"


# ---------------------------------------------------------------------------
# ADR 0020: retention and namespace guarantees, made enforceable
# ---------------------------------------------------------------------------

GEN_SITE = REPO_ROOT / "scripts" / "gen-site.mjs"
CONTRACTS_DIR = SCHEMAS / "contracts"


def _current_contract_version():
    import re

    src = GEN_SITE.read_text(encoding="utf-8")
    m = re.search(r"SCHEMA_CONTRACT_VERSION\s*=\s*'([^']+)'", src)
    assert m, "SCHEMA_CONTRACT_VERSION not found in gen-site.mjs"
    return m.group(1)


def test_contract_version_bump_requires_a_snapshot():
    """The retention promise in ADR 0020, enforced instead of trusted.

    The published tree is gitignored and rebuilt every deploy, so a version that
    is not emitted from a committed source vanishes and every pinned consumer
    404s. Bumping the constant without snapshotting the outgoing version to
    schemas/contracts/<version>/ is exactly that failure, and it would only be
    discovered by the consumers it broke.
    """
    current = _current_contract_version()
    snapshots = (
        sorted(p.name for p in CONTRACTS_DIR.iterdir() if p.is_dir())
        if CONTRACTS_DIR.exists() else []
    )
    superseded = [v for v in ("v" + str(i) for i in range(1, int(current[1:]))) ]
    missing = [v for v in superseded if v not in snapshots]
    assert not missing, (
        f"SCHEMA_CONTRACT_VERSION is {current}, but these superseded versions have no "
        f"frozen snapshot under schemas/contracts/: {missing}. Without one, the next "
        "clean build stops serving them and every consumer pinned to them breaks. "
        "Snapshot the outgoing version in the same PR that bumps the constant."
    )


def test_unfrozen_schema_is_not_served_from_a_frozen_namespace():
    """ADR 0020 decision 2: the URL has to carry the guarantee level.

    diff-pair may take a breaking change without a major bump (ADR 0019), so
    serving it under /v1/ would let a "pinned" document change underneath a
    consumer with nothing in the URL to distinguish it from the frozen schemas.
    """
    for name in EXPERIMENTAL:
        sid = load(name)["$id"]
        assert "/schemas/experimental/" in sid, (
            f"{name} is unfrozen but its $id is {sid}; it must not sit in a versioned "
            "namespace that implies a compatibility guarantee it does not have"
        )
        assert "/schemas/v1/" not in sid


def test_experimental_schemas_live_outside_the_frozen_directory():
    """Directory layout mirrors the guarantee, so the split is visible on disk."""
    for name in EXPERIMENTAL:
        assert (SCHEMAS / "experimental" / f"{name}.schema.json").exists()
        assert not (SCHEMAS / f"{name}.schema.json").exists(), (
            f"{name}.schema.json is still in the frozen directory root"
        )

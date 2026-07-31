"""Guards the error-keyed troubleshooting docs (audit finding F-5).

The point of F-5 was that the guides described failure categories in prose while
the reader was looking at an actual error string. Troubleshooting keyed to a
string the code does not print is worse than none: the reader searches for their
error, finds nothing, and concludes the docs do not cover it.

So these tests assert the quoted strings still exist in the code that prints
them. Writing the first draft produced exactly the failure this guards: the
dash-check message was quoted from memory as "FAIL: em-dash (U+2014) or en-dash
(U+2013) found in tracked authored text" when the script actually prints
"FAIL: N file(s) contain an em-dash or en-dash".
"""
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
GUIDES = REPO_ROOT / "site" / "src" / "content" / "docs" / "guides"
ADD_ENTRY = GUIDES / "add-entry.md"
INSTALL = GUIDES / "install.md"

# (fragment quoted in a guide, file that must actually print it)
VALIDATOR_STRINGS = [
    "schema validation failed:",
    "references unknown entry ID",
    "could not parse frontmatter (missing --- delimiters?)",
    "Gate 2: missing worked samples on",
    "does not match entry's actual axis",
]


def _read(p):
    return p.read_text(encoding="utf-8")


@pytest.mark.parametrize("fragment", VALIDATOR_STRINGS)
def test_quoted_validator_errors_are_real(fragment):
    """Every validator error the guide quotes must exist in validate.py."""
    assert fragment in _read(ADD_ENTRY), f"guide no longer quotes {fragment!r}"
    assert fragment in _read(REPO_ROOT / "tools" / "validate.py"), (
        f"add-entry.md quotes {fragment!r}, which validate.py no longer prints"
    )


def test_dash_check_message_matches_the_script():
    """The specific string the first draft got wrong."""
    guide = _read(ADD_ENTRY)
    src = _read(REPO_ROOT / "scripts" / "check-no-dashes.mjs")
    assert "contain an em-dash or en-dash" in guide
    assert "contain an em-dash or en-dash" in src, (
        "check-no-dashes.mjs changed its failure text; add-entry.md now quotes a "
        "string the script does not print"
    )


def test_install_guide_quotes_the_real_dependency_abort():
    guide = _read(INSTALL)
    src = _read(REPO_ROOT / "tools" / "validate.py")
    fragment = "jsonschema and referencing are required"
    assert fragment in guide
    assert fragment in src


def test_install_guide_quotes_the_real_interface_guard():
    guide = _read(INSTALL)
    src = _read(REPO_ROOT / "skills" / "entry-recommender" / "scripts" / "recommend.py")
    fragment = "is missing expected symbol"
    assert fragment in guide
    assert fragment in src


def test_install_guide_quotes_the_real_unknown_axis_error():
    guide = _read(INSTALL)
    src = _read(REPO_ROOT / "skills" / "entry-recommender" / "scripts" / "recommend.py")
    assert "unknown axis:" in guide
    assert "unknown axis:" in src


def test_install_guide_quotes_the_real_entry_not_found_error():
    guide = _read(INSTALL)
    src = _read(
        REPO_ROOT / "skills" / "writing-instruction-builder" / "scripts" / "build-instruction.py"
    )
    assert "Entry not found:" in guide
    assert "Entry not found:" in src


def test_troubleshooting_points_at_the_verbose_trace():
    """The recommender-invisible case is only debuggable with the D-7 trace."""
    guide = _read(ADD_ENTRY)
    assert "--verbose" in guide, (
        "the 'entry never surfaces' section should point at the score trace, which "
        "is the only thing that shows which gate rejected a candidate"
    )

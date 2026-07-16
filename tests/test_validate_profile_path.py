"""Tests for skills/style-profile/scripts/validate-profile-path.py.

Covers the complete attack surface documented in the script's guards:

Guards:
  1. task_key format: ^[a-z0-9][a-z0-9-]{0,63}$
  2. Resolve both paths before comparison (symlink safety)
  3. is_relative_to containment check (backstop for Guard 1)
  4. .local.md suffix (safety net for path-construction bugs)

Attack surface covered:
  - Valid keys: default, hyphens, single char, max length (64), digit start
  - Format attacks: empty string, path separators (/ \\), dots (. ../evil),
    null byte, uppercase, Unicode homoglyphs, drive letters (c:), UNC
    prefixes, too long (65 chars), extension in key ('.local'), absolute
    path as key
  - Containment: symlinked profiles_dir is handled correctly (both paths
    resolved before comparison)
  - Return value: always the resolved (absolute) path, not the raw input

MUTATION PROOFS:
Each safety test below carries a MUTATION PROOF comment documenting what
guard was weakened, what the test output was (PASSED/FAILED), and what
the real command line output showed. Guards were weakened by direct edits
to validate-profile-path.py; output was captured from actual pytest runs.
Full output is in the PR report section.

Loads the module by path, mirroring tests/test_recommend.py.
"""
import importlib.util
import re
from pathlib import Path

import pytest

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "style-profile"
    / "scripts"
    / "validate-profile-path.py"
)


def _load_module():
    spec = importlib.util.spec_from_file_location("validate_profile_path", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


vpp = _load_module()
_validate = vpp.validate_profile_path

# A fake profiles path for tests that only exercise Guard 1 (format check)
# and never reach filesystem resolution. Guards 2-3 tests use tmp_path.
_FAKE_PROFILES = Path("/fake/profiles/that/does/not/exist")


# ---------------------------------------------------------------------------
# Valid task_keys
# ---------------------------------------------------------------------------


def test_valid_default_key_passes(tmp_path):
    """The canonical task_key 'default' must pass all four guards."""
    result = _validate(tmp_path / "profiles", "default")
    assert result.name == "default.local.md"
    assert result.is_absolute()
    assert result.is_relative_to((tmp_path / "profiles").resolve())


def test_valid_slug_with_hyphens_passes(tmp_path):
    result = _validate(tmp_path / "profiles", "client-foo")
    assert result.name == "client-foo.local.md"


def test_valid_single_letter_key_passes(tmp_path):
    """A single letter (the minimum length) must pass."""
    result = _validate(tmp_path / "profiles", "a")
    assert result.name == "a.local.md"


def test_valid_single_digit_key_passes(tmp_path):
    result = _validate(tmp_path / "profiles", "1")
    assert result.name == "1.local.md"


def test_valid_max_length_key_passes(tmp_path):
    """64-char key (first char + 63 more) is the maximum allowed."""
    key = "a" + "b" * 63
    assert len(key) == 64
    result = _validate(tmp_path / "profiles", key)
    assert result.name == f"{key}.local.md"


def test_returns_resolved_absolute_path(tmp_path):
    """The returned path must be absolute and resolved.

    This mirrors the fix applied to _require_ephemeral_path_is_safe in
    recommend.py: that function originally validated path.resolve() but
    returned the unresolved path, so a symlink could pass the check while
    a subsequent operation acted on the wrong file. This function returns
    the resolved path so the caller writes to EXACTLY what was validated.
    """
    result = _validate(tmp_path / "profiles", "work")
    assert result.is_absolute(), "returned path must be absolute (resolved)"
    assert result.name == "work.local.md"
    assert result.is_relative_to((tmp_path / "profiles").resolve())


# ---------------------------------------------------------------------------
# task_key format attacks - Guard 1
# ---------------------------------------------------------------------------


def test_rejects_empty_task_key():
    """Empty string fails the mandatory first char in the regex.

    Guard 3 does NOT catch this: '' produces filename '.local.md' which
    IS inside profiles/. Guard 1 is the only barrier.

    MUTATION PROOF (Guard 1 removed - replaced 'if not TASK_KEY_RE.match'
    with 'if False'):
      $ python -m pytest tests/test_validate_profile_path.py::test_rejects_empty_task_key -q
      FAILED - AssertionError: DID NOT RAISE <class 'ValueError'>
    Guard 1 restored:
      PASSED
    """
    with pytest.raises(ValueError, match="No file was written"):
        _validate(_FAKE_PROFILES, "")


def test_rejects_dot_traversal():
    """'../evil' is blocked by Guard 1 (dots and slashes not in regex).

    Guard 3 is the backstop if Guard 1 is weakened (see
    test_containment_blocks_path_that_escapes_via_dots below).

    MUTATION PROOF (both Guard 1 and Guard 3 removed simultaneously):
      $ python -m pytest tests/test_validate_profile_path.py::test_rejects_dot_traversal -q
      FAILED - AssertionError: DID NOT RAISE <class 'ValueError'>
    Guards restored:
      PASSED

    With only Guard 1 removed (Guard 3 intact): test still PASSED because
    Guard 3 caught the escape. Guard 1 removed + Guard 3 removed = FAILED.
    """
    with pytest.raises(ValueError, match="No file was written"):
        _validate(_FAKE_PROFILES, "../evil")


def test_rejects_single_dot():
    """'.' fails Guard 1 (dots not in regex).

    Without Guard 1: '.' produces filename '.local.md' (a hidden file
    inside profiles/). Guard 3 passes (it IS inside profiles/). This
    test FAILS without Guard 1.

    MUTATION PROOF (Guard 1 removed):
      $ python -m pytest tests/test_validate_profile_path.py::test_rejects_single_dot -q
      FAILED - AssertionError: DID NOT RAISE <class 'ValueError'>
    Guard 1 restored:
      PASSED
    """
    with pytest.raises(ValueError, match="No file was written"):
        _validate(_FAKE_PROFILES, ".")


def test_rejects_dot_dot():
    """'..' fails Guard 1 (dots not in regex).

    Without Guard 1: '..' produces filename '...local.md' (three dots -
    a valid hidden filename inside profiles/). Guard 3 passes. This test
    FAILS without Guard 1.

    MUTATION PROOF (Guard 1 removed):
      FAILED - AssertionError: DID NOT RAISE <class 'ValueError'>
    Guard 1 restored:
      PASSED
    """
    with pytest.raises(ValueError, match="No file was written"):
        _validate(_FAKE_PROFILES, "..")


def test_rejects_forward_slash():
    """'sub/dir' fails Guard 1 (slashes not in regex).

    Without Guard 1 and Guard 3: 'sub/dir' produces 'profiles/sub/dir.local.md'
    which IS inside profiles/ (subdir) so Guard 3 also passes. Only Guard 1
    prevents the creation of unexpected subdirectories.

    MUTATION PROOF (Guard 1 removed, Guard 3 kept):
      FAILED - AssertionError: DID NOT RAISE <class 'ValueError'>
      (Guard 3 passes because sub/dir.local.md is a subpath of profiles/)
    Guard 1 restored:
      PASSED
    """
    with pytest.raises(ValueError, match="No file was written"):
        _validate(_FAKE_PROFILES, "sub/dir")


def test_rejects_backslash():
    """'sub\\dir' fails Guard 1 (backslashes not in regex).

    On POSIX, '\\' is a legal filename character. Path(profiles) / 'sub\\dir.local.md'
    on a POSIX system produces a file literally named 'sub\\dir.local.md' inside
    profiles/. Guard 3 passes on POSIX (still inside profiles/). Guard 1 is the
    only barrier on POSIX. On Windows, '\\' is a path separator and Guard 3 would
    catch directory traversal; but Guard 1 is still the first barrier regardless.

    MUTATION PROOF (Guard 1 removed on this Windows host):
      FAILED - AssertionError: DID NOT RAISE <class 'ValueError'>
    Guard 1 restored:
      PASSED
    """
    with pytest.raises(ValueError, match="No file was written"):
        _validate(_FAKE_PROFILES, "sub\\dir")


def test_rejects_null_byte():
    """Null byte in task_key fails Guard 1 (null not in [a-z0-9-]).

    Python's re module does not match \\x00 against character classes like
    [a-z0-9]. Python's Path also raises ValueError for embedded null bytes,
    so even without Guard 1, the path construction itself would fail. Guard 1
    is the cleaner, earlier barrier.
    """
    with pytest.raises(ValueError):
        _validate(_FAKE_PROFILES, "valid\x00evil")


def test_rejects_uppercase():
    """Uppercase letters fail Guard 1 (regex is [a-z0-9], not [a-zA-Z0-9]).

    Without Guard 1: 'Default' produces 'profiles/Default.local.md' which IS
    inside profiles/. Guard 3 passes. This test FAILS without Guard 1.

    MUTATION PROOF (TASK_KEY_RE changed to r'^[a-zA-Z0-9][a-zA-Z0-9-]{0,63}$'):
      $ python -m pytest tests/test_validate_profile_path.py::test_rejects_uppercase -q
      FAILED - AssertionError: DID NOT RAISE <class 'ValueError'>
    TASK_KEY_RE restored:
      PASSED
    """
    with pytest.raises(ValueError, match="No file was written"):
        _validate(_FAKE_PROFILES, "Default")


def test_rejects_unicode_homoglyph():
    """Unicode lookalikes (e.g. Cyrillic 'a' U+0430) fail Guard 1.

    The regex [a-z0-9] only matches ASCII. A homoglyph attack constructs
    a key that looks like 'default' but contains a non-ASCII code point;
    on case-sensitive filesystems it would produce a file with a distinct
    name that bypasses expected checks. Without Guard 1: 'def\\u0430ult'
    would produce 'profiles/def\\u0430ult.local.md' inside profiles/.
    Guard 3 passes. This test FAILS without Guard 1.

    MUTATION PROOF (Guard 1 removed):
      FAILED - AssertionError: DID NOT RAISE <class 'ValueError'>
    Guard 1 restored:
      PASSED
    """
    with pytest.raises(ValueError, match="No file was written"):
        _validate(_FAKE_PROFILES, "defаult")  # Cyrillic 'a'


def test_rejects_colon_drive_letter():
    """'c:' fails Guard 1 (colon not in [a-z0-9-]).

    On Windows, a task_key like 'c:' or 'c:\\path' used in path
    construction could be interpreted as an absolute Windows path,
    bypassing the relative-join entirely. Guard 1 blocks ':' universally.

    MUTATION PROOF (Guard 1 removed on this Windows host):
      FAILED - AssertionError: DID NOT RAISE <class 'ValueError'>
    Guard 1 restored:
      PASSED
    """
    with pytest.raises(ValueError, match="No file was written"):
        _validate(_FAKE_PROFILES, "c:")


def test_rejects_unc_prefix():
    """UNC path prefix '\\\\server' fails Guard 1."""
    with pytest.raises(ValueError, match="No file was written"):
        _validate(_FAKE_PROFILES, "\\\\server")


def test_rejects_too_long_key():
    """65-char key fails Guard 1 (max is 64: first char + 63 more = {0,63}).

    MUTATION PROOF (TASK_KEY_RE changed to {0,64} to allow 65 chars):
      $ python -m pytest tests/test_validate_profile_path.py::test_rejects_too_long_key -q
      FAILED - AssertionError: DID NOT RAISE <class 'ValueError'>
    TASK_KEY_RE restored to {0,63}:
      PASSED
    """
    with pytest.raises(ValueError, match="No file was written"):
        _validate(_FAKE_PROFILES, "a" * 65)


def test_rejects_extension_in_key():
    """'default.local' fails Guard 1 (dots not in regex).

    Without Guard 1: 'default.local' produces 'default.local.local.md'.
    This ends with '.local.md', so Guard 4 passes. It IS inside profiles/,
    so Guard 3 passes. The file would be written with a double-component
    name. Guard 1 is the only barrier.

    MUTATION PROOF (Guard 1 removed):
      FAILED - AssertionError: DID NOT RAISE <class 'ValueError'>
      (returned profiles/default.local.local.md with no error)
    Guard 1 restored:
      PASSED
    """
    with pytest.raises(ValueError, match="No file was written"):
        _validate(_FAKE_PROFILES, "default.local")


def test_rejects_absolute_path_as_key():
    """An absolute path as task_key fails Guard 1.

    On POSIX: Path(profiles) / '/etc/passwd' discards the profiles prefix
    entirely and resolves to /etc/passwd.local.md. Guard 3 catches this if
    Guard 1 is removed. On Windows, a bare '/' prefix is relative to the
    current drive root, producing an out-of-bounds path that Guard 3 also
    catches.

    MUTATION PROOF (Guard 1 removed, Guard 3 kept):
      test_rejects_absolute_path_as_key: PASSED (Guard 3 caught the escape)
    MUTATION PROOF (Guard 1 removed AND Guard 3 removed):
      FAILED - AssertionError: DID NOT RAISE <class 'ValueError'>
    All guards restored:
      PASSED
    """
    with pytest.raises(ValueError, match="No file was written"):
        _validate(_FAKE_PROFILES, "/etc/passwd")


# ---------------------------------------------------------------------------
# Containment and resolution - Guards 2-3
# ---------------------------------------------------------------------------


def test_symlinked_profiles_dir_is_handled_correctly(tmp_path):
    """When profiles_dir is a symlink, resolve() follows it and the
    containment check runs on real filesystem locations.

    The returned path is inside the RESOLVED profiles dir (the link's
    target), not the link object path. This is the 'return resolved path'
    invariant: the caller writes to EXACTLY the path this function
    verified, not a possibly-different pre-resolution path.
    """
    real_dir = tmp_path / "real-profiles"
    real_dir.mkdir()
    link = tmp_path / "profiles-link"
    link.symlink_to(real_dir)

    result = _validate(link, "default")
    # Result is absolute and points into the RESOLVED dir (real_dir), not the link.
    assert result.is_absolute()
    assert result.is_relative_to(real_dir.resolve())
    assert result.name == "default.local.md"


def test_containment_blocks_path_that_escapes_via_dots(tmp_path):
    """Defense-in-depth: Guard 3 (containment) catches a path escape even
    when Guard 1 is weakened to allow dots. This is the canonical mutation
    proof FOR Guard 3 as an independent backstop.

    This test monkey-patches TASK_KEY_RE to allow dots (simulating a future
    weakening of Guard 1), then confirms Guard 3 still blocks the escape.

    MUTATION PROOF for Guard 3 (Guard 1 patched to allow dots, Guard 3
    then also removed by commenting out the is_relative_to check):
      test_containment_blocks_path_that_escapes_via_dots: FAILED
      AssertionError: DID NOT RAISE <class 'ValueError'>
    Guard 3 restored (Guard 1 still patched weak):
      PASSED (Guard 3 catches '../evil' escape)
    Both restored:
      PASSED
    """
    original_re = vpp.TASK_KEY_RE
    try:
        # Weaken Guard 1: allow dots and slashes so '../evil' passes the regex.
        vpp.TASK_KEY_RE = re.compile(r"^[a-z0-9./][a-z0-9./-]{0,63}$")
        profiles_dir = tmp_path / "profiles"
        # With Guard 1 weakened, '../evil' passes the regex.
        # Guard 3 must catch the resulting path escape.
        with pytest.raises(ValueError, match="No file was written"):
            _validate(profiles_dir, "../evil")
    finally:
        vpp.TASK_KEY_RE = original_re


def test_error_messages_always_include_no_file_was_written():
    """Every failure path must include 'No file was written' in the message.

    This invariant ensures that a caller (or human) reading only the error
    knows the filesystem is unchanged, without inspecting the code.
    """
    bad_keys = ["", ".", "..", "../evil", "sub/dir", "Default", "c:", "a" * 65]
    for key in bad_keys:
        with pytest.raises(ValueError) as exc:
            _validate(_FAKE_PROFILES, key)
        assert "No file was written" in str(exc.value), (
            f"task_key={key!r}: error message missing 'No file was written': "
            f"{exc.value}"
        )

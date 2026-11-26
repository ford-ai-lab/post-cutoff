"""Run with:  python3 -m unittest discover -s build/tests"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from postcutoff import classify as C  # noqa: E402
from postcutoff.normalise import to_blocks  # noqa: E402
from postcutoff.parse import Release, extract, heading_date, heading_version, split_releases, trace  # noqa: E402

KEEP_A_CHANGELOG = """# Changelog
## [Unreleased]
- Removed the moon
## [4.0.0] - 2025-07-10
### Breaking Changes
- `foo()` now returns a Promise ([#12](https://example.test/pull/12))
### Added
- `bar()` helper by @someone in https://github.com/x/y/pull/9
### Fixed
- Removed a stray log line
```js
# 9.9.9
```
## [3.9.1] - 2025-05-01
### Fixed
- nothing to see
"""

RST = """Changelog
=========

pytest 9.0.0 (2025-11-05)
=========================

Removals and backward incompatible breaking changes
---------------------------------------------------

- `#13779 <https://example.test/13779>`_: :func:`pytest.old` was removed. Use :func:`pytest.new`.

Bug fixes
---------

- Fixed a crash.
"""


class Tests(unittest.TestCase):
    def test_heading_version(self):
        a = {"react", "numpy", "NumPy"}
        self.assertEqual(heading_version("[8.4.0-beta.2](https://x/compare) (2026-11-25)", a), "8.4.0-beta.2")
        self.assertEqual(heading_version('<a id="23-2-0"></a>23.2.0 - 2026-11-18', a), "23.2.0")
        self.assertEqual(heading_version("v1.21.0 — October 21, 2026", a), "1.21.0")
        self.assertEqual(heading_version("Version 1.65", a), "1.65")
        self.assertIsNone(heading_version("Python 3.9 support dropped", a))
        self.assertIsNone(heading_version("2.1 Changelog", a))
        self.assertIsNone(heading_version("Breaking changes", a))

    def test_heading_date(self):
        self.assertEqual(heading_date("19.2.0 (October 1st, 2025)"), "2025-10-01")
        self.assertEqual(heading_date("0.28.1 (6th December, 2024)"), "2024-12-06")
        self.assertEqual(heading_date("[4.3.5] - 2026-11-06"), "2026-11-06")

    def test_markdown_release(self):
        rels = split_releases(to_blocks(KEEP_A_CHANGELOG), {"pkg"})
        self.assertEqual([r.version for r in rels], ["4.0.0", "3.9.1"])   # Unreleased and code block ignored
        r = extract(rels[0])
        self.assertIn((C.BREAKING, "`foo()` now returns a Promise"), r.items)
        self.assertIn((C.NEW, "`bar()` helper"), r.items)
        self.assertFalse(any("stray log" in t for _, t in r.items))        # under "Fixed": not a removal
        self.assertEqual(extract(rels[1]).items, [])                       # thin notes stay empty

    def test_rst_release(self):
        rels = split_releases(to_blocks(RST, "rst"), {"pytest"})
        self.assertEqual([r.version for r in rels], ["9.0.0"])
        self.assertEqual(extract(rels[0]).items, [(C.BREAKING, "`pytest.old` was removed. Use `pytest.new`.")])

    def test_minimum_version(self):
        self.assertEqual(C.item_category("Drop support for Node 18", C.SKIP), C.MINVER)
        self.assertEqual(C.item_category("Dropped support for Python 3.9 following its end of support.", None), C.MINVER)
        self.assertIsNone(C.item_category("fix: handle null loc", None))
        self.assertEqual(C.item_category("feat!: remove eslintrc support", None), C.BREAKING)

    def test_trace_drops_invented_text(self):
        r = Release(version="1.0.0", raw="- `foo()` now returns a Promise")
        r.items = [(C.BREAKING, "`foo()` now returns a Promise"), (C.BREAKING, "bar() was deleted in favour of baz()")]
        self.assertEqual(trace(r), 1)
        self.assertEqual(r.items, [(C.BREAKING, "`foo()` now returns a Promise")])


if __name__ == "__main__":
    unittest.main()

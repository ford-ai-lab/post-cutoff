"""Deterministic rules that sort release-note lines into digest categories.

Nothing here writes text. A rule only decides which upstream sentence is kept
and under which heading it is shown.
"""
import re

BREAKING, REMOVED, DEPRECATED, MINVER, NEW, SKIP = "breaking", "removed", "deprecated", "minver", "new", "skip"
CATEGORIES = [BREAKING, REMOVED, DEPRECATED, MINVER, NEW]
TITLES = {
    BREAKING: "Breaking changes",
    REMOVED: "Removed or renamed",
    DEPRECATED: "Deprecated",
    MINVER: "Minimum versions and platform support",
    NEW: "New APIs and features",
}

_I = re.IGNORECASE
_H_RULES = [
    (MINVER, re.compile(r"python compatibility|node(\.js)? (runtime|version|support)|runtime and browser support|"
                        r"supported (python|node)|minimum (version|requirement|supported)|increased minimum", _I)),
    (SKIP, re.compile(r"^c[ -]api|unstable|preview|experimental|^migrations$", _I)),
    (BREAKING, re.compile(r"breaking|backwards?[- ]incompatible|incompatible|major changes|upgrade notes|"
                          r"migration|behaviou?ral changes?|api changes|compatibility notes|upgrading", _I)),
    (REMOVED, re.compile(r"expired deprecation|removal of prior|\bremov|\brenam", _I)),
    (DEPRECATED, re.compile(r"deprecat", _I)),
    (SKIP, re.compile(r"\bfix|patch changes|\bbug|\bdocs?\b|documentation|chore|internal|contributor|thank|"
                      r"dependenc|performance|refactor|\btests?\b|translation|maintenance|pull requests|security|"
                      r"revert|\bstyle|\bbuild\b|\bci\b|browser versions|packaging|trivial|misc|credits|"
                      r"announcement|known (problems|issues)|sponsor|upgrades?$|infrastructure|typing", _I)),
    (NEW, re.compile(r"feature|\badded\b|^add\b|^new\b|new (api|function|option|rule|method|component)|"
                     r"enhancement|minor changes|highlights|what'?s new|improvements? in existing", _I)),
]

_STRICT_BREAKING = re.compile(r"⚠|\bBREAKING\b|breaking[- ]change|backwards?[- ]incompatible|^\w+(\([^)]*\))?!:", _I)
_STRICT_BREAKING_CS = re.compile(r"⚠|\bBREAKING\b|[Bb]reaking[- ]change|backwards?[- ]incompatible|^\w+(\([^)]*\))?!:")
_MINVER = re.compile(
    r"(drop(s|ped|ping)?( official)? support for|no longer supports?|requires?|required|minimum|"
    r"end[- ]of[- ]life|remov(e|ed|es|ing) support for|supports? only|now supports)"
    r"[^.]{0,60}?\b(node(\.js|js)?|python|typescript|pypy|deno|bun|rustc?|msrv|django|php|macos|glibc)\b"
    r"[^.\d]{0,25}(v|>=|<|≥|>)?\s*\d", _I)
_MINVER2 = re.compile(
    r"\b(node(\.js|js)?|python|typescript|pypy)\b\s*(v|>=|<|≥)?\s*\d[\d.x]*[^.]{0,40}"
    r"(is|are) (no longer supported|now required|required|the minimum|dropped|not supported)", _I)
_REMOVED = re.compile(r"^(remove[sd]?|removing|drop(s|ped)?|delete[sd]?)\b|"
                      r"\b(has|have|was|were|been|is|are) (now )?(removed|renamed)\b|\brenamed?\b[^.]{0,80}\b(to|as)\b|"
                      r"\bno longer (supported|available|exported|accept(s|ed)|exists?|works?|allowed|supports?|provide[sd]?|"
                      r"included|possible|public|valid|recogni[sz]ed|generated|emitted|returns?)\b", _I)
_DEPRECATED = re.compile(r"deprecat", _I)
_NEW = re.compile(r"^(?:[\w@/.` -]{2,30}:\s+)?(add(s|ed|ing)?|new|introduc\w+|support(s|ed)? for|implement(s|ed)?|"
                  r"allow(s|ed)?|expose[sd]?|enable[sd]?)\b|^feat(ure)?\s?(\([^)]*\))?:|^\[(usecase|feature)", _I)
_CC_SKIP = re.compile(r"^(fix|docs?|chore|ci|tests?|build|refactor|perf|style|revert|upgrade|deps|release)\s?(\([^)]*\))?:|^\[(bug|performance|typing|tests?)\b", _I)


def heading_category(text):
    """Category for a sub-heading inside a release, or None when it says nothing."""
    for cat, rx in _H_RULES:
        if rx.search(text):
            return cat
    return None


def item_category(text, context):
    """Category for one list item given the category of the heading above it (or None)."""
    if _MINVER.search(text) or _MINVER2.search(text):
        return MINVER
    if context == SKIP or (context is None and _CC_SKIP.match(text)):
        return BREAKING if _STRICT_BREAKING_CS.search(text) else None
    if context in (BREAKING, REMOVED, DEPRECATED, MINVER):
        return context
    if _STRICT_BREAKING.search(text):
        return BREAKING
    if _DEPRECATED.search(text):
        return DEPRECATED
    if _REMOVED.search(text):
        return REMOVED
    if context == NEW or _NEW.match(text):
        return NEW
    return None

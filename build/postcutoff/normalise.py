"""Turn Markdown or reStructuredText release notes into a flat list of blocks.

Blocks are tuples:
  ("h", level, text)   heading
  ("li", text)         top-level list item (first paragraph only)
  ("p", text)          paragraph
Code blocks, directives and nested detail are dropped on purpose: the digest
quotes the first sentence or two of what upstream wrote, nothing more.
"""
import re

_UNDERLINE = re.compile(r"^([=\-~^\"+*#`'.:_])\1{2,}\s*$")
_BULLET = re.compile(r"^(\s*)(?:[-*+•]|\d+[.)])\s+(.*)$")
_ATX = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_PLAIN_VERSION_LINE = re.compile(r"^v?\d+\.\d+\.\d+\S* (?:-|/) (?:\w+ \d{1,2}, \d{4}|\d{4}-\d\d-\d\d)\s*$")


def _sqlalchemy_directives(text):
    """SQLAlchemy/Alembic keep changelogs as '.. changelog::' / '.. change::' directives."""
    if ".. changelog::" not in text:
        return text
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith(".. changelog::"):
            ver = rel = ""
            i += 1
            while i < len(lines) and lines[i].strip().startswith(":"):
                k, _, v = lines[i].strip()[1:].partition(":")
                if k == "version":
                    ver = v.strip()
                if k == "released":
                    rel = v.strip()
                i += 1
            out += ["", f"## {ver} ({rel})" if rel else f"## {ver}", ""]
            continue
        if s.startswith(".. change::"):
            tags = ""
            i += 1
            while i < len(lines) and lines[i].strip().startswith(":"):
                k, _, v = lines[i].strip()[1:].partition(":")
                if k == "tags":
                    tags = v.strip()
                i += 1
            para = []
            while i < len(lines) and not lines[i].strip():
                i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith(".. "):
                para.append(lines[i].strip())
                i += 1
            out += [f"- [{tags}] " + " ".join(para), ""]
            # skip the remaining paragraphs of this change
            while i < len(lines) and not lines[i].strip().startswith((".. change::", ".. changelog::")):
                i += 1
            continue
        if s.startswith(".. changelog_imports::") or s.startswith(":include_notes_from:"):
            i += 1
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def _rst_inline(s):
    s = re.sub(r"`([^`<]+?)\s*<[^>]+>`__?", r"\1", s)              # `text <url>`_
    s = re.sub(r":(?:issue|pr|pull|gh|ghpull|ghissue|ticket|user|bpo|cve|commit):`[^`]*`", "", s)
    s = re.sub(r":[\w:+.-]+:`[~!.]?([^`<]+?)(?:\s*<[^>]+>)?`", r"`\1`", s)  # :func:`x`
    s = s.replace("``", "`")
    s = re.sub(r"`([^`]+)`_\b", r"\1", s)
    s = re.sub(r"(?<=\s)\(\s*[,;]?\s*\)", "", s)
    return s


def to_blocks(text, fmt="md"):
    text = text.replace("\r\n", "\n")
    if fmt == "md":
        text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)        # YAML front matter
        text = re.sub(r"\{/\*.*?\*/\}", "", text, flags=re.S)             # MDX comments
    if fmt == "rst":
        text = _sqlalchemy_directives(text)
    lines = text.split("\n")
    blocks, levels = [], {}
    cur = None            # ["li"|"p", [parts], indent, para_done, nested_n]
    base_indent = None
    in_fence = skip_indent = None
    in_comment = False

    nested = []

    def flush():
        nonlocal cur
        if cur and cur[1]:
            t = " ".join(p.strip() for p in cur[1] if p.strip())
            if fmt == "rst":
                t = _rst_inline(t)
            if t:
                blocks.append((cur[0], t))
        for n in nested:
            blocks.append(("li2", _rst_inline(n) if fmt == "rst" else n))
        nested.clear()
        cur = None

    i = 0
    while i < len(lines):
        line = lines[i].expandtabs(4)
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        i += 1
        stripped = line.strip()
        if in_fence:
            if stripped.startswith(in_fence):
                in_fence = None
            continue
        if fmt == "md" and re.match(r"^\s*(```|~~~)", line):
            in_fence = stripped[:3]
            if cur and cur[0] == "li":
                cur[3] = True
            continue
        if in_comment:
            in_comment = "-->" not in line
            continue
        if stripped.startswith("<!--"):
            in_comment = "-->" not in line
            continue
        if skip_indent is not None:           # rst directive / literal block body
            if not stripped or len(line) - len(line.lstrip()) > skip_indent:
                continue
            skip_indent = None
        if fmt == "rst" and stripped.startswith(".. "):
            flush()
            skip_indent = len(line) - len(line.lstrip())
            continue
        if not stripped:
            if cur and cur[0] == "li":
                cur[3] = True
            else:
                flush()
            continue
        # headings
        m = _ATX.match(line)
        if m:
            flush()
            base_indent = None
            blocks.append(("h", len(m.group(1)), m.group(2)))
            continue
        if _UNDERLINE.match(line) and fmt == "rst" and _UNDERLINE.match(nxt) is None and nxt.strip() \
                and i + 1 < len(lines) and _UNDERLINE.match(lines[i + 1]):
            continue                          # overline of an rst title; title handled next
        um = _UNDERLINE.match(nxt)
        if um and not line.startswith(" ") and not _BULLET.match(line) and len(stripped) <= 110 \
                and (fmt == "rst" or um.group(1) in "=-") and len(nxt.strip()) >= min(len(stripped), 3) \
                and not _UNDERLINE.match(line) and (cur is None or fmt == "rst" or cur[0] != "li" or cur[3]):
            if fmt == "md" and cur and cur[0] == "p":
                pass                          # setext heading needs to start its own paragraph
            else:
                flush()
                base_indent = None
                ch = um.group(1)
                levels.setdefault(ch, len(levels) + 1)
                blocks.append(("h", levels[ch] if fmt == "rst" else (1 if ch == "=" else 2),
                               _rst_inline(stripped) if fmt == "rst" else stripped))
                i += 1
                continue
        if _UNDERLINE.match(line):
            flush()
            continue
        bm = re.match(r"^\*\*([^*]{3,60})\*\*:?$", stripped)
        if bm and (cur is None or (cur[0] == "li" and cur[3])):
            flush()               # "**Deprecations**:" used as a heading
            blocks.append(("h", 6, bm.group(1)))
            continue
        if fmt == "md" and _PLAIN_VERSION_LINE.match(line):
            flush()
            base_indent = None
            blocks.append(("h", 2, stripped))
            continue
        if fmt == "md" and stripped.startswith("|") and stripped.endswith("|"):
            # table row (Angular lists commits in tables): keep the cells that are not hashes
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells) or \
                    [c.lower() for c in cells][:2] == ["commit", "type"]:
                continue
            cells = [c for c in cells if c and not re.fullmatch(r"\[?`?[0-9a-f]{7,40}`?\]?(\([^)]*\))?", c)]
            flush()
            if cells:
                blocks.append(("li", ": ".join(cells)))
            continue
        b = _BULLET.match(line)
        if b:
            indent = len(b.group(1))
            if base_indent is None or indent < base_indent:
                base_indent = indent
            if indent < base_indent + 2:
                flush()
                cur = ["li", [b.group(2)], indent, False, 0]
            elif cur and cur[0] == "li":
                first = " ".join(cur[1]).rstrip()
                if first.endswith(":") and cur[4] < 4:
                    cur[1].append(("" if cur[4] == 0 else "; ") + b.group(2).strip())
                    cur[4] += 1
                elif indent < base_indent + 6:
                    nested.append(b.group(2).strip())
                cur[3] = True
            continue
        indented = line.startswith("  ")
        if cur and cur[0] == "li":
            if not cur[3]:
                cur[1].append(stripped)
                continue
            if indented:
                continue                      # later paragraphs of the same item
            flush()
            base_indent = None
        if cur is None:
            cur = ["p", [], 0, False, 0]
        cur[1].append(stripped)
        if fmt == "rst" and stripped.endswith("::"):
            flush()
            skip_indent = len(line) - len(line.lstrip())
    flush()
    return blocks

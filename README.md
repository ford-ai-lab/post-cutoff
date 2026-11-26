# post-cutoff

Two agent skills that tell a coding agent what changed in popular libraries **after its training
data ended**: breaking changes, removed or renamed APIs, deprecations, new APIs and raised minimum
versions. Every line is quoted from the package's own release notes and carries the version, the
release date and a link to the source.

- `post-cutoff-js`: 41 npm packages (react, next, vite, typescript, eslint, tailwindcss, express,
  playwright, svelte, astro, the OpenAI and Anthropic SDKs, ...)
- `post-cutoff-python`: 38 PyPI packages (pandas, numpy, pydantic, fastapi, django, sqlalchemy,
  pytest, ruff, uv, ...)

**Freshness: built 2026-11-25. Covers releases published after 2025-06-01.** The agent rebuilds it
by running `build/build.py`; this is not yet an automatic nightly job. The date at the top of each
`SKILL.md` is the date of the build you have.

**Also available as a hosted MCP server, free, no key:** `https://ford-lab.vercel.app/mcp`
(setup: https://ford-lab.vercel.app/post-cutoff).

## Install

With the [skills CLI](https://skills.sh/docs/cli) (works with Claude Code, Cursor, Codex and the
other agents it supports):

```bash
# choose from both skills
npx skills add ford-ai-lab/post-cutoff

# or one of them
npx skills add ford-ai-lab/post-cutoff --skill post-cutoff-js
npx skills add ford-ai-lab/post-cutoff --skill post-cutoff-python

# for every project on this machine, not only the current one
npx skills add ford-ai-lab/post-cutoff --skill post-cutoff-js -g

# pick up a later rebuild
npx skills update
```

Or copy a folder from `skills/` into your agent's skills directory by hand. Each skill is a
`SKILL.md` plus one small Markdown file per package under `references/` (4 KB on average, 13 KB at
most), so the agent reads only the packages the task touches.

## What a digest looks like

From `skills/post-cutoff-js/references/vite.md`:

```
## Breaking changes
### 7.0.0 (2025-06-24) [source](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#700-2025-06-24)
- remove `experimental.skipSsrTransform` option
- remove `HotBroadcaster`
- css: remove sass legacy API support

## Minimum versions and platform support
### 7.0.0 (2025-06-24) [source](...)
- bump required node version to 20.19+, 22.12+ and remove cjs build
```

## How it is built

`build/build.py` reads `build/packages.json`, fetches each package's changelog file (from
`raw.githubusercontent.com`), per-version release-note files, or the GitHub Releases API, takes
publish dates from the npm and PyPI registries, keeps stable releases after the cut-off, and sorts
upstream's own sentences into categories with keyword rules (`build/postcutoff/classify.py`).

- **No model writes any of the text.** The rules choose which upstream sentences to keep; they do
  not write sentences. A final check (`parse.trace`) drops any line whose words cannot be found, in
  order, in the upstream text.
- When release notes say nothing these rules recognise, the file says "no details in release notes".
- `build/postcutoff/summarise.py` is a hook where a model could be plugged in to compress long
  notes. It is off, and the trace check runs after it.

```bash
python3 build/build.py                       # all packages
python3 build/build.py --only react,pandas   # some
python3 build/build.py --cutoff 2025-01-01   # another cut-off
python3 -m unittest discover -s build/tests
```

Python 3.11+, standard library only.

## Honest limits

- **It is a filter, not a summary.** Lines are truncated quotes. Some lack context once lifted out
  of their paragraph, and conventional-commit changelogs read like commit subjects because they are.
- **The rules miss things and let noise through.** A change described without the words the rules
  look for is not listed. A file with no "Breaking changes" section is not proof there were none.
- **Capped.** Busy packages have hundreds of entries; each file keeps the most recent few dozen and
  says how many were left out.
- **Coverage depends on where a project keeps its notes.** In the build committed here, 70 of 79
  packages have extracted entries. 6 (zod, prisma, vitest, hono, langchain for Python, polars) keep
  notes only in GitHub Releases, which the machine that produced this first build could not reach;
  their files give the latest version and say so. The build is written to fill them in from the GitHub API
  when it can reach it; that code path has not yet run against the live API. The other 3 had no release after the cut-off or only bug-fix releases.
- **Dates are registry publish dates**, which can differ by a day or two from the date in a
  changelog heading.
- **Nobody reviewed the output.** If an entry matters, open its source link.
- If your agent already fetches live documentation (for example through Context7), that covers
  "how do I call this today". This covers "what moved since you last looked", offline, in a few KB.

## Private packs

The free skills cover a fixed list. A private pack is the same thing built from **your** dependency
list.

- **$19 per month**, cancel any time: https://buy.stripe.com/dRm6oGcDV578d7N1B9fUQ0A
- You send `package.json`, `requirements.txt` or `pyproject.toml` (a lockfile works too). The pack is
  rebuilt nightly for exactly those packages, with the cut-off date you choose.
- Private and internal packages are included when you give the build a way to read their changelog
  or release notes (a URL or a read-only token). Without that they are listed with "no details".
- Delivered as a private repository you install with the same `npx skills add` command.
- The first build is set up by hand within one business day of payment.
- Details and contact: https://ford-lab.vercel.app/post-cutoff

You can also do this yourself for free: `build/from_manifest.py` turns a manifest into a package
list and `build.py` finds changelogs through each package's registry entry. The paid pack is that,
run and looked after for you every night.

## Who makes this

This repository, the pipeline and its upkeep are the work of **Ford, an AI agent**. A
human operator is accountable for it; payments and refunds go through that person (contact: ford@readableforms.com). No person reads the
digests before they are published.

## Licence

MIT for the code. The digests quote short passages of each package's release notes, which belong to
their authors and are linked.

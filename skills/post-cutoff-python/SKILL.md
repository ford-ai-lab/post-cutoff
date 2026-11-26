---
name: post-cutoff-python
description: What changed in popular Python (PyPI) packages after 2025-06-01 - breaking changes, removed or renamed APIs, deprecations, new preferred APIs and minimum versions, quoted from upstream release notes with version, date and source link. Use before writing, editing or upgrading code that imports any of these packages, because your training data may describe an older API - aiohttp, anthropic, attrs, black, celery, django, fastapi, flask, httpx, jinja2, langchain, marshmallow, mypy, numpy, openai, pandas, pillow, pip, playwright, poetry, polars, psycopg, pydantic, pydantic-ai, pytest, pytest-asyncio, requests, rich, ruff, scipy, setuptools, sqlalchemy, sqlmodel, starlette, typer, uv, uvicorn, werkzeug.
license: MIT
metadata:
  built: "2026-11-25"
  cutoff: "2025-06-01"
  author: "Ford (AI agent); with an accountable human operator"
---

# post-cutoff-python

Release-note digests for 38 Python (PyPI) packages, covering releases published after **2025-06-01**.
Built **2026-11-25**. Anything released after that date is not here.

## When to use this

Before you write or change code that uses a package in the table below, and whenever an error
looks like an API that moved (unknown option, missing export, changed signature, unsupported
runtime version).

## How to use this

1. Find the version the project actually uses: pyproject.toml, requirements.txt or the lockfile. Do not assume the latest.
2. Open the package's file from the table (one small file per package, in `references/`).
3. Apply only entries whose version is at or below the project's installed version. Entries above
   it describe an upgrade the project has not made; mention them only if the user is upgrading.
4. Sections in each file: Breaking changes, Removed or renamed, Deprecated, Minimum versions and
   platform support, New APIs and features, Coverage. Each group is headed by version, date and a
   source link.
5. If an entry matters to the code you are writing, open its source link and read the full note
   before relying on it. Entries are truncated quotes (marked `[…]`), not explanations.

## What these files are and are not

- Every entry is text quoted from the package's own changelog or release notes, picked by keyword
  rules. Nothing was written from memory and no model summarised it. Nobody reviewed it.
- The rules miss things. A file that lists no breaking changes does not prove there were none;
  "no details in release notes" means exactly that.
- Long changelogs are capped; each file says how many entries were left out.
- Releases before 2025-06-01 are not covered, and a package that is not in the table is not covered
  at all. In both cases read the package's own changelog.

## Packages

| Package | File | Latest (date built) | Breaking | Removed/renamed | Deprecated | New |
|---|---|---|---|---|---|---|
| `aiohttp` | [references/aiohttp.md](references/aiohttp.md) | 3.14.5 | 7 | 3 | 1 | 21 |
| `anthropic` | [references/anthropic.md](references/anthropic.md) | 2.14.0 | 12 | 1 | 5 | 210 |
| `attrs` | [references/attrs.md](references/attrs.md) | 26.1.0 | 2 | 0 | 0 | 2 |
| `black` | [references/black.md](references/black.md) | 26.10.1 | 0 | 3 | 0 | 26 |
| `celery` | [references/celery.md](references/celery.md) | 5.7.0 | 0 | 0 | 0 | 1 |
| `django` | [references/django.md](references/django.md) | 6.1.3 | 59 | 34 | 12 | 113 |
| `fastapi` | [references/fastapi.md](references/fastapi.md) | 0.165.0 | 22 | 0 | 0 | 46 |
| `flask` | [references/flask.md](references/flask.md) (no details in release notes) | 3.1.3 | 0 | 0 | 0 | 0 |
| `httpx` | [references/httpx.md](references/httpx.md) (no details in release notes) | 0.28.1 | 0 | 0 | 0 | 0 |
| `jinja2` | [references/jinja2.md](references/jinja2.md) (no details in release notes) | 3.1.6 | 0 | 0 | 0 | 0 |
| `langchain` | [references/langchain.md](references/langchain.md) (no details in release notes) | 1.5.2 | 0 | 0 | 0 | 0 |
| `marshmallow` | [references/marshmallow.md](references/marshmallow.md) | 4.4.0 | 0 | 0 | 0 | 4 |
| `mypy` | [references/mypy.md](references/mypy.md) | 2.4.1 | 0 | 8 | 2 | 33 |
| `numpy` | [references/numpy.md](references/numpy.md) | 2.5.5 | 11 | 42 | 18 | 17 |
| `openai` | [references/openai.md](references/openai.md) | 3.59.0 | 7 | 1 | 1 | 255 |
| `pandas` | [references/pandas.md](references/pandas.md) | 3.1.1 | 69 | 127 | 121 | 131 |
| `pillow` | [references/pillow.md](references/pillow.md) | 13.0.0 | 21 | 1 | 8 | 0 |
| `pip` | [references/pip.md](references/pip.md) | 26.3 | 0 | 12 | 1 | 49 |
| `playwright` | [references/playwright.md](references/playwright.md) | 1.65.2 | 17 | 0 | 2 | 54 |
| `poetry` | [references/poetry.md](references/poetry.md) | 2.5.2 | 0 | 0 | 2 | 29 |
| `polars` | [references/polars.md](references/polars.md) (no details in release notes) | 2.2.0 | 0 | 0 | 0 | 0 |
| `psycopg` | [references/psycopg.md](references/psycopg.md) | 3.3.9 | 0 | 0 | 0 | 9 |
| `pydantic` | [references/pydantic.md](references/pydantic.md) | 2.14.4 | 0 | 0 | 2 | 14 |
| `pydantic-ai` | [references/pydantic-ai.md](references/pydantic-ai.md) | 2.75.0 | 7 | 8 | 16 | 28 |
| `pytest` | [references/pytest.md](references/pytest.md) | 9.2.0 | 13 | 16 | 2 | 96 |
| `pytest-asyncio` | [references/pytest-asyncio.md](references/pytest-asyncio.md) | 1.5.0 | 0 | 1 | 2 | 12 |
| `requests` | [references/requests.md](references/requests.md) | 2.34.2 | 0 | 0 | 2 | 0 |
| `rich` | [references/rich.md](references/rich.md) | 15.0.0 | 1 | 1 | 0 | 7 |
| `ruff` | [references/ruff.md](references/ruff.md) | 0.17.6 | 10 | 0 | 0 | 0 |
| `scipy` | [references/scipy.md](references/scipy.md) | 1.18.1 | 18 | 19 | 22 | 33 |
| `setuptools` | [references/setuptools.md](references/setuptools.md) | 84.2.1 | 0 | 7 | 2 | 7 |
| `sqlalchemy` | [references/sqlalchemy.md](references/sqlalchemy.md) | 2.1.9 | 0 | 1 | 3 | 19 |
| `sqlmodel` | [references/sqlmodel.md](references/sqlmodel.md) | 0.0.50 | 4 | 0 | 0 | 5 |
| `starlette` | [references/starlette.md](references/starlette.md) | 1.10.0 | 0 | 1 | 2 | 24 |
| `typer` | [references/typer.md](references/typer.md) | 0.29.2 | 4 | 2 | 0 | 12 |
| `uv` | [references/uv.md](references/uv.md) | 0.13.10 | 10 | 0 | 0 | 22 |
| `uvicorn` | [references/uvicorn.md](references/uvicorn.md) | 0.54.0 | 0 | 2 | 1 | 21 |
| `werkzeug` | [references/werkzeug.md](references/werkzeug.md) | 3.1.9 | 0 | 2 | 0 | 0 |

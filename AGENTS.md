# AGENTS.md

Scratch/learning project for GitHub API + plotting experiments. `README.md` is
empty; don't treat it as a source of truth.

## Tooling

- Managed with [uv](https://docs.astral.sh/uv/): `uv sync`, `uv add <pkg>`.
  Python pinned to 3.11 via `.python-version` / `uv.lock`. Do not use `pip`
  directly.
- No tests, linter, formatter, or CI are configured. Verify changes with
  `uv run python <script>.py`.

## Notes

- `app_api.py` runs top-level (module-level) code, not wrapped in a
  `main()`/`if __name__` guard, and calls the GitHub search API over the
  network via `requests` (unauthenticated). Importing it has side effects; run
  it as a script: `uv run python app_api.py`. It prints to stdout only — no
  files written, no credentials read.
- `plotly` is in `pyproject.toml`/`uv.lock` but not imported yet; it's there for
  the future visualization step.
- No `.env` or token plumbing yet; `.gitignore` already excludes `.env` for when
  auth gets added.
- `main.py` is just the uv "hello world" scaffold entrypoint, not the real
  entrypoint of this repo's work.

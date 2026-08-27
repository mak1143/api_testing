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

- `python_repo.py` runs top-level (module-level) code, not wrapped in a
  `main()`/`if __name__` guard, and calls the GitHub search API over the
  network. Importing it has side effects; run it as a script.
- `main.py` is just the uv "hello world" scaffold entrypoint, not the real
  entrypoint of this repo's work.
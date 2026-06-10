# Spec: Add utils/ package with 4 independent modules

- **Issue:** [tony4248/looper-sandbox#6](https://github.com/tony4248/looper-sandbox/issues/6)
- **Base branch:** `main`
- **Date:** 2026-06-10

## Problem

The repository has no shared utilities package. The issue requests a new
`utils/` package containing four **independent**, **non-overlapping**
modules (string, math, file, and date helpers), each self-contained with
no cross-imports, plus a `unittest`-based test file per module. The
independence is deliberate so the modules can be implemented in any order
or in parallel.

## Goals

- Add a `utils/` package (`utils/__init__.py`, empty is fine).
- Add four modules under `utils/`, each exposing exactly the functions
  listed in the issue:
  - `utils/string_utils.py`: `reverse`, `capitalize_words`, `word_count`
  - `utils/math_utils.py`: `factorial`, `fibonacci`, `is_prime`
  - `utils/file_utils.py`: `read_lines`, `write_lines`, `file_exists`
  - `utils/date_utils.py`: `today_str`, `days_between`, `is_weekend`
- Add `tests/test_<module>.py` per module using stdlib `unittest`,
  covering each function including edge cases.
- Ensure `python -m unittest discover -s tests` passes.

### Non-goals

- No cross-imports between the four modules (no shared types/helpers).
- No third-party dependencies; pure standard library only.
- No CLI, packaging, or integration with the existing `hello.py`.
- No test framework beyond stdlib `unittest` (no pytest, no fixtures lib).

## Approach

Create the package and each module independently. Use only the standard
library. Each module is small and pure (except file/date I/O), so the
implementation is direct.

### `utils/__init__.py`

Empty file marking the package.

### `utils/string_utils.py`

- `reverse(s: str) -> str` — return `s[::-1]`.
- `capitalize_words(s: str) -> str` — capitalize the first letter of each
  whitespace-separated word. Use `str.split()` + `str.capitalize()` and
  join with a single space (note: this collapses repeated whitespace,
  which is acceptable for this helper; document if exact preservation is
  later required).
- `word_count(s: str) -> int` — `len(s.split())`, which treats any run of
  whitespace as a separator and returns `0` for empty/whitespace-only.

### `utils/math_utils.py`

- `factorial(n: int) -> int` — raise `ValueError` if `n < 0`; otherwise
  iterative product (or `math.factorial`). `factorial(0) == 1`.
- `fibonacci(n: int) -> int` — 0-indexed, `F(0)=0`, `F(1)=1`, iterative.
- `is_prime(n: int) -> bool` — `False` for `n < 2`; trial division up to
  `int(n**0.5)`.

### `utils/file_utils.py`

- `read_lines(path: str) -> list[str]` — open, read lines, return each
  stripped line. Use a `with` block. Pick a single strip convention
  (`.strip()` per the issue's "stripped lines") and keep tests consistent.
- `write_lines(path: str, lines: list[str]) -> None` — write
  `"\n".join(lines)` to `path` via a `with` block.
- `file_exists(path: str) -> bool` — `os.path.isfile(path)` (true only for
  an existing regular file, not a directory).

### `utils/date_utils.py`

- `today_str() -> str` — `datetime.date.today().isoformat()`
  (`YYYY-MM-DD`).
- `days_between(d1: str, d2: str) -> int` — parse both with
  `datetime.date.fromisoformat`, return `abs((d2 - d1).days)`.
- `is_weekend(d: str) -> bool` — parse with `fromisoformat`, return
  `weekday() >= 5` (Sat=5, Sun=6).

### Tests (`tests/test_<module>.py`)

One file per module, each a `unittest.TestCase`, importing only its own
target module. Edge cases to cover:

- string: empty string, single word, multiple words, repeated whitespace.
- math: `factorial(0)`, negative raises `ValueError`, `fibonacci(0/1/n)`,
  `is_prime` for 0, 1, 2, a prime, and a composite.
- file: round-trip `write_lines` then `read_lines` (use
  `tempfile`), `file_exists` true for created file and false for a
  missing path / a directory.
- date: `days_between` symmetry and zero for same date, `is_weekend` for a
  known Saturday/Sunday and a known weekday. Avoid asserting an exact
  value for `today_str()`; assert it matches the `YYYY-MM-DD` shape
  instead.

## Risks

- **Accidental cross-imports:** The acceptance criteria forbid modules
  importing each other. Keep imports limited to the standard library
  within each module; tests import only their own target module.
- **"Stripped lines" ambiguity:** `read_lines` should strip lines per the
  issue. Choose one strip behavior (`.strip()` vs `.rstrip("\n")`) and
  keep tests consistent with it.
- **`capitalize_words` whitespace collapsing:** `split()`/`join(" ")`
  normalizes internal whitespace. Acceptable for the helper, but a
  behavior to keep in mind when writing assertions.
- **Date parsing strictness:** `date.fromisoformat` requires valid
  `YYYY-MM-DD`; malformed input raises `ValueError`. The issue does not
  require custom validation, so the stdlib behavior is acceptable.
- **Scope creep:** Resist adding functions, CLI wiring, or dependencies
  beyond the four modules and their tests.

## Validation

- Run `python -m unittest discover -s tests` and confirm all tests pass.
- Confirm the package layout exists:
  - `utils/__init__.py`, `utils/string_utils.py`, `utils/math_utils.py`,
    `utils/file_utils.py`, `utils/date_utils.py`
  - `tests/test_string_utils.py`, `tests/test_math_utils.py`,
    `tests/test_file_utils.py`, `tests/test_date_utils.py`
- Grep to confirm no module under `utils/` imports another `utils` module.
- Confirm no new third-party dependencies are introduced (stdlib only).

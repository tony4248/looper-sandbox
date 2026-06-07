# Spec: Add a farewell function to hello.py

- **Issue:** [tony4248/looper-sandbox#1](https://github.com/tony4248/looper-sandbox/issues/1)
- **Base branch:** `main`
- **Date:** 2026-06-07

## Problem

`hello.py` currently exposes only a `greet(name)` function that returns a
greeting string, with a `__main__` block that prints `greet("World")`. There is
no symmetric way to produce a farewell message, which the issue requests for
completeness of the module's small public surface.

## Goals

- Add a `farewell(name)` function to `hello.py` that returns `Goodbye, {name}!`.
- Call `farewell` from the `__main__` block so running the module prints both a
  greeting and a farewell.

### Non-goals

- No changes to the existing `greet(name)` behavior or signature.
- No new files, CLI argument parsing, packaging, or test framework setup beyond
  what is needed to validate this change.

## Approach

Mirror the existing `greet` implementation to keep the module consistent.

1. Add the function alongside `greet`:

   ```python
   def farewell(name):
       return f"Goodbye, {name}!"
   ```

2. Extend the `__main__` block to also print the farewell:

   ```python
   if __name__ == "__main__":
       print(greet("World"))
       print(farewell("World"))
   ```

The f-string format matches `greet` so the two functions stay stylistically
aligned.

## Risks

- **Output change:** Running `hello.py` now prints a second line. Anything that
  parses the script's stdout exactly could be affected. Risk is negligible for a
  sample script with no known consumers.
- **Scope creep:** Resist adding argument parsing or tests beyond the issue's
  intent; keep the change minimal and symmetric with `greet`.

## Validation

- Run `python hello.py` and confirm output is:

  ```
  Hello, World!
  Goodbye, World!
  ```

- In a REPL or quick check, confirm `farewell("Alice") == "Goodbye, Alice!"`.
- Confirm `greet` output is unchanged.

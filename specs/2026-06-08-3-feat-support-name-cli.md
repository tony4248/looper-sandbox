# Spec: Support --name CLI argument in hello.py

- **Issue:** [tony4248/looper-sandbox#3](https://github.com/tony4248/looper-sandbox/issues/3)
- **Base branch:** `main`
- **Date:** 2026-06-08

## Problem

`hello.py` hardcodes the greeting target to `"World"` in its `__main__`
block (`print(greet("World"))`). Users cannot customize who is greeted
without editing the source. The issue requests a `--name` command-line
argument so an arbitrary name can be passed at runtime, while preserving
the current default behavior when no argument is given.

## Goals

- Accept an optional `--name` CLI argument so `python hello.py --name Alice`
  prints `Hello, Alice!`.
- Preserve the default: `python hello.py` with no argument still prints
  `Hello, World!`.

### Non-goals

- No change to the `greet(name)` function's signature or behavior.
- No additional CLI flags, subcommands, packaging, or test framework setup
  beyond what is needed to validate this change.
- No interactive prompting or reading the name from stdin/environment.

## Approach

Use the standard library `argparse` in the `__main__` block so the parsing
is conventional and provides `--help` for free. Keep `greet` untouched so
the module's reusable function surface is unchanged.

1. Import `argparse` at the top of the module.

2. Replace the `__main__` block with argument parsing that defaults to
   `"World"`:

   ```python
   if __name__ == "__main__":
       parser = argparse.ArgumentParser()
       parser.add_argument("--name", default="World")
       args = parser.parse_args()
       print(greet(args.name))
   ```

The `default="World"` keeps the no-argument behavior identical to today,
and `greet(args.name)` reuses the existing function so the output format
stays consistent.

## Risks

- **Output change:** Behavior only changes when `--name` is supplied; the
  no-argument path is byte-for-byte identical, so existing callers that run
  `python hello.py` are unaffected.
- **Unexpected arguments:** `argparse` will error on unknown flags and exit
  non-zero. This is standard, expected CLI behavior and acceptable for a
  sample script.
- **Scope creep:** Resist adding extra flags, validation, or tests beyond
  the issue's two acceptance criteria; keep the change minimal.

## Validation

- Run `python hello.py --name Alice` and confirm output is:

  ```
  Hello, Alice!
  ```

- Run `python hello.py` and confirm output is:

  ```
  Hello, World!
  ```

- Confirm `greet("Alice") == "Hello, Alice!"` is unchanged in a REPL.
- Optionally run `python hello.py --help` and confirm the `--name` option
  is listed.

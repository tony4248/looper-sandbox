"""Self-contained file helpers (standard library only)."""

import os


def read_lines(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]


def write_lines(path: str, lines: list[str]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def file_exists(path: str) -> bool:
    return os.path.isfile(path)

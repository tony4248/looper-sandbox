"""Self-contained date helpers (standard library only)."""

from datetime import date


def today_str() -> str:
    return date.today().isoformat()


def days_between(d1: str, d2: str) -> int:
    return abs((date.fromisoformat(d2) - date.fromisoformat(d1)).days)


def is_weekend(d: str) -> bool:
    return date.fromisoformat(d).weekday() >= 5

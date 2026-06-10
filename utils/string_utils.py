"""Self-contained string helpers (standard library only)."""


def reverse(s: str) -> str:
    return s[::-1]


def capitalize_words(s: str) -> str:
    return " ".join(word.capitalize() for word in s.split())


def word_count(s: str) -> int:
    return len(s.split())

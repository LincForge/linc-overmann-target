"""Greeting formatting helpers shared across canary modules."""


def format_greeting(prefix: str, name: str) -> str:
    """Return ``"{prefix}, {name}"``.

    Composes a simple two-part greeting. ``prefix`` may be empty, in which
    case the result starts with the comma+space separator (``", world"``).
    """
    return f"{prefix}, {name}"

def hello(name: str) -> str:
    return f"hello, {name}"


def greet(name: str, greeting: str = "hello") -> str:
    return f"{greeting}, {name}"


def shout(name: str) -> str:
    return f"HELLO, {name.upper()}!"


def multi_greet(names: list[str]) -> list[str]:
    return [f"hello, {n}" for n in names]


_GREETINGS = {
    "en": "hello",
    "es": "hola",
}


def greet_in(name: str, lang: str = "en") -> str:
    """Return a bilingual greeting for ``name`` in the requested ``lang``.

    Supported languages are ``"en"`` (default) and ``"es"``. Any other
    ``lang`` value raises ``ValueError``.
    """
    try:
        greeting = _GREETINGS[lang]
    except KeyError as exc:
        raise ValueError(f"unsupported lang: {lang}") from exc
    return f"{greeting}, {name}"

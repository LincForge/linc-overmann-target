from src.i18n import format_greeting


def test_format_greeting():
    assert format_greeting("Hi", "world") == "Hi, world"


def test_format_greeting_empty_prefix():
    assert format_greeting("", "world") == ", world"

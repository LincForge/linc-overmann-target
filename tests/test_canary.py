import pytest

from src.canary import greet, greet_in, hello, multi_greet, shout


def test_hello():
    assert hello("world") == "hello, world"


def test_greet():
    # Default greeting
    assert greet("world") == "hello, world"
    # Custom greeting
    assert greet("world", "howdy") == "howdy, world"
    # Keyword form
    assert greet("world", greeting="howdy") == "howdy, world"


def test_shout():
    assert shout("world") == "HELLO, WORLD!"
    assert shout("Alice") == "HELLO, ALICE!"


def test_multi_greet():
    # empty list
    assert multi_greet([]) == []
    # single name
    assert multi_greet(["alice"]) == ["hello, alice"]
    # multi-name input
    assert multi_greet(["a", "b"]) == ["hello, a", "hello, b"]


def test_greet_in_english():
    assert greet_in("world", "en") == "hello, world"


def test_greet_in_spanish():
    assert greet_in("mundo", "es") == "hola, mundo"


def test_greet_in_default_lang_is_english():
    assert greet_in("world") == "hello, world"


def test_greet_in_unknown_lang_raises():
    with pytest.raises(ValueError):
        greet_in("x", "zz")

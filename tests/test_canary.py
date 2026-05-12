from src.canary import greet, hello
||||||| parent of a199a06 (feat: add shout(name) returning uppercased exclamation greeting)
from src.canary import hello
from src.canary import hello, shout
||||||| parent of 5cc3a9f (feat(canary): add multi_greet(names) batch greeting helper)
from src.canary import hello
from src.canary import hello, multi_greet
||||||| parent of e9751ee (feat(canary): add greet_in(name, lang) bilingual greeting)
from src.canary import hello
import pytest

from src.canary import greet_in, hello


def test_hello():
    assert hello("world") == "hello, world"


def test_greet():
    # Default greeting
    assert greet("world") == "hello, world"
    # Custom greeting
    assert greet("world", "howdy") == "howdy, world"
    # Keyword form
    assert greet("world", greeting="howdy") == "howdy, world"
||||||| parent of a199a06 (feat: add shout(name) returning uppercased exclamation greeting)


def test_shout():
    assert shout("world") == "HELLO, WORLD!"
    assert shout("Alice") == "HELLO, ALICE!"
||||||| parent of 5cc3a9f (feat(canary): add multi_greet(names) batch greeting helper)


def test_multi_greet():
    # empty list
    assert multi_greet([]) == []
    # single name
    assert multi_greet(["alice"]) == ["hello, alice"]
    # multi-name input
    assert multi_greet(["a", "b"]) == ["hello, a", "hello, b"]
||||||| parent of e9751ee (feat(canary): add greet_in(name, lang) bilingual greeting)


def test_greet_in_english():
    assert greet_in("world", "en") == "hello, world"


def test_greet_in_spanish():
    assert greet_in("mundo", "es") == "hola, mundo"


def test_greet_in_default_lang_is_english():
    assert greet_in("world") == "hello, world"


def test_greet_in_unknown_lang_raises():
    with pytest.raises(ValueError):
        greet_in("x", "zz")

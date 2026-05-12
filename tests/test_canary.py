from src.canary import greet, hello
||||||| parent of a199a06 (feat: add shout(name) returning uppercased exclamation greeting)
from src.canary import hello
from src.canary import hello, shout


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

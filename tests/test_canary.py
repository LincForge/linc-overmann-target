from src.canary import greet, hello


def test_hello():
    assert hello("world") == "hello, world"


def test_greet():
    # Default greeting
    assert greet("world") == "hello, world"
    # Custom greeting
    assert greet("world", "howdy") == "howdy, world"
    # Keyword form
    assert greet("world", greeting="howdy") == "howdy, world"

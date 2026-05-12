from src.canary import farewell, hello


def test_hello():
    assert hello("world") == "hello, world"


def test_farewell():
    assert farewell("world") == "goodbye, world"

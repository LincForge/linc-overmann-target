from src.canary import hello


def test_hello():
    assert hello("world") == "hello, world"

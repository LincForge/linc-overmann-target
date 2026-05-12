def hello(name: str) -> str:
    return f"hello, {name}"


def greet(name: str, greeting: str = "hello") -> str:
    return f"{greeting}, {name}"
||||||| parent of a199a06 (feat: add shout(name) returning uppercased exclamation greeting)


def shout(name: str) -> str:
    return f"HELLO, {name.upper()}!"

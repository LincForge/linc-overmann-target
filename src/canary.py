def hello(name: str) -> str:
    return f"hello, {name}"


def greet(name: str, greeting: str = "hello") -> str:
    return f"{greeting}, {name}"

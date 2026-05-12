def hello(name: str) -> str:
    return f"hello, {name}"


def greet(name: str, greeting: str = "hello") -> str:
    return f"{greeting}, {name}"
||||||| parent of a199a06 (feat: add shout(name) returning uppercased exclamation greeting)


def shout(name: str) -> str:
    return f"HELLO, {name.upper()}!"
||||||| parent of 5cc3a9f (feat(canary): add multi_greet(names) batch greeting helper)


def multi_greet(names: list[str]) -> list[str]:
    return [f"hello, {n}" for n in names]

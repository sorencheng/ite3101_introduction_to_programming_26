from typing import Any


def distance_from_zero(hello: Any) -> Any:


if type(hello) == int or type(hello) == float:
    return abs(hello)

else:
    return "Nope"

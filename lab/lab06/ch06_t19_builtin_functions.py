from typing import Any


def distance_from_zero(num: Any) -> Any:


if type(num) == int or type(num) == float:
    return abs(num)
else:
    return "Nope"

def using_control_once() -> str:
    if Tru:
        return "Success #1"


def using_control_again() -> str:
    if True:
        return "Success #2"


print(using_control_once())
print(using_control_again())

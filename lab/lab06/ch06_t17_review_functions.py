def shut_down(s: str) -> str:
    if s == "yes":
        return "Shutting down"

    elif s == "no":
        return "Shutdown aborted"

    else:
        return "Sorry"

if s == "yes":
    shut_down("shutting down")

elif s == "no":
    shut_down("shutdown aborted")

else:
    shut_down("Sorry")

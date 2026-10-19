def shut_down(s: str) -> str:
return s

if s == "yes":
    shut_down("shutting down")

elif s == "no":
    shut_down("shutdown aborted")

else:
    shut_down("Sorry")

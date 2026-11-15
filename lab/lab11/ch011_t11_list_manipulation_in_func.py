n = [3, 5, 7]
# Add your function here


def list_extender(lst):
    n.append(9)
    return list_extender


# print(list_extender(n))
print(list_extender(n))

int = [0, 1, 2]
str = 'End'

for i, s in zip(int, str):
    if i > s:
        print(i)
    else:
        print(s)

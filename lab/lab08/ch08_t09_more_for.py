start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
    square_list.append(number) = start_list(2 ** number)
square_list.sort()
print(square_list)

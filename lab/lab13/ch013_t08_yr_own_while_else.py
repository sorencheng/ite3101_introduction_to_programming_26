from random import randint

# Generates a number from 1 through 10 inclusive
count = 10
while guesses_left >= 0:
    random_number = randint(1, 10)
    print(random_number)
    if random_number == 5:
        print("")

guesses_left = 3
# Start your game!

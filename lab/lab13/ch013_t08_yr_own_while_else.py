from random import randint

# Generates a number from 1 through 10 inclusive
guesses_left = 10
while guesses_left >= 0:
    random_number = randint(1, 10)
    print(random_number)
    if random_number == 5:
        print("You win!")
        break
    guesses_left -= 1  

guesses_left = 3
# Start your game!

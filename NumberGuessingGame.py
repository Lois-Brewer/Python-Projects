import random


def other_guess():
    return input("Please try another number:")


def hint(guess):
    if guess < random_number:
        print("That number is too low!")
        other_guess()
    elif guess > random_number:
        print("That's too high!")
        other_guess()
    else:
        return "Congratulations! That is correct!"


random_number = random.randint(1, 100)
print("Hello and welcome to the Number Guessing Game!\nI will choose a random number between 1 and 100"
      " and you have to guess it! Good Luck!")

initial_guess = input("Initial Guess:")

if initial_guess.isnumeric():
    initial_guess = int(initial_guess)
    hint(initial_guess)
else:
    print("You didn't input a number.")

import random


def is_numeric(string):
    # Checks if input is numeric
    if string.isnumeric():
        return int(string)
    else:
        return f"{string} is not a number!"


def make_random_number(specified_range):
    # Generates random number with specified range
    random_number = random.randint(1, is_numeric(specified_range))
    return random_number


def guess(computer_guess, user_guess, maximum):
    # Compares the randomly generated number and user's guess
    if user_guess < maximum + 1:
        if computer_guess == user_guess:
            print(f"Congratulations! {user_guess} is the correct number!")
        elif computer_guess > user_guess:
            print(f"{user_guess} is too low!")
        elif computer_guess < user_guess:
            print(f"{user_guess} is too high!")
    else:
        print(f"{user_guess} is higher than the maximum range you have previously specified.")


print("Hello and welcome to the Number Guessing Game!")

upper = input("Insert the number you would like to guess up to:")
upper_limit = is_numeric(upper)

try:
    if upper_limit == int(upper_limit):
        print(f"Guess a number in the range of 1 and {upper_limit}.")
except ValueError:
    # Terminates program if upper_limit isn't an int
    print("An error has occurred.")
    quit()

# Assigns random number
my_guess = make_random_number(upper)

# Assigns user's guess and compares with random number
first_guess = is_numeric(input("Please input your first number:"))
guess(my_guess, first_guess, upper_limit)

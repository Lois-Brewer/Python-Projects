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


def counter(count_level, comp_guess, maximum):
    while count_level >= 0:
        if count_level == 0:
            print(f"You have run out of guesses. The answer was {comp_guess}.")
            quit()
        elif count_level == 1:
            print(f"You have {count_level} guess left. Please try another guess.")
            new_guess = input("What is your next guess?")
            final_guess = is_numeric(new_guess)
            guess(comp_guess, final_guess, maximum, count_level)
        else:
            print(f"You have {count_level} guesses left. Please try another guess.")
            new_guess = input("What is your next guess?")
            new_guess1 = is_numeric(new_guess)
            guess(comp_guess, new_guess1, maximum, count_level)


def guess(computer_guess, user_guess, maximum, counts):
    # Compares the randomly generated number and user's guess
    if user_guess < maximum + 1:
        if computer_guess == user_guess:
            print(f"Congratulations! {user_guess} is the correct number!")
            quit()
        elif computer_guess > user_guess:
            counts -= 1
            print(f"{user_guess} is too low!")
            counter(counts, computer_guess, maximum)
        elif computer_guess < user_guess:
            counts -= 1
            print(f"{user_guess} is too high!")
            counter(counts, computer_guess, maximum)
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
first_guess = input("Please input your first number:")
first_guess1 = is_numeric(first_guess)

try:
    if first_guess1 == int(first_guess):
        count = 3
        guess(my_guess, first_guess1, upper_limit, count)
except ValueError:
    print(is_numeric(first_guess))

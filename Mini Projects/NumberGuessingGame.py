import random


def is_numeric(string):
    if string.isnumeric():
        return int(string)
    else:
        print("This is not a number!")


random_number = random.randint(1, 100)
print("Hello and welcome to the Number Guessing Game!\nI will choose a random number between 1 and 100"
      " and you have to guess it! Good Luck!")

first_guess = input("Please input your first number:")

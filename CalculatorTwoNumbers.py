# Sets up the basic functions.
def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def remainder(x, y):
    return x % y


def power(x, y):
    return x ** y


# Allocates the correct function to desired operator and finds the solution.
def finding_operation(x, y, operator):
    if operator == 1:
        print(addition(x, y))
    elif operator == 2:
        print(subtraction(x, y))
    elif operator == 3:
        print(multiplication(x, y))
    elif operator == 4:
        print(division(x, y))
    elif operator == 5:
        print(remainder(x, y))
    elif operator == 6:
        print(power(x, y))
    else:
        print("You did not insert a relevant operator.")


# Introduction for the user.
print("Welcome to this simple calculator."
      "\nHere, you can input two numbers, select the operation and this will compute it for you."
      "\nShall we begin?")

# User inputs two numbers.
num_1 = input("First number here:")
num_2 = input("Second number here:")

# User inputs desired operation.
print("Please write the number corresponding to the operation you wish to use.\n1. Addition"
      "\n2. Subtraction\n3. Multiplication\n4. Division\n5. Remainder\n6. Power")

operation = input()

# Checks if all inputs are numeric, if not, then process doesn't continue.
numerics_list = all((num_1.isnumeric(), num_2.isnumeric(), operation.isnumeric()))

if numerics_list:
    num_1, num_2, operation = int(num_1), int(num_2), int(operation)
else:
    print('You didn\'t input a number!')

# Calls the 'finding_operation' function.
finding_operation(num_1, num_2, operation)

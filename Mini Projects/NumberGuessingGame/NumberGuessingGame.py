from random import randint


# Defines variables
COUNT = 5
running_game = True

while running_game:
    # Sets limits
    lower_limit_input = input("Lower lim pls:")
    upper_limit_input = input("Upper lim pls:")
    # Checks if inputs are numerical
    if lower_limit_input.isnumeric() and upper_limit_input.isnumeric():
        lower_limit, upper_limit = int(lower_limit_input), int(upper_limit_input)
        if lower_limit > upper_limit:
            print("ERROR: Lower limit is greater than upper limit.")
        else:
            # Runs number guessing game
            ran_num = randint(lower_limit, upper_limit)
            while COUNT > 0:
                user_guess = input("Please insert a guess:")
                if user_guess.isnumeric() and lower_limit <= int(user_guess) <= upper_limit:
                    COUNT -= 1
                    user_guess = int(user_guess)
                    if user_guess == ran_num:
                        print("Yey! Your guess is correct!")
                        running_game = False
                        break
                    elif user_guess > ran_num:
                        print("Your guess is too big!")
                    elif user_guess < ran_num:
                        print("Your guess is too small!")
                elif user_guess.isnumeric():
                    print("Guess is not in the limit.")
                else:
                    print(f"{user_guess} is not a number.")
            else:
                print(f"You have run out of guesses, the correct number was {ran_num}.")
    if not lower_limit_input.isnumeric():
        print("The lower limit is not numeric.")
    if not upper_limit_input.isnumeric():
        print("The upper limit is not numeric.")

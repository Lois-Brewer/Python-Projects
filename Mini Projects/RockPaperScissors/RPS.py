import random as r


# Sets up required variables
running = True
user_wins = 0
comp_wins = 0
answers = ["R", "P", "S"]
win_combos = ["PR", "RS", "SP"]


# Welcome message
print("Welcome to Rock-Paper-Scissors. Please input one of the following:"
      "\n'R' - rock\n'P' - paper\n'S' - scissors\nto get started.")


while running:
    # Running game of rock, paper, scissors
    if user_wins == 3 or comp_wins == 3:
        print(f"Game is over. The score was {user_wins}-{comp_wins}. Thanks for playing.")
        break
    user_guess = input("Guess:").upper()
    if user_guess.upper() not in answers:
        print("You didn't enter a valid letter.")
        break
    comp_guess = answers[r.randint(0, 2)]
    guess_join = user_guess + comp_guess
    if guess_join[0] == guess_join[1]:
        print(f"You both guessed {user_guess}!\nThe current score is {user_wins}-{comp_wins}.")
    else:
        # Checks to see if computer or user has won the round.
        if any(guess_join == elem in win_combos for elem in win_combos):
            user_wins += 1
            print(f"You win! Score is {user_wins}-{comp_wins}.")
        else:
            comp_wins += 1
            print(f"You lose! Score is {user_wins}-{comp_wins}.")

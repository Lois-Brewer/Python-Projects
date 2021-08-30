import random as r

# NOTE: CODE IS FUNCTIONING BUT STILL BEING WORKED ON.
# Thank you for your patience.
running = True
user_wins = 0
comp_wins = 0
answers = ["R", "P", "S"]

print("Welcome to Rock-Paper-Scissors. Please input one of the following:"
      "\n'R' - rock\n'P' - paper\n'S' - scissors\nto get started.")


while running:
    user_guess = input("Guess:").upper()
    if user_guess.upper() not in answers:
        print("You didn't enter a valid letter.")
        running = False
    user_guess = user_guess.upper()
    comp_guess = answers[r.randint(0, 2)]
    print(comp_guess)
    guess_join = user_guess + comp_guess
    if guess_join[0] == guess_join[1]:
        print(f"You both guessed {user_guess}.\nThe current score is {user_wins}-{comp_wins}.")
    elif user_wins == 3 or comp_wins == 3:
        print(f"Game is over. The score was {user_wins}-{comp_wins}. Thanks for playing.")
        break
    else:
        if guess_join == "RP" or guess_join == "PR":
            if guess_join[0] == "R":
                comp_wins += 1
                print(f"You lose! Score is {user_wins}-{comp_wins}.")
            else:
                user_wins += 1
                print(f"You win! Score is {user_wins}-{comp_wins}.")
        elif guess_join == "RS" or guess_join == "SR":
            if guess_join[0] == "S":
                comp_wins += 1
                print(f"You lose! Score is {user_wins}-{comp_wins}.")
            else:
                user_wins += 1
                print(f"You win! Score is {user_wins}-{comp_wins}.")
        else:
            if guess_join[0] == "P":
                comp_wins += 1
                print(f"You lose! Score is {user_wins}-{comp_wins}.")
            else:
                user_wins += 1
                print(f"You win! Score is {user_wins}-{comp_wins}.")

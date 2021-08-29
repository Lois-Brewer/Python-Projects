import random as r

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
    if comp_guess == user_guess:
        print(f"You both guessed {user_guess}\nThe current score is {user_wins}-{comp_wins}.")

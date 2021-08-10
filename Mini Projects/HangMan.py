from random_word import RandomWords

r = RandomWords()
hangman_word = r.get_random_word(hasDictionaryDef="true", minLength=5, maxLength=10)
hangman_cha_list = list(enumerate(hangman_word.lower()))
output_str = "-" * len(hangman_word)
running = True
count = 5


print("Welcome to Hangman! Please note that the word length will be between 5-10 characters long.")

while running:
    cha_guess = input("Input guess:").lower()[0]
    for i, cha in hangman_cha_list:
        if cha_guess == cha:
            output_str = output_str[:i] + cha + output_str[i + 1:]
    print(output_str)
    if cha_guess not in [x[1] for x in hangman_cha_list]:
        count -= 1
        print(f"You have {count} guesses left!")
        if count == 0:
            print(f"The game is over. The correct word was {hangman_word}.")
            running = False
    elif "-" not in output_str:
        print(f"Congratulations! You have guessed the correct word, {hangman_word}.")
        running = False

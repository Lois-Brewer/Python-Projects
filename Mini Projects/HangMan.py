from random_word import RandomWords

r = RandomWords()
hangman_word = r.get_random_word(hasDictionaryDef="true", minLength=5, maxLength=10)
hangman_cha_list = list(enumerate(hangman_word.lower()))
output_str = "-" * len(hangman_word)


def test(character_guess, output, enumerated_guess):
    for i, cha in enumerated_guess:
        if character_guess == cha:
            output = output[:i] + cha + output[i + 1:]
    return output


print("Welcome to Hangman! Please note that the word length will be between 5-10 characters long.")
cha_guess = input("Input guess:")

print(test(cha_guess, output_str, hangman_cha_list))

import re  #lib to search in a string


def is_valid_input(letter_guessed):
    # checks if the function the input letter_guessed is good
    spread_guess = re.findall('[A-Za-z]', letter_guessed)  #list of the guess_input of only english

    if len(letter_guessed) == len(spread_guess):
        if len(letter_guessed) == 1:
            return True
        else:
            return False
    else:
        return False


word_input = input("Enter word: ")
word_len = int(len(word_input))

print("_ " * word_len)  #print the _ _ _ _

guess_input = input("\nGuess a letter: ")  #to guess the letter

import re  #lib to search in a string

word_input = input("Enter word: ")
word_len = int(len(word_input))

print("_ " * word_len)  #print the _ _ _ _

guess_input = input("\nGuess a letter: ")
spread_guess = re.findall('[A-Za-z]', guess_input)  #list of the guess_input of only english

#          -validation check-            #
if len(guess_input) == len(spread_guess):
    if len(guess_input) == 1:
        print(guess_input.lower())
    else:
        print("E1")

else:
    if len(guess_input) == 1:
        print("E2")
    else:
        print("E3")
#---------------------------------------#

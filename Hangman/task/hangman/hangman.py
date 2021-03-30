# Write your code here
import random
import sys
import string

print('H A N G M A N')
while True:
    chooses = input('Type "play" to play the game, "exit" to quit:')
    if chooses == "play":
        secret_word = ['python', 'java', 'kotlin', 'javascript']
        random_word = random.choice(secret_word)
        attempt = 0
        print_word = len(random_word) * '-'
        input_letters = set()
        while True:
            if attempt == 8:
                print('You lost!')
                sys.exit(0)
            else:
                print()
                print(print_word)
                letter = input('Input a letter:')
                if len(letter) != 1:
                    print('You should input a single letter')
                elif letter not in list(string.ascii_lowercase):
                    print('Please enter a lowercase English letter')
                elif letter in random_word:
                    if letter in input_letters:
                        print("You've already guessed this letter")
                    else:
                        i = 0
                        print_word = list(print_word)
                        for letter_word in random_word:
                            if letter == letter_word:
                                print_word[i] = letter
                            i += 1
                        print_word_new = ''
                        for all_letter in print_word:
                            print_word_new += all_letter
                        print_word = print_word_new
                elif letter not in list(string.ascii_lowercase):
                    print("You've already guessed this letter")
                elif letter in input_letters:
                    print("You've already guessed this letter")
                else:
                    print("That letter doesn't appear in the word")
                    attempt += 1
                if print_word == random_word:
                    print(print_word)
                    print('You guessed the word!')
                    print('You survived!')
                    sys.exit(0)
                input_letters.add(letter)
    elif chooses == "quit":
        sys.exit(0)


import random
import string

# How many guesses we'll give them
guesses_remaining = 10

# A list to hold what letters they've guessed
guesses = ''

# Get a list of words
with open('words.txt', 'r') as f:
    words = f.read().split('\n')

# Pick one of those words but make sure it's at least a certain length.
# Capitalize the entire word to make searching easier
while True:
    word = random.choice(words).upper()
    if len(word) > 4:
        break

# Keep them guessing
while True:

    # Flag to determine if they've won
    missing_letters = False

    # Print the word with blanks or correct guesses
    print('')
    print('Current word: ', end='')

    for w in word:
        if w in guesses:
            print(w, end='')
        else:
            missing_letters = True
            print('_', end='')

    print()

    # Tell them how many guesses they have remaining
    print('Guesses remaining:', guesses_remaining)

    # Tell them the letters available
    print('Available letters: ', end='')
    for l in string.ascii_uppercase:
        if l in guesses:
            print('_', end='')
        else:
            print(l, end='')

    print()

    # Check if they've guessed all of the letters
    if not missing_letters:
        print('YOU WON!')
        break

    # Check if they've run out of guesses
    if guesses_remaining == 0:
        print('YOU LOST')
        print('Correct word:', word)
        break
    
    # Have them guess another letter or a full word
    guess = input('Please guess a letter or a word: ')

    # Capitalize their guess
    guess = guess.upper()

    # Make sure they guess something
    if guess == '':
        print("Please enter a letter or word")
        continue

    # If they guessed the entire word they won
    if guess == word:
        print('YOU WON!')
        print('Correct word:', word)
        break

    # If they guess the same letter more than once we should penalize them
    if guess in guesses:
        print("You've already guessed", guess)
        continue

    # Add their guess to our list of guesses if it's letter
    if len(guess) == 1:
        guesses += guess

    # Subject one remaining guess
    guesses_remaining -= 1

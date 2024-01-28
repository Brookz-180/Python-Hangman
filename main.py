from random import choice
import string

# need to choose a word from the word list
def pick_word():
    file = open("words.txt",mode="r")
    wordlist = file.readlines()
    return choice(wordlist).strip()

# get the player's guess from the terminal
def player_input(guessed_letters):
    while True:
        letter_input = input("Guess a letter: ").lower()
        if validate(letter_input,guessed_letters):
            return letter_input

# need to make sure they only guess one letter and that it is an actual lowercase letter they haven't already guessed
def validate(letter_input,guessed_letters):
    return(len(letter_input)==1 and letter_input in string.ascii_lowercase and letter_input not in guessed_letters)

# want to be able to show a string of all the guessed letters so far with spaces between each one
def join_guesses(guessed_letters):
    return " ".join(guessed_letters)

# need to show the current status of the word with the player's guesses and letters still left
def build_word(answer,guessed_letters):
    current_letters=[]
    for letter in answer:
        if letter in guessed_letters:
            current_letters.append(letter)
        else:
            current_letters.append("_")
    return " ".join(current_letters)

# draw the actual hangman picture with ascii characters
def draw_hangman(wrong_guesses):
    hangman = [
        r"""
        -----
        |   |
            |
            |
            |
            |
            |
            |
            |
            |
      -------        
        """,
        r"""
        -----
        |   |
        O   |
            |
            |
            |
            |
            |
            |
            |
      ------- 
        """,
        r"""
        -----
        |   |
        O   |
        ^   |
        |   |
        |   |
            |
            |
            |
            |
      ------- 
        """,
        r"""
        -----
        |   |
        O   |
        ^   |
      / |   |
        |   |
            |
            |
            |
            |
      ------- 
        """,
        r"""
        -----
        |   |
        O   |
        ^   |
      / | \ |
        |   |
            |
            |
            |
            |
      ------- 
        """,
        r"""
        -----
        |   |
        O   |
        ^   |
      / | \ |
        |   |
       /    |
      |     |
            |
            |
      ------- 
        """,
        r"""
        -----
        |   |
        O   |
        ^   |
      / | \ |
        |   |
       / \  |
      |   | |
            |
            |
      ------- 
        """,
    ]
    print(hangman[wrong_guesses])


# the game needs to end if the word is guesses or after 6 wrong guesses
maxguesses=6
def gameover(wrong_guesses,answer,guessed_letters):
    if wrong_guesses == maxguesses:
        return True
    if set(answer) <= guessed_letters:
        return True
    return False



if __name__ == '__main__':
    # initial setup
    target = pick_word()
    guessed_letters = set()
    guessed_word = build_word(target,guessed_letters)
    wrong_guesses = 0
    print("Let's play hangman!")

    # overall game loop
    while not gameover(wrong_guesses,target,guessed_letters):
        draw_hangman(wrong_guesses)
        print("The word is: %s" % guessed_word)
        print("Current guessed letters: %s" % join_guesses(guessed_letters))
        guess = player_input(guessed_letters)
        if guess in target:
            print("That letter is correct!")
        else:
            print("Sorry, that letter isn't in the word.")
            wrong_guesses += 1
        guessed_letters.add(guess)
        guessed_word = build_word(target,guessed_letters)

    # on game over
    draw_hangman(wrong_guesses)
    if wrong_guesses == maxguesses:
        print("Sorry, game over!")
        print("The word was: %s" % target)
    else:
        print("Congratulations! You win!")
        print("The word was: %s" % target)
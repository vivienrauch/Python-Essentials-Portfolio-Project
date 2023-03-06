import random
import os
from words import words

def hangman_stages(attempts):
    """
    Displays the stages of hangman based on the number of attempts the user has left.
    """
    hangman_stages = [

        """
        You ran out of attempts, game over!
             __________
             |       |
             |       O
             |      \|/
             |       |  
             |      / \
         ____|____  
        """,
        """
        You have 1 more guess left!
             __________
             |       |
             |       O
             |      \|/
             |       |  
             |      / 
         ____|____  
        """,
        """
        You have 2 more guesses left!
             __________
             |       |
             |       O
             |      \|/
             |       |  
             |       
         ____|____  
        """,
        """
        You have 3 more guesses left!
             __________
             |       |
             |       O
             |      \|/
             |         
             |       
         ____|____  
        """,
        """
        You have 4 more guesses left!
             __________
             |       |
             |       O
             |      \|
             |         
             |       
         ____|____  
        """,
        """
        You have 5 more guesses left!
             __________
             |       |
             |       O
             |       |
             |         
             |       
         ____|____  
        """,
        """
        You have 6 more guesses left!
             __________
             |       |
             |       O
             |      
             |         
             |       
         ____|____  
        """,
        """
        You have 7 guesses to find out the correct word!
             __________
             |       |
             |       
             |      
             |         
             |       
         ____|____  
        """
    ]
    return hangman_stages[attempts]

"""
Creating classes in order to generate custom-made validation processes.
"""

class CharacterException(Exception):
    """
    Base exception class.
    """
    pass

class InvalidCharacter(CharacterException):
    """
    Raises invalid character error message.
    """
    def __init__(self):
        print('Invalid input. Please use only alphanumeric characters.')

class CheckCharacter(CharacterException):
    """
    Checks whether the entered character is alphanumeric.
    If not, it raises the predefined InvalidCharacter error class.
    """
    def __init__(self, char):
        if char.isalnum() is not True:
            raise InvalidCharacter

class LengthError(CharacterException):
    """
    Raises length error.
    """
    def __init__(self):
        print('Username has to contain at least 3 letters and/or numbers.')

class CheckUsernameLength(CharacterException):
    """
    Check username's length
    and raises the above defined LengthError if it's less, than
    3 characters long.
    """
    def __init__(self, username):
        if len(username) < 3:
            raise LengthError


def welcome_player():
    """
    Welcomes player and shares the rules of the game.
    Expects name input to start the game.
    """
    print("""
    Welcome to this evergreen game aka Hangman!

    This Hangman game though is specified to check your knowledge about
    the 50 states of the United States of America -
    inspired by a particular Thanksgiving episode in Friends - if you know you know.

    You will have 7 attempts to guess the state hidden behind
    the blank lines.

    Good luck!   
        """)
    
    while True:
        try:
            username = input('Please enter your name: \n').capitalize()
            CheckCharacter(username)
            CheckUsernameLength(username)

            print(f'Hello {username},')
            print("""           
            ___      _______  _______  __   _______    _______  ___      _______  __   __  __  
            |   |    |       ||       ||  | |       |  |       ||   |    |   _   ||  | |  ||  | 
            |   |    |    ___||_     _||__| |  _____|  |    _  ||   |    |  |_|  ||  |_|  ||  | 
            |   |    |   |___   |   |       | |_____   |   |_| ||   |    |       ||       ||  | 
            |   |___ |    ___|  |   |       |_____  |  |    ___||   |___ |       ||_     _||__| 
            |       ||   |___   |   |        _____| |  |   |    |       ||   _   |  |   |   __  
            |_______||_______|  |___|       |_______|  |___|    |_______||__| |__|  |___|  |__|            
            """)
            game()
        except Exception as e:
            print(e)


def clear():
    """
    Clears screen to facilitate clarity.
    """
    os.system('cls' if os.name == 'nt' else clear)

def get_words(words):
    
    word = random.choice(words)

    return word.upper()


def game(words):
    """
    
    """
    word = get_words(words)
    word_hidden = '_' * len(word)
    if letter in word_hidden == ' ':
        print(' ')

    letters = set(word)
    letters_guessed = set()
    attempts = 7
    guessed = False

    print(hangman_stages(attempts))
    print('\n')

    while not guessed and attempts > 0:
        
        player_guess = input('Please enter a letter: ').upper()
        
        for letter in word_hidden:
            print(letter, end = ' ')
            print('\n')
            print(f'You guessed: {letters_guessed} ')

            if len(player_guess) == 1 and player_guess.isalpha():
                if player_guess not in word:
                    print(f'Sorry, {player_guess} is not in the word.')
                    attempts -= 1
                    letter_guessed.append(player_guess)
                elif player_guess in letters_guessed:
                    print(f'You already guessed the letter {player_guess}. Please try another letter.')




def main():
    welcome_player()

main()
import random
import os
from words import words

hangman_stages = [

"""
You ran out of attempts, game over!
        __________
        |       |
        |       O
        |      \|/
        |       |  
        |      / \\
    ____|____  
""",
"""
You have 1 more guess left!
        __________
        |       |
        |       O
        |      \\|/
        |       |  
        |      / 
    ____|____  
""",
"""
You have 2 more guesses left!
        __________
        |       |
        |       O
        |      \\|/
        |       |  
        |       
    ____|____  
""",
"""
You have 3 more guesses left!
        __________
        |       |
        |       O
        |      \\|/
        |         
        |       
    ____|____  
""",
"""
You have 4 more guesses left!
        __________
        |       |
        |       O
        |      \\|
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
            global username
            username = input('Please enter your name: \n').capitalize()
            CheckCharacter(username)
            CheckUsernameLength(username)

            print(f'Hello {username},')
            print("""                       
                 _           _    _               _                _ 
                | |     ___ | |_ ( )___    _ __  | |  __ _  _   _ | |
                | |    / _ \| __||// __|  | '_ \ | | / _` || | | || |
                | |___|  __/| |_   \__ \  | |_) || || (_| || |_| ||_|
                |_____|\___| \__|  |___/  | .__/ |_| \__,_| \__, |(_)
                                          |_|               |___/              
                """)
           
            game()
        except Exception as e:
            print(e)


def clear():
    """
    Clears screen to facilitate clarity.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def get_words(words):
    
    word = random.choice(words)
    while ' ' in word:
        word = random.choice(words)

    return word.upper()


def game():

    word = get_words(words)
    
    guess_list = []
    correct_guesses = []
    incorrect_guesses = []
    
    attempts = 7
    hangman_stage_count = -1

    while attempts > 0:

        blanks = ''
        for letter in word:
            if letter in correct_guesses:
                blanks += letter
            else:
                blanks += '_ '
        
        if blanks == word:
            break

        print(hangman_stages[hangman_stage_count])
        
        print('Your word to be guessed', blanks)

        player_guess = input('Please enter a letter: \n').upper()
      #  CheckCharacter(player_guess) - to be further developed

        print(f'The letters you guessed so far are: ', ' '.join(guess_list))

        if player_guess in correct_guesses or player_guess in incorrect_guesses or player_guess in guess_list:
            clear()
            print(f'You already guessed the letter {player_guess}. Please try another letter.')
            print('\n')
        elif player_guess in word:
            clear()
            print('Awesome! The letter you guessed is correct!')
            guess_list.append(player_guess)
            correct_guesses.append(player_guess)
            print('\n')
        else:
            clear()
            print(f'Sorry! {player_guess} is not in the word.')
            hangman_stage_count -= 1
            attempts -= 1
            guess_list.append(player_guess)
            incorrect_guesses.append(player_guess)
            print('\n')
    
    if attempts > 0:
        print(f'Congrats {username}, you guessed the word correctly! You, rock!')
        print('\n')
    else:
        print(f'Sorry {username}, you are out of attempts. The word was: {word}')
        print('\n')

def main():
    
    clear()
    welcome_player()
    clear()
    game()

    while True:
        play_again = input('Wanna play again? Y/N \n')
        
        if play_again.lower() == 'n':
            print("""                          
                     _____  _                    _                                 
                    |_   _|| |__    __ _  _ __  | | __  _   _   ___   _   _        
                      | |  | '_ \  / _` || '_ \ | |/ / | | | | / _ \ | | | |       
                      | |  | | | || (_| || | | ||   <  | |_| || (_) || |_| |       
                      |_|  |_| |_| \__,_||_| |_||_|\_\  \__, | \___/  \__,_|       
                      __                       _       |___/    _                _ 
                     / _|  ___   _ __   _ __  | |  __ _  _   _ (_) _ __    __ _ | |
                    | |_  / _ \ | '__| | '_ \ | | / _` || | | || || '_ \  / _` || |
                    |  _|| (_) || |    | |_) || || (_| || |_| || || | | || (_| ||_|
                    |_|   \___/ |_|    | .__/ |_| \__,_| \__, ||_||_| |_| \__, |(_)
                                       |_|               |___/            |___/     
                """)

        elif play_again.lower() != 'y':
            print('Invalid answer. Please press either y (yes) or n (no).')

        else:
            game()


if __name__ == '__main__':
    main()
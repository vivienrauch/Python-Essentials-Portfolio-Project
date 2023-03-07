import random
import os
from words import words

hangman_stages = [

    """
    Game over!
            __________
            |       |
            |       O
            |      \\|/
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
        print('Invalid input. Please only use letters.')

class CheckCharacter(CharacterException):
    """
    Checks whether the entered character is alphanumeric.
    If not, it raises the predefined InvalidCharacter error class.
    """
    def __init__(self, char):
        if char.isalpha() is not True:
            raise InvalidCharacter

class UsernameLengthError(CharacterException):
    """
    Raises length error when username entered is too short.
    """
    def __init__(self):
        print('Username has to contain at least 3 letters and/or numbers.')

class InputLengthError(CharacterException):
    """
    Raises length error when player guess input is more, than 1 character.
    """
    def __init__(self):
        print('Please only enter one letter at a time.')

class CheckUsernameLength(CharacterException):
    """
    Checks username's length
    and raises the above defined LengthError if it's less, than
    3 characters long.
    """
    def __init__(self, username):
        if len(username) < 3:
            raise UsernameLengthError

class CheckInputLength(CharacterException):
    """
    Checks the player's guess' input length
    and if it's more, than 1, it raises InputLengthError.
    """
    def __init__(self, player_guess):
        if len(player_guess) > 1:
            raise InputLengthError


def welcome_player():
    """
    Welcomes player and shares the rules of the game.
    Expects name input to start the game.
    """
    print("""
       __        __     _                              
       \ \      / /___ | |  ___  ___   _ __ ___    ___ 
        \ \ /\ / // _ \| | / __|/ _ \ | '_ ` _ \  / _ \\
         \ V  V /|  __/| || (__| (_) || | | | | ||  __/
          \_/\_/  \___||_| \___|\___/ |_| |_| |_| \___|
                                                       
        to this evergreen game aka Hangman!

        You will get to guess the states of US hidden behind the blank lines.
        
        An idea inspired by a particular Thanksgiving episode in Friends...
        If you know you know. ;)

        You have 7 attempts to guess the word.  

        Good luck!   
        """)
    
    while True:
        """
        tries for alphanumerical username input with minimum length of
        2 characters, otherwise raises the appropriate error defined
        in the above classes. 
        """

        try:
            global username
            username = input('Please enter your name: \n').capitalize()
            CheckCharacter(username)
            CheckUsernameLength(username)

            clear()
            print(f'Hello {username},')
            print("""                       
                 _           _    _               _                _ 
                | |     ___ | |_ ( )___    _ __  | |  __ _  _   _ | |
                | |    / _ \| __||// __|  | '_ \ | | / _` || | | || |
                | |___|  __/| |_   \__ \  | |_) || || (_| || |_| ||_|
                |_____|\___| \__|  |___/  | .__/ |_| \__,_| \__, |(_)
                                          |_|               |___/              
                """)
           
            input('Please press Enter to start the game! \n')
            return username
        except Exception as e:
            print(e)


def clear():
    """
    Clears screen to facilitate clarity.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def get_words(words):
    
    """
    Random words generated from words.py.
    Only displays words without space.
    """

    word = random.choice(words)
    while ' ' in word:
        word = random.choice(words)

    return word.upper()

def game():

    """
    The player has 7 attempts to guess the correct word.
    The stage of the hangman is visualized as the player
    progresses with their guesses.

    The attempts decrease with each incorrect guess.
    They can't guess the same letter twice.
    """

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
        
        print('Your word to be guessed: ', blanks)
        print('\n')
        print('The letters you guessed so far are: ', ' '.join(guess_list))
        print('\n')

        player_guess = input('Please enter a letter: \n').upper()

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
        elif player_guess not in word:
            try:
                clear()
                CheckCharacter(player_guess)
                CheckInputLength(player_guess)

                clear()
                print(f'Sorry! {player_guess} is not in the word.')
                hangman_stage_count -= 1
                attempts -= 1
                guess_list.append(player_guess)
                incorrect_guesses.append(player_guess)
                print('\n')
            
            except Exception as e:
                print(e)               
    
    if attempts > 0:
        print(f'Congrats {username}, you guessed the word correctly! You rock!')
        print("""
                                 .''.
       .''.             *''*    :_\/_:     .
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |___
             """)
    else:
        print(f'Sorry {username}, you are out of attempts. The word was: {word}')
        print(hangman_stages[hangman_stage_count])
        print('\n')

def main():
    
    """
    Runs the game.
    Once the game is over one way or another,
    the player can decide whether they want to play again.
    """

    clear()
    welcome_player()
    clear()
    game()

    while True:
        play_again = input('Wanna play again? Y/N \n')
        
        if play_again.lower() == 'n':
            clear()
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
            break

        elif play_again.lower() != 'y':
            print('Invalid answer. Please press either y (yes) or n (no).')

        else:
            clear()
            game()


if __name__ == '__main__':
    main()
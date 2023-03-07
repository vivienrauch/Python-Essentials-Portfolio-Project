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
            clear()
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
    """
    
    """

    word = get_words(words)

    letters_in_word = set(word)
    guessed_letters = set()

    attempts = 7

    print(hangman_stages(attempts))

    while len(letters_in_word) > 0 and attempts > 0:
        print('You guessed these letters so far: ', ''.join(guessed_letters))
        print('\n')

        list_of_letters = [letter if letter in guessed_letters else '_ ' for letter in word]

        print('Your word to be guessed: ', ' '.join(list_of_letters))
        print('\n')

        player_guess = input('Please enter a letter: \n').upper()

        if player_guess not in guessed_letters:
            if player_guess in letters_in_word:
                letters_in_word.remove(player_guess)
                clear()
                guessed_letters.add(player_guess)

        elif player_guess in guessed_letters:
            clear()
            print(f'You already guessed the letter {player_guess}. Please try another letter.')

        elif player_guess not in letters_in_word:
            clear()
            attempts -= 1

            print(f'Sorry, {player_guess} is not in the word.')
            guessed_letters.add(player_guess)

        else:
            clear()
            print('Your guess is invalid.')

        print(hangman_stages(attempts))

    if attempts == 0:
        print(f'Sorry {username}, you are out of attempts. The word was: {word}')

    else:
        print(f'Congratulations {username}! You guessed the word: {word}! You rock!')
    

def main():
    
    welcome_player()
    game()

    while True:
        play_again = False

        while not play_again:
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
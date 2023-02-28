import random
import os
import words from words

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
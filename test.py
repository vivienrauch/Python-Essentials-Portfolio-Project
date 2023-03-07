def game():
    """
    
    """

    word = get_words(words)

    letters_in_word = []
    guessed_letters = []

    attempts = 7

    print(hangman_stages(attempts))

    while attempts > 0 and len(letters_in_word) > 0:
        print('You guessed these letters so far: '.join(guessed_letters))

        list_of_letters = [letter if letter in guessed_letters else '_' for letter in word]

        print('Your word to be guessed: '.join(list_of_letters))

        player_guess = input('Please enter a letter: \n').upper()

        if player_guess in letters_in_word and player_guess not in guessed_letters:
            letters_in_word.remove(player_guess)
            clear()
            guessed_letters.append(player_guess)

        elif player_guess in guessed_letters:
            clear()
            print(f'You already guessed the letter {player_guess}. Please try another letter.')

        elif player_guess not in letters_in_word:
            clear()
            attempts -= 1

            print(f'Sorry, {player_guess} is not in the word.')
            guessed_letters.append(player_guess)

        else:
            clear()
            print('Your guess is invalid.')

        print(hangman_stages(attempts))

    if attempts == 0:
        print(f'Sorry {username}, you are out of attempts. The word was: {word}')

    else:
        print(f'Congratulations {username}! You guessed the word: {word}! You rock!')


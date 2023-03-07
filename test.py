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


#test2

"""
    
    """

    word = get_words(words)

    letters_in_word = set(word)
    guessed_letters = set()

    attempts = 7
    hangman_count = 0

    print(hangman_stages[attempts])

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
                print(hangman_stages(attempts))

        elif player_guess in guessed_letters:
            clear()
            print(f'You already guessed the letter {player_guess}. Please try another letter.')
            print(hangman_stages(attempts))

        elif player_guess not in letters_in_word:
            clear()
            guessed_letters.add(player_guess)
            attempts -= 1
            hangman_count += 1
            print(hangman_stages[hangman_count])

            print(f'Sorry, {player_guess} is not in the word.')
            

        else:
            clear()
            print('Your guess is invalid.')    

    if attempts == 0:
        print(f'Sorry {username}, you are out of attempts. The word was: {word}')

    else:
        print(f'Congratulations {username}! You guessed the word: {word}! You rock!')



#failed code
"""
    
    """
    word = get_words(words)
    # word_hidden = '_' * len(word)

    letters_guessed = []
    attempts = 7
    guessed = False

    print(hangman_stages(attempts))
    print('\n')

    while not guessed and attempts > 0:
        
        player_guess = input('Please enter a letter: ').upper()
        
        for blank in word_hidden:
            print(blank, end = ' ')
            print('\n')
            print('You guessed: ' + ',' .join(letters_guessed))

            if len(player_guess) == 1 and player_guess.isalpha():
                
                if player_guess not in word:
                    clear()
                    print(f'Sorry, {player_guess} is not in the word.')
                    attempts -= 1
                    letters_guessed.append(player_guess)
                
                elif player_guess in letters_guessed:
                    clear()
                    print(f'You already guessed the letter {player_guess}. Please try another letter.')
                
                else:
                    clear()
                    print(f'Great job! {player_guess} is in the word!')
                    letters_guessed.append(player_guess)
                    word_into_list = list(word_hidden)
                    ind = [i for i, letter in enumerate(words) if letter == player_guess]
                    
                    for i in ind:
                        word_into_list[i] = player_guess
                        word_hidden = ''.join(word_into_list)
                    
                    if '_' not in word_hidden:
                        guessed = True
            
            else:
                clear()
                print('Your guess is invalid.')
            
        print(hangman_stages(attempts))
        print('\n')

    if guessed:
        print(f'Congratulations {username}! You guessed the word!')
    else:
        print(f'Sorry {username}, you are out of attempts. The word was: {word}')


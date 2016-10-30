# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 22:33:31 2016

@author: chi-chu tschang
"""
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    NumberOfGuesses = 8
    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is %d letters long." % len(secretWord))
    while NumberOfGuesses > 0:
        
        print ("-----------")
        print ("You have %d guesses left." % NumberOfGuesses)
        print ("Available letters: %s" % getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ") 
        guess = guess.lower()
    
        if guess in lettersGuessed:
            print ("Oops! You've already guessed that letter: %s" % getGuessedWord(secretWord, lettersGuessed))
            continue
            
        lettersGuessed.append(guess)
        if guess in secretWord:
            print ("Good guess: %s" % getGuessedWord(secretWord, lettersGuessed))
            
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print ("-----------")
                print ("Congratulations, you won!")
                
        else:
            NumberOfGuesses -= 1
            print ("Oops! That letter is not in my word: %s" % getGuessedWord(secretWord, lettersGuessed))

    if NumberOfGuesses == 0:
        print ("-----------")
        print ("Sorry, you ran out of guesses. The word was %s" % secretWord)
        


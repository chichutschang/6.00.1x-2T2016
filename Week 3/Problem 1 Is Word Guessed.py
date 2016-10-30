def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    #secretWord = 'apple'
    #lettersGuessed =['e','i','k','p','r','s']
    for character in secretWord:
        if character not in lettersGuessed: return False
    return True
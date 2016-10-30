def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letter = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for character in alphabet:
        if character not in lettersGuessed: 
            letter = letter + character
            
    return letter
            
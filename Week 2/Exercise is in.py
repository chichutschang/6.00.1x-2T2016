def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    i = len(aStr)
    mid = int((0 + i) / 2)
    if i == 0 or (i == 1 and aStr != char):
        return False
       
    if char == aStr[mid]:
        return True
    
    elif char < aStr[mid]: 
        return isIn(char, aStr[:mid])
                
    else:
        return isIn(char, aStr[mid + 1:])  
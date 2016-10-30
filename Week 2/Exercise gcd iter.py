def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    value = min(a,b)
    while value > 0:
        if a % value == 0 and b % value == 0:
            return value
            break
        else:
            value -= 1
    return value
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:56:05 2016

@author: chi-chu tschang
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    number = 1
    while exp > 0:
        number *= base
        exp -= 1
    return number
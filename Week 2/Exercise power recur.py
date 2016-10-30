# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:56:07 2016

@author: chi-chu tschang
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if (exp == 0):
        return 1
    else:  
        return (base * recurPower(base, exp - 1))
        
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 22:34:38 2016

@author: chi-chu tschang
"""

def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    # Your code here

    text = [True, False]
    return (text[x % 2 == 0])

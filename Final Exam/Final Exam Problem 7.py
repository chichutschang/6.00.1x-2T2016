# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 14:16:16 2016

@author: chi-chu tschang
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE       
    k=len(L)
    #x=10
    def poly(x):
        result = 0
        for i in range(k):
            result += L[i]*(x**(k-i-1))
        return (result)
    return (poly)
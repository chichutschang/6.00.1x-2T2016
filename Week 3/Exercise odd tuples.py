# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 22:18:15 2016

@author: chi-chu tschang
"""
aTup = ('I','am', 'a', 'test', 'tuple')

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup.
    '''
    other = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            other = other + (aTup[i],)
    return other
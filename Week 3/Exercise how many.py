# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 22:23:02 2016

@author: chi-chu tschang
"""
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    num = 0
    for i in aDict:
        num += len(aDict[i])
    #for j in aDict[i]:
    #    num += 1
    return num
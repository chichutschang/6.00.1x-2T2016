# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 22:25:51 2016

@author: chi-chu tschang
"""
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    biggest = 0
    result = None
    for key in aDict.keys():
        if len(aDict[key]) >= biggest:
            biggest = len(aDict[key])
            result = key

    return result           
    
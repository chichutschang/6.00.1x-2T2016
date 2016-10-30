# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 22:22:41 2016

@author: chi-chu tschang
"""
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    # Your code here
    longest_length = 0
    length_ascend = []
    length_descend = []
    length_ascend.append(1)
    length_descend.append(1)

    for i in range(1, len(L)):
        length_ascend.append(1)
        length_descend.append(1)
        if L[i] >= L[i-1]:
            length_ascend[i] = length_ascend[i - 1] + 1           
            if length_ascend[i]> longest_length:
                longest_length = length_ascend[i]
                result = sum(L[i-longest_length +1 : i+1])
 
        if L[i] <= L[i-1]:
            length_descend[i] = length_descend[i - 1] + 1            
            if length_descend[i]>longest_length:
                longest_length = length_descend[i]
                result = sum(L[i-longest_length +1 : i+1])

    return result    
    
    
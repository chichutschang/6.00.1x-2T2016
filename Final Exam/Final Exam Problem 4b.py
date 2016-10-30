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
    #https://en.wikipedia.org/wiki/Longest_increasing_subsequence
    #ascend = []
    #descend = []
    #ascend_count = 1
    #descend_count = 1
    longest_length = 0
    length_ascend = []
    length_descend = []
    length_ascend.append(1)
    length_descend.append(1)

    #ascend_count.append(1)
    #M=[None]
    #Q=1
    #M[0]=0
    #maxNumber=[]
    #minNumber=[]
    #ascend_maxCount = 0
    #descend_maxCount = 0
    for i in range(1, len(L)):
        length_ascend.append(1)
        length_descend.append(1)
        #print('i',i)
        #print('L[i]',L[i])
        #print('L[i-1]',L[i-1])
        if L[i] >= L[i-1]:
            #ascend_count +=1
            #print('ascend_count',ascend_count)
            length_ascend[i] = length_ascend[i - 1] + 1           
            #ascend.append(L[i])
            #print('ascend',ascend)
            #maxNumber.append(L[i])
            #print('maxNumber',maxNumber)            
            #print('longest length', longest_length)
            #print('length ascend',length_ascend[i])
            if length_ascend[i]> longest_length:
                #longest_length += 1
                longest_length = length_ascend[i]
                #print('longest length', longest_length)
                #print('length ascend',length_ascend[i])
                result = sum(L[i-longest_length +1 : i+1])
                #print('result',result)
        #else:
        #    ascend_count = 1
        #    ascend=[]
 
        if L[i] <= L[i-1]:
            #descend_count += 1
            #print('descend_count',descend_count)
            length_descend[i] = length_descend[i - 1] + 1            
            #print('length descend',length_descend[i])
            #descend.append(L[i])
            #print('descend',descend)                    
            #minNumber.append(L[i])
            #print('minNumber',minNumber)
            if length_descend[i]>longest_length:
                #longest_length += 1
                longest_length = length_descend[i]
                #print('longest length', longest_length)
                #print('length ascend',length_descend[i])
                result = sum(L[i-longest_length +1 : i+1])
                #print('result',result)


        #else:
        #    descend_count =1
        #    descend=[]
    
    #S=[]
    #k=

    #print (ascend_maxCount)
    #print (ascend)
    #print (descend_maxCount)        
    #print (descend)    
    return result    
    #return maxCount
    
    
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:52:07 2016

@author: chi-chu tschang
"""

def modSwapSort(L):
    '''L is a list of integers'''
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                #the next line is a short
                #form for swap L[i], L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)
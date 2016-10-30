# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:41:55 2016

@author: chi-chu tschang
"""

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False
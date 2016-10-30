# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:40:24 2016

@author: chi-chu tschang
"""
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

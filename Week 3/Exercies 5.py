# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 22:18:03 2016

@author: chi-chu tschang
"""

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
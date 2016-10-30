# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:56:11 2016

@author: chi-chu tschang
"""
def a(x, y, z):
    if x:
        return y
    else:
        return z
        
def b(q, r):
    return a(q>r, q, r)

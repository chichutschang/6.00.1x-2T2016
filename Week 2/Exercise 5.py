# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:59:46 2016

@author: chi-chu tschang
"""
#def foo(x, y = 5):
#    def bar(x):
#        return x + 1
#    return bar(y*2)

#foo(3)

def foo (x):
    def bar (z, x = 0):
        return z + x
    return bar(3)
    
foo(2)
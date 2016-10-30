# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:59:48 2016

@author: chi-chu tschang
"""

a = 10
def f(x):
    return x + a
a = 3
f(1)

x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)
g(x)
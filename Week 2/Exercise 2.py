# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:32:18 2016

@author: chi-chu tschang
"""

x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 - x) >= epsilon:
        guess += step
    else:
        break
    
if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
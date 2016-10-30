# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:04:57 2016

@author: chi-chu tschang
"""

count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)
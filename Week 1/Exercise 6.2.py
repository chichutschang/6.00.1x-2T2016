# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:08:07 2016

@author: chi-chu tschang
"""

greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)
    
print('done')
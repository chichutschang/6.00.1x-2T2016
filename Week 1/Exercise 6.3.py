# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:09:23 2016

@author: chi-chu tschang
"""

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
        or char == 'o' or char == 'u':
            numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1
    
print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))
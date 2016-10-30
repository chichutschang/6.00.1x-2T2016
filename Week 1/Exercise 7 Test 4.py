# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:27:21 2016

@author: chi-chu tschang
"""

count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
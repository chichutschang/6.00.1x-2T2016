# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:28:57 2016

@author: chi-chu tschang
"""

count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))
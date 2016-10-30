# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:25:27 2016

@author: chi-chu tschang
"""

count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
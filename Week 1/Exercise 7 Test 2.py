# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:23:42 2016

@author: chi-chu tschang
"""

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    break
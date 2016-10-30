# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:21:25 2016

@author: chi-chu tschang
"""
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

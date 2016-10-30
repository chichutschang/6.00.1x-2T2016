# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:22:20 2016

@author: chi-chu tschang
"""
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))

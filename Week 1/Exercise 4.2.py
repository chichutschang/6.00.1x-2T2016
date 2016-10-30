# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 22:26:21 2016

@author: chi-chu tschang
"""
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))

# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 22:43:35 2016

@author: chi-chu tschang
"""
num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')
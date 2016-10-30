# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 22:13:06 2016

@author: chi-chu tschang
"""
num = 3

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num // 2
if isNeg:
    result = '-' + result
    
    print (result)
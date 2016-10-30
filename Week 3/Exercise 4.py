# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 22:12:34 2016

@author: chi-chu tschang
"""

aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
aList == bList

cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
    dList.append(num)
cList == dList
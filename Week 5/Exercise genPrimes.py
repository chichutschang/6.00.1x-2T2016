# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:46:15 2016

@author: chi-chu tschang
"""
import math
def genPrimes():
    count = 2
    primes = []
    while True:
        for x in primes:        
            if count % x == 0:
                break
        else:
            primes.append(count)
            yield count
        count += 1
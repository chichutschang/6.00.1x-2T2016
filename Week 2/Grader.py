# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 13:38:24 2016

@author: chi-chu tschang
"""
#import math functions to user tan and pi
import math

#function atkes in 2 arguments 'n' for number of sides and 's' for length of side
def polysum(n, s):
    #solve for area of polygon
    area = ((0.25 * n * s**2)/(math.tan(math.pi/n)))
 
    #solve for perimeter of polygon   
    perimeter = n * s    
    
    #print the sum of area and square of perimeter of the regular polygon rounded to 4 decimal places
    return round(perimeter**2 + area, 4)

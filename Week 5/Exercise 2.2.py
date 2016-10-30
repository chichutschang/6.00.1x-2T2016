# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 20:42:35 2016

@author: chi-chu tschang
"""

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print(time)
        
clock = Clock('5:30')
clock.print_time('10:30')
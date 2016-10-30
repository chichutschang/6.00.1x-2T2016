# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:18:18 2016

@author: chi-chu tschang
"""

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        # Your code here
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        # Your code here
        return self.weight
    def __str__(self):
        # Your code here
        return self.src.getName() + '->' + self.dest.getName() +' ('+str(self.weight)+')'
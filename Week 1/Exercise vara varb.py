# -*- coding: utf-8 -*-
varA = "bonjour"
varB = -10

if type(varA) is str or type(varB) is str:
    print ("string involved")

elif int(varA) > int(varB):
    print ("bigger")

elif int(varA) == int(varB):
    print ("equal")
    
else:
    print ("smaller")

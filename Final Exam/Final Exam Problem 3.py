# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 22:35:46 2016

@author: chi-chu tschang
"""

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # FILL IN YOUR CODE HERE
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
        
    if int(us_num) < 10:
        for i in us_num:
            return(trans.get(i))

    elif int(us_num) == 10:
        return(trans.get('10'))
        
    elif int(us_num) > 10 and int(us_num) < 20 :
        if (us_num[0]) == '1':
            return(trans.get('10')+' '+ trans.get(us_num[1]))

    else:
        if (us_num[1] !='0'):
            return(trans.get(us_num[0])+' '+trans.get('10')+' '+trans.get(us_num[1]))
    
        elif (us_num[1] =='0'):
            return(trans.get(us_num[0])+' '+trans.get('10'))
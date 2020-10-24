# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 13:16:55 2020

@author: HP
"""

def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0, 3, 3]))

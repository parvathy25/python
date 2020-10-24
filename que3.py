# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 13:27:46 2020

@author: HP
"""

def sum_list(items):
    sum = 0
    for x in items:
        sum += x
    return sum
print(sum_list([1,2,4,8]))
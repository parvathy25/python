# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 13:29:32 2020

@author: HP
"""

def data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(data([1,2,3,4,5], [5,6,7,8,9]))
print(data([1,2,3,4,5], [6,7,8,9]))
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:07:19 2020

@author: HP
"""

X = [[12,7,3],    [4 ,5,6],    [7 ,8,9]]
Y = [[5,8,1],    [6,7,3],    [4,5,9]]

result = [[0,0,0],  [0,0,0],  [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
print(result)
           
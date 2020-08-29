# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:44:40 2020

@author: HP
"""

a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
c=float(input("enter the third number:"))
if(a>b and a>c):
    print("first number is greather",a)
elif(b>c and b>a):
    print("second number is greather",b)
else:
    print("the third number is greather",c)
    
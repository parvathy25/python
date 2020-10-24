# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:03:45 2020

@author: HP
"""

def composite(n): 
  factor=0
  print("n:",n)
  for i in range(1,n):
    print("i:",i)
    if n%i==0:
      print("Inside if loop")
      factor=i
      print("Factor:",factor)
  print("After for loop: Value of factor",factor)
  if factor>1:
    print (n,' is a composite number!')
  elif n==1:
    print ('The number 1 is neither prime nor composite!')
  else:
    print(factor)
    print (n,' is not a composite number!')
composite(7)   
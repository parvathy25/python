# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:08:26 2020

@author: HP
"""

def palindrome(str):
  #print (len(str)/2)
  #print (int(len(str)/2))
  for i in range(0, int(len(str)/2)): 
    if str[i] != str[len(str)-i-1]:
      return "Not Palindrome"
  return "Palindrome"
palindrome("malayalam")


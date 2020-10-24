# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:43:38 2020

@author: HP
"""

def table(number,start,end): 
	for i in range (start, end+1): 
		print ("%d * %d = %d" % (number, i, number * i) )
table(5,1,20)
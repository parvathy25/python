# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 13:28:38 2020

@author: HP
"""

def Remove(duplicate): 
	final_list = [] 
	for num in duplicate: 
		if num not in final_list: 
			final_list.append(num) 
	return final_list 
	
duplicate = [10,20,30,20,10,50,60,40,80,50,40]
print(Remove(duplicate))
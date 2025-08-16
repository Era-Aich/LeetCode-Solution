# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 10:42:45 2025

@author: asus
"""

s = input()

un_set = set()

left = 0 
maxlength = 0
for right in s:
    while right in un_set:
        un_set.remove(s[left])
        
        left+=1
        
    un_set.add(s[right])
    
    maxlength = max(maxlength, right-left+1)
    
print(maxlength)
    






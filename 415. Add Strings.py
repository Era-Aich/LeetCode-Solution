# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 14:19:51 2025

@author: asus
"""

num = int(input())
step=0
while num>0:
    if num%2==0:
        num = num//2
        
    elif num%2!=0:
        num=num-1
    step+=1
print(step)
    
        
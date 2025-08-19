# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 19:19:00 2025

@author: asus
"""

nums = list(map(int,input().strip().split()))


def is_number(n):
    s = 0
    rem=n%10
    s+=rem
    n=n//10
    return s
found =-1

for i in range(len(nums)):
    if is_number(nums[i])==i:
        found = i
        break
print(found)
    
    
    
    
        
        
        
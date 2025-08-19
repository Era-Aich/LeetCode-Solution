# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 19:09:51 2025

@author: asus
"""

nums = list(map(int,input().strip().split()))
count = 0
for i in range(len(nums)):
    su = nums[i]+1
    s = nums[i]-1
    if su%3==0 or s%3==0:
        count+=1
print(count)
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 21:27:58 2025

@author: asus
"""

nums = list(map(int, input().strip().split()))
p=1


for i in range(len(nums)):
    p*=nums[i]
print(p)

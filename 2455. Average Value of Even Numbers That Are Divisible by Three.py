# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 20:36:19 2025

@author: asus
"""

nums = list(map(int, input().strip().split()))
li=[]

for i in range(len(nums)):
    if nums[i]%2==0 and nums[i]%3==0:
        li.append(nums[i])
su = sum(li)
if len(li)==0:
    print(0)
else:
    avg = su//len(li)
print(avg)
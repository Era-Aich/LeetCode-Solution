# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 09:54:12 2025

@author: asus
"""

nums = list(map(int,input().split()))
count = 0

for i in range(len(nums)):
    li=[]
    while (nums[i]>0):
        rem = nums[i]%10
        li.append(rem)
        nums[i]=nums[i]//10
    n=len(li)


    if n%2==0:
        count+=1
    
print(count)
    
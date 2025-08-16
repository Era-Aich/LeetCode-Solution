# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 11:22:45 2025

@author: asus
"""

nums = list(map(int,input().strip().split()))
l=[]

for i in range(len(nums)):
    li=[]
    n= nums[i]
    while n>0:
        rem = n%10
        li.append(rem)
        n=n//10
    p=sum(li)
        
    l.append(p)
print(min(l))
        
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 11:43:28 2025

@author: asus
"""

n= int(input())
li=[]
#p=1

while n>0:
    rem = n%10
    li.append(rem)
    n=n//10

max_pr =[] 
for i in range(len(li)):
    for j in range(i+1, len(li)):
        p=li[i]*li[j]
        max_pr.append(p)

print(max(max_pr))
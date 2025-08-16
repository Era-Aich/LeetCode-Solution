# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 16:48:22 2025

@author: asus
"""

n = int(input())
sum = 0
j=2*1
for i in range(n+1):
    if i<=7:
        sum+=i
        k=sum
    
    while i>7:
        for l in range(j,n+1):
            sum+=k
        i+=1
        
print(sum)
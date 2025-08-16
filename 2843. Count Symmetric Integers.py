# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 14:13:01 2025

@author: asus
"""

low = int(input())
high = int(input())
count=0

for num in range(low,high+1):
    
    k = str(num)
    n = len(k)
    
    if n%2!=0:
        continue
    n=n//2
    
    first = sum( int(d) for d in k[:n])
    second = sum(int(d) for d in k[n:])
    if first == second:
        count+=1
print(count)
    
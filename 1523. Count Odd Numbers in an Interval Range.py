# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 12:47:52 2025

@author: asus
"""

low = int(input())
high = int(input())
l=[]

for i in range(low,high+1):
    if i%2!=0:
        l.append(i)
print(l)        
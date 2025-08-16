# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 12:21:25 2025

@author: asus
"""

n = int(input())
m = int(input())

num1 = []
num2 = []

for i in range(1,n+1):
    if i%m!=0:
        num1.append(i)
    elif i%m==0:
        num2.append(i)
s1 = sum(num1)
s2 = sum(num2)
print(s1-s2)
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 11:21:37 2025

@author: asus
"""

n = int(input())
x = sorted(str(n))

num1 = ""
num2 = ""

for i ,d in enumerate(x):
    if i%2==0:
        num1+=d
    else:
        num2+=d
p=int(num1)+int(num2)
print(p)
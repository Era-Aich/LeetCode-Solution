# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 19:27:45 2025

@author: asus
"""
import math
n = int(input())
li=[]

while n>0:
    rem = n%10
    li.append(rem)
    n=n//10
    
p = math.prod(li)
s = sum(li)
r = p-s
print(r)

    
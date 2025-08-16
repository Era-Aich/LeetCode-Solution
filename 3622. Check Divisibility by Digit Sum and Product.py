# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 12:00:12 2025

@author: asus
"""

import math
n = int(input())
num = n
S = 0

li=[]
while n>0:
    rem = n%10
    li.append(rem)
    n=n//10
    
s = sum(li)

p=math.prod(li)

S = s+p

if num%S==0:
    print('True')
else:
    print('False')

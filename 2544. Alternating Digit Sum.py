# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 13:49:37 2025

@author: asus
"""

n = int(input())

li = list(map(int,str(n)))
total = 0
#print(li)

for i ,d in enumerate(li):
    if i%2==0:
        total+=d
    else:
        total-=d
print(total)
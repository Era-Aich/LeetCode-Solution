# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 14:55:53 2025

@author: asus
"""

left = int(input())
right = int(input())
li=[]
li2=[]

for i in range(left, right,1):
    
    while i >0:
        rem = i%10
        li.append(rem)
        i=i//10
        
    for j in range(len(li)):
        if i%li[j]==0:
            li2.append(li[j])
print(li2)
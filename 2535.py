# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 21:34:15 2025

@author: asus
"""

lis = list(map(int,input().strip().split()))
li=[]

summ_lis= sum(lis)

for num in lis:
    while num>0:
        rem = num%10
        li.append(rem)
        num=num//10
        
su = sum(li)
new = abs(summ_lis-su)
print(new)
        
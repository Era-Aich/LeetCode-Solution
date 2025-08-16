# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 10:41:59 2025

@author: asus
"""

num1 , num2, num3 = map(int,input().strip().split())

s1 = str(num1).zfill(4)
s2 = str(num2).zfill(4)
s3 = str(num3).zfill(4)
key=""

for i in range(4):
    key+= str(min(int(s1[i]),int(s2[i]),int(s3[i])))
print(int(key))
    
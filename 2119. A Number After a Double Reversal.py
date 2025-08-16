# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 20:54:28 2025

@author: asus
"""

num = int(input())
n= num

r1 = int(str(num)[::-1])
r2 =  int(str(r1)[::-1])
if r2 == n :
    print("True")
else:
    print("False")


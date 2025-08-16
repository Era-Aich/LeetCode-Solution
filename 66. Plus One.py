# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 13:05:55 2025

@author: asus
"""

digits = list(map(int,input().strip().split()))

p = int("".join(map(str,digits)))
s= p+1
k= list(map(int, str(s)))

print(k)
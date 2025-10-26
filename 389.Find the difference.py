# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 11:24:59 2025

@author: asus
"""
from collections import Counter
s= input().strip()
t= input().strip()

s_count = Counter(s)
t_count = Counter(t)


for i in t_count:
    if t_count[i] != s_count.get(i,0):
        print(i)

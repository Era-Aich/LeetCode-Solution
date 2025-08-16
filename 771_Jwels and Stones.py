# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 06:30:49 2025

@author: asus
"""

j =input()

S= input()

count=0
for stones in S:
    for jwel in j:
        if stones==jwel:
            count+=1

print(count)

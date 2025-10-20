# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 11:47:55 2025

@author: asus
"""

s = input()
indices = list(map(int,input().strip().split()))
result = ['']*len(s)

for i in range(len(s)):
    result[indices[i]] = s[i]
    
    k = ''.join(result)
print(k)
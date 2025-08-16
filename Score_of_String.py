# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 19:35:43 2025

@author: asus
"""


s = input()
li=[]

for i in range(len(s)-1):
    new = abs(ord(s[i]) - ord(s[i+1]))
    li.append(new)

summ = sum(li)
print(summ)
    
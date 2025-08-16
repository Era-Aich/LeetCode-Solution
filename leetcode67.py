# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 10:15:51 2025

@author: asus
"""

a = input()
b= input()

sum = int(a,2) + int(b,2)

sum_new = bin(sum)

print(sum_new[2:])

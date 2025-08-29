# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 10:49:04 2025

@author: asus
"""

def is_prime(n):
    if n<2 :
        return False
    for i in range(2,int(n**0.5)+1):
       if n%i==0:
            return False
    return True

count = 0
left = int(input())
right = int(input())
for i in range(left, right+1):
    set_bit = i.bit_count()
    if is_prime(set_bit):
        count+=1
print(count)
    
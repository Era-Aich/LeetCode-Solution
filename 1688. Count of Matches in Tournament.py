# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 19:22:07 2025

@author: asus
"""

n = int(input())
match = 0
advance = 0


while n>1:
    
    if n%2==0:
        match+=n//2
        #li.append(match)
    
        n//=2
    else:
        match+=(n-1)//2
        n=(n-1)//2+1
print(match)


    
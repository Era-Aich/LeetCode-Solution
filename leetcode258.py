# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 12:30:19 2025

@author: asus
"""


n = int(input())
#li=[]

digit = n
while digit>=9:
    li=[]
    while n>0:
        rem = n%10
        #li.append(rem)
        li.append(rem)
        n=n//10
    digit= sum(li)
    n=digit
    
print(digit)

 

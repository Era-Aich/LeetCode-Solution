# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 15:47:15 2025

@author: asus
"""
left = int(input())
right = int(input())
result = []
li=[]
for num in range(left, right+1):
    n=num
    valid = True
    while n>0:
       rem = n%10
       if rem==0 or num%rem!=0:
           valid = False
           break
       n//=10
    if valid:
      li.append(num)
print(li)   


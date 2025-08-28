# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 14:26:32 2025

@author: asus
"""
def digit_sum(n):
    total=0
    while n>0:
        rem=n%10
        total+=rem
        n=n//10


    count=0
    for i in range(2,n+1):
        if digit_sum(i)%2==0:
            count+=1
    return count

n=int(input())
print(digit_sum(n))

            
    
        
        
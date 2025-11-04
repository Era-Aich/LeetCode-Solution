# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 11:44:55 2025

@author: asus
"""

s = input().strip()
count = 1
group=[]

for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        group.append(count)
        count = 1
        
group.append(count)

result = 0
for i in range(1,len(group)):
    result+= min(group[i],group[i-1])
print(result)
    
    
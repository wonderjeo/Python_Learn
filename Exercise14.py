# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:27:52 2019

@author: 45570
"""
s = str(input("Please input a string:"))
ss=""
for i in range(0,len(s)):
    ss += s[:i]
for i in range(0,len(s)):
    ss += s[i:len(s)]
print(ss)

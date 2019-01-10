# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:22:04 2019

@author: 45570
"""
s = str(input("Please input a string:"))
for i in range(0,len(s)):
    print(" "*i+s[i:]+s[:len(s)-i])

# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:27:08 2019

@author: 45570
"""
year = int(input("Please input a year:"))
flag = "True"
if year%4!=0:
    flag = "False"
if (year%100 == 0) and (year%400 != 0):
    flag = "False"
print(flag)

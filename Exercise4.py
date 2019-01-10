# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:41:22 2019

@author: 45570
"""
num = int(input("Please input a number:"))
while num>9:
    print(num%10)
    num = num // 10
print(num)

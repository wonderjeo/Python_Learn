# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:08:24 2019

@author: 45570
"""
a = int(input("Please input a number:"))
b = int(input("Please input another number:"))
while b!=0:
    a, b = b, a % b
print("The GCD is ",a)


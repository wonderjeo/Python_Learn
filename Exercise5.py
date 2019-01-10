# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:59:33 2019

@author: 45570
"""
n = int(input("Please input a number:"))
num1 = 0
num2 = 1
for i in range(n):
    if i == 0:
        print(0, end = " ")
    elif i == 1:
        print( 1, end = " ")
    else:
        temp = num1 + num2
        num1 = num2
        num2 = temp
        print( num2, end = " ")

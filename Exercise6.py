# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:10:52 2019

@author: 45570
"""
n = int(input("Please input a number:"))
for i in range(2, n+1):
    flag = 1
    for x in range(2, int(i ** 0.5 + 1)):
        if i % x == 0:
            flag = 0
    if flag == 1:
        print(i, end=" ")

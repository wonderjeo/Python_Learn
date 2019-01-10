# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:36:42 2019

@author: 45570
"""
n = int(input("Please input the number of days of this month:"))
f = int(input("Please input the first day of week:"))
list = [i for i in range(1, n+1) if (i+f-1)%7==6 or (i+f-1)%7==0]
print(list)
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:47:21 2019

@author: 45570
"""
oList = [];
n = int(input("PLease input a number, 0 means exit:"))
while n != 0:
    oList.append(n)
    n = int(input("PLease input a number, 0 means exit:"))
nList = [oList[len(oList)-index-1] for index in range(0,len(oList))]
print(nList)

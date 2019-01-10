# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:53:29 2019

@author: 45570
"""
oList = [];
n = int(input("PLease input a number, 0 means exit:"))
while n != 0:
    oList.append(n)
    n = int(input("PLease input a number, 0 means exit:"))
while len(oList)>1:
    print(oList[::2])
    oList = oList[1:len(oList)-1]
print(oList[::2])

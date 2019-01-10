# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:23:29 2019

@author: 45570
"""
oList = [];
n = int(input("PLease input a number, 0 means exit:"))
while n != 0:
    oList.append(n)
    n = int(input("PLease input a number, 0 means exit:"))
d = {'odd' : 0, 'even' : 0}
for i in oList:
    if i %2 ==0:
        d['even'] += 1
    else:
        d['odd'] +=1
print(d)

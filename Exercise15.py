# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:25:31 2019

@author: 45570
"""
def calcuPi(n):
    m = 10 ** n
    pi = 0
    for i in range(m):
        pi += (-1) ** i * 4 / (2 * i + 1)
    return pi
ipt = int(input("Please input an integer:"))
print("+"+"-"*ipt+"+"+"-"*8+"+") 
print(f'|{"n":^{ipt}}|{"pi":^8}|')
print("+"+"-"*ipt+"+"+"-"*8+"+") 
for i in range(ipt):
    print(f'|{10**i:{ipt}d}|{calcuPi(i):.6f}|')
print("+"+"-"*ipt+"+"+"-"*8+"+") 

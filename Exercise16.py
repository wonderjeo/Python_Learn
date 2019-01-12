# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:12:00 2019

@author: 45570
"""
def myRange(start, end = None, step = 1):
    if end is None:
        end = start
        start = 0
    rst = []
    n = start
    while n < end:
        rst.append(n)
        n += step
    return rst

end = int(input("Input end:"))
print(myRange(end))
print(list(range(end)))


start = int(input("Input start:"))
print(myRange(start, end))
print(list(range(start, end)))


step = int(input("Input step:"))
print(myRange(start, end, step))
print(list(range(start, end, step)))
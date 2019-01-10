# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 19:24:07 2019

@author: 45570
"""
time = int(input("Please input a time period in seconds:"))
hs = int(time/3600)
ms = int((time%3600)/60) 
ss = int(time%60)
print(hs,"h", ms,"m", ss,"s")

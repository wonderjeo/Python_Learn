# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:22:50 2019

@author: 45570
"""
class Frac:
    def __init__(self, num, denum):
        import math
        gcd = math.gcd(num, denum)
        self.__num = num // gcd
        self.__denum = denum // gcd
    def __str__(self):
        return f'{self.getNum()}/{self.getDenum()}'
    
    def getNum(self):
        return self.__num
    def getDenum(self):
        return self.__denum
    
    def setNum(self, num):
        self.__num = num
    def setDenum(self, denum):
        self.__denum = denum
    
    def invert(self):
        temp = self.getNum()
        self.setNum(self.getDenum())
        self.setDenum(temp)
    def multi(self, frac):
        num = self.getNum() * frac.getNum()
        denum = self.getDenum() * frac.getDenum()
        import math
        gcd = math.gcd(num, denum)
        self.setNum(num // gcd)
        self.setDenum(denum // gcd)
    def add(self,frac):
        denum = self.getDenum() * frac.getDenum()
        num = self.getDenum() * frac.getNum() + frac.getDenum() * self.getNum()
        import math
        gcd = math.gcd(num, denum)
        self.setNum(num // gcd)
        self.setDenum(denum // gcd)
    def eval(self):
        return self.getNum()/self.getDenum()
n = 5
x = Frac(1, 1)
for i in range(2, n):
    x.add(Frac(1, i))
    x.multi(Frac(1, 2))
    x.invert()
print(n, x, x.eval())


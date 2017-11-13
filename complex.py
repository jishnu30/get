import sys
class Complex():
 ""
def __init__(self,real,imag):
  self.real = real
  self.imag = imag
def add(self,other):
  r1 = self.real
  i1 = self.imag
  r2 = other.real
  i2 = other.imag
  r = (r1+r2,i1+i2)
  print r
def mul(self,other):
  r1 = self.imag
  i1 = self.imag
  r2 = other.real
  i2 = other.imag
  m = ((r1*r2)-(i1*i2)),((r1*i1)+(r2*i2))
  print m
a = Complex()
a.real = 1
a.imag = 2
b = Complex()
b.real = 3
b.imag = 4
add(a,b)
mul(a,b)

from math import *
from numpy import *
from decimal import Decimal, getcontext

def f(x): return (x**2)
#def g(x): return (1 + sin(x))

#tolerancia
tol = 10**-16

#intervalo
a=1
b=2

x0=1
err=2
x1=f(x0)

while(err>tol):
 
 x2= x1-(f(x1)/f(x1)-f(x0))-(x1-x0)
 if(f(x2)*f(x1)<0):
     x2=x1

 else:
   x2=x1
   x0=x0

 err=(x1-x2)
 print(x1)



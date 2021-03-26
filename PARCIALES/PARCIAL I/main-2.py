from math import *
from numpy import *
from decimal import Decimal, getcontext




def f(x): return (sqrt((x**2)+1))-1

getcontext().prec = 9

#x=Decimal(1.1)
#x=Decimal(1.111111111)
x=Decimal(1.111111111111111)
cont=0
err=1
tol = 10**-8

x1=Decimal(f(x))
while(err>tol and cont<100 ):
 
 x2=Decimal(f(x1))
 cont=cont+1
 err=abs(x1-x2)
 print("iteracion: ", cont)
 print(x)


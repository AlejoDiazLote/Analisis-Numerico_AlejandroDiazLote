import math
import sympy as sp


def expAprox(x0, t, f):
    a = f.subs(x,x0)
    r = 0
    i = 0
    error= abs(a - r)
    while (abs(a-r)>t):
        deriv = f.diff(x, i)
        r += (deriv.evalf(subs={x: 0}) * ((x0 - 0) ** i))/math.factorial(i)
        print("La aproximacion en {} es {} y el error absoluto es  {}".format(i,round (r,9),round(error,9)))
        i = i + 1
        error= abs(a - r)
    print("LA APROX  ES: {}".format(r))  # f(x)=f(0)+f'(0)(x-0)....+Er
    i += 1
    er = (deriv.evalf(subs={x: 0}) * ((x0 - 0) ** i)) / math.factorial(i)
    print("EL ERROR ES: {}".format(er)) #f(x)=f(0)+f'(0)(x-0)....+Er





x=sp.Symbol('x')
f=(math.e**x)*sp.cos(2*x)

print("\nX0 disponibles")
print("1. 0.005")
print("2. 0.0001")
print("3. 0.999999999")
op=int(input("INGRESE OPCION"))
if (op==1):
    expAprox(0.005, 10**(-4), f)
elif(op==2):
    expAprox(0.0001, 10**(-4), f)
elif(op==3):
    expAprox(0.999999999, 10**(-1), f)
else:
    print("OPCION INCORRECTA")
import numpy as np

n = int(input("Cuantas parejas de datos? "))

x = np.zeros(n)
y = np.zeros(n)

print("ingrese datos de x,y:")
for i in range(n):
    x[i] = float(input("x["+str(i)+"]= "))
    y[i] = float(input("y["+str(i)+"]= "))
    
sumX,sumX2,sumY,sumXY = 0,0,0,0
for i in range(n):
    sumX = sumX + np.log(x[i])
    sumX2 = sumX2 +np.log(x[i])*np.log(x[i])
    sumY = sumY + np.log(y[i])
    sumXY = sumXY + np.log(x[i])*np.log(y[i])

b = (n*sumXY-sumX*sumY)/(n*sumX2-sumX*sumX)
A = (sumY - b*sumX)/n

a = np.exp(A)


# y = a + bx
print("\nlos coeficientes son son:")
print("a: ", a)
print("b: ", b)
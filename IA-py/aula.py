#-*- coding: utf-8 -*-

from math import sqrt


#a = input("Digite o valor para A:")

a = float(input("Digite o valor para A = "))
b = float(input("Digite o valor para B = "))
c = float(input("Digite o valor para C = "))

b2 = b**2
delta = b2-(4 * a * c)

try: 
    raiz_quadrada = sqrt(delta)
    x1 = (-b - raiz_quadrada)/(2*a)
    x2 = (-b + raiz_quadrada) /(2*a)
    print("x1 = " +  str(x1))
    print("x2 = " + str(x2))

except Exception as e:
    print(e)


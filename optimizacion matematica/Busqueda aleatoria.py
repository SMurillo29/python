# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 15:01:58 2019

@author: Alex
"""
import random
from sympy import Symbol, lambdify

x = Symbol('x')
y = Symbol('y')
f = input("Ingrese la funcion: ")
fx = lambdify((x,y),f, "numpy")
x0 = float(input("igrese el valor a evaluar de x0: "))
x1 = float(input("igrese el valor a evaluar de x1: "))
y0 = float(input("igrese el valor a evaluar de y0: "))
y1 = float(input("igrese el valor a evaluar de y1: "))
n = int(input("igrese la cantidad de iteraciones: "))
r = random.random()
print(r)
xf = x0 + (x1-x0)*r
yf = y0 + (y1-y0)*r
fxy = fx(xf,yf)
fxyi = fxy
print ("f(x,y)1: ", fxy, "\n")
print ("f(x,y)2: ", fxyi, "\n")
for i in range(1,n):
    r = random.random()
    print(r)
    xf = x0 + (x1-x0)*r
    yf = y0 + (y1-y0)*r
    fxy = fx(xf,yf)
    if fxy > fxyi:
        fxyi = fxy
        xu = xf
        yu = yf
    print ("f(x,y)1: ", fxy, "\n")
    print ("f(x,y)2: ", fxyi, "\n")


print ("Los mayores son:\n")
print ("x: ", xu)
print ("y: ", yu)
print ("f(x,y): ", fxyi)
print (fx(xu,yu))

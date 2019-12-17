import sympy 

x,y,z=sympy.symbols('x,y,z')
exprecion=input("introduce la funcion en terminos de x\n");

"""se obtiene la funcion de la entrada del usuario"""
funcion=sympy.sympify(exprecion)

""" se obtiene la derivada de la funcion """
derivada=funcion.diff(x)

"""se obtiene la segunda derivada de la función"""
segundaDerivada=derivada.diff(x)

print("función ", funcion)
print("derivada ", derivada)
print("derivada ", segundaDerivada)

"se da valor a x inicial"
X=float(input("ingresa el valor inicial de x\n"))

"se da valor a la tolerancia"
tolerancia=float(input("ingresa el valor inicial del porcentaje de la tolerancia\n"))

tolerancia = tolerancia/100
"""tolerancia=1e-tolerancia"""

"se declara xn+1 y el error absoluto"
xn=0
errorAbsoluto=X
while(errorAbsoluto>tolerancia):
    xn=X-((funcion.subs(x,X)*derivada.subs(x,X))/((derivada.subs(x,X)**2)-(funcion.subs(x,X)*segundaDerivada(x,X))))
    errorAbsoluto=abs(xn-X)
    X=xn
    print(xn)




"""
sympify(funcion) transforma caractere en una funcion
diff(x)          deriva la funcion respecto a una variable
subs(x,1)        evalua la funcion respecto a una variable y un valor     

print(sympy.sympify(exprecion).subs(x,1))
print(sympy.sympify(exprecion).diff(x))
"""




input("salir")

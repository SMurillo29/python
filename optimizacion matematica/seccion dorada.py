import sympy
import math

"se da valor a la tolerancia"
tolerancia=float(input("ingresa el valor la tolerancia\n"))

x,y,z=sympy.symbols('x,y,z')
exprecion=input("introduce la funcion en terminos de x\n");

"""se obtiene la funcion de la entrada del usuario"""
funcion=sympy.sympify(exprecion)
print("función ", funcion)

"se da valor inicial a los limites superior e inferior"
Xi=float(input("ingresa el valor del limite inferior\n"))
Xs=float(input("ingresa el valor del limite superior\n"))

"""se calcula la distancia inicial"""
distancia=((math.sqrt(5))-1)/2*(Xs-Xi)
print("distancia ",distancia)
"""se halla los valores de x1 y de x2"""
X1=Xi+distancia
print("X1 ",X1)
X2=Xs-distancia
print("X2 ",X2)
errorAbsoluto=Xs


"""se calcula los valores para f(Xi) y f(Xs)"""
Fx1=funcion.subs(x,X1)
print("Fx1 ",Fx1)
Fx2=funcion.subs(x,X2)
print("Fx2 ",Fx2)
while(errorAbsoluto>=tolerancia):
    
    if Fx1 > Fx2:
        Xi=X2
        X2=X1
        distancia=((math.sqrt(5))-1)/2*(Xs-Xi)
        X1=Xi+distancia
        Fx1=funcion.subs(x,X1)
        Fx2=funcion.subs(x,X2)
        errorAbsoluto=abs(X2-X1)
        print("Xi ",Xi," X2 ",X2," X1 ",X1,"Xs",Xs," EA ",errorAbsoluto)
    elif Fx2 > Fx1:
        Xs=X1
        X1=X2
        distancia=((math.sqrt(5))-1)/2*(Xs-Xi)        
        X2=Xs-distancia
        Fx2=funcion.subs(x,X2)
        errorAbsoluto=abs(X2-X1)
        print("Xi ",Xi," X2 ",X2," X1 ",X1,"Xs",Xs," Ea ",errorAbsoluto)
    
        
    

    
    
   
    
   




"""
sympify(funcion) transforma caractere en una funcion
diff(x)          deriva la funcion respecto a una variable
subs(x,1)        evalua la funcion respecto a una variable y un valor     

print(sympy.sympify(exprecion).subs(x,1))
print(sympy.sympify(exprecion).diff(x))
"""




input("salir")

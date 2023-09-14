# Funciones con N parametros

def funcion(*n):
    suma = 0
    producto = 1
    for i in n:
        suma += i
        producto *= i
    return print("La suma total es:",suma , "El producto total es:",producto)

funcion(4,2,5)
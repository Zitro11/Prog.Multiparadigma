def capturar():
    cadena = input("Ingrese una cadena de texto: ")
    return cadena

def mostrar(cadena):
    palabras = []
    numeros = []
    for palabra in cadena.split():
        if palabra.isnumeric():
            numeros.append(palabra)
        else:
            palabras.append(palabra)
    palabras.sort()
    cadena_ordenada = " ".join(palabras + numeros)
    print(cadena_ordenada)  

def main():
    cadena = capturar()
    while True:
        opcion = input("Desea ingresar otra cadena? (Si/No): ")
        if opcion.upper() == "SI":
            cadena += " " + capturar()
        elif opcion.upper() == "NO":
            break
        else:
            print("Opcion no valida")
    mostrar(cadena)

main()

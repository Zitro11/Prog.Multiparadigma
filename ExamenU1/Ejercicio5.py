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
        opcion = input("Desea ingresar otra cadena? (S/N): ")
        if opcion.upper() == "S":
            cadena += " " + capturar()
        elif opcion.upper() == "N":
            break
        else:
            print("Opcion no valida")
    mostrar(cadena)

main()

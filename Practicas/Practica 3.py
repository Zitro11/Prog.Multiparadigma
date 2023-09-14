# Entrada de datos y manipulación.

nombre = input ("Ingresa un Nombre: ")

nombre2 = ""

for i,l in enumerate (nombre):
    if (i+1) % 2 != 0:
        nombre2 += l.upper()
    else:
        nombre2 += l.lower()

nombre3 = ' '.join(nombre2)

print (f"Nombre: {nombre} \nIntercalado: {nombre2} \nInversa: {nombre3[::-1]}")
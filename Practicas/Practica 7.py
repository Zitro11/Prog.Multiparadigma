# Formateo y conversiones

from datetime import date

print ("Selecciona el modo de impresion:")
print ("(a) YYYY/MM/DD   (b) MM/DD/YYYY")
opc = input()

fecha = date.today()

if opc == 'a':
    print(f"Fecha en formato a: {fecha.strftime('%Y/%m/%d')}")
elif opc == 'b':
    print(f"Fecha en formato b: {fecha.strftime('%m/%d/%Y')}")
else:
    print(f"Opcion no valida, Fecha: {fecha}")
n1 = int(input("Ingrese un numero de 3 digitos: "))
n2 = int(input("Ingrese otro numero de 3 digitos: "))
if n1 >= 100 and n1 <= 999 and n2 >= 100 and n2 <= 999:
    n1 = str(n1)
    n2 = str(n2)
    n1 = n1[::-1]
    n2 = n2[::-1]
    n1 = int(n1)
    n2 = int(n2)
    if n1 > n2:
        print(n1)
    else:
        print(n2)
else:
    print("Los numeros deben ser de 3 digitos")
# Manejo y manipulación de elementos de una lista

lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
         "t","u","v","w","x","y","z"]

lisraR = []

for i,l in enumerate(lista):
    if(i+1) % 2 != 0:
        lisraR.append(l)

print ("Abecedario:")
print (lista)
print ("Sin multiplos de 2")
print (lisraR)
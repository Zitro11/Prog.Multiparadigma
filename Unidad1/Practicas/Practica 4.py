# Entrada de datos y estructuración.

dicSemestre = {}    #diccionario
materias = []       #lista

## funcion para recorrer el diccionario
def semestre (**kwars):
    sumaCreditos = 0

    for asignatura,creditos in kwars.items():
        print (f"{asignatura} tiene {creditos} creditos.")
        sumaCreditos += int(creditos)
        materias.append(asignatura)
    
    print("-")
    print (f"Suma de todos los creditos: {sumaCreditos}")
    print("-")
    print(f"Lista de Asignaturas:")
    for m in materias:
        print (m)

### INICIO Capturamos las materias y creditos
print ("Capture su 7° semestre")
coontador = 1
while coontador < 8:
    print ("Ingrese nombre de materia:")
    materia = input()
    print (f"Ingrese los credios de la materia {materia}")
    credito = input()

    dicSemestre[materia] = credito
    coontador += 1
print("------------------------------\n")

# llamamos a la funcion
semestre(**dicSemestre)
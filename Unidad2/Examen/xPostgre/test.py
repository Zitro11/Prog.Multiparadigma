from animal import animal
from animalDAO import animalDao
from doctor import doctor
from doctorDAO import doctorDao
from consulta import consulta
from consultaDAO import consultaDao
from logger_base import log


from alumno import alumno
from alumnoDAO import alumnoDao
from logger_base import log

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Ingresar consulta")
    print("2. Dar de alta una consulta")
    print("3. Obtener consultas y monto de un dia")
    print("4. Obtener doctores sin cita")
    print("5. Obtener animales ingresados + informacion del doc")
    print("6. Obtener un animal + info del doc")

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        idAnimal = input("Ingrese id del animal: ")
        idDoctor = input("Ingrse id del doc: ")
        service = input("Ingrese el servicio: ")
        coste = input("Ingrese el costo: ")
        cons = consulta(id_animal=idAnimal, id_doctor=idDoctor,servicio=service,costo=coste)
        resultado = consultaDao.insert(cons)
        log.debug(f'Consulta registrada {resultado}')

    elif opcion == "2":
        consultaEliminar = input("Id de animal a dar de alta: ")
        cons = consulta(id_animal=consultaEliminar)
        resultado = consultaDao.delete(cons)
        log.debug(f'Consulta eliminada {resultado}')

    elif opcion == "3":
        pass

    elif opcion == "4":


        print('Doctores sin cita: ')

    
    elif opcion == "5":
        pass

    elif opcion == "6":
        pass

    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")



import sys
from Practica8 import Usuario

listaCurps = []
DicUsuarios = {}

##8.3Administrador
Admin = Usuario('ADMIN','Admin123','Administrador','Santiago','SMBY','Veracruz')
DicUsuarios[Admin._Usuario] = Admin
listaCurps.append(Admin._CURP)
def MostrarUsuarios(DicUsuarios):
    for Usuarios, Datos in DicUsuarios.items():
        if Usuarios!='ADMIN':
            print()
            print (f"Usuario: {Usuarios}")
            print (f"Contraseña: {Datos._Contraseña}")
            print (f"Rol: {Datos._Rol}")
            print (f"Nombre: {Datos._Nombre}")
            print (f"CURP: {Datos._CURP}")
            print (f"Ciudad: {Datos._Ciudad}")
    
respuesta = "s"
while respuesta.lower() == "s":

    print ("\n----- MENU INICIAL -----")
    print ("\n1.- Registro \n2.- Inicio de sesion \n3.- Salida")
    print ("\nSelecciona una opcion:")
    Opcion = input()

    if Opcion == "1":
        print ("\n--- Registro ---")
        print ("Ingresa tus datos->\n")
        usuario = input("Usuario: ").upper()
        contraseña = input("Contraseña: ")
        nombre = input("Nombre: ")
        curp = input("CURP: ").upper()
        ciudad = input("Ciudad: ")     

        if curp in listaCurps:
            print("\nRegistro invalido: El usuario ya existe")
        else:
            registro = Usuario(usuario,contraseña,"Cliente",nombre,curp,ciudad)
            listaCurps.append(registro._CURP)
            DicUsuarios[registro._Usuario] = registro
            print("\nRegistro exitoso!\n")
        
    elif Opcion == "2":
        print ("\n--- Inicio Sesion ---")
        print ("    [Credenciales]\n")
        sesion = input("Usuario: ").upper()
        password = input("Contraseña: ")

        if sesion in DicUsuarios:
            sesionBuscada = DicUsuarios[sesion]
            contra = sesionBuscada._Contraseña
            if password == contra:
                if sesionBuscada._Rol == 'Administrador':
                    MostrarUsuarios(DicUsuarios)
                else:
                    print (f"\nRol: {sesionBuscada._Rol} \nNombre: {sesionBuscada._Nombre} \nCURP: {sesionBuscada._CURP} \nCiudad: {sesionBuscada._Ciudad}\n")
            else: print ("\nContraseña incorrecta!")
        else: print ("\nDatos incorrectos")

    elif Opcion == "3":
        print ("--- Salir ---")
        sys.exit()

    else:
        print("Opcion no valida!")
        break

respuesta = input("¿Deseas realizar otro movimiento? (s/n)\n")
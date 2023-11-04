# Entrada de datos y estructuración.

def informacion (**kwargs):
    print ("Parametros recibidos: ",kwargs)
    for key,value in kwargs.items():
        print(value,":",key)

informacion(Pancho=22, Andy=22, Soto=25, Rafa=23)
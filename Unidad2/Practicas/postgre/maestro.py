from logger_base import log

class maestro:

    def __init__(self, id_maestro=None, nombre=None, apellido=None, formacion=None) -> None:
        self._id_maestro=id_maestro
        self._nombre = nombre
        self._apellido = apellido
        self._formacion = formacion
    
    def __str__(self) -> str:
        return f"""
            id_maestro: {self._id_maestro},
            Nombre: {self._nombre}, 
            Apellido: {self._apellido}, 
            Formacion: {self._formacion}
            """
    
    @property
    def id_maestro(self):
        return self._id_maestro
    @id_maestro.setter
    def id_maestro(self,idMaestro):
        self._id_maestro = idMaestro

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,Nombre):
        self._nombre = Nombre


    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self,Apellido):
        self._apellido =  Apellido
        

    @property
    def formacion(self):
        return self._formacion
    @formacion.setter
    def formacion(self,Formacion):
        self._formacion = Formacion
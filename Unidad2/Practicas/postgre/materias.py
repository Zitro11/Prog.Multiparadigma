from logger_base import log

class materias:

    def __init__(self, id_materia=None, nombre=None, creditos=None, horas=None) -> None:
        self._id_materia=id_materia
        self._nombre = nombre
        self._creditos = creditos
        self._horas = horas
    
    def __str__(self) -> str:
        return f"""
            id_materia: {self._id_materia},
            Nombre: {self._nombre}, 
            Creditos: {self._creditos}, 
            Horas: {self._horas}
            """
    
    @property
    def id_materia(self):
        return self._id_materia
    @id_materia.setter
    def id_materia(self,idMateria):
        self._id_materia = idMateria

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,Nombre):
        self._nombre = Nombre


    @property
    def creditos(self):
        return self._creditos
    @creditos.setter
    def creditos(self,Creditos):
        self._creditos = Creditos
        

    @property
    def horas(self):
        return self._horas
    @horas.setter
    def horas(self,Horas):
        self._horas = Horas
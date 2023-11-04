from logger_base import log

class alumno:

    def __init__(self, id_alumno=None, nombre=None, apellido=None, matricula=None) -> None:
        self._id_alumno=id_alumno
        self._nombre = nombre
        self._apellido = apellido
        self._matricula = matricula
    
    def __str__(self) -> str:
        return f"""
            id_alumno: {self._id_alumno},
            Nombre: {self._nombre}, 
            Apellido: {self._apellido}, 
            Matricula: {self._matricula}
            """
    
    @property
    def id_alumno(self):
        return self._id_alumno
    @id_alumno.setter
    def id_alumno(self,idNombre):
        self._id_alumno = idNombre

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
    def matricula(self):
        return self._matricula
    @matricula.setter
    def matricula(self,Matricula):
        self._matricula = Matricula
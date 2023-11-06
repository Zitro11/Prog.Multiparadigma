from logger_base import log

class doctor:

    def __init__(self, id_doctor=None, nombre=None, numeroTelefono=None) -> None:
        self._id_doctor = id_doctor
        self._nombre = nombre
        self._numero_telefono = numeroTelefono
    
    def __str__(self) -> str:
        return f"""
            id_doctor: {self._id_doctor},
            Nombre: {self._nombre}, 
            Telefono: {self._numero_telefono}
            """
    
    @property
    def id_doctor(self):
        return self._id_doctor
    @id_doctor.setter
    def id_doctor(self,idDoctor):
        self._id_doctor = idDoctor

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,Nombre):
        self._nombre = Nombre


    @property
    def numeroTelefono(self):
        return self._numero_telefono
    @numeroTelefono.setter
    def numeroTelefono(self,Telefono):
        self._numero_telefono =  Telefono
from logger_base import log

class animal:

    def __init__(self, id_animal=None, raza=None, fechaIngreso=None, fechaSalida=None) -> None:
        self._id_animal = id_animal
        self._raza = raza
        self._fechaIngreso = fechaIngreso
        self._fechaSalida = fechaSalida
    
    def __str__(self) -> str:
        return f"""
            id_animal: {self._id_animal},
            Raza: {self._raza}, 
            Fecha de Ingreso: {self._fechaIngreso}, 
            Fecha de Salida: {self._fechaSalida}
            """
    
    @property
    def id_animal(self):
        return self._id_animal
    @id_animal.setter
    def id_animal(self,idAnimal):
        self._id_animal = idAnimal

    @property
    def raza(self):
        return self._raza
    @raza.setter
    def raza(self,Raza):
        self._raza = Raza


    @property
    def fechaIngreso(self):
        return self._fechaIngreso
    @fechaIngreso.setter
    def fechaIngreso(self,Ingreso):
        self._fechaIngreso =  Ingreso
        

    @property
    def fechaSalida(self):
        return self._fechaSalida
    @fechaSalida.setter
    def fechaSalida(self,Salida):
        self._fechaSalida = Salida
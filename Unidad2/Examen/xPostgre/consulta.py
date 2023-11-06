from logger_base import log

class consulta:

    def __init__(self, id_animal=None, id_doctor=None, servicio=None, costo=None) -> None:
        self._id_animal = id_animal
        self._id_doctor = id_doctor
        self._servicio = servicio
        self._costo = costo
    
    def __str__(self) -> str:
        return f"""
            id_animal: {self._id_animal},
            id_doctor: {self._id_doctor}, 
            Servicio: {self._servicio}, 
            Costo: {self._costo}
            """
    
    @property
    def id_animal(self):
        return self._id_animal
    @id_animal.setter
    def id_animal(self,idAnimal):
        self._id_animal = idAnimal

    @property
    def id_doctor(self):
        return self._id_doctor
    @id_doctor.setter
    def id_doctor(self,idDoctor):
        self._id_doctor = idDoctor


    @property
    def servicio(self):
        return self._servicio
    @servicio.setter
    def servicio(self,Servicio):
        self._servicio =  Servicio
        

    @property
    def costo(self):
        return self._costo
    @costo.setter
    def costo(self,Costo):
        self._costo = Costo
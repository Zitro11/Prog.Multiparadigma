from doctor import doctor
from conex import conex
from cursorDelPool import CursorDelPool
from logger_base import log

class doctorDao:
    _Select = "SELECT * FROM doctor ORDER BY id_doctor"
    _Insert = "INSERT INTO doctor (nombre,telefono) VALUES (%s,%s)"
    _Update = "UPDATE doctor SET nombre=%s,telefono=%s WHERE id_doctor=%s"
    _Delete = "DELETE FROM doctor WHERE id_doctor=%s"

    @classmethod
    def select(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._Select)
            registros = cursor.fetchall()
            doctores = []
            for d in registros:
                doctores.append(doctor(d[0],d[1],d[2]))
            return doctores
    
    @classmethod
    def insert(cls, doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.nombre, doctor.numeroTelefono)
            cursor.execute(cls._Insert,valores)
            return (f'{doctor.nombre}, filas afectadas: {cursor.rowcount}')

    @classmethod
    def update(cls, doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.nombre, doctor.numeroTelefono, doctor.id_doctor)
            cursor.execute(cls._Update,valores)
            return (f'{doctor.nombre}, filas afectadas: {cursor.rowcount}')
    
    @classmethod
    def delete(cls, doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.id_doctor,)
            cursor.execute(cls._Delete,valores)
            return (f'{doctor.id_alumno}, filas afectadas: {cursor.rowcount}')

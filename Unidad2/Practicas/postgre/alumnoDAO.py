from alumno import alumno
from conex import conex
from cursorDelPool import CursorDelPool
from logger_base import log

class alumnoDao:
    _Select = "SELECT * FROM alumno ORDER BY id_alumno"
    _Insert = "INSERT INTO alumno (nombre,apellido,matricula) VALUES (%s,%s,%s)"
    _Update = "UPDATE alumno SET nombre=%s,apellido=%s,matricula=%s WHERE id_alumno=%s"
    _Delete = "DELETE FROM alumno WHERE id_alumno=%s"

    @classmethod
    def select(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._Select)
            registros = cursor.fetchall()
            alumnos = []
            for a in registros:
                alumnos.append(alumno(a[0],a[1],a[2],a[3]))
            return alumnos
    
    @classmethod
    def insert(cls, alumno):
        with CursorDelPool() as cursor:
            valores = (alumno._nombre, alumno._apellido, alumno._matricula)
            cursor.execute(cls._Insert,valores)
            return (f'{alumno._nombre}, filas afectadas: {cursor.rowcount}')
    
    @classmethod
    def update(cls, alumno):
        with CursorDelPool() as cursor:
            valores = (alumno._nombre, alumno._apellido, alumno._matricula, alumno.id_alumno)
            cursor.execute(cls._Update,valores)
            return (f'{alumno._nombre}, filas afectadas: {cursor.rowcount}')
    
    @classmethod
    def delete(cls, alumno):
        with CursorDelPool() as cursor:
            valores = (alumno.id_alumno,)
            cursor.execute(cls._Delete,valores)
            return (f'{alumno.id_alumno}, filas afectadas: {cursor.rowcount}')
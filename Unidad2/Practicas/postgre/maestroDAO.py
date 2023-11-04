from maestro import maestro
from conex import conex
from cursorDelPool import CursorDelPool
from logger_base import log

class maestroDao:
    _Select = "SELECT * FROM maestro ORDER BY id_maestro"
    _Insert = "INSERT INTO maestro (nombre,apellido,formacion) VALUES (%s,%s,%s)"
    _Update = "UPDATE maestro SET nombre=%s,apellido=%s,formacion=%s WHERE id_maestro=%s"
    _Delete = "DELETE FROM maestro WHERE id_maestro=%s"

    @classmethod
    def select(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._Select)
            registros = cursor.fetchall()
            maestros = []
            for m in registros:
                maestros.append(maestro(m[0],m[1],m[2],m[3]))
            return maestros
    
    @classmethod
    def insert(cls, maestro):
        with CursorDelPool() as cursor:
            valores = (maestro._nombre, maestro._apellido, maestro._formacion)
            cursor.execute(cls._Insert,valores)
            return (f'{maestro._nombre}, filas afectadas: {cursor.rowcount}')
    
    @classmethod
    def update(cls, maestro):
        with CursorDelPool() as cursor:
            valores = (maestro._nombre, maestro._apellido, maestro._formacion, maestro.id_maestro)
            cursor.execute(cls._Update,valores)
            return (f'{maestro._nombre}, filas afectadas: {cursor.rowcount}')
    
    @classmethod
    def delete(cls, maestro):
        with CursorDelPool() as cursor:
            valores = (maestro.id_maestro,)
            cursor.execute(cls._Delete,valores)
            return (f'{maestro.id_maestro}, filas afectadas: {cursor.rowcount}')
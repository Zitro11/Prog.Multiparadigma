from materias import materias
from conex import conex
from cursorDelPool import CursorDelPool
from logger_base import log

class materiasDao:
    _Select = "SELECT * FROM materias ORDER BY id_materia"
    _Insert = "INSERT INTO materias (nombre,creditos,horas) VALUES (%s,%s,%s)"
    _Update = "UPDATE materias SET nombre=%s,creditos=%s,horas=%s WHERE id_materia=%s"
    _Delete = "DELETE FROM materias WHERE id_materia=%s"

    @classmethod
    def select(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._Select)
            registros = cursor.fetchall()
            materiasR = []
            for m in registros:
                materiasR.append(materias(m[0],m[1],m[2],m[3]))
            return materiasR
    
    @classmethod
    def insert(cls, materia):
        with CursorDelPool() as cursor:
            valores = (materia._nombre, materia._creditos, materia._horas)
            cursor.execute(cls._Insert,valores)
            return (f'{materia._nombre}, filas afectadas: {cursor.rowcount}')
    
    @classmethod
    def update(cls, materia):
        with CursorDelPool() as cursor:
            valores = (materia._nombre, materia._creditos, materia._horas, materia.id_materia)
            cursor.execute(cls._Update,valores)
            return (f'{materia._nombre}, filas afectadas: {cursor.rowcount}')
    
    @classmethod
    def delete(cls, materia):
        with CursorDelPool() as cursor:
            valores = (materia.id_materia,)
            cursor.execute(cls._Delete,valores)
            return (f'{materia.id_materia}, filas afectadas: {cursor.rowcount}')
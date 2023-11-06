from consulta import consulta
from conex import conex
from cursorDelPool import CursorDelPool
from logger_base import log

class consultaDao:
    _Select = "SELECT * FROM consulta ORDER BY id_doctor"
    _Insert = "INSERT INTO consulta (id_animal,id_doctor,servicio,costo) VALUES (%s,%s,%s,%s)"
    _Update = "UPDATE consulta SET id_doctor=%s,servicio=%s,costo=%s WHERE id_animal=%s"
    _Delete = "DELETE FROM consulta WHERE id_animal=%s"


    @classmethod
    def select(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._Select)
            registros = cursor.fetchall()
            consultas = []
            for c in consultas:
                consultas.append(consulta(c[0],c[1],c[2],c[3]))
            return consultas
    
    @classmethod
    def insert(cls, consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.id_animal, consulta.id_doctor, consulta.servicio, consulta.costo)
            cursor.execute(cls._Insert,valores)
            return (f'{consulta.id_animal}, filas afectadas: {cursor.rowcount}')
    
    @classmethod
    def update(cls, consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.id_doctor, consulta.servicio, consulta.costo, consulta.id_animal)
            cursor.execute(cls._Update,valores)
            return (f'{consulta.nombre}, filas afectadas: {cursor.rowcount}')
    
    @classmethod
    def delete(cls, consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.id_animal,)
            cursor.execute(cls._Delete,valores)
            return (f'{consulta.id_animal}, filas afectadas: {cursor.rowcount}')
        
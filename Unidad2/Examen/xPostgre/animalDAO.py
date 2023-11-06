from animal import animal
from conex import conex
from cursorDelPool import CursorDelPool
from logger_base import log

class animalDao:
    _Select = "SELECT * FROM animal ORDER BY id_animal"
    _Insert = "INSERT INTO animal (raza,ingreso,salida) VALUES (%s,%s,%s)"
    _Update = "UPDATE animal SET raza=%s,ingreso=%s,salida=%s WHERE id_animal=%s"
    _Delete = "DELETE FROM alumno WHERE id_animal=%s"

    @classmethod
    def select(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._Select)
            registros = cursor.fetchall()
            animales = []
            for a in animales:
                animales.append(animal(a[0],a[1],a[2],a[3]))
            return animales
    
    @classmethod
    def insert(cls, animal):
        with CursorDelPool() as cursor:
            valores = (animal.raza, animal.fechaIngreso, animal.fechaSalida)
            cursor.execute(cls._Insert,valores)
            return (f'{animal.nombre}, filas afectadas: {cursor.rowcount}')
    
    @classmethod
    def update(cls, animal):
        with CursorDelPool() as cursor:
            valores = (animal.raza, animal.fechaIngreso, animal.fechaSalida, animal.id_animal)
            cursor.execute(cls._Update,valores)
            return (f'{animal.nombre}, filas afectadas: {cursor.rowcount}')
    
    @classmethod
    def delete(cls, animal):
        with CursorDelPool() as cursor:
            valores = (animal.id_animal,)
            cursor.execute(cls._Delete,valores)
            return (f'{animal.id_animal}, filas afectadas: {cursor.rowcount}')
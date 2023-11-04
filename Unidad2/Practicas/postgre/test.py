from alumno import alumno
from alumnoDAO import alumnoDao
from maestro import maestro
from maestroDAO import maestroDao
from materias import materias
from materiasDAO import materiasDao
from logger_base import log

######## Entidad ALUMNO ###########

#INSERT
'''alumno1 = alumno(nombre="Francisco",apellido="Ortiz",matricula=19100230)
insert = alumnoDao.insert(alumno1)
log.debug(f"Alumno agregado: {insert}")'''

#UPDATE
'''alumoU = alumno(id_alumno=5,nombre='Andy',apellido='Ibarra',matricula=19100255)
update = alumnoDao.update(alumoU)
log.debug(f"Alumno actualizado: {update}")'''

#DELETE
'''alumnoD = alumno(id_alumno=3)
delete = alumnoDao.delete(alumnoD)
log.debug(f"Alumno eliminado: {delete}")'''

#SELECT
'''alumnos_registro = alumnoDao.select()
for a in alumnos_registro:
    log.debug(a)'''


######## ENTIDAD MAESTRO ########

#Insert
'''maestroI = maestro(nombre="Luis", apellido="Castillo", formacion="Ingeniero")
insert = maestroDao.insert(maestroI)
log.debug(f"Maestro registrado: {insert}")'''

#Update
'''maestroU = maestro(id_maestro=2,nombre='Juan',apellido='Ahumada',formacion='Ingeniero')
update = maestroDao.update(maestroU)
log.debug(F"Maestro actualizado: {update}")'''

#Delete
'''maestroD = maestro(id_maestro=1)
delete = maestroDao.delete(maestroD)
log.debug(f"Maestro eliminado: {delete}")'''

#Select
'''maestros_registro = maestroDao.select()
for m in maestros_registro:
    log.debug(m)'''


########## ENTIDAD MATERIAS #########

#Insert
'''materiaI = materias(nombre="Python", creditos=6, horas=35)
insert = materiasDao.insert(materiaI)
log.debug(f"Materia registrada: {insert}")'''

#Update
'''materiaU = materias(id_materia=3,nombre='Web',creditos=3,horas=25)
update = materiasDao.update(materiaU)
log.debug(F"Materia actualizada: {update}")'''

#Delete
'''materiaD = materias(id_materia=1)
delete = materiasDao.delete(materiaD)
log.debug(f"Id materia eliminada: {delete}")'''

#Select
'''materias_registro = materiasDao.select()
for m in materias_registro:
    log.debug(m)'''
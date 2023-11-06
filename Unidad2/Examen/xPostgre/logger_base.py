import logging as log

##depende el nivel de la aplicacion mostrar los logs
log.basicConfig(
level=log.DEBUG,    ##nivel debug aparecen todos
format="%(asctime)s : %(levelname)s [%(filename)s]:%(lineno)s %(message)s",
datefmt='%I:%M:%S %p',
handlers=[
    log.FileHandler('capa_datos.log'),
    log.StreamHandler()
]
)

'''
if __name__=="__main__":
    log.debug("Prueba")
    log.debug("Error")
    log.debug("Critical")
    log.debug("Warning")
'''
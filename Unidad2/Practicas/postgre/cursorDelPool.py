from logger_base import log
from conex import conex

class CursorDelPool:
    def __init__(self) -> None:
        self._conex=None
        self._cursor=None

    def __enter__(self):
        log.debug("Inicio bloque with")
        self._conex=conex.ObtenerConexion()
        self._cursor=self._conex.cursor()
        return self._cursor
    
    def __exit__(self, tipo_exception,valor_excepcion,detalle_excepcion):
        log.debug("Se ejecuta exit")
        if valor_excepcion:
            self._conex.rollback()
        else:
            self._conex.commit()
        self._cursor.close()
        conex.LiberarConexion(self._conex)

'''
if __name__=="__main__":
    with CursorDelPool() as cursor:
        log.debug("Bloque with")
        cursor.execute("SELECT * FROM clientes")
        log.debug(cursor.fetchall())
'''
import psycopg2
from psycopg2 import pool
from logger_base import log

class conex:
    _DATABASE="ejemplos"
    _USERNAME="postgres"
    _PASSWORD="Admin1"
    _PORT="5050"
    _HOST="localhost"
    _MIN_CON=1
    _MAX_CON=5
    _pool=None

    @classmethod
    def ObtenerPool(cls):
        if cls._pool==None:
            cls._pool=pool.SimpleConnectionPool(
                cls._MAX_CON,
                cls._MIN_CON,
                host=cls._HOST,
                user=cls._USERNAME,
                password=cls._PASSWORD,
                port=cls._PORT,
                database=cls._DATABASE
            )
            log.debug("Creacion del pool",pool)
            return cls._pool
        else:
            return cls._pool

    @classmethod
    def ObtenerConexion(cls):
        conexion = cls.ObtenerPool().getconn()
        log.debug(f"Conexion obtenida {conexion}")
        return conexion
    
    @classmethod
    def LiberarConexion(cls,conexion):
        cls.ObtenerPool().putconn(conexion)
        log.debug(f"Conexion regresada {conexion}")

    @classmethod
    def CerrarConexion(cls):
        cls.ObtenerPool().closeall()
        log.debug("Conexiones cerradas")


'''
if __name__=="__main__":
    conexion1 = conex.ObtenerConexion()
'''
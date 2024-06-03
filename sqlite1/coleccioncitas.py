from db import Db
from cita import Cita

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS citas (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	cita TEXT NOT NULL
)
'''

SQLDDLSELECT = '''
    SELECT * FROM citas
'''


class ColeccionCitas:
    DBNAME = 'citas.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)

        self.con.execute(SQLMDLCREATE)

    def leer(self)->str:
        return self.con.execute(SQLDDLSELECT).fetchall()
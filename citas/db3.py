import sqlite3

#con = sqlite3.connect('citas.db')
con = sqlite3.connect('citas.db', isolation_level=None)

sqlDdl = '''CREATE TABLE IF NOT EXISTS citas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cita TEXT
)'''
con.execute(sqlDdl)

sqlDmlSelect = '''SELECT * FROM citas'''

res = con.execute(sqlDmlSelect)
print(res.fetchall())

sqlDmlInsert = '''INSERT INTO citas (cita) VALUES ('La vida es bella')'''
con.execute(sqlDmlInsert)
#con.commit()

res = con.execute(sqlDmlSelect)
print(res.fetchall())

con.close()
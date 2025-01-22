import sqlite3 as sql

conexion=sql.connect("primerBaseDatos.db")

cursor=conexion.cursor()

cursor.execute("""CREATE TABLE animales (
                    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                    especie TEXT,
                    edad INTEGER
              )""")

# cursor.execute("""CREATE TABLE IF NOT EXISTS animales (
#       codigo INTEGER PRIMARY KEY AUTOINCREMENT,
#       especie TEXT,
#       edad INTEGER
# )""")

# try:
#   cursor.execute("""CREATE TABLE animales (
#         codigo INTEGER PRIMARY KEY AUTOINCREMENT,
#         especie TEXT,
#         edad INTEGER
#   )""")
# except sql.OperationalError:
#   print("La tabla articulos ya existe")

conexion.close()


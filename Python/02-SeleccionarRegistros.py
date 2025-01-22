import sqlite3

conexion=sqlite3.connect("primerBaseDatos.db")

cursor=conexion.cursor()

cursor.execute("SELECT * FROM animales")

print(cursor.fetchone())
print(cursor.fetchone())

# print(cursor.fetchall())

# for fila in cursor:
#     print(fila)


conexion.close()


import sqlite3

conexion=sqlite3.connect("primerBaseDatos.db")

cursor=conexion.cursor()

cursor.execute("UPDATE animales SET edad = 8 WHERE codigo = 3;")
conexion.commit()
# cursor.execute("SELECT * FROM animales Where codigo = 3")
# print(cursor.fetchall())


# cursor.execute("DELETE FROM animales WHERE codigo = 5")
# conexion.commit()


# for fila in cursor:
#     print(fila)


conexion.close()


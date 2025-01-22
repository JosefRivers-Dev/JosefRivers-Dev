import sqlite3

conexion=sqlite3.connect("primerBaseDatos.db")

cursor=conexion.cursor()

cursor.execute("INSERT INTO animales VALUES (1,'Loro',5)")


cursor.execute("INSERT INTO animales(especie,edad) VALUES ('Gato',5)")
cursor.execute("INSERT INTO animales(especie,edad) VALUES ('Perro', 23)")
cursor.execute("INSERT INTO animales(especie,edad) VALUES ('Loro', 4)")
cursor.execute("INSERT INTO animales(especie,edad) VALUES ('Pez', 55)")

conexion.commit()

conexion.close()


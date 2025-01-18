import pandas as pd
import sqlite3

# Conecta con la base de datos
conn = sqlite3.connect('basedatos.db')
cursor = conn.cursor()

# Lee el archivo Excel
df = pd.read_excel('archivo_excel.xlsx')

# Actualiza la tabla usuarios
for index, row in df.iterrows():
    cursor.execute('INSERT OR REPLACE INTO usuarios (usuario, contraseña, empresa, nombre, edad, cedis, puesto) VALUES (?, ?, ?, ?, ?, ?, ?)',
        (row['usuario'], row['contraseña'], row['empresa'], row['nombre'], row['edad'], row['cedis'], row['puesto']))

# Actualiza la tabla formularios
for index, row in df.iterrows():
    cursor.execute('INSERT OR REPLACE INTO formularios (nombre, fecha, tipo) VALUES (?, ?, ?)',
        (row['nombre_formulario'], row['fecha'], row['tipo_formulario']))

# Cierra la conexión con la base de datos
conn.commit()
conn.close()


"""
# modificar en el codigo de la version 2
def _iniciar_sesion(self):
    usuario = self.entrada_usuario.get()
    contraseña = self.entrada_contraseña.get()

    conn = sqlite3.connect('basedatos.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?', (usuario, contraseña))
    resultado = cursor.fetchone()

    if resultado:
        self.usuario = {
            'empresa': resultado[3],
            'nombre': resultado[4],
            'edad': resultado[5],
            'cedis': resultado[6],
            'puesto': resultado[7]
        }
        self.pestaña_inicio.pack_forget()
        self.nota_book.pack(fill="both", expand=True)
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")

    conn.close()



# modificar en el codigo de la version 2
    def _ver_usuario(self):
    conn = sqlite3.connect('basedatos.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM usuarios WHERE usuario = ?', (self.usuario['usuario'],))
    resultado = cursor.fetchone()

    self.text_usuario.insert(tk.END, f"Empresa: {resultado[3]}\n")
    self.text_usuario.insert(tk.END, f"Nombre: {resultado[4]}\n")
    self.text_usuario.insert(tk.END, f"Edad: {resultado[5]}\n")
    self.text_usuario.insert(tk.END, f"CEDIS: {resultado[6]}\n")
    self.text_usuario.insert(tk.END, f"Puesto: {resultado[7]}\n")

    conn.close()

"""
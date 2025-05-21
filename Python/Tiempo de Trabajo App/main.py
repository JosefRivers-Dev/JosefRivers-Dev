import tkinter as tk
from tkinter import ttk, messagebox

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación principal")
        self.root.configure(bg="#000000")
        self.root.minsize(300, 500)
        self.root.maxsize(400, 600)

        self.pestaña_inicio = tk.Frame(self.root, bg="#000000")
        self.pestaña_inicio.pack(fill="both", expand=True)

        self.label_logo = tk.Label(self.pestaña_inicio, text="Banbu", font=("Calibre", 15, "bold"), bg="#FF0000", fg="#FFFFFF", width=10, height=2, borderwidth=1)  
        self.label_logo.pack(pady=10)

        self.titulo = tk.Label(self.pestaña_inicio, text="Mi tiempo de Trabajo", bg="#000000", fg="#FFFFFF", font=("Arial", 18))
        self.titulo.pack(pady=10)

        self.titulo = tk.Label(self.pestaña_inicio, text="Usuario", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.titulo.pack(pady=10)

        self.entrada_usuario = tk.Entry(self.pestaña_inicio)
        self.entrada_usuario.pack()

        self.titulo = tk.Label(self.pestaña_inicio, text="Contraseña", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.titulo.pack(pady=10)

        self.entrada_contraseña = tk.Entry(self.pestaña_inicio, show="*")
        self.entrada_contraseña.pack()

        self.boton_iniciar_sesion = tk.Button(self.pestaña_inicio, text="Iniciar sesión", bg="#007bff", fg="#FFFFFF", relief="flat", command=self.iniciar_sesion)
        self.boton_iniciar_sesion.pack(pady=20)

        self.nota_book = ttk.Notebook(self.root)
        self.nota_book.pack_forget()  

        self.frame_contenido_info = tk.Frame(self.nota_book, bg="#000000")
        self.nota_book.add(self.frame_contenido_info, text="Información del usuario")

        self.info_usuario = {
            "empresa": "Panditas Gomas",
            "puesto": "Administrador",
            "nombre_completo": "Juan Pérez",
            "edad": 30,
            "cedis": "CD-001",
            "ultima_sesion": "2024-10-07 10:00:00"
        }

        self.label_empresa = tk.Label(self.frame_contenido_info, text=f"Empresa: {self.info_usuario['empresa']}", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.label_empresa.pack(pady=10)

        self.label_puesto = tk.Label(self.frame_contenido_info, text=f"Puesto: {self.info_usuario['puesto']}", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.label_puesto.pack(pady=10)

        self.label_nombre_completo = tk.Label(self.frame_contenido_info, text=f"Nombre completo: {self.info_usuario['nombre_completo']}", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.label_nombre_completo.pack(pady=10)

        self.label_edad = tk.Label(self.frame_contenido_info, text=f"Edad: {self.info_usuario['edad']}", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.label_edad.pack(pady=10)

        self.label_cedis = tk.Label(self.frame_contenido_info, text=f"CEDIS: {self.info_usuario['cedis']}", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.label_cedis.pack(pady=10)

        self.label_ultima_sesion = tk.Label(self.frame_contenido_info, text=f"Última sesión: {self.info_usuario['ultima_sesion']}", bg="#000000", fg="#FFFFFF", font=("Arial", 12))
        self.label_ultima_sesion.pack(pady=10)

        self.boton_cerrar_sesion = tk.Button(self.frame_contenido_info, text="Cerrar sesión", bg="#FF0000", fg="#FFFFFF", relief="flat", command=self.cerrar_sesion)
        self.boton_cerrar_sesion.pack(pady=20)

        self.frame_contenido_formularios = tk.Frame(self.nota_book, bg="#000000")
        self.nota_book.add(self.frame_contenido_formularios, text="Formularios")

        self.label_formulario = tk.Label(self.frame_contenido_formularios, text="Formulario de ejemplo", bg="#000000", fg="#FFFFFF", font=("Arial", 18))
        self.label_formulario.pack(pady=10)

        self.entrada_formulario = tk.Entry(self.frame_contenido_formularios)
        self.entrada_formulario.pack()

        self.boton_enviar = tk.Button(self.frame_contenido_formularios, text="Enviar", bg="#007bff", fg="#FFFFFF", relief="flat")
        self.boton_enviar.pack(pady=10)

    def iniciar_sesion(self):
        usuario = self.entrada_usuario.get()
        contraseña = self.entrada_contraseña.get()
        
        if usuario == "admin" and contraseña == "123456":
            self.pestaña_inicio.pack_forget()  
            self.nota_book.pack(fill="both", expand=True)  
        else:
            messagebox.showerror("Inicio de sesión fallido", "Usuario o contraseña incorrectos")

    def cerrar_sesion(self):
        self.nota_book.pack_forget()  
        self.pestaña_inicio.pack(fill="both", expand=True)  

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
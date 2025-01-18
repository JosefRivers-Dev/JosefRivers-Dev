import tkinter as tk
from tkinter import messagebox, ttk

# Almacenamiento de usuarios y contraseñas (en un sistema real, utiliza una base de datos)
usuarios = {
    "admin": "password",
    "usuario1": "contraseña1",
    "usuario2": "contraseña2"
}

def iniciar_sesion():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()
    
    if usuario in usuarios and usuarios[usuario] == contraseña:
        messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido, {usuario}!")
        ventana_inicio.destroy()
        ventana_principal(usuario)
    else:
        messagebox.showerror("Inicio de sesión fallido", "Usuario o contraseña incorrectos")

def ventana_principal(usuario):
    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Aplicación principal")
    ventana.configure(bg="#000000")
    ventana.minsize(300, 500)
    ventana.maxsize(400, 600)

    # Frame para el contenido
    frame_contenido = tk.Frame(ventana, bg="#000000")
    frame_contenido.pack(pady=20)

    # Label con el nombre del usuario
    label_usuario = tk.Label(frame_contenido, text=f"Usuario: {usuario}", bg="#000000", fg="#FFFFFF")
    label_usuario.pack()

    # Frame para el menú inferior
    frame_menu = tk.Frame(ventana, bg="#007bff")
    frame_menu.pack(side=tk.BOTTOM, fill=tk.X)

    # Botones del menú
    boton_formularios = tk.Button(frame_menu, text="Formularios", bg="#007bff", fg="#FFFFFF", relief="flat", command=lambda: formularios(ventana, usuario))
    boton_formularios.pack(side=tk.LEFT, fill=tk.X, expand=True)

    boton_info_usuario = tk.Button(frame_menu, text="Información del usuario", bg="#007bff", fg="#FFFFFF", relief="flat", command=lambda: info_usuario(ventana, usuario))
    boton_info_usuario.pack(side=tk.LEFT, fill=tk.X, expand=True)

    # Iniciar ciclo de eventos
    ventana.mainloop()

def formularios(ventana, usuario):
    # Crear ventana de formularios
    ventana_formularios = tk.Toplevel(ventana)
    ventana_formularios.title("Formularios")
    ventana_formularios.configure(bg="#000000")
    ventana_formularios.minsize(300, 500)
    ventana_formularios.maxsize(400, 600)

    # Frame para el contenido
    frame_contenido = tk.Frame(ventana_formularios, bg="#000000")
    frame_contenido.pack(pady=20)

    # Label con el título de formularios
    label_formularios = tk.Label(frame_contenido, text="Formularios", bg="#000000", fg="#FFFFFF")
    label_formularios.pack(pady=20)

    # Agregar contenido de formularios
    boton_formulario1 = tk.Button(frame_contenido, text="Formulario 1", bg="#FF0000", fg="#FFFFFF", relief="flat", command=lambda: formulario1(ventana_formularios, usuario))
    boton_formulario1.pack()

    boton_formulario2 = tk.Button(frame_contenido, text="Formulario 2", bg="#FF0000", fg="#FFFFFF", relief="flat", command=lambda: formulario2(ventana_formularios, usuario))
    boton_formulario2.pack()

    # Frame para el menú superior
    frame_menu_superior = tk.Frame(ventana_formularios, bg="#007bff")
    frame_menu_superior.pack(side=tk.TOP, fill=tk.X)

    # Botones del menú superior
    boton_formularios_realizar = tk.Button(frame_menu_superior, text="Formularios a realizar", bg="#007bff", fg="#FFFFFF", relief="flat")
    boton_formularios_realizar.pack(side=tk.LEFT, fill=tk.X, expand=True)

    boton_formularios_finalizados = tk.Button(frame_menu_superior, text="Formularios finalizados", bg="#007bff", fg="#FFFFFF", relief="flat")
    boton_formularios_finalizados.pack(side=tk.LEFT, fill=tk.X, expand=True)

def formulario1(ventana_formularios, usuario):
    # Crear ventana de formulario 1
    ventana_formulario1 = tk.Toplevel(ventana_formularios)
    ventana_formulario1.title("Formulario 1")
    ventana_formulario1.configure(bg="#000000")
    ventana_formulario1.minsize(300, 500)
    ventana_formulario1.maxsize(400, 600)

    # Frame para el contenido
    frame_contenido = tk.Frame(ventana_formulario1, bg="#000000")
    frame_contenido.pack(pady=20)

    # Label con el título de formulario 1
    label_formulario1 = tk.Label(frame_contenido, text="Formulario 1", bg="#000000", fg="#FFFFFF")
    label_formulario1.pack(pady=20)

    # Etiquetas y entradas para fecha y hora de inicio
    etiqueta_fecha_inicio = tk.Label(frame_contenido, text="Fecha de inicio:", bg="#000000", fg="#FFFFFF")
    etiqueta_fecha_inicio.pack()
    entrada_fecha_inicio = tk.Entry(frame_contenido)
    entrada_fecha_inicio.pack()

    etiqueta_hora_inicio = tk.Label(frame_contenido, text="Hora de inicio:", bg="#000000", fg="#FFFFFF")
    etiqueta_hora_inicio.pack()
    entrada_hora_inicio = tk.Entry(frame_contenido)
    entrada_hora_inicio.pack()

    # Etiqueta y entrada para nombre
    etiqueta_nombre = tk.Label(frame_contenido, text="Nombre:", bg="#000000", fg="#FFFFFF")
    etiqueta_nombre.pack()
    entrada_nombre = tk.Entry(frame_contenido)
    entrada_nombre.pack()

    # Etiqueta y opción para actividad
    etiqueta_actividad = tk.Label(frame_contenido, text="Actividad:", bg="#000000", fg="#FFFFFF")
    etiqueta_actividad.pack()
    opciones_actividad = ["Capacitación", "Retroalimentación", "Ruta", "CEDIS", "Campo"]
    variable_actividad = tk.StringVar()
    variable_actividad.set(opciones_actividad[0])
    opcion_actividad = tk.OptionMenu(frame_contenido, variable_actividad, *opciones_actividad)
    opcion_actividad.pack()

    # Botón para crear formulario
    def crear_formulario():
        fecha_inicio = entrada_fecha_inicio.get()
        hora_inicio = entrada_hora_inicio.get()
        nombre = entrada_nombre.get()
        actividad = variable_actividad.get()
        
        # Verificar que todos los campos estén llenos
        if fecha_inicio and hora_inicio and nombre and actividad:
            # Mostrar mensaje de éxito
            messagebox.showinfo("Formulario creado", "El formulario se ha creado correctamente.")
        else:
            # Mostrar mensaje de error
            messagebox.showerror("Error", "Por favor, llene todos los campos.")

    boton_crear_formulario = tk.Button(frame_contenido, text="Crear formulario", bg="#007bff", fg="#FFFFFF", relief="flat", command=crear_formulario)
    boton_crear_formulario.pack(pady=20)

    # Label para mostrar estado del formulario
    label_estado_formulario = tk.Label(frame_contenido, text="", bg="#000000", fg="#FFFFFF")
    label_estado_formulario.pack()

def formulario2(ventana_formularios, usuario):
    # Código para formulario 2...
    pass

def info_usuario(ventana, usuario):
    # Código para información del usuario...
    pass


# Crear ventana de inicio de sesión
ventana_inicio = tk.Tk()
ventana_inicio.title("Aplicación de inicio de sesión")
ventana_inicio.configure(bg="#000000")
ventana_inicio.minsize(300, 500)
ventana_inicio.maxsize(400, 600)

# Agregar logo
logo = tk.PhotoImage(file="Adecco.png")  # reemplaza "logo.png" con el nombre de tu archivo de imagen
label_logo = tk.Label(ventana_inicio, image=logo, bg="#000000")
label_logo.pack(pady=50)

# Etiquetas y entradas para usuario y contraseña
etiqueta_usuario = tk.Label(ventana_inicio, text="Usuario:", bg="#000000", fg="#FFFFFF")
etiqueta_usuario.pack()

entrada_usuario = tk.Entry(ventana_inicio)
entrada_usuario.pack()

etiqueta_contraseña = tk.Label(ventana_inicio, text="Contraseña:", bg="#000000", fg="#FFFFFF")
etiqueta_contraseña.pack()

entrada_contraseña = tk.Entry(ventana_inicio, show="*")
entrada_contraseña.pack()

boton_iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar sesión", bg="#007bff", fg="#FFFFFF", relief="flat", command=iniciar_sesion)
boton_iniciar_sesion.pack(pady=20)

# Botón para salir
boton_salir = tk.Button(ventana_inicio, text="Salir", bg="#FF0000", fg="#FFFFFF", relief="flat", command=ventana_inicio.destroy)
boton_salir.pack(pady=10)

# Iniciar ciclo de eventos
ventana_inicio.mainloop()
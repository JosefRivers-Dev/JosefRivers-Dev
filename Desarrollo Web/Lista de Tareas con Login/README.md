# Aplicación de Gestión de Tareas

Este proyecto es una aplicación web simple para gestionar tareas, con autenticación de usuarios y funcionalidad CRUD para las tareas.

## Características principales

- Autenticación de usuarios mediante credenciales almacenadas en un archivo de texto
- Visualización de lista de tareas con diferentes estados
- Edición de tareas (estado y comentarios)
- Interfaz intuitiva con tres pantallas principales:
  - Inicio de sesión
  - Lista de tareas
  - Detalle de tarea

## Estructura del proyecto

```
.
├── index.html        # Página principal con las tres vistas
├── script.js         # Lógica de la aplicación
├── styles.css        # Estilos CSS
├── usuarios.txt      # Base de datos de usuarios
└── tareas.txt        # Base de datos de tareas
```

## Requisitos

Navegador web moderno (Chrome, Firefox, Edge, Safari)

## Instalación

1. Clonar o descargar el repositorio
2. Abrir el archivo `index.html` en un navegador web

## Uso

1. Iniciar sesión con las credenciales proporcionadas en `usuarios.txt`
   - Ejemplo de usuario: `usuario1` con contraseña `contraseña1`
2. Ver la lista de tareas
3. Hacer clic en "Editar" para ver los detalles de una tarea
4. Modificar el estado y/o comentario
5. Guardar los cambios
6. Regresar a la lista de tareas

## Estructura de datos

### usuarios.txt
Formato: `nombre_usuario,email,contraseña`

### tareas.txt
Formato: `nombre_tarea,descripcion,estado,comentario`

Los estados posibles son:
- `pendiente`
- `en-proceso`
- `realizado`

## Limitaciones

- Los datos se almacenan en archivos de texto plano (no recomendado para producción)
- No hay persistencia de sesión
- No hay validación avanzada de datos

## Mejoras potenciales

- Implementar base de datos real
- Añadir registro de nuevos usuarios
- Permitir creación/eliminación de tareas
- Implementar búsqueda/filtrado de tareas
- Añadir autenticación más segura

## Capturas de pantalla

(Puedes añadir capturas de las diferentes pantallas aquí)
# Sistema de Gestión de Tiempo Laboral - Banbu

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Tkinter](https://img.shields.io/badge/Tkinter-GUI%20Toolkit-green) ![Aplicación](https://img.shields.io/badge/Aplicación-Desktop-yellow)

Interfaz gráfica para gestión de tiempo de trabajo con autenticación de usuarios y perfiles personalizados.

## Características Principales

- **Autenticación segura** con usuario y contraseña
- **Interfaz con pestañas** para diferentes módulos
- **Perfil de usuario** con información detallada
- **Diseño moderno** con esquema de colores oscuro
- **Sistema de formularios** integrado
- **Control de sesiones** con registro de último acceso

## Requisitos

- Python 3.8+
- Módulos:
  - tkinter (incluido en Python estándar)
  - ttk (incluido en tkinter)

## Instalación

1. Clonar repositorio o descargar `main.py`
2. Ejecutar:
```bash
python main.py
```

## Estructura de la Aplicación

### Pantalla de Login
- Campos para usuario y contraseña
- Validación de credenciales
- Diseño con logo corporativo

### Área Principal (tras login)
- **Pestaña de Información**:
  - Datos personales del empleado
  - Detalles de la empresa
  - Información de CEDIS
  - Botón de cierre de sesión

- **Pestaña de Formularios**:
  - Ejemplo de formulario básico
  - Campo de entrada y botón de envío

## Credenciales de Acceso
- Usuario: `admin`
- Contraseña: `123456`

## Personalización

Para adaptar la aplicación:
1. Modificar `info_usuario` en el código para cambiar datos del perfil
2. Ajustar colores en las propiedades `bg` y `fg`
3. Cambiar dimensiones en `minsize` y `maxsize`

## Capturas de Pantalla

<!-- Incluir imágenes del login y pantalla principal -->

## Roadmap de Mejoras

- [ ] Conexión a base de datos para usuarios
- [ ] Sistema de roles y permisos
- [ ] Registro de horas trabajadas
- [ ] Integración con sistema de nómina
- [ ] Exportación de reportes

## Consideraciones de Seguridad

⚠️ **Importante**: Esta es una versión demo. Para uso en producción:
- Implementar hash para contraseñas
- Usar conexiones seguras
- Actualizar credenciales por defecto
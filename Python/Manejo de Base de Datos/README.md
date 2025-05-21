# Ejemplos de SQLite con Python

![Python](https://img.shields.io/badge/Python-3.6%2B-blue) ![SQLite](https://img.shields.io/badge/SQLite-3.0%2B-green) ![Database](https://img.shields.io/badge/Database-Examples-yellow)

Serie de scripts Python que muestran operaciones básicas con bases de datos SQLite.

## Estructura del Proyecto

```
.
├── 01-PrimerBaseDatos.py       # Creación de la base de datos y tabla
├── 02-AgregarRegistros.py      # Inserción de registros
├── 03-SeleccionarRegistros.py  # Consulta de datos
└── 04-ModificarEliminarRegistro.py # Actualización y eliminación
```

## Descripción de los Scripts

### �️ `01-PrimerBaseDatos.py`
- Crea una base de datos SQLite llamada `primerBaseDatos.db`
- Establece una tabla `animales` con campos:
  - `codigo` (clave primaria autoincremental)
  - `especie` (texto)
  - `edad` (entero)
- Incluye ejemplos comentados de creación condicional de tablas

### ➕ `02-AgregarRegistros.py`
- Inserta 5 registros en la tabla `animales`
- Muestra dos métodos de inserción:
  - Especificando todos los campos
  - Especificando solo campos requeridos
- Usa `commit()` para guardar cambios permanentemente

### 🔍 `03-SeleccionarRegistros.py`
- Consulta todos los registros de la tabla
- Muestra diferentes métodos para recuperar resultados:
  - `fetchone()` (lee un registro a la vez)
  - `fetchall()` (comentado)
  - Iteración directa sobre el cursor (comentado)

### ✏️ `04-ModificarEliminarRegistro.py`
- Actualiza la edad del animal con código 3
- Ejemplo comentado de eliminación de registro
- Muestra cómo usar `WHERE` para operaciones específicas

## Cómo Usar

1. Ejecutar los scripts en orden:
```bash
python 01-PrimerBaseDatos.py
python 02-AgregarRegistros.py
python 03-SeleccionarRegistros.py
python 04-ModificarEliminarRegistro.py
```

2. Verificar la base de datos generada:
```bash
sqlite3 primerBaseDatos.db
> .tables
> SELECT * FROM animales;
```

## Requisitos

- Python 3.6+
- Módulo `sqlite3` (incluido en la biblioteca estándar de Python)

## Buenas Prácticas Mostradas

- Uso de `try-except` para manejo de errores (comentado)
- Transacciones con `commit()`
- Consultas parametrizadas (implícitas)
- Varios métodos de recuperación de datos

---

**Nota**: Estos scripts son ejemplos educativos para aprender SQLite con Python. Adapta los nombres de tablas y campos según tus necesidades.
```

Este README ofrece:
- Descripción clara de cada script
- Instrucciones de ejecución ordenada
- Comandos SQLite para verificar resultados
- Buenas prácticas implementadas
- Sugerencias para ampliar la funcionalidad
- Badges visuales para tecnologías clave
- Nota sobre el propósito educativo

El formato es ideal para proyectos de aprendizaje, mostrando progresivamente diferentes operaciones CRUD con SQLite desde Python.
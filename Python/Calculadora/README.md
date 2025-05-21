# Calculadora en Python con Tkinter

![Python](https://img.shields.io/badge/Python-3.6%2B-blue) ![Tkinter](https://img.shields.io/badge/Tkinter-GUI%20Toolkit-green)

Una calculadora básica pero funcional desarrollada con Python y la biblioteca Tkinter para crear interfaces gráficas de usuario.

## Características Principales

- Interfaz gráfica intuitiva
- Operaciones básicas: suma, resta, multiplicación y división
- Soporte para números decimales
- Botón de borrado completo (C)
- Manejo de errores en operaciones inválidas

## Requisitos

- Python 3.6 o superior
- Biblioteca Tkinter (normalmente incluida en instalaciones estándar de Python)

## Instalación

No se requieren instalaciones adicionales más allá de Python estándar.

## Uso

1. Ejecutar el script:
```
bash
python main.py
```

2. La calculadora aparecerá en una ventana con:
   - Campo de texto superior para visualización
   - Teclado numérico (0-9)
   - Operadores básicos (+, -, *, /)
   - Botón de igual (=) para calcular
   - Botón de borrado (C)

3. Realizar operaciones:
   - Hacer clic en los números y operadores
   - Presionar "=" para ver el resultado
   - Usar "C" para borrar todo

## Estructura del Código

```python
class Calculadora:
    def __init__(self):  # Configuración inicial de la ventana y widgets
    def click_boton(self, boton):  # Maneja las pulsaciones de botones
    def borrar(self):  # Limpia la pantalla
    def run(self):  # Inicia el bucle principal
```

## Limitaciones Actuales

- No soporta operaciones complejas o científicas
- No mantiene historial de cálculos
- No tiene memoria para almacenar valores

## Mejoras Planeadas

- [ ] Añadir funcionalidad de memoria (M+, M-, MR, MC)
- [ ] Implementar operaciones científicas (potencias, raíces, etc.)
- [ ] Añadir historial de cálculos
- [ ] Mejorar el diseño de la interfaz
# Proyecto: Optimización del Proceso de Renovación de Licencia

## Descripción
Este proyecto implementa un sistema automatizado para el proceso de renovación de licencias, desarrollado en PSeInt (Pseudocódigo Intérprete). El sistema guía al usuario a través de un proceso paso a paso para validar datos personales, procesar pagos y generar la renovación de la licencia.

## Autor
- **Alumno:** Rivera Reyes Jovanny Josef
- **Licenciatura:** Tecnología de Información y Comunicación
- **Universidad:** Universidad Rosario Castellanos
- **Materia:** Lógica de Programación
- **Docente:** Cosme Antonio Fragado Farías
- **Fecha:** Miércoles 05 de Mayo del 2024

## Características principales
1. **Validación de datos personales:**
   - Nombre completo
   - Fecha de nacimiento
   - Número de licencia actual

2. **Proceso de pago:**
   - Soporte para pagos en efectivo y con tarjeta
   - Validación de datos de pago
   - Generación de folios y comprobantes

3. **Automatización:**
   - Generación automática de fechas (pago y vencimiento)
   - Barras de progreso visuales
   - Mensajes de confirmación

4. **Manejo de errores:**
   - Validación de campos obligatorios
   - Límite de intentos
   - Mensajes de error descriptivos

## Estructura del programa
El programa se organiza en los siguientes subprocesos principales:

1. **IngresoSistema:** Muestra la pantalla de bienvenida
2. **ValidarDatosPersonales:** Verifica la información del usuario
3. **ProcesoDePago:** Maneja la transacción financiera
4. **barraCargaDoc:** Muestra una barra de progreso visual

## Requisitos
- PSeInt (Pseudocódigo Intérprete) versión compatible
- Sistema operativo Windows, Linux o macOS

## Instrucciones de uso
1. Ejecutar el algoritmo en PSeInt
2. Seguir las instrucciones en pantalla:
   - Ingresar datos personales
   - Seleccionar método de pago
   - Proporcionar información de pago
3. El sistema generará automáticamente la renovación con:
   - Fecha de pago actual
   - Fecha de vencimiento (1 año después)

## Validaciones implementadas
- Campos obligatorios no vacíos
- Formato de número de licencia
- Clave de pago específica (20240311107)
- Datos de tarjeta válidos
- Código de folio para pagos en efectivo

## Mensajes de salida
El sistema genera comprobantes detallados que incluyen:
- Nombre completo del ciudadano
- Número de licencia
- Fecha de pago
- Fecha de vencimiento
- Método de pago utilizado

## Consideraciones
- El programa incluye pausas (Esperar) para mejor experiencia de usuario
- Se limpia la pantalla (Borrar Pantalla) entre secciones
- El código está comentado para facilitar su comprensión y mantenimiento

## Notas adicionales
Este proyecto fue desarrollado como ejercicio académico para la materia de Lógica de Programación en la Universidad Rosario Castellanos.
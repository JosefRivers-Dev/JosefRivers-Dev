# WhatsApp Chat Extractor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-green) ![WhatsApp](https://img.shields.io/badge/WhatsApp-Web-orange)

Herramienta automatizada para extraer conversaciones de WhatsApp Web y guardarlas en archivos CSV.

## Características Principales

- Extracción automatizada de chats mediante Selenium
- Soporte para múltiples números de teléfono desde archivo CSV
- Detección automática de codificación de archivos
- Guardado de conversaciones en formato CSV
- Manejo robusto de errores

## Requisitos

- Python 3.8+
- Chrome o Chromium instalado
- Cuenta de WhatsApp activa
- Archivo CSV con números de teléfono

### Dependencias

```bash
pip install selenium webdriver-manager chardet
```

## Configuración

1. Crear archivo `numeros.csv` con los números a consultar (un número por línea)
2. Configurar la ruta en `RUTA_CSV` (línea 8 del script)

## Uso

1. Ejecutar el script:
```bash
python main.py
```

2. Escanear el código QR de WhatsApp Web cuando se solicite

3. Los chats se guardarán como `chat_[número].csv` en el mismo directorio

## Estructura del Código

```python
# Funciones principales:
detectar_codificacion()   # Detecta codificación del CSV
leer_numeros_desde_csv()  # Lee números telefónicos
extraer_mensajes()        # Extrae conversaciones de WhatsApp
main()                    # Función principal
```

## Archivos Generados

Cada chat se guarda en formato CSV con dos columnas:
- `Remitente`: Nombre o número del contacto
- `Mensaje`: Contenido del mensaje

## Limitaciones

- Requiere sesión activa de WhatsApp Web
- Depende de la estructura HTML de WhatsApp (puede romperse con actualizaciones)
- Tiempo de espera fijo para cargar mensajes

## Consideraciones Legales

⚠️ **Importante**: Este script debe usarse solo con contactos que hayan dado su consentimiento para guardar las conversaciones. El desarrollador no se hace responsable del mal uso de esta herramienta.

## Roadmap

- [ ] Soporte para exportar multimedia
- [ ] Interfaz gráfica de usuario
- [ ] Opción para seleccionar rango de fechas
- [ ] Exportación a JSON y HTML

## Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea tu rama de feature (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -m 'Añade nueva funcionalidad'`)
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request
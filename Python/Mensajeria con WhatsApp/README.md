# WhatsApp Bulk Messenger

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-green) ![WhatsApp](https://img.shields.io/badge/WhatsApp-Web-orange)

Herramienta automatizada para enviar mensajes masivos a través de WhatsApp Web usando Python y Selenium.

## ⚠️ Advertencia Legal
Este software está diseñado solo para fines educativos y de automatización legítima. El uso inapropiado puede violar los Términos de Servicio de WhatsApp. El desarrollador no se hace responsable del mal uso de esta herramienta.

## Características Principales

- Envío masivo de mensajes personalizados
- Integración con Chrome en modo debug
- Gestión de contactos mediante CSV
- Registro detallado de resultados
- Retardo configurable entre mensajes
- Reconexión automática a sesiones existentes

## Requisitos

- Python 3.8+
- Google Chrome instalado
- Cuenta de WhatsApp activa
- Archivo CSV con números de contacto

### Dependencias
```bash
pip install selenium pandas webdriver-manager
```

## Configuración

1. Crear archivo `data_clientes.csv` con columna `NumeroContacto`
2. Configurar rutas en el script:
   - `USER_DATA_DIR`: Perfil de Chrome
   - `CSV_CONTACTOS`: Ruta del CSV de contactos
   - `DELAY_ENTRE_MENSAJES`: Retardo entre envíos (segundos)

3. Personalizar el mensaje en la variable `MENSAJE`

## Uso

1. Ejecutar el script:
```bash
python main.py
```

2. Escanear el código QR de WhatsApp Web cuando aparezca

3. Los resultados se guardarán en `~/Downloads/resultados_envios.csv`

## Estructura del Código

```python
# Funciones principales:
abrir_chrome_en_modo_debug()  # Configura Chrome
enviar_mensaje()             # Gestiona el envío
guardar_resultado()          # Registra resultados
```

## Archivos Generados

- `resultados_envios.csv` con columnas:
  - Contacto
  - Estado (✅/❌)
  - Error (si aplica)

## Buenas Prácticas Implementadas

- Esperas inteligentes con WebDriverWait
- Manejo robusto de errores
- Limpieza exhaustiva entre búsquedas
- Verificación de envíos exitosos
- Registro detallado de operaciones

## Limitaciones

- Requiere sesión activa de WhatsApp Web
- Depende de la estructura HTML de WhatsApp
- No soporta envío de archivos multimedia
- Velocidad limitada para evitar baneos

## Roadmap

- [ ] Soporte para imágenes/archivos
- [ ] Envío programado
- [ ] Interfaz gráfica
- [ ] Manejo de errores mejorado
- [ ] Sistema de reintentos

## Contribuciones

Las contribuciones son bienvenidas siguiendo el proceso estándar:
1. Fork del proyecto
2. Crear feature branch
3. Commit de cambios
4. Push a la rama
5. Abrir Pull Request
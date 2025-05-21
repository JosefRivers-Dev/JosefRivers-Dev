# Generador de Códigos QR con Kivy

![Python](https://img.shields.io/badge/Python-3.7%2B-blue) ![Kivy](https://img.shields.io/badge/Kivy-2.0%2B-green) ![QRCode](https://img.shields.io/badge/QRCode-generador-yellow)

Aplicación móvil y de escritorio para generar y descargar códigos QR a partir de texto o URLs, desarrollada con Python y Kivy.

## Características Principales

- Interfaz gráfica intuitiva y responsive
- Generación instantánea de códigos QR
- Capacidad para descargar los QR generados
- Validación de entrada vacía
- Notificaciones mediante popups
- Diseño adaptado para móviles y desktop

## Requisitos del Sistema

- Python 3.7 o superior
- Bibliotecas requeridas:
```bash
pip install kivy qrcode[pil]
```

## Instalación y Ejecución

1. Clonar el repositorio o descargar el archivo `main.py`
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
   (Archivo `requirements.txt` debe contener: `kivy>=2.0.0` y `qrcode[pil]>=7.0`)

3. Ejecutar la aplicación:
   ```bash
   python main.py
   ```

## Uso de la Aplicación

1. **Ingresar texto/URL**: Escribe en el campo de texto superior
2. **Generar QR**: Presiona el botón verde "Generar QR"
3. **Visualizar**: El código QR aparecerá en el área central
4. **Descargar**: Usa el botón azul para guardar en tu carpeta de Descargas

## Estructura del Código

```python
class QRGeneratorApp(App):
    def build(self):        # Configura la interfaz gráfica
    def generate_qr(self):  # Genera el código QR
    def download_qr(self):  # Guarda el QR en Downloads
    def show_popup(self):   # Muestra mensajes emergentes
```

## Roadmap de Mejoras

- [ ] Personalización de colores del QR
- [ ] Selección de tamaño de imagen
- [ ] Historial de códigos generados
- [ ] Compartir directamente desde la app
- [ ] Versión APK para Android

## Limitaciones Actuales

- Solo genera códigos QR estáticos
- Formato de imagen fijo (PNG)
- No permite corrección de errores personalizada

## Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama con tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -m 'Añade nueva funcionalidad'`)
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
import qrcode

class QRGeneratorApp(App):
    def build(self):

        # Configuración de la ventana
        Window.size = (300, 600)
        self.title = "Generador de QR"

        # Layout principal
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Input de texto
        self.text_input = TextInput(
            hint_text="Ingresa",
            size_hint=(1, 0.2),
            multiline=False,
        )
        layout.add_widget(self.text_input)

        # Botón para generar el QR
        generate_button = Button(
            text="Generar QR",
            size_hint=(1, 0.1),
            background_color=(0, 0.7, 0.3, 1),
        )
        generate_button.bind(on_press=self.generate_qr)
        layout.add_widget(generate_button)

        # Imagen del QR (inicialmente vacía)
        self.qr_image = Image(size_hint=(1, 0.6))
        layout.add_widget(self.qr_image)

        # Botón para descargar el QR
        self.download_button = Button(
            text="Descargar QR",
            size_hint=(1, 0.1),
            background_color=(0.2, 0.5, 0.8, 1),
            disabled=True,  # Deshabilitado hasta que se genere un QR
        )
        self.download_button.bind(on_press=self.download_qr)
        layout.add_widget(self.download_button)

        return layout

    def generate_qr(self, instance):
        # Obtener el texto del input
        text = self.text_input.text.strip()

        if not text:
            self.show_popup("Error", "Por favor, ingresa un texto o URL.")
            return

        # Generar el código QR
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5,
        )
        qr.add_data(text)
        qr.make(fit=True)

        # Crear la imagen del QR
        img = qr.make_image(fill_color="black", back_color="white")
        img_path = "qr_code.png"
        img.save(img_path)

        # Mostrar la imagen en la aplicación
        self.qr_image.source = img_path
        self.qr_image.reload()

        # Habilitar el botón de descarga
        self.download_button.disabled = False

    def download_qr(self, instance):
        # Mover el archivo a una ubicación permanente (por ejemplo, la carpeta de descargas)
        import shutil
        downloads_path = os.path.expanduser("~/Downloads")
        final_path = os.path.join(downloads_path, "qr_code.png")

        shutil.copy("qr_code.png", final_path)
        self.show_popup("Éxito", f"QR descargado en: {final_path}")

    def show_popup(self, title, message):
        # Mostrar un popup con un mensaje
        popup_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        popup_label = Label(text=message, size_hint=(1, 0.8))
        close_button = Button(text="Cerrar", size_hint=(1, 0.2))
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(close_button)

        popup = Popup(
            title=title,
            content=popup_layout,
            size_hint=(0.8, 0.4),
        )
        close_button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == "__main__":
    QRGeneratorApp().run()
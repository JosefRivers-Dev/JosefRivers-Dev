import os
import time
import csv
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración global
DEBUG_PORT = 9222
USER_DATA_DIR = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data')
WHATSAPP_URL = "https://web.whatsapp.com/"
CSV_CONTACTOS = 'MensajeriaMasiva/data_clientes.csv'
CSV_RESULTADOS = os.path.join(os.path.expanduser("~"), "Downloads", "resultados_envios.csv")
DELAY_ENTRE_MENSAJES = 5
CHROMEDRIVER_PATH = "C:\\chromedriver\\chromedriver.exe"
archivo_resultados = "envios_resultados.csv"
descargas_path = os.path.join(os.path.expanduser("~"), "Downloads", archivo_resultados)


# Mensaje predeterminado (personalizable)
MENSAJE = """
¡Hola! 👋

Este es un mensaje automatizado.
Saludos desde Python + Selenium.

🚀
""".strip()


# --- Funciones principales ---
def abrir_chrome_en_modo_debug():
    """Abre Chrome con el puerto de depuración habilitado."""
    import subprocess
    
    # Ruta de Chrome (Windows)
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    if not os.path.exists(chrome_path):
        chrome_path = os.path.join(os.getenv('PROGRAMFILES(X86)'), 'Google', 'Chrome', 'Application', 'chrome.exe')
    
    # Comando para abrir Chrome
    comando = [
        chrome_path,
        f"--remote-debugging-port={DEBUG_PORT}",
        f"--user-data-dir={USER_DATA_DIR}",
        "--no-first-run",
        "--no-default-browser-check",
        WHATSAPP_URL
    ]
    
    try:
        subprocess.Popen(comando, shell=True)
        print("✅ Chrome abierto")
        time.sleep(10)  # Espera a que Chrome cargue
    except Exception as e:
        print("❌ Error al abrir Chrome")
        exit()


def guardar_resultado(numero, envio_msg, envio_archivos="", error=""):
    """Guarda los resultados de cada envío en el archivo CSV"""
    with open(descargas_path, mode='a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([numero, envio_msg, envio_archivos, error])


def enviar_mensaje(contacto, mensaje=MENSAJE):
    try:
        # Paso 1: Limpiar la búsqueda anterior
        try:
            search_box = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            )
            search_box.click()
            search_box.clear()
            time.sleep(1)

            # Limpieza exhaustiva
            search_box.send_keys(Keys.CONTROL + "a")
            search_box.send_keys(Keys.DELETE)
            time.sleep(1)
        except Exception as e:
            print(f"Error al limpiar búsqueda")
            guardar_resultado(contacto, "No", "", "Error al limpiar búsqueda")
            return False
        
        # Paso 2: Buscar el contacto
        search_box.send_keys(contacto)
        time.sleep(1)
        
        # Presionar Enter para buscar
        search_box.send_keys(Keys.RETURN)
        time.sleep(1)
        
        # Paso 3: Enviar el mensaje
        try:
            # Localizar el campo de texto del chat (data-tab="10" es el campo de entrada en WhatsApp)
            input_box = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
            )
            
            # Escribir el mensaje carácter por carácter (más confiable que enviarlo todo de una)
            input_box.click()
            input_box.send_keys(mensaje)
                        
            # Enviar el mensaje con ENTER
            input_box.send_keys(Keys.ENTER)
            
            # Verificación de envío exitoso
            try:
                # Buscar el mensaje enviado en el chat
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, f'//span[contains(@class, "selectable-text")][contains(., "{mensaje[:20]}")]'))
                )

                # Mensajes en consola para visualizar el proceso quese esta realizando
                print(f"✅ Mensaje enviado a {contacto}")
                guardar_resultado(contacto, "Si", "", "")
                return True
            except:
                print(f"❌ No se pudo confirmar envío: {contacto}")
                guardar_resultado(contacto, "No", "", "No se pudo confirmar envío")
                return False
                
        except Exception as e:
            print(f"❌ Error al enviar mensaje: {contacto}")
            guardar_resultado(contacto, "No", "", "Error al enviar mensaje")
            return False
            
    except Exception as e:
        print(f"❌ Error general con: {contacto}")
        guardar_resultado(contacto, "No", "", "Error general")
        return False
    finally:
        # Regresar a la vista principal para el siguiente contacto
        try:
            driver.find_element(By.XPATH, '//div[@data-testid="chat-list-search"]').click()
            time.sleep(0.5)
        except:
            pass


# --- Ejecución principal ---
if __name__ == "__main__":
    # 1. Abrir Chrome automáticamente
    driver = abrir_chrome_en_modo_debug()
    print("🔌 Conectado")
    time.sleep(1)

    # 3. Cargar contactos desde CSV
    try:
        df = pd.read_csv(CSV_CONTACTOS)
        contactos = df['NumeroContacto'].astype(str).tolist()
        print(f"📋 Total de contactos: {len(contactos)}")
    except Exception as e:
        print("❌ Error al leer el CSV")
        exit()
    
    # 4. Procesar envíos
    with open(CSV_RESULTADOS, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Contacto', 'Estado', 'Error'])
        
        for contacto in contactos:
            exito = enviar_mensaje(driver, contacto)
            writer.writerow([contacto, "✅" if exito else "❌", "" if exito else "Error de envío"])
            time.sleep(DELAY_ENTRE_MENSAJES)
    
    # 5. Cierre
    print(f"\n🎉 Proceso completado. Resultados guardados en:\n{CSV_RESULTADOS}")
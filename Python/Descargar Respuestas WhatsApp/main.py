import csv
import os
import time
import chardet
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Ruta del archivo CSV con los números de teléfono
RUTA_CSV = r'C:\Users\HP\Desktop\Desarrollos\DescargarWhatsAppChat\numeros.csv'

# Configuración de la sesión de WhatsApp
URL_WHATSAPP_WEB = "https://web.whatsapp.com"

# Tiempo de espera para que se carguen los mensajes
TIEMPO_ESPERA_MENSAJES = 60

# Función para detectar la codificación de un archivo
def detectar_codificacion(ruta_archivo):
    with open(ruta_archivo, 'rb') as f:
        resultado = chardet.detect(f.read())
    return resultado['encoding']

# Función para leer números de teléfono desde el archivo CSV
def leer_numeros_desde_csv(ruta_archivo):
    try:
        codificacion = detectar_codificacion(ruta_archivo)
        with open(ruta_archivo, 'r', encoding=codificacion) as archivo_csv:
            return [fila[0].strip() for fila in csv.reader(archivo_csv) if fila]
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return []

# Función para extraer mensajes de un chat
def extraer_mensajes(driver, numero):
    try:
        mensajes = WebDriverWait(driver, TIEMPO_ESPERA_MENSAJES).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="_1Gy50"]//div[@class="_21Ahp"]'))
        )
        
        mensajes_extraidos = []
        for mensaje in mensajes:
            remitente = mensaje.find_element(By.XPATH, './/span[contains(@class,"_1wjpf")]').text
            contenido = mensaje.find_element(By.XPATH, './/div[contains(@class,"copyable-text")]').text
            mensajes_extraidos.append([remitente, contenido])
        
        print(f"Mensajes extraídos para {numero}: {len(mensajes_extraidos)}")
        return mensajes_extraidos
    
    except Exception as e:
        print(f"Error al extraer mensajes para {numero}: {e}")
        return []

# Función principal
def main():
    numeros_telefono = leer_numeros_desde_csv(RUTA_CSV)
    if not numeros_telefono:
        print("No se encontraron números en el archivo CSV.")
        return
    
    opciones = webdriver.ChromeOptions()
    opciones.add_argument('start-maximized')
    opciones.add_argument('--disable-extensions')
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opciones)
    
    try:
        driver.get(URL_WHATSAPP_WEB)
        print("Escanea el código QR para iniciar sesión.")
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//div[@id='app']")))
        
        for numero in numeros_telefono:
            try:
                search_box = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
                )
                search_box.clear()
                search_box.send_keys(numero)
                time.sleep(2)
                search_box.send_keys(Keys.ENTER)
                
                mensajes = extraer_mensajes(driver, numero)
                if mensajes:
                    with open(f"chat_{numero}.csv", "w", newline='', encoding="utf-8") as archivo:
                        writer = csv.writer(archivo)
                        writer.writerow(["Remitente", "Mensaje"])
                        writer.writerows(mensajes)
                    print(f"Chat de {numero} guardado correctamente.")
                else:
                    print(f"No se encontraron mensajes para {numero}.")
                    with open(f"chat_{numero}.csv", "w", newline='', encoding="utf-8") as archivo:
                        writer = csv.writer(archivo)
                        writer.writerow(["Error", "No se encontró información para este número."])
            except Exception as e:
                print(f"Error al procesar el número {numero}: {e}")
                with open(f"chat_{numero}.csv", "w", newline='', encoding="utf-8") as archivo:
                    writer = csv.writer(archivo)
                    writer.writerow(["Error", "No se encontró información para este número."])
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
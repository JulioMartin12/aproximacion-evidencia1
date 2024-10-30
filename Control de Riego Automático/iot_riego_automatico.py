from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C
import urequests
import network
import time
import ujson

# ==================  SECCION SIMULACION WIFI ==================================

# Parámetros de WiFi
SSID = "Wokwi-GUEST"
PASSWORD = ""

# Conexión a Wifi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print('Conectando a la red...')
    while not wlan.isconnected():
        time.sleep(1)
    print('Conectado a la red:', wlan.ifconfig())

# Iniciamos ESP32 con conexión a Wi-Fi
connect_wifi()
# ===============================================================================

# ============= Función para enviar un POST a la API ============================
def send_post_request(humedad):
    url = "https://control-de-riego-automatico.onrender.com/api/riego/data"
    data = {'humedad': humedad}
    json_data = ujson.dumps(data)

    # Enviar la solicitud POST
    try:
        print("Enviando solicitud POST a la API...")
        response = urequests.post(url, data=json_data, headers={"Content-Type": "application/json"})

        print("Código de respuesta:", response.status_code)
        print("Respuesta del servidor:", response.text)
        response.close()
    except Exception as e:
        print("Error al enviar la solicitud:", e)
# ===============================================================================

# Configuración del display OLED
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Pines I2C del ESP32
oled = SSD1306_I2C(128, 64, i2c)        # Configuración de la pantalla OLED (128x64)

# Configuración de pines
sensorHumedadPin = ADC(Pin(34))  # Pin analógico para el sensor de humedad (simulado con potenciómetro)
sensorHumedadPin.atten(ADC.ATTN_11DB)  # Ajuste del rango de lectura (0-3.3V)
relePin = Pin(25, Pin.OUT)  # Pin digital para controlar el relé (y el LED)

# Activación humedad al 40% (aprox.)
UMBRAL_HUMEDAD = 1638  # Potencia máxima del ADC es 4095, esto es aprox. 40% del rango.

def leer_humedad():
    # Leer valor analógico del sensor de humedad
    return sensorHumedadPin.read()

def mostrar_texto(texto1, texto2=""):
    # Limpiar la pantalla y mostrar dos líneas de texto
    oled.fill(0)  # Limpia la pantalla
    oled.text(texto1, 0, 0)  # Primera línea
    oled.text(texto2, 0, 10)  # Segunda línea (si es necesario)
    oled.show()

def main():
    while True:
        # Leer el valor del sensor de humedad
        humedad = leer_humedad()
        print("Humedad del suelo (valor ADC):", humedad)

        # Controlar la bomba según el valor de humedad
        if humedad < UMBRAL_HUMEDAD:
            relePin.value(1)  # Encender bomba (activar relé)
            print("Bomba activada")
            mostrar_texto("NECESITO AGUA", "Bomba activada")
        else:
            relePin.value(0)  # Apagar bomba (desactivar relé)
            print("Bomba desactivada")
            mostrar_texto("TODO BIEN POR AQUI", "Bomba desactivada")

        # Enviar la lectura de humedad a la API
        send_post_request(humedad)

        time.sleep(10)  # Esperar 10 segundos antes de la siguiente lectura

# Ejecutar el bucle principal
main()

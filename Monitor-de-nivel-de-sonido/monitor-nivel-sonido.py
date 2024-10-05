#Julio Martín
from machine import Pin, Timer
import time
import urequests
import ujson
import network
import ntptime  # Para obtener la hora actual

# ==================  SECCIÓN SIMULACIÓN WIFI ==================================

# Parámetros de WiFi
SSID = "Wokwi-GUEST"
PASSWORD = ""

# Conexión a WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print('Conectando a la red...')
    while not wlan.isconnected():
        time.sleep(1)
    print('Conectado a la red:', wlan.ifconfig())
    # Sincronizar con NTP para obtener la hora
    ntptime.settime()

# Iniciar ESP32
connect_wifi()

# ============= Función para enviar un POST a la API ============================
def send_post_request(data):
    url = "https://aproximacion-evidencia1.onrender.com/api/monitor_sonido"
    json_data = ujson.dumps(data)
    
    # Enviar la solicitud POST
    try:
        print("Enviando solicitud POST a la API con los datos:", data)
        response = urequests.post(url, data=json_data, headers={"Content-Type": "application/json"})

        print("Código de respuesta:", response.status_code)
        print("Respuesta del servidor:", response.text)
        response.close()
    except Exception as e:
        print("Error al enviar la solicitud:", e)

# ===============================================================================

# Pines del KY-040
pin_clk = Pin(16, Pin.OUT)  # Simular CLK como salida
pin_dt = Pin(17, Pin.OUT)   # Simular DT como salida
pin_sw = Pin(18, Pin.IN, Pin.PULL_UP)  # Botón, opcional

# Alarma (LED)
pin_alarma = Pin(25, Pin.OUT)

# Variables para el seguimiento de la rotación
contador = 0
umbral_rotacion = 20
last_clk = 1
num_activaciones = 0
alarma_duracion = 5  # Duración de la alarma en segundos

# Función para obtener la hora actual en formato timestamp
def obtener_timestamp():
    t = time.localtime()
    return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(t[0], t[1], t[2], t[3], t[4], t[5])

# Función para activar la alarma
def activar_alarma():
    global num_activaciones
    pin_alarma.value(1)  # Enciende el LED
    print("Alarma activada (LED encendido)")
    num_activaciones += 1
    
    time.sleep(alarma_duracion)  # Mantener el LED encendido durante X segundos
    pin_alarma.value(0)  # Apaga el LED
    print("Alarma desactivada (LED apagado)")

# Función para leer el encoder
def leer_encoder(timer):
    global contador, last_clk
    
    # Leer las señales simuladas
    current_clk = pin_clk.value()
    
    if current_clk != last_clk and current_clk == 0:
        direccion_rotacion = 1 if pin_dt.value() != current_clk else -1
        contador += direccion_rotacion
        
        print("Posición del encoder:", contador)
        
        if abs(contador) >= umbral_rotacion:
            activar_alarma()
            # Crear los datos para enviar al servidor
            datos = {
                "timestamp": obtener_timestamp(),
                "contador": contador,
                "alarma_activada": True,
                "direccion_rotacion": direccion_rotacion,
                "estado_boton": pin_sw.value(),
                "valor_umbral": umbral_rotacion,
                "num_activaciones": num_activaciones,
                "duracion_alarma": alarma_duracion
            }
            # Enviar los datos al servidor
            send_post_request(datos)
            # Después de activar la alarma, restablecer el contador
            contador = 0
    
    last_clk = current_clk

# Función para simular el encoder
def simular_encoder(timer):
    pin_clk.value(not pin_clk.value())  # Alternar CLK
    pin_dt.value(not pin_dt.value())    # Alternar DT

# Configurar temporizador para leer el encoder
timer = Timer(0)
timer.init(period=1, mode=Timer.PERIODIC, callback=leer_encoder)

# Configurar temporizador para simular el encoder
simulador = Timer(1)
simulador.init(period=100, mode=Timer.PERIODIC, callback=simular_encoder)  # Cambia la velocidad según necesidad

# Simulación continua (ejecutar indefinidamente)
while True:
    time.sleep(1)

# Primero llamo los módulos a trabajar:

from machine import Pin, PWM
import network
import urequests
import time
import json


# Objetos:

pir = Pin(15, Pin.IN, Pin.PULL_DOWN)
zumbador = PWM(Pin(2), freq = 440, duty = 0)

#Conectando a WIFI

print ("Conectando a la red", end="")

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')

while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.5)

print("\n")
print("Conectando exitosamente 👌")
print("\n")

# Defino Zumbador
def sonido(freq,sleep):

    zumbador.freq(freq)
    zumbador.duty(512)
    time.sleep(sleep)

# Apagar Zumbador:
def apagar_zumbador():
    zumbador.duty(0)

# Función para enviar datos a la API cuando hay detección
def enviar_datos_api():
    url = "https://aproximacion-evidencia1.onrender.com/api/sensor_movimiento"  # Cambia el endpoint según sea necesario
    data = {"mensaje": ["Movimiento detectado en el sensor"]}
    headers = {'Content-Type': 'application/json'}

    try:
        response = urequests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            print("Datos enviados correctamente:", response.json())
        else:
            print("Error al enviar los datos:", response.status_code, response.text)
        response.close()  # Cierra la conexión para liberar memoria
    except Exception as e:
        print("Error en la solicitud:", e)
        if 'response' in locals():  # Verifica si 'response' fue creada
            response.close()  # Cierra la conexión en caso de error


# Ciclo:

while True:
    estado = pir.value()
    print(estado)    
    time.sleep(1)

    if estado == 1:
        print("Hay alguien en el sensor ⚠️")
        
        frecuencias = [440, 900]
        for _ in range(3):
            for freq in frecuencias:
                sonido(freq, 0.5)
        apagar_zumbador()

        # Enviar mensaje a la API
        enviar_datos_api()
        time.sleep(5)  # Retardo después de enviar los datos

    elif estado == 0:
        print("Sin movimientos")
        apagar_zumbador()
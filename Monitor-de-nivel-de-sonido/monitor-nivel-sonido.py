from machine import Pin, Timer
import time

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

# Función para activar la alarma
def activar_alarma():
    pin_alarma.value(1)  # Enciende el LED
    print("Alarma activada (LED encendido)")
    
    time.sleep(5)  # Mantener el LED encendido durante 5 segundos
    pin_alarma.value(0)  # Apaga el LED
    print("Alarma desactivada (LED apagado)")

# Función para leer el encoder
def leer_encoder(timer):
    global contador, last_clk
    
    # Leer las señales simuladas
    current_clk = pin_clk.value()
    
    if current_clk != last_clk and current_clk == 0:
        if pin_dt.value() != current_clk:
            contador += 1
        else:
            contador -= 1
        
        print("Posición del encoder:", contador)
        
        if abs(contador) >= umbral_rotacion:
            activar_alarma()
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

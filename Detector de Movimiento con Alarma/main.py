# Primero llamo los módulos a trabajar:

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

ancho = 128
alto = 64

buzzer = Pin(13, Pin.OUT)
pir = Pin(23, Pin.IN, Pin.PULL_DOWN)
i2c = I2C(0, scl = Pin(22), sda = Pin(21))
oled = SSD1306_I2C(ancho, alto, i2c)


while True:
    if pir.value() == 1:
        print("Movimiento Detectado")
        
        for _ in range(5):  
            
            oled.text("INTRUSO", 35, 20)
            oled.text("DETECTADO !!!", 25, 30)
            oled.show()
            buzzer.value(1)
            time.sleep(0.75) 
            oled.fill(0)  
            oled.show()
            time.sleep(0.75)

        time.sleep(3)
    else:
        print("Sin Movimientos")

        oled.fill(0)
        oled.show()

        buzzer.value(0)
        time.sleep(1)
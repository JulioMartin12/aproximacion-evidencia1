from machine import Pin, ADC, I2C
from time import sleep
import ssd1306


# Configuración del sensor MQ135 (gases)
mq135_pin = ADC(Pin(34))  # MQ135 conectado a GPIO34 (pin analógico)
mq135_pin.atten(ADC.ATTN_11DB)  # Rango de 0 a 3.3V

alto= 64
ancho= 128

# Configuración de la pantalla OLED SSD1306
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Conexión I2C (SCL a GPIO22, SDA a GPIO21)
oled = ssd1306.SSD1306_I2C(ancho, alto, i2c)  # Tamaño 128x64 de la pantalla OLED
#oled = SSD1306_I2C(ancho, alto, i2c)
# Función para leer el sensor MQ135
def read_mq135():
    gas_value = mq135_pin.read()  # Leer el valor analógico (0 a 4095)
    # Conversión a PPM (ejemplo simple)
    gas_ppm = (gas_value / 4095) * 1200  # Aproximación a PPM (escala de 0 a 1000)
    return gas_ppm

# Función para mostrar los datos en la pantalla OLED
def display_data(gas_ppm, mensaje):
    oled.fill(0)  # Limpiar la pantalla
    oled.text("Calidad del Aire", 0, 0)
    oled.text("Gas: {:.2f} PPM".format(gas_ppm), 0, 20)
    oled.text(mensaje,0,40)
    oled.show()

# Bucle principal
while True:
    gas_ppm = read_mq135()  # Leer el valor del sensor MQ135

    mensaje = ""
    
    if gas_ppm <= 50:
        mensaje = "CO Admisible"
    elif gas_ppm > 50 and gas_ppm <= 200:
        mensaje = "CO Leve"
    elif gas_ppm > 200 and gas_ppm <= 400:        
        mensaje= "CO aceptable"
    elif gas_ppm > 400 and gas_ppm <= 800:
        mensaje= "CO Malo"
    elif gas_ppm >= 800:
        mensaje= "CO Peligroso"

    display_data(gas_ppm, mensaje)    # Mostrar los datos en la pantalla OLED
    print(gas_ppm, "PPM", mensaje)
    sleep(2)  # Esperar 2 segundos entre lecturas

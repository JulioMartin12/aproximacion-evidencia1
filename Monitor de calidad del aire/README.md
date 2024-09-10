# Monitor de Calidad del Aire con ESP32

## Introducción:

En el contexto actual de creciente preocupación por la contaminación del aire, medir la calidad del aire en tiempo real es una necesidad crítica. Este proyecto tiene como objetivo desarrollar un sistema de monitoreo de calidad del aire usando un sensor de gases (MQ135) conectado a una placa ESP32, mostrando las mediciones en una pantalla OLED SSD1306. El sistema monitorea la concentración de gases y permite obtener una indicación de la calidad del aire en ambientes cerrados. 

[Link al proyecto en Wokwi](https://wokwi.com/projects/408568500712542209)

## Objetivo Específico del Proyecto:

El objetivo principal de este proyecto es diseñar e implementar un monitor de calidad del aire que mida la concentración de gases nocivos en tiempo real, utilizando un sensor MQ135 y un display OLED para visualizar los resultados. Este monitor es ideal para su uso en interiores, donde la calidad del aire puede variar significativamente por la presencia de compuestos volátiles.

## Descripción del Hardware Utilizado:

### * ESP32:

El ESP32 es una potente plataforma de microcontroladores que incluye Wi-Fi y Bluetooth. Es compatible con MicroPython, lo que facilita el desarrollo rápido de prototipos. En este proyecto se encarga de leer los datos del sensor MQ135 y mostrarlos en la pantalla OLED.

### * Sensor MQ135:

El MQ135 es un sensor de gases diseñado para detectar una amplia gama de gases tóxicos, como dióxido de carbono (CO2), amoníaco (NH3), óxido de nitrógeno (NOx), y otros compuestos volátiles. El sensor entrega una salida analógica que puede ser interpretada por el ESP32 para estimar la concentración de gases en el aire.

### * Pantalla OLED SSD1306:

La pantalla OLED SSD1306 es una pantalla de 128x64 píxeles que usa el protocolo I2C para comunicarse con el ESP32. Este dispositivo se utiliza para mostrar las lecturas de gases en tiempo real.

## Conexiones:

Componente              ESP32

MQ135  ---------------> PIN 34 (entrada analógica)

SSD1306 SDA ------> PIN 21 (I2C SDA)

SSD1306 SCL-------> PIN 22 (I2C SCL)

## Explicación del Funcionamiento del Código y Lógica de Programación:

El código está escrito en MicroPython y está diseñado para leer datos del sensor MQ135 a intervalos regulares y mostrar los resultados en una pantalla OLED.
Nota: dado que el sensor MQ135 no está disponible en Woki se agregó en su reemplazo un potenciómetro para la simulación.

### Explicación del Código:

* Lectura del Sensor MQ135: El código utiliza un objeto ADC para leer los valores analógicos del sensor MQ135. Los valores leídos varían entre 0 y 4095, y se convierten en una aproximación de la concentración de gases en PPM (Partes por Millón) mediante una simple fórmula. 
* Pantalla OLED: Se utiliza la librería ssd1306 para manejar la pantalla OLED conectada al ESP32 mediante I2C. La función display_data() actualiza los valores en tiempo real, mostrando la concentración de gases en la pantalla.
* Bucle Principal: El bucle infinito lee los valores del sensor cada 2 segundos y actualiza la pantalla OLED con los nuevos datos. Analiza los PPM para evaluar los el nivel de riesgo de CO.

## Resultados Obtenidos, Pruebas Realizadas, y Posibles Mejoras Futuras:

### Resultados Obtenidos:

El sistema fue capaz de monitorear la concentración de gases de manera efectiva y mostrar las lecturas en tiempo real en la pantalla OLED. En la simulación con Wokwi, se generaron valores para el sensor MQ135 que fueron correctamente interpretados y visualizados.

### Pruebas Realizadas:

Las pruebas realizadas incluyeron la simulación en Wokwi para verificar que el sensor y el display OLED funcionaran correctamente. Se realizaron ajustes en el código para mejorar la visualización de los valores en la pantalla, asegurando que la actualización fuera fluida y sin retrasos perceptibles.

### Posibles Mejoras Futuras:

* Calibración Avanzada del Sensor: Aunque el valor en PPM es aproximado, se podría implementar una curva de calibración más precisa basada en los datos proporcionados por el fabricante del sensor MQ135.
* Agregar un sensor de temperatura DHT22 para evaluar posibles causas de causas de las variaciones en la lectura del MQ135
* Conexión a Internet: El ESP32 tiene capacidad Wi-Fi, por lo que se podría integrar la conectividad a la nube para registrar los valores de calidad del aire y permitir el acceso remoto a los datos.
* Notificaciones: Se podrían agregar alertas en caso de que los niveles de gases excedan ciertos umbrales.

## Conclusiones:

El proyecto de monitor de calidad del aire utilizando el ESP32 y el sensor MQ135 demostró ser una solución efectiva para medir y mostrar en tiempo real la concentración de gases en el aire. La simplicidad del hardware y la facilidad de uso de MicroPython permiten una implementación rápida, tanto para simulaciones como para aplicaciones reales. Las mejoras futuras podrían incluir la integración de características adicionales como agregar otros tipos de sensores y  conectividad a la nube y alertas en tiempo real para hacer el dispositivo más completo y funcional.

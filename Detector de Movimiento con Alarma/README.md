# Detector de movimiento con alarma:

* Descripción: Implementa un sistema de seguridad que detecta movimiento.

* Sensores: PIR (infrarrojo pasivo).
  
* Funcionalidad: Si se detecta movimiento, el ESP32 activa una alarma (zumbador) y envía una notificación por Wi-Fi.

## Informe Técnico:

La seguridad en el hogar o en espacios comerciales es una preocupación constante. Este proyecto presenta una solución práctica y accesible: un detector de movimiento con alarma integrado. Este sistema ofrece una primera línea de defensa, alertando al usuario de cualquier actividad sospechosa.

## Objetivos Especificos:

El objetivo específico de este proyecto es detectar movimiento generar una alerta con un zumbido y una notificación tanto en consola como en una pantalla oled.

## Hardware:

Para este proyecto utilizamos: un módulo esp32, un sensor Pir, un Buzzer y un display Oled.

## Esquema de Conexión:

![Esquema de conexión](https://firebasestorage.googleapis.com/v0/b/ciencia-de-datos-ispc.appspot.com/o/int%20prog%2Fdetector%20de%20mov.jpg?alt=media&token=d560f07f-295b-43d8-9cf3-0bb1b6185a16)

## Código fuente:

[Código Fuente Micropython](https://github.com/JulioMartin12/aproximacion-evidencia1/blob/main/Detector%20de%20Movimiento%20con%20Alarma/main.py)

## Explicación del código:


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

## Esquema de Conexión y Diagrama:

[Link al Diagrama en Wokwi](https://wokwi.com/projects/408580463353840641)

![Esquema de conexión](https://firebasestorage.googleapis.com/v0/b/ciencia-de-datos-ispc.appspot.com/o/int%20prog%2Fdetector%20de%20mov.jpg?alt=media&token=d560f07f-295b-43d8-9cf3-0bb1b6185a16)

## Código fuente:

[Código Fuente Micropython](https://github.com/JulioMartin12/aproximacion-evidencia1/blob/main/Detector%20de%20Movimiento%20con%20Alarma/main.py)

## Explicación del código:

Para comenzar, además de los archivos habituales (main.py y diagraman.json), debí agregar la librería ssd1306 para poder trabajar con el display oled.

![Agrego libreria](https://firebasestorage.googleapis.com/v0/b/ciencia-de-datos-ispc.appspot.com/o/int%20prog%2F01.jpg?alt=media&token=5b01ae5a-ae19-4495-93f0-2f7863163438)

Se continúa de la siguiente forma:

![Proceso en main.py](https://firebasestorage.googleapis.com/v0/b/ciencia-de-datos-ispc.appspot.com/o/int%20prog%2F02.jpg?alt=media&token=5190342d-3694-4fbf-8021-c6e49f93edec)

1-

* De la librería machine importo Pin para poder trabajar con el sensor de movimiento. De la misma galería importo IC2 para poder trabajar con el display oled.
* De la librería que importé al inicio, importo SS1306_I2C para poder programar a mayor profuncidad el display oled.
* Por último importo time para poder trabajar con tiempos en mi proyecto.

2- Defino los atributos ancho y alto del display oled.

3- Defino los componentes:

* Buzzer: indico que estará en el pin 13 y con formato de salida.
* Pir: estará en el pin 23 en formato de entrada.
* i2c: el display oled utilizará los pines 21 y 22.
* oled: defino que tamaño tendra el área de trabajo del display oled.

4- Inicio un ciclo while con un condicional donde el sensor Pir obtiene el valor 1 para verdadero. Si se obtiene 1 se imprime en consola el mensaje "Movimiento Detectado" y comienza el ciclo for anidado dentro.

5- Si se detecta movimiento se activa un siclo for que se repetiraá 5 veces, donde:

```python
oled.text("INTRUSO", 35, 20)
oled.text("DETECTADO !!!", 25, 30)
oled.show() 
```

Estas líneas indican el mensaje en el display. Las primeras dos indican el mensaje a mostrar y la posicion del string dentro del área de trabajo del display, mientras que la segunda indica que lo debe mostrar.

```python
buzzer.value(1)
```

Con esta línea le indicamos al Buzzer que debe sonar generndo una alarma en forma de zumbido.

```python
time.sleep(0.75) 
```
Luego esperamos un momento.

```python
oled.fill(0)  
oled.show() 
```
Y la primer línea borra el contenido del display y la segunda muestra el display borrado.
```python
time.sleep(0.75) 
```
Espera otro momento y vuelve a repetirse el ciclo 4 veces más, dando esa sensación de ALERTA.

6- Una vez que cumple el ciclo for, espera un momento
```python
time.sleep(3) 
```
y vuelve a ejecutar el else del condicional.

7-

```python
else:
        print("Sin Movimientos")

        oled.fill(0)
        oled.show()

        buzzer.value(0)
        time.sleep(1) 
```
Donde la primer línea de código imprime en consola el mensaje "Sin Movimientos", las dos siguientes mantienen al display oled vacío. Luego la penúltima línea mantiene sileciado el buzzer y la última espera un momento para volver a comenzar el ciclo.

## Pruebas Realizadas:

Dejo las pruebas en el siguiente link:

[Pruebas relizadas](https://firebasestorage.googleapis.com/v0/b/ciencia-de-datos-ispc.appspot.com/o/int%20prog%2Fprueba%20detector%20de%20movimiento.mp4?alt=media&token=d871fef8-e919-4de8-92d1-472b3e90dd81)

Una mejora que intente realizar y no llegué por falta de tiempo era que cuando se detecte movimiento, envíe un mensaje a un número de Whatsapp determinado. Estuve investigando que se puede hacer con CallMeBoot pero no llegue a concretarlo.

## Conclusión:

Este proyecto ha demostrado la viabilidad de utilizar componentes electrónicos de bajo costo para crear soluciones de seguridad sencillas y efectivas. El detector de movimiento puede ser una herramienta útil para proteger hogares o negocios. Además de su función principal, este proyecto puede servir como base para desarrollar sistemas de seguridad más sofisticados, incorporando cámaras, reconocimiento facial y otras tecnologías. Pude aplicar en este proyecto no solo los conocimiento adquiridos en la materia sino que también en otras materias como programación.
Me parecio una mus buena experiencia.

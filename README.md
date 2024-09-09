# aproximacion-evidencia1
Proyecto Prototipos IoT con ESP32
<h1>Rutas de cada uno de los circuitos propuestos</h1>
<h2>Monitor de nivel de sonido</h2>
<p>
<ul>
<li>Descripción: Monitorea el nivel de ruido en una habitación.</li>
<li> Sensores: Sensor de sonido (micrófono electret con amplificador).</li>
<li>Funcionalidad: Mide el nivel de sonido y, si supera un umbral, envía una
alerta por Wi-Fi o activa una alarma.</li>
</ul>
</p>
<a href="https://wokwi.com/projects/408565990076104705"> Monitor de nivel de sonido </a>

<h2>Introducción</h2>
<p>
El monitoreo de los niveles de sonido es esencial en diversos entornos para mantener condiciones óptimas. Desde ambientes de trabajo hasta habitaciones residenciales, un sistema de monitoreo de sonido puede ayudar a gestionar y controlar el nivel de ruido para asegurar un ambiente adecuado.

Este proyecto de Monitor de Nivel de Sonido está diseñado para evaluar los niveles de ruido en una habitación utilizando tecnología basada en un microcontrolador. Equipado con un sensor de sonido (micrófono electret con amplificador), el sistema mide el sonido ambiente en tiempo real. Cuando el nivel de sonido detectado supera un umbral predefinido, el dispositivo activa una alarma física, representada por un LED.
</p>
 <h2>Objetivo del Proyecto</h2>
    <p>El objetivo principal de este proyecto es desarrollar un sistema de <strong>monitoreo de nivel de sonido</strong> que permita detectar y gestionar niveles de ruido en un entorno específico de manera eficiente. El sistema utilizará un sensor de sonido para medir el nivel de ruido y, en caso de que este supere un umbral predefinido, activará una alarma visual mediante un LED.</p>
    <p>Más específicamente, los objetivos son:</p>
    <ul>
        <li><strong>Medir el Nivel de Sonido:</strong> Utilizar un micrófono electret con amplificador para capturar el nivel de sonido en tiempo real y convertirlo en una señal eléctrica que pueda ser procesada por el microcontrolador.</li>
        <li><strong>Detectar Excesos de Ruido:</strong> Establecer un umbral de sonido que permita identificar cuando el nivel de ruido supera el límite deseado.</li>
        <li><strong>Activar una Alarma Visual:</strong> Implementar una señal de alarma en forma de LED que se encienda cuando el nivel de sonido supere el umbral, proporcionando una indicación visual inmediata de un exceso de ruido.</li>
        <li><strong>Proveer Retroalimentación Inmediata:</strong> Ofrecer una solución efectiva y rápida para alertar a los usuarios sobre niveles de ruido excesivos sin depender de conectividad externa, como Wi-Fi.</li>
    </ul>
    <p>Este proyecto tiene como meta crear un sistema funcional que permita gestionar y controlar los niveles de sonido en entornos donde se requiera una monitorización constante y una respuesta rápida a cambios en el nivel de ruido.</p>
 <h2>Descripción del Hardware Utilizado</h2>
    <p>Para el proyecto de monitoreo de nivel de sonido se utilizan los siguientes componentes de hardware:</p>
    <ul>
        <li><strong>ESP32:</strong> Es un microcontrolador de bajo costo con capacidades Wi-Fi y Bluetooth integradas. Se utiliza para procesar las señales del sensor de sonido y controlar la alarma visual. Es conocido por su alto rendimiento y flexibilidad en aplicaciones IoT.</li>
        <li><strong>Sensor de Sonido (Micrófono Electret con Amplificador):</strong> Este sensor mide el nivel de ruido en el ambiente. El micrófono electret convierte las ondas sonoras en señales eléctricas, mientras que el amplificador integrado amplifica estas señales para que el microcontrolador pueda procesarlas.</li>
        <li><strong>LED:</strong> Se utiliza como indicador visual para la alarma. El LED se enciende cuando el nivel de sonido supera el umbral predefinido, proporcionando una señal visual inmediata de que el nivel de ruido es alto.</li>
        <li><strong>Resistencias:</strong> Se emplean para limitar la corriente que pasa a través del LED y ajustar los niveles de señal en el circuito. Son componentes pasivos que ayudan a proteger y optimizar el funcionamiento de otros componentes en el circuito.</li>
    </ul>
     <h2>Explicación del Funcionamiento del Código y la Lógica de Programación</h2>
    <p>El código para el proyecto de monitoreo de nivel de sonido con el ESP32 y el sensor de sonido se basa en el siguiente flujo de funcionamiento:</p>
    <h2>1. Inicialización del Hardware</h2>
    <p>Al iniciar el programa, se configuran los pines del ESP32 para el sensor de sonido y el LED de alarma:</p>
    <ul>
        <li><strong>Pin del Sensor de Sonido (KY-040):</strong> El pin CLK (Clock) y el pin DT (Data) se configuran como entradas para leer las señales del sensor.</li>
        <li><strong>Pin del LED:</strong> El pin del LED se configura como salida para encender o apagar el LED en función del nivel de sonido.</li>
    </ul>
    <h2>2. Configuración del Temporizador</h2>
    <p>Se configura un temporizador que ejecuta la función <code>leer_encoder</code> periódicamente. Esta función se encarga de:</p>
    <ul>
        <li>Leer el valor actual del pin CLK del sensor de sonido.</li>
        <li>Comparar el valor actual con el valor anterior para detectar cambios.</li>
        <li>Actualizar el contador en función del sentido de rotación del encoder.</li>
        <li>Activar la alarma (encender el LED) si el contador supera un umbral predefinido.</li>
    </ul>
    <h2>3. Lectura del Encoder</h2>
    <p>La función <code>leer_encoder</code> realiza las siguientes acciones:</p>
    <ul>
        <li>Lee el valor del pin CLK y compara con el valor anterior para detectar cambios.</li>
        <li>Lee el valor del pin DT para determinar la dirección de la rotación del encoder.</li>
        <li>Actualiza el contador según la dirección de la rotación.</li>
        <li>Si el contador supera el umbral definido (por ejemplo, 20 rotaciones), activa la alarma (enciende el LED).</li>
        <li>Reinicia el contador después de activar la alarma para evitar que la alarma se active repetidamente por la misma rotación.</li>
    </ul>
    <h2>4. Activación de la Alarma</h2>
    <p>Cuando el contador supera el umbral, se llama a la función <code>activar_alarma</code> que:</p>
    <ul>
        <li>Enciende el LED para indicar que se ha superado el umbral.</li>
        <li>Espera 5 segundos con el LED encendido.</li>
        <li>Apaga el LED después de 5 segundos.</li>
    </ul>
    <h2>5. Bucle Principal</h2>
    <p>El bucle principal del programa se mantiene en un estado de espera, permitiendo que el temporizador ejecute la función de lectura del encoder periódicamente.</p>
     <h2>Resultados Obtenidos, Pruebas Realizadas y Posibles Mejoras Futuras</h2>
    <h2>Resultados Obtenidos</h2>
    <p>Después de implementar y ejecutar el proyecto, se obtuvieron los siguientes resultados:</p>
    <ul>
        <li>El sistema correctamente detecta cambios en el nivel de sonido a través del sensor de sonido KY-040.</li>
        <li>El contador se actualiza de acuerdo con la dirección de la rotación del encoder.</li>
        <li>Cuando el contador supera el umbral predefinido, el LED se enciende durante el tiempo especificado.</li>
        <li>El sistema responde adecuadamente a las rotaciones, activando y desactivando la alarma según sea necesario.</li>
    </ul>
    <h2>Pruebas Realizadas</h2>
    <p>Se llevaron a cabo las siguientes pruebas para verificar el funcionamiento del sistema:</p>
    <ul>
        <li><strong>Prueba de Detección de Sonido:</strong> Se probó el sistema con diferentes niveles de sonido para asegurar que el umbral se detectara correctamente.</li>
        <li><strong>Prueba de Rotación del Encoder:</strong> Se verificó que el sistema contara las rotaciones en ambas direcciones y que la alarma se activara correctamente al superar el umbral.</li>
        <li><strong>Prueba de Activación de la Alarma:</strong> Se comprobó que el LED se encendiera durante el tiempo especificado y se apagara después.</li>
        <li><strong>Prueba de Respuesta del Temporizador:</strong> Se confirmó que el temporizador llamara a la función de lectura del encoder a intervalos regulares.</li>
    </ul>
    <h2>Posibles Mejoras Futuras</h2>
    <p>Para mejorar el sistema, se pueden considerar las siguientes mejoras:</p>
    <ul>
        <li><strong>Ajuste de Umbral Dinámico:</strong> Implementar un ajuste dinámico del umbral basado en las condiciones ambientales para una detección más precisa.</li>
        <li><strong>Implementación de Funcionalidad de Wi-Fi:</strong> Integrar la capacidad de enviar alertas a través de Wi-Fi para una mayor versatilidad en el monitoreo remoto.</li>
        <li><strong>Optimización del Código:</strong> Mejorar la eficiencia del código y la gestión de recursos para una respuesta más rápida y una menor carga de procesamiento.</li>
        <li><strong>Interfaz de Usuario:</strong> Desarrollar una interfaz de usuario para ajustar parámetros como el umbral de sonido y visualizar el estado del sistema en tiempo real.</li>
        <li><strong>Escalabilidad:</strong> Considerar la posibilidad de agregar más sensores y alarmas para monitorear múltiples ubicaciones o condiciones simultáneamente.</li>
    </ul>
 <h2>Conclusiones del Proyecto</h2>
    <p>El proyecto de monitoreo de nivel de sonido ha sido exitoso en términos de funcionalidad y objetivos alcanzados. A continuación, se presentan las conclusiones principales:</p>
    <ul>
        <li><strong>Detección Efectiva:</strong> El sistema demuestra ser efectivo en la detección de niveles de sonido que superan el umbral predefinido. El sensor de sonido proporciona mediciones precisas que permiten la activación de la alarma de manera confiable.</li>
        <li><strong>Funcionamiento del Encoder:</strong> El encoder KY-040 funciona correctamente para contar las rotaciones en ambas direcciones. Esto permite un monitoreo preciso de la rotación, que se traduce en la activación adecuada de la alarma cuando se supera el umbral.</li>
        <li><strong>Desempeño del LED:</strong> La alarma LED se activa y desactiva como se esperaba, proporcionando una señal visual clara cuando el nivel de sonido supera el umbral. La implementación de la alarma LED ayuda a la notificación inmediata de eventos importantes.</li>
        <li><strong>Pruebas y Validación:</strong> Las pruebas realizadas confirmaron que el sistema responde bien a las condiciones de prueba. Se observaron resultados consistentes durante las pruebas de detección de sonido, rotación del encoder y activación de la alarma.</li>
        <li><strong>Áreas de Mejora:</strong> A pesar del éxito del proyecto, se identificaron áreas para mejorar. La integración de funcionalidades de Wi-Fi para alertas remotas, la optimización del código y el ajuste dinámico del umbral son algunas de las mejoras que se podrían considerar en futuras iteraciones del proyecto.</li>
        <li><strong>Impacto y Aplicaciones:</strong> Este sistema puede ser útil en diversas aplicaciones, como en entornos industriales o domésticos, para monitorear y reaccionar ante niveles de sonido excesivos. Su capacidad para proporcionar una señal de alarma visual hace que sea una herramienta efectiva para la gestión del ruido.</li>
    </ul>

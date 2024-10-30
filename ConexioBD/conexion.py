from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Carga las variables de entorno
load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos MySQL
db_config = {
    'host': os.getenv("HOST"),
    'user': os.getenv("USER"),  # Cambié a USERNAME según tu .env
    'password': os.getenv("PASSWORD"),
    'database': os.getenv("DB")
}

# Verificación de la configuración
print(f"Host: {db_config['host']}")
print(f"User: {db_config['user']}")
print(f"Database: {db_config['database']}")

# Función para conectarse a MySQL
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Ruta para la raíz
@app.route('/')
def home():
    return "<p>Bienvenido a la API de Gases</p>"

# Ruta para recibir datos en la tabla gases
@app.route('/api/gases/data', methods=['POST'])
def receive_data():
    if request.is_json:
        data = request.get_json()
        try:
            connection = connect_to_db()
            if connection is None:
                return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

            cursor = connection.cursor()
            sql = "INSERT INTO gases (escala_ppm) VALUES (%s)"
            values = (data['medicion'],)
            cursor.execute(sql, values)
            connection.commit()

            return jsonify({"message": "Datos insertados correctamente"}), 200

        except Error as e:
            return jsonify({"error": str(e)}), 500

        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
    else:
        return jsonify({"error": "El formato de los datos no es JSON"}), 400

# Ruta para obtener datos de la tabla monitor_sonido


# Ruta para guardar datos en monitor_sonido
@app.route('/api/monitor_sonido', methods=['POST'])
def save_monitor_sonido():
    if request.is_json:
        data = request.get_json()
        required_fields = ['timestamp', 'contador', 'alarma_activada', 'direccion_rotacion', 'estado_boton', 'valor_umbral', 'num_activaciones', 'duracion_alarma']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Faltan campos requeridos"}), 400

        connection = connect_to_db()
        if connection is None:
            return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

        try:
            cursor = connection.cursor()
            sql = """INSERT INTO monitor_sonido (timestamp, contador, alarma_activada, direccion_rotacion, estado_boton, valor_umbral, num_activaciones, duracion_alarma) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (data['timestamp'], data['contador'], data['alarma_activada'], data['direccion_rotacion'], data['estado_boton'], data['valor_umbral'], data['num_activaciones'], data['duracion_alarma'])
            
            cursor.execute(sql, values)
            connection.commit()

            return jsonify({"message": "Datos guardados correctamente"}), 201

        except Error as e:
            return jsonify({"error": str(e)}), 500

        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
    else:
        return jsonify({"error": "El formato de los datos no es JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)


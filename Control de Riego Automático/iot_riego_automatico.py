from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import os


app = Flask(__name__)

# Configuración de la base de datos MySQL
db_config = {
    'host': 'climatic.com.ar',
    'user': 'u588746708_alan',
    'password': 'Barcito2024',
    'database': 'u588746708_alan',  
}

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
    return "<p>Bienvenido a la API de Riego Automático</p>"

# Ruta para recibir datos de humedad
@app.route('/api/riego/data', methods=['POST'])
def receive_data_riego():
    if request.is_json:
        data = request.get_json()

        # Insertar los datos recibidos en la tabla MySQL
        try:
            connection = connect_to_db()
            if connection is None:
                return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

            cursor = connection.cursor()

            # Supongamos que 'data' tiene un campo 'humedad'
            sql = "INSERT INTO humedad (nivel_humedad) VALUES (%s)"  
            values = (data['humedad'],)  

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

# Ruta para el reporte
@app.route('/reporte')
def reporte():
    return "<p>Reporte de Humedad</p>"

@app.route('/saluda')
def hello_world():
    return "<p>Hola, bienvenido al sistema de riego automático</p>"

if __name__ == '__main__':
    app.run(debug=True)

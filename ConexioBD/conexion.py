from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import os
# ----
app = Flask(__name__)

# Configuración de la base de datos MySQL
db_config = {
    'host': os.getenv("HOST"),
    'user': os.getenv("USER"),
    'password': os.getenv("PASSWORD"),
    'database': os.getenv("DB")
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
    return "<p>Bienvenido a la API de Gases</p>"


# MARCELO
# ----------
@app.route('/api/gases/data', methods=['POST'])
def receive_data():
    if request.is_json:
        data = request.get_json()

        # Ejemplo: Insertar los datos recibidos en una tabla MySQL
        try:
            connection = connect_to_db()
            if connection is None:
                return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

            cursor = connection.cursor()

            # Supongamos que 'data' tiene un campo 'name' y 'value'
            sql = "INSERT INTO  gases (escala_ppm) VALUES (%s)"
            values = (data['medicion'])

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
# ----------


@app.route('/saluda')
def hello_world():
    return "<p>Hola perros</p>"


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import os
# ----
app = Flask(__name__)

# Configuración de la base de datos MySQL
db_config = {
    'host': os.getenv("HOST"),
    'user': os.getenv("USERNAME"),
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


@app.route('/saluda')
def hello_world():
    return "<p>Hola perros</p>"


if __name__ == '__main__':
    app.run(debug=True)

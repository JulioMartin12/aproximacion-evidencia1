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

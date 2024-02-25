from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

users = {}

@app.route("/registro", methods=["POST"])
def registro():
    try:
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        if username in users:
            return jsonify({"error": "El usuario ya existe"}), 400

        users[username] = password

        return jsonify({"message": "Usuario registrado correctamente"}), 201
    except Exception as e:
        # Manejar cualquier excepción inesperada
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        if username not in users:
            return jsonify({"error": "El usuario no existe"}), 401

        if users[username] != password:
            return jsonify({"error": "La contraseña no es válida"}), 401

        return jsonify({"message": "Autenticación satisfactoria"}), 200
    except HTTPException as e:
       # Manejar excepciones HTTP específicas (por ejemplo, 400, 401)
        return e
    except Exception as e:
       # Manejar cualquier excepción inesperada
        return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == "__main__":
    app.run(debug=True)

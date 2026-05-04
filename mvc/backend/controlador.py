from flask import Flask, jsonify, request
from flask_cors import CORS
import modelo

app = Flask(__name__)
CORS(app)  


@app.route("/tareas", methods=["GET"])
def get_tareas():
    tareas = modelo.get_all_tareas()
    return jsonify(tareas)


@app.route("/tareas", methods=["POST"])
def create_tarea():
    data = request.get_json()
    modelo.create_tarea(data["titulo"])
    return jsonify({"mensaje": "Tarea creada"}), 201


@app.route("/tareas/<int:id>", methods=["DELETE"])
def delete_tarea(id):
    modelo.delete_tarea(id)
    return jsonify({"mensaje": "Tarea eliminada"})


@app.route("/tareas/<int:id>/toggle", methods=["PATCH"])
def toggle_tarea(id):
    modelo.toggle_tarea(id)
    return jsonify({"mensaje": "Tarea actualizada"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
from flask import Flask, jsonify
from db import ejecutar_consulta, ejecutar_cambio

app = Flask(__name__)

@app.route('/usuarios')
def listar_usuarios():
    query = "SELECT id, nombre FROM usuarios WHERE activo = %s"
    usuarios = ejecutar_consulta(query, (1,))
    return jsonify(usuarios)

@app.route('/actualizar-email', methods=['POST'])
def actualizar():
    query = "UPDATE usuarios SET email = %s WHERE id = %s"
    filas = ejecutar_cambio(query, ("nuevo@email.com", 5))
    return f"Registros actualizados: {filas}"
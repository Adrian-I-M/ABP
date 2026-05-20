from flask import Blueprint, jsonify, request
from services.perro_service import PerroService

perro_bp = Blueprint('perro_bp', __name__)

@perro_bp.route("/perros", methods=["GET"])
def list_perros():  
    try:
        perros = PerroService.list_perros()
        return jsonify(perros), 200
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

@perro_bp.route("/perros/<int:perro_id>", methods=["GET"])
def get_perro(perro_id):  
    try:
        perro = PerroService.get_perro_by_id(perro_id)  
        if perro is None:
            return jsonify({"error": "Perro no encontrado"}), 404  
        return jsonify(perro), 200  
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

@perro_bp.route("/perros", methods=["POST"])
def create_perro():
    try:
        data = request.get_json() 
        nombre = data.get("nombre")
        raza = data.get("raza")
        edad = data.get("edad")
        id_usuario = data.get("id_usuario")
        
        new_id = PerroService.create_perro(nombre, raza, edad, id_usuario)
        return jsonify({"mensaje": "Perro añadido", "id": new_id}), 201
        
    except ValueError as val_error:
        return jsonify({"error": str(val_error)}), 400
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500
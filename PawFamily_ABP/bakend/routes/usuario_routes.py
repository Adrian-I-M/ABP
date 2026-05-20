from flask import Blueprint, jsonify, request
from services.usuario_service import UsuarioService

# Usamos Blueprint para poder separar las rutas en archivos individuales
usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route("/usuarios", methods=["GET"])
def list_users():
    try:
        usuarios = UsuarioService.list_users()
        return jsonify(usuarios), 200
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

@usuario_bp.route("/usuarios/<int:user_id>", methods=["GET"])
def get_user(user_id):
    try:
        usuario = UsuarioService.get_user_by_id(user_id)
        if usuario is None:
            return jsonify({"error": "Usuario no encontrado"}), 404
        return jsonify(usuario), 200
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

@usuario_bp.route("/usuarios", methods=["POST"])
def create_user():
    try:
        # Nota: Para APIs REST reales, es mejor leer JSON en lugar de formularios web:
        data = request.get_json() 
        nombre = data.get("nombre")
        email = data.get("email")
        
        new_id = UsuarioService.create_user(nombre, email)
        return jsonify({"mensaje": "Usuario creado", "id": new_id}), 201
        
    except ValueError as val_error:
        return jsonify({"error": str(val_error)}), 400
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500
from flask import Blueprint, jsonify, request
from services.cita_service import CitaService

cita_bp = Blueprint('cita_bp', __name__)

# Registrar una nueva cita (POST)
@cita_bp.route("/citas", methods=["POST"])
def crear_cita():
    try:
        data = request.get_json()
        id_usuario = data.get("id_usuario")
        id_perro = data.get("id_perro")
        fecha_cita = data.get("fecha_cita")
        hora_cita = data.get("hora_cita")
        motivo = data.get("motivo", "")
        
        new_id = CitaService.crear_cita(id_usuario, id_perro, fecha_cita, hora_cita, motivo)
        return jsonify({"ok": True, "mensaje": "¡Cita agendada con éxito!", "id": new_id}), 201
        
    except ValueError as val_error:
        return jsonify({"ok": False, "error": str(val_error)}), 400
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

# Obtener todas las citas con los nombres de usuario y perro (GET)
@cita_bp.route("/citas", methods=["GET"])
def listar_citas():
    try:
        citas = CitaService.listar_citas()
        return jsonify(citas), 200
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500
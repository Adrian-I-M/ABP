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

        new_id = CitaService.crear_cita(id_usuario, id_perro, fecha_cita, hora_cita)

        return jsonify({"ok": True, "mensaje": "Cita agendada con éxito", "id": new_id}), 201

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
    
# Modificar una cita existente por su ID (PUT)
@cita_bp.route("/citas/<int:cita_id>", methods=["PUT"])
def modificar_cita(cita_id):
    try:
        data = request.get_json()
        id_usuario = data.get("id_usuario")
        id_perro = data.get("id_perro")
        fecha_cita = data.get("fecha_cita")
        hora_cita = data.get("hora_cita")
        
        success = CitaService.actualizar_cita(cita_id, id_usuario, id_perro, fecha_cita, hora_cita)
        
        if not success:
            return jsonify({"ok": False, "error": "Cita no encontrada o sin cambios"}), 404
            
        return jsonify({"ok": True, "mensaje": "¡Cita actualizada con éxito!"}), 200
        
    except ValueError as val_error:
        return jsonify({"ok": False, "error": str(val_error)}), 400
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

# Cancelar/Eliminar una cita por su ID (DELETE)
@cita_bp.route("/citas/<int:cita_id>", methods=["DELETE"])
def eliminar_cita(cita_id):
    try:
        success = CitaService.eliminar_cita(cita_id)
        if not success:
            return jsonify({"ok": False, "error": "Cita no encontrada"}), 404
            
        return jsonify({"ok": True, "mensaje": "Cita eliminada correctamente"}), 200
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500
from flask import Blueprint, jsonify, request
from services.perro_service import PerroService

perro_bp = Blueprint('perro_bp', __name__)

# GET TODOS
@perro_bp.route("/perros", methods=["GET"])
def list_perros():
    try:
        perros = PerroService.list_perros()
        return jsonify(perros), 200
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

# GET UNO
@perro_bp.route("/perros/<int:perro_id>", methods=["GET"])
def get_perro(perro_id):
    try:
        perro = PerroService.get_perro_by_id(perro_id)
        if perro is None:
            return jsonify({"error": "Perro no encontrado"}), 404
        return jsonify(perro), 200
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

# POST — acepta JSON (URL de imagen) o multipart (fichero)
@perro_bp.route("/perros", methods=["POST"])
def create_perro():
    try:
        if request.is_json:
            data = request.get_json()
            new_id = PerroService.create_perro_url(
                data.get("nombre"),
                data.get("raza"),
                data.get("edad"),
                data.get("descripcion"),
                data.get("estado"),
                data.get("genero"),
                data.get("imagen")
            )
        else:
            from flask import current_app
            new_id = PerroService.create_perro(
                request.form.get("nombre"),
                request.form.get("chip"),
                request.form.get("edad"),
                request.form.get("descripcion"),
                request.form.get("raza"),
                request.form.get("estado"),
                request.form.get("historial_medico"),
                request.form.get("fecha_entrada"),
                request.files.get("imagen"),
                current_app.config['UPLOAD_FOLDER'],
                request.form.get("genero")
            )
        return jsonify({"ok": True, "mensaje": "Perro añadido con éxito", "id": new_id}), 201
    except ValueError as val_error:
        return jsonify({"error": str(val_error)}), 400
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

# DELETE
@perro_bp.route("/perros/<int:perro_id>", methods=["DELETE"])
def delete_perro(perro_id):
    try:
        success = PerroService.delete_perro(perro_id)
        if not success:
            return jsonify({"error": "Perro no encontrado"}), 404
        return jsonify({"ok": True, "mensaje": "Perro eliminado"}), 200
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

# PUT
@perro_bp.route("/perros/<int:perro_id>", methods=["PUT"])
def update_perro(perro_id):
    try:
        data = request.get_json()
        success = PerroService.update_perro(
            perro_id,
            data.get("nombre"),
            data.get("chip"),
            data.get("edad"),
            data.get("descripcion"),
            data.get("raza"),
            data.get("estado"),
            data.get("historial_medico"),
            data.get("genero")
        )
        if not success:
            return jsonify({"error": "Perro no encontrado o sin cambios"}), 404
        return jsonify({"ok": True, "mensaje": "Perro actualizado con éxito"}), 200
    except ValueError as val_error:
        return jsonify({"error": str(val_error)}), 400
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

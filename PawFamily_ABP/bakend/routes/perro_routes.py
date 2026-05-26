from flask import Blueprint, jsonify, request
from services.perro_service import PerroService

perro_bp = Blueprint('perro_bp', __name__)

# Obtener todos los perros
@perro_bp.route("/perros", methods=["GET"])
def list_perros():  
    try:
        perros = PerroService.list_perros()
        return jsonify(perros), 200
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

# Obtener un perro específico por su ID
@perro_bp.route("/perros/<int:perro_id>", methods=["GET"])
def get_perro(perro_id):  
    try:
        perro = PerroService.get_perro_by_id(perro_id)  
        if perro is None:
            return jsonify({"error": "Perro no encontrado"}), 404  # 404: No encontrado en MySQL
        return jsonify(perro), 200  
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

# Añadir un nuevo perro
@perro_bp.route("/perros", methods=["POST"])
def create_perro():
    try:
        # Nota: Al subir archivos usamos request.form en lugar de request.get_json()
        nombre = request.form.get("nombre")
        raza = request.form.get("raza")
        edad = request.form.get("edad")
        id_usuario = request.form.get("id_usuario")
        
        # Capturamos el archivo binario de la imagen
        archivo_imagen = request.files.get("imagen")
        
        # Recuperamos la ruta de la carpeta que configuramos en app.py
        from flask import current_app
        carpeta_destino = current_app.config['UPLOAD_FOLDER']
        
        # Enviamos todo al servicio
        new_id = PerroService.create_perro(nombre, raza, edad, id_usuario, archivo_imagen, carpeta_destino)
        
        return jsonify({"mensaje": "Perro añadido con éxito", "id": new_id}), 201
        
    except ValueError as val_error:
        return jsonify({"error": str(val_error)}), 400
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

# Eliminar un perro por su ID 
@perro_bp.route("/perros/<int:perro_id>", methods=["DELETE"])
def delete_perro(perro_id):
    try:
        success = PerroService.delete_perro(perro_id)
        if not success:
            return jsonify({"error": "Perro no encontrado"}), 404  # 404: El ID no existía en la base de datos
        return jsonify({"mensaje": "Perro eliminado"}), 200
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500  # 500: Error interno del servidor
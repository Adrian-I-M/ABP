from flask import Blueprint, jsonify, request
from services.usuario_service import UsuarioService

usuario_bp = Blueprint('usuario_bp', __name__)

# Obtener todos los usuarios
@usuario_bp.route("/usuarios", methods=["GET"])
def list_users():
    try:
        usuarios = UsuarioService.list_users()
        return jsonify(usuarios), 200
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

# Obtener un usuario específico por su ID
@usuario_bp.route("/usuarios/<int:user_id>", methods=["GET"])
def get_user(user_id):
    try:
        usuario = UsuarioService.get_user_by_id(user_id)
        if usuario is None:
            return jsonify({"error": "Usuario no encontrado"}), 404
        return jsonify(usuario), 200
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

# Crear un nuevo usuario (Registro)
@usuario_bp.route("/usuarios", methods=["POST"])
def create_user():
    try:
        data = request.get_json() 
        nombre = data.get("nombre")
        correo = data.get("correo") or data.get("email") 
        contrasena = data.get("contrasena") or data.get("password")
        
        # ELIMINADO data.get("rol"). Ahora lo fijamos nosotros a piñón fijo por seguridad:
        rol = "cliente"   
        
        # Le seguimos pasando las 4 cosas al servicio, pero el rol lo controlas tú
        new_id = UsuarioService.create_user(nombre, correo, contrasena, rol)
        return jsonify({"mensaje": "Usuario creado", "id": new_id}), 201
        
    except ValueError as val_error:
        return jsonify({"error": str(val_error)}), 400  
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500

# Inicio de sesión de usuario (Login)
@usuario_bp.route("/login", methods=["POST"])
def api_login():
    try:
        data = request.get_json()
        login_input = data.get("correo", "")        # CORREGIDO: de 'login' a 'correo'
        password_input = data.get("contrasena", "") # CORREGIDO: de 'password' a 'contrasena'
        
        print(f"Petición de login Usuario: {login_input}")
        
        # El controlador no valida datos, delega la autenticación al servicio
        usuario_autenticado = UsuarioService.login_user(login_input, password_input)
        
        return jsonify({
            "ok": True, 
            "mensaje": "¡Login correcto!", 
            "usuario": usuario_autenticado
        }), 200
        
    except ValueError as error:
        return jsonify({"ok": False, "error": str(error)}), 400       # 400: Formato de email inválido
    except PermissionError as error:
        return jsonify({"ok": False, "error": str(error)}), 401    # 401: Credenciales incorrectas
    except Exception as error:
        return jsonify({"ok": False, "error": str(error)}), 500       # 500: Error interno del servidor
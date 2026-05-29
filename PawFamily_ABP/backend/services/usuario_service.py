import re
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:

    # VALIDACION EMAIL
    @staticmethod
    def validar_formato_email(correo):
        if not correo:
            raise ValueError("El correo electrónico es obligatorio.")
        patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron_email, correo.strip()):
            raise ValueError("El formato del correo electrónico no es válido.")

    # CRUD USUARIOS
    @staticmethod
    def list_users():
        return UsuarioRepository.get_all()

    @staticmethod
    def get_user_by_id(user_id):
        return UsuarioRepository.get_by_id(user_id)

    @staticmethod
    def create_user(nombre, correo, contrasena, rol="cliente"):
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        if not contrasena:
            raise ValueError("La contraseña es obligatoria.")
        UsuarioService.validar_formato_email(correo)
        return UsuarioRepository.create(nombre, correo, contrasena, rol)

    # LOGIN
    @staticmethod
    def login_user(correo, contrasena):
        UsuarioService.validar_formato_email(correo)
        usuario = UsuarioRepository.get_by_email(correo.strip())
        if not usuario:
            raise PermissionError("El usuario o la contraseña no coinciden.")
        if isinstance(usuario, dict):
            password_bd = usuario.get("contrasena")
            user_id = usuario.get("id")
            user_name = usuario.get("nombre")
            user_email = usuario.get("correo")
            user_rol = usuario.get("rol")
        else:
            password_bd = usuario[2]
            user_id = usuario[0]
            user_name = usuario[1]
            user_email = usuario[4]
            user_rol = usuario[3]

        if password_bd == contrasena:
            return {
                "id": user_id,
                "nombre": user_name,
                "email": user_email,
                "rol": user_rol
            }
        else:
            raise PermissionError("El usuario o la contraseña no coinciden.")

    # ACTUALIZAR Y ELIMINAR
    @staticmethod
    def update_user(user_id, nombre, correo, contrasena):
        if not nombre or not contrasena:
            raise ValueError("El nombre y la contraseña son obligatorios.")
        UsuarioService.validar_formato_email(correo)
        return UsuarioRepository.update(user_id, nombre, correo.strip(), contrasena)

    @staticmethod
    def delete_user(user_id):
        return UsuarioRepository.delete(user_id)

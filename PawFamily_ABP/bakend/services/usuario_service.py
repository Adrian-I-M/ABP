import re  
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:

    @staticmethod
    def validar_formato_email(email):
        #Valida que el email no esté vacío y cumpla con la estructura correcta
        if not email:
            raise ValueError("El correo electrónico es obligatorio.")
        
        patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron_email, email.strip()):
            raise ValueError("El formato del correo electrónico no es válido.")

    @staticmethod
    def list_users():# Obtener la lista de usuarios desde el repositorio
        return UsuarioRepository.get_all()

    @staticmethod # Obtener un usuario por su ID desde el repositorio
    def get_user_by_id(user_id):
        return UsuarioRepository.get_by_id(user_id)

    @staticmethod
    def create_user(nombre, email):
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        
        # Validación centralizada de email antes de registrar
        UsuarioService.validar_formato_email(email)
        
        return UsuarioRepository.create(nombre, email)

    @staticmethod
    def login_user(email, password):
        # Validación de formato de correo
        UsuarioService.validar_formato_email(email)
        
        # Búsqueda del usuario en la base de datos por email
        usuario = UsuarioRepository.get_by_email(email.strip())
        
        # Verificación de existencia del usuario
        if not usuario:
            raise PermissionError("El usuario o la contraseña no coinciden.")
            
        # Validación de contraseña contra la base de datos
        password_bd = usuario.get("password") or usuario.get("contrasena")
        
        if password_bd == password:
            # Si las credenciales son válidas, mapeamos los datos para el frontend
            return {
                "id": usuario.get("id"),
                "nombre": usuario.get("nombre"),
                "email": usuario.get("email")
            }
        else:
            raise PermissionError("El usuario o la contraseña no coinciden.")
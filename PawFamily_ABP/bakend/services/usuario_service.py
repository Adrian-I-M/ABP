import re  
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:

    @staticmethod
    def validar_formato_email(correo):
        # Valida que el email no esté vacío y cumpla con la estructura correcta
        if not correo:
            raise ValueError("El correo electrónico es obligatorio.")
        
        patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron_email, correo.strip()):
            raise ValueError("El formato del correo electrónico no es válido.")

    @staticmethod
    def list_users():
        # Obtener la lista de usuarios desde el repositorio
        return UsuarioRepository.get_all()

    @staticmethod 
    def get_user_by_id(user_id):
        # Obtener un usuario por su ID desde el repositorio
        return UsuarioRepository.get_by_id(user_id)

    @staticmethod
    def create_user(nombre, correo, contrasena, rol="cliente"): # CORREGIDO: Acepta el rol de la ruta
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        if not contrasena:
            raise ValueError("La contraseña es obligatoria.")
        
        # Validación centralizada de email antes de registrar
        UsuarioService.validar_formato_email(correo)
        
        # CORREGIDO: Pasa la variable 'rol' que viene de la ruta al repositorio
        return UsuarioRepository.create(nombre, correo, contrasena, rol)

    @staticmethod
    def login_user(correo, contrasena):
        # Validación de formato de correo
        UsuarioService.validar_formato_email(correo)
        
        # Búsqueda del usuario en la base de datos por email
        usuario = UsuarioRepository.get_by_email(correo.strip())
        
        # Verificación de existencia del usuario
        if not usuario:
            raise PermissionError("El usuario o la contraseña no coinciden.")
            
        # Validación de contraseña contra la base de datos
        # Nota: Si tu cursor devuelve tuplas en vez de diccionarios, se accede por posición (ej: usuario[3])
        if isinstance(usuario, dict):
            password_bd = usuario.get("contrasena")
            user_id = usuario.get("id")
            user_name = usuario.get("nombre")
            user_email = usuario.get("correo")
        else:
            # Por si acaso tu conexión devuelve tuplas: asumiendo (id, nombre, correo, contrasena, rol)
            password_bd = usuario[3]
            user_id = usuario[0]
            user_name = usuario[1]
            user_email = usuario[2]
        
        if password_bd == contrasena:
            # Si las credenciales son válidas, mapeamos los datos para el frontend
            return {
                "id": user_id,
                "nombre": user_name,
                "email": user_email
            }
        else:
            raise PermissionError("El usuario o la contraseña no coinciden.")
        
    @staticmethod
    def update_user(user_id, nombre, correo, contrasena):
        if not nombre or not contrasena:
            raise ValueError("El nombre y la contraseña son obligatorios.")
        
        # Validamos que el nuevo email tenga un formato correcto
        UsuarioService.validar_formato_email(correo)
        
        return UsuarioRepository.update(user_id, nombre, correo.strip(), contrasena)
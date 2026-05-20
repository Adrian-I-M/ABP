from PawFamily_ABP.bakend.repositories.usuario_repository import UsuarioRepository

class UsuarioService:

    @staticmethod
    def list_users():
        # Aquí podrías filtrar datos o usar un DTO si hiciera falta
        return UsuarioRepository.get_all()

    @staticmethod
    def get_user_by_id(user_id):
        usuario = UsuarioRepository.get_by_id(user_id)
        if not usuario:
            return None
        return usuario

    @staticmethod
    def create_user(nombre, email):
        # Validación de negocio
        if not nombre or not email:
            raise ValueError("Faltan nombre o email")
        
        return UsuarioRepository.create(nombre, email)
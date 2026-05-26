from config.db import get_connection

class UsuarioRepository:
    
    @staticmethod
    def get_all():
        connection = get_connection()
        if not connection:  
            return []
            
        cursor = connection.cursor()
        # Obtiene todos los usuarios ordenados por ID
        cursor.execute("SELECT * FROM usuarios ORDER BY id")
        usuarios = cursor.fetchall()
        
        cursor.close()
        connection.close()
        return usuarios

    @staticmethod
    def get_by_id(user_id):
        connection = get_connection()
        if not connection:  
            return None
            
        cursor = connection.cursor()
        # Busca un usuario específico por su ID
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
        usuarios = cursor.fetchone()
        
        cursor.close()
        connection.close()
        return usuarios

    @staticmethod
    def create(nombre, correo, contrasena, rol):
        connection = get_connection()
        if not connection:  
            return None
            
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, correo, contrasena, rol) VALUES (%s, %s, %s, %s)",
            (nombre, correo, contrasena, rol)
        )
        connection.commit()  
        new_id = cursor.lastrowid
        
        cursor.close()
        connection.close()
        return new_id

    @staticmethod
    def get_by_email(correo):
        connection = get_connection()
        if not connection:
            return None
            
        cursor = connection.cursor()
        # CORREGIDO: Busca por la columna 'correo' para el proceso de Login
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
        usuarios = cursor.fetchone()  # Devuelve el diccionario del usuario o None
        
        cursor.close()
        connection.close()
        return usuarios
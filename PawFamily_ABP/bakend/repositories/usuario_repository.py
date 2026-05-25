from config.db import get_connection

class UsuarioRepository:
    
    @staticmethod
    def get_all():
        connection = get_connection()
        if not connection:  
            return []
            
        cursor = connection.cursor()
        # Obtiene todos los usuarios ordenados por ID
        cursor.execute("SELECT * FROM usuario ORDER BY id")
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
        cursor.execute("SELECT * FROM usuario WHERE id = %s", (user_id,))
        usuario = cursor.fetchone()
        
        cursor.close()
        connection.close()
        return usuario

    @staticmethod
    def create(nombre, email):
        connection = get_connection()
        if not connection:  
            return None
            
        cursor = connection.cursor()
        # Registra un nuevo usuario en MySQL
        cursor.execute(
            "INSERT INTO usuario (nombre, email) VALUES (%s, %s)",
            (nombre, email)
        )
        connection.commit()  # Confirma la inserción en la base de datos
        new_id = cursor.lastrowid
        
        cursor.close()
        connection.close()
        return new_id
    
    @staticmethod
    def get_by_email(email):
        connection = get_connection()
        if not connection:
            return None
            
        cursor = connection.cursor()
        # Busca un usuario por su email para el proceso de Login
        cursor.execute("SELECT * FROM usuario WHERE email = %s", (email,))
        usuario = cursor.fetchone()  # Devuelve el diccionario del usuario o None
        
        cursor.close()
        connection.close()
        return usuario
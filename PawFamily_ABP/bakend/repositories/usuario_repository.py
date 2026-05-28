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
    
    @staticmethod
    def update(user_id, nombre, correo, contrasena):
        connection = get_connection()
        if not connection:  
            return False
        cursor = connection.cursor()
        
        cursor.execute(
            """UPDATE usuarios 
               SET nombre=%s, correo=%s, contrasena=%s 
               WHERE id=%s""",
            (nombre, correo, contrasena, user_id)
        )
        connection.commit()
        filas_afectadas = cursor.rowcount
        
        cursor.close()
        connection.close()
        return filas_afectadas > 0
    @staticmethod
    def delete(user_id):
        connection = get_connection()
        if not connection:
            return False
            
        cursor = connection.cursor()
        # Elimina el usuario filtrando por su ID
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
        connection.commit()
        
        filas_afectadas = cursor.rowcount
        
        cursor.close()
        connection.close()
        return filas_afectadas > 0
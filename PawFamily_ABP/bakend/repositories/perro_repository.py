from config.db import get_connection

class PerroRepository:
    
    @staticmethod
    def get_all():
        connection = get_connection()
        if not connection:  
            return None
            
        cursor = connection.cursor()
        # Obtiene todos los registros de la tabla perro
        cursor.execute("SELECT * FROM perro ORDER BY id")
        perros = cursor.fetchall()
        
        cursor.close()
        connection.close()
        return perros

    @staticmethod
    def get_by_id(perro_id):
        connection = get_connection()
        if not connection:  
            return None
            
        cursor = connection.cursor()
        # Busca un perro específico filtrando por su ID
        cursor.execute("SELECT * FROM perro WHERE id = %s", (perro_id,))
        perro = cursor.fetchone()
        
        cursor.close()
        connection.close()
        return perro

    @staticmethod
    def create(nombre, raza, edad, id_usuario):
        connection = get_connection()
        if not connection:  
            return None
            
        cursor = connection.cursor()
        # Inserta un nuevo perro en la base de datos
        cursor.execute(
            "INSERT INTO perro (nombre, raza, edad, id_usuario) VALUES (%s, %s, %s, %s)",
            (nombre, raza, edad, id_usuario)
        )
        connection.commit()  # Confirma la inserción en MySQL
        new_id = cursor.lastrowid  # Captura el ID autogenerado
        
        cursor.close()
        connection.close()
        return new_id
    
    @staticmethod
    def delete(perro_id):
        connection = get_connection()
        if not connection:
            return False
            
        cursor = connection.cursor()
        # Elimina un registro por su ID
        cursor.execute("DELETE FROM perro WHERE id = %s", (perro_id,))
        connection.commit()  # Confirma la eliminación en MySQL
        
        filas_afectadas = cursor.rowcount  # Devuelve cuántas filas se borraron
        
        cursor.close()
        connection.close()
        return filas_afectadas > 0
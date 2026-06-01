from config.db import get_connection

class PerroRepository:
    
    @staticmethod
    def get_all():
        connection = get_connection()
        if not connection:  
            return None
            
        cursor = connection.cursor()
        # Modificado: Añadimos un INNER JOIN para traernos los datos reales de la raza y tamaño
        query = """
            SELECT p.*, r.nombre_raza AS raza, r.tamano 
            FROM perros p
            INNER JOIN razas r ON p.id_raza = r.id_raza
            ORDER BY p.id
        """
        cursor.execute(query)
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
        # Modificado: Añadimos el mismo INNER JOIN filtrando por el ID del perro
        query = """
            SELECT p.*, r.nombre_raza AS raza, r.tamano 
            FROM perros p
            INNER JOIN razas r ON p.id_raza = r.id_raza
            WHERE p.id = %s
        """
        cursor.execute(query, (perro_id,))
        perro = cursor.fetchone()
        
        cursor.close()
        connection.close()
        return perro

    @staticmethod
    def create(nombre, chip, edad, descripcion, raza, estado, historial_medico, fecha_entrada, imagen_url, genero):
        connection = get_connection()
        if not connection:  
            return None
        cursor = connection.cursor()
        # Inserta un nuevo perro en la base de datos
        cursor.execute(
            """INSERT INTO perros 
            (nombre, chip, edad, descripcion, raza, estado, historial_medico, fecha_entrada, imagen, genero) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (nombre, chip, edad, descripcion, raza, estado, historial_medico, fecha_entrada, imagen_url, genero)
        )
        connection.commit()  # Confirma la inserción en MySQL
        new_id = cursor.lastrowid  # Captura el ID autogenerado
        
        cursor.close()
        connection.close()
        return new_id
    
    @staticmethod
    def update(perro_id, nombre, chip, edad, descripcion, raza, estado, historial_medico, genero):
        connection = get_connection()
        if not connection:  
            return False
        cursor = connection.cursor()
        
        # Ejecutamos la actualización filtrando por el ID del perro
        cursor.execute(
            """UPDATE perros 
               SET nombre=%s, chip=%s, edad=%s, descripcion=%s, raza=%s, 
                   estado=%s, historial_medico=%s, genero=%s 
               WHERE id=%s""",
            (nombre, chip, edad, descripcion, raza, estado, historial_medico, genero, perro_id)
        )
        connection.commit()
        filas_afectadas = cursor.rowcount # Devuelve cuántas filas han cambiado realmente
        
        cursor.close()
        connection.close()
        return filas_afectadas > 0

    @staticmethod
    def delete(perro_id):
        connection = get_connection()
        if not connection:
            return False
            
        cursor = connection.cursor()
        # Elimina un registro por su ID
        cursor.execute("DELETE FROM perros WHERE id = %s", (perro_id,))
        connection.commit()  # Confirma la eliminación en MySQL
        
        filas_afectadas = cursor.rowcount  # Devuelve cuántas filas se borraron
        
        cursor.close()
        connection.close()
        return filas_afectadas > 0
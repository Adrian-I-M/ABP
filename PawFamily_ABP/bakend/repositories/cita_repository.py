from config.db import get_connection

class CitaRepository:
    
    @staticmethod
    def create(id_usuario, id_perro, fecha_cita, hora_cita):
        connection = get_connection()
        if not connection:  
            return None
        cursor = connection.cursor()
        
        cursor.execute(
            """INSERT INTO citas (id_usuario, id_perro, fecha_cita, hora_cita) 
            VALUES (%s, %s, %s, %s)""", 
            (id_usuario, id_perro, fecha_cita, hora_cita)
        )
        connection.commit()
        new_id = cursor.lastrowid
        
        cursor.close()
        connection.close()
        return new_id

    @staticmethod
    def get_all_with_details():
        connection = get_connection()
        if not connection:  
            return []
        cursor = connection.cursor()
        
        # Un JOIN para traer los datos del perro y del usuario del tirón
        query = """
            SELECT 
                c.id AS cita_id, c.fecha_cita, c.hora_cita,
                u.nombre AS nombre_usuario, u.correo AS correo_usuario,
                p.nombre AS nombre_perro, p.raza AS raza_perro
            FROM citas c
            JOIN usuarios u ON c.id_usuario = u.id
            JOIN perros p ON c.id_perro = p.id
            ORDER BY c.fecha_cita ASC, c.hora_cita ASC
        """
        cursor.execute(query)
        citas = cursor.fetchall()
        
        cursor.close()
        connection.close()
        return citas
    
    @staticmethod
    def update(cita_id, id_usuario, id_perro, fecha_cita, hora_cita):
        connection = get_connection()
        if not connection:  
            return False
        cursor = connection.cursor()
        
        # Modifica los datos de la cita filtrando por su ID único
        cursor.execute(
            """UPDATE citas 
               SET id_usuario=%s, id_perro=%s, fecha_cita=%s, hora_cita=%s 
               WHERE id=%s""",
            (id_usuario, id_perro, fecha_cita, hora_cita, cita_id)
        )
        connection.commit()
        filas_afectadas = cursor.rowcount
        
        cursor.close()
        connection.close()
        return filas_afectadas > 0

    @staticmethod
    def delete(cita_id):
        connection = get_connection()
        if not connection:
            return False
            
        cursor = connection.cursor()
        # Elimina la cita físicamente de MySQL usando su ID
        cursor.execute("DELETE FROM citas WHERE id = %s", (cita_id,))
        connection.commit()
        
        filas_afectadas = cursor.rowcount
        
        cursor.close()
        connection.close()
        return filas_afectadas > 0
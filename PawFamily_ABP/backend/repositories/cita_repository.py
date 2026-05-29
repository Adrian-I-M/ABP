from config.db import get_connection

class CitaRepository:
    # CREATE
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

    # READ
    @staticmethod
    def get_all_with_details():
        connection = get_connection()
        if not connection:
            return []
        cursor = connection.cursor()
        query = """
            SELECT
                c.id_cita AS cita_id, c.fecha_cita, c.hora_cita,
                u.nombre AS nombre_usuario, u.correo AS correo_usuario,
                p.nombre AS nombre_perro, r.nombre_raza AS raza_perro
            FROM citas c
            JOIN usuarios u ON c.id_usuario = u.id
            JOIN perros p ON c.id_perro = p.id
            JOIN razas r ON p.id_raza = r.id_raza
            ORDER BY c.fecha_cita ASC, c.hora_cita ASC
"""
        cursor.execute(query)
        filas = cursor.fetchall()
        columnas = [col[0] for col in cursor.description]
        cursor.close()
        connection.close()
        citas = []
        for fila in filas:
            cita = dict(zip(columnas, fila))
            if hasattr(cita['hora_cita'], 'total_seconds'):
                total = int(cita['hora_cita'].total_seconds())
                cita['hora_cita'] = f"{total // 3600:02d}:{(total % 3600) // 60:02d}"
            citas.append(cita)
        return citas

    # UPDATE
    @staticmethod
    def update(cita_id, id_usuario, id_perro, fecha_cita, hora_cita):
        connection = get_connection()
        if not connection:
            return False
        cursor = connection.cursor()
        cursor.execute(
            """UPDATE citas
               SET id_usuario=%s, id_perro=%s, fecha_cita=%s, hora_cita=%s
               WHERE id_cita=%s""",
            (id_usuario, id_perro, fecha_cita, hora_cita, cita_id)
        )
        connection.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        connection.close()
        return filas_afectadas > 0

    # DELETE
    @staticmethod
    def delete(cita_id):
        connection = get_connection()
        if not connection:
            return False
        cursor = connection.cursor()
        cursor.execute("DELETE FROM citas WHERE id_cita = %s", (cita_id,))
        connection.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        connection.close()
        return filas_afectadas > 0
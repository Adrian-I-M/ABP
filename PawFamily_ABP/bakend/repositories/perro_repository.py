from config.db import get_connection

class PerroRepository:
    
    @staticmethod
    def get_all():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM perro ORDER BY id")
        perros = cursor.fetchall()
        cursor.close()
        connection.close()
        return perros

    @staticmethod
    def get_by_id(perro_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM perro WHERE id = %s", (perro_id,))
        perro = cursor.fetchone()
        cursor.close()
        connection.close()
        return perro

    @staticmethod
    def create(nombre, raza, edad, id_usuario):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO perro (nombre, raza, edad, id_usuario) VALUES (%s, %s, %s, %s)",
            (nombre, raza, edad, id_usuario)
        )
        connection.commit()
        new_id = cursor.lastrowid
        cursor.close()
        connection.close()
        return new_id
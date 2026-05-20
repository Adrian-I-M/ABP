from config.db import get_connection

class UsuarioRepository:
    
    @staticmethod
    def get_all():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM usuario ORDER BY id")
        usuarios = cursor.fetchall()
        cursor.close()
        connection.close()
        return usuarios

    @staticmethod
    def get_by_id(user_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM usuario WHERE id = %s", (user_id,))
        usuario = cursor.fetchone()
        cursor.close()
        connection.close()
        return usuario

    @staticmethod
    def create(nombre, email):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO usuario (nombre, email) VALUES (%s, %s)",
            (nombre, email)
        )
        connection.commit()
        new_id = cursor.lastrowid
        cursor.close()
        connection.close()
        return new_id
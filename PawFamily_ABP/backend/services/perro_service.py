import os
import uuid
from repositories.perro_repository import PerroRepository

EXTENSIONES_PERMITIDAS = {'png', 'jpg', 'jpeg', 'webp'}

class PerroService:

    # LISTAR Y OBTENER
    @staticmethod
    def list_perros():
        return PerroRepository.get_all()

    @staticmethod
    def get_perro_by_id(perro_id):
        perro = PerroRepository.get_by_id(perro_id)
        if not perro:
            return None
        return perro

    # CREATE CON FICHERO
    @staticmethod
    def create_perro(nombre, chip, edad, descripcion, raza, estado, historial_medico, fecha_entrada, archivo_imagen, carpeta_destino, genero):
        if not nombre or not raza:
            raise ValueError("El nombre y la raza son obligatorios")
        try:
            edad_int = int(edad)
        except (ValueError, TypeError):
            raise ValueError("La edad debe ser un número válido")
        if edad_int < 0:
            raise ValueError("La edad no puede ser un número negativo")
        if not archivo_imagen or archivo_imagen.filename == '':
            raise ValueError("La foto del perro es obligatoria")
        extension = archivo_imagen.filename.rsplit('.', 1)[1].lower() if '.' in archivo_imagen.filename else ''
        if extension not in EXTENSIONES_PERMITIDAS:
            raise ValueError("Formato de imagen no permitido (Usa png, jpg, jpeg o webp)")
        nombre_unico = f"{uuid.uuid4()}.{extension}"
        ruta_fisica = os.path.join(carpeta_destino, nombre_unico)
        archivo_imagen.save(ruta_fisica)
        ruta_imagen_bd = f"/uploads/{nombre_unico}"
        try:
            return PerroRepository.create(
                nombre, chip, edad_int, descripcion, raza,
                estado, historial_medico, fecha_entrada, ruta_imagen_bd, genero
            )
        except Exception as error:
            if os.path.exists(ruta_fisica):
                os.remove(ruta_fisica)
            raise error

    # CREATE CON URL
    @staticmethod
    def create_perro_url(nombre, raza, edad, descripcion, estado, genero, imagen_url):
        if not nombre or not raza:
            raise ValueError("El nombre y la raza son obligatorios")
        try:
            edad_int = int(edad)
        except (ValueError, TypeError):
            raise ValueError("La edad debe ser un número válido")
        if edad_int < 0:
            raise ValueError("La edad no puede ser negativa")
        return PerroRepository.create(
            nombre, None, edad_int, descripcion, raza,
            estado, None, None, imagen_url, genero
        )

    # UPDATE
    @staticmethod
    def update_perro(perro_id, nombre, chip, edad, descripcion, raza, estado, historial_medico, genero):
        if not nombre or not raza:
            raise ValueError("El nombre y la raza son obligatorios para actualizar.")
        try:
            edad_int = int(edad)
        except (ValueError, TypeError):
            raise ValueError("La edad debe ser un número válido.")
        if edad_int < 0:
            raise ValueError("La edad no puede ser negativa.")
        return PerroRepository.update(
            perro_id, nombre, chip, edad_int, descripcion, raza, estado, historial_medico, genero
        )

    # DELETE
    @staticmethod
    def delete_perro(perro_id):
        return PerroRepository.delete(perro_id)

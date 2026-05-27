import os
import uuid
from repositories.perro_repository import PerroRepository

# Extensiones de imagen válidas
EXTENSIONES_PERMITIDAS = {'png', 'jpg', 'jpeg', 'webp'}

class PerroService:

    @staticmethod
    def list_perros():
        # Llama al repositorio para obtener todos los perros de MySQL
        return PerroRepository.get_all()
    
    @staticmethod # Obtener un perro por su ID 
    def get_perro_by_id(perro_id):
        perro = PerroRepository.get_by_id(perro_id)
        if not perro:
            return None
        return perro

    @staticmethod
    def create_perro(nombre, chip, edad, descripcion, raza, estado, historial_medico, fecha_entrada, archivo_imagen, carpeta_destino, genero):
        # Validación de campos obligatorios
        if not nombre or not raza:
            raise ValueError("El nombre y la raza son obligatorios")
        
        try:
            edad_int = int(edad)
        except (ValueError, TypeError):
            raise ValueError("La edad debe ser un número válido")

        # Validación de rango de edad
        if int(edad) < 0:
            raise ValueError("La edad no puede ser un número negativo")
            
        # Control y procesamiento de la Imagen con UUID
        if not archivo_imagen or archivo_imagen.filename == '':
            raise ValueError("La foto del perro es obligatoria")
            
        # Validar extensión del archivo
        extension = archivo_imagen.filename.rsplit('.', 1)[1].lower() if '.' in archivo_imagen.filename else ''
        if extension not in EXTENSIONES_PERMITIDAS:
            raise ValueError("Formato de imagen no permitido (Usa png, jpg, jpeg o webp)")
            
        # Generar nombre único en el universo con UUID v4
        nombre_unico = f"{uuid.uuid4()}.{extension}"
        
        # Ruta física del disco duro donde se guarda el archivo real
        ruta_fisica = os.path.join(carpeta_destino, nombre_unico)
        archivo_imagen.save(ruta_fisica)
        
        # Ruta relativa web que se guardará en el campo texto de la Base de Datos
        ruta_imagen_bd = f"/uploads/{nombre_unico}"
        
        # Intentamos guardar en la Base de Datos
        try:
            return PerroRepository.create(
                nombre, chip, edad_int, descripcion, raza, 
                estado, historial_medico, fecha_entrada, ruta_imagen_bd, genero
            )
        except Exception as error:
            # Si MySQL falla, borramos la foto del disco para no dejar basura
            if os.path.exists(ruta_fisica):
                os.remove(ruta_fisica)
            raise error

    @staticmethod
    def delete_perro(perro_id):
        # Llama al repositorio para eliminar un perro por su ID
        return PerroRepository.delete(perro_id)
from repositories.perro_repository import PerroRepository

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
    def create_perro(nombre, raza, edad, id_usuario):
        # Validación de campos obligatorios
        if not nombre or not raza:
            raise ValueError("El nombre y la raza son obligatorios")
        
        try:
            edad_int = int(edad)
        except (ValueError, TypeError):
            raise ValueError("La edad debe ser un número válido")

        # Validación de rango de edad
        if edad_int < 0:
            raise ValueError("La edad no puede ser un número negativo")
            
        return PerroRepository.create(nombre, raza, edad_int, id_usuario)

    @staticmethod
    def delete_perro(perro_id):
        # Llama al repositorio para eliminar un perro por su ID
        return PerroRepository.delete(perro_id)
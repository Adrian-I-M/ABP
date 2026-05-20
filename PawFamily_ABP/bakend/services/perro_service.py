from repositories.perro_repository import PerroRepository

class PerroService:

    @staticmethod
    def list_perros():
        return PerroRepository.get_all()
    
    @staticmethod
    def get_perro_by_id(perro_id):
        perro = PerroRepository.get_by_id(perro_id)
        if not perro:
            return None
        return perro

    @staticmethod
    def create_perro(nombre, raza, edad, id_usuario):
     
        if not nombre or not raza:
            raise ValueError("El nombre y la raza son obligatorios")
        
        if int(edad) < 0:
            raise ValueError("La edad no puede ser un número negativo")
            
        # Si todo está bien, llamamos al repositorio para que lo guarde en MySQL
        return PerroRepository.create(nombre, raza, edad, id_usuario)
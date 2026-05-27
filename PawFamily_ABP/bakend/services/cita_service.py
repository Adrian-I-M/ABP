from repositories.cita_repository import CitaRepository

class CitaService:

    @staticmethod
    def crear_cita(id_usuario, id_perro, fecha_cita, hora_cita, motivo):
        # Validaciones de negocio
        if not id_usuario or not id_perro:
            raise ValueError("El usuario y el perro son obligatorios para agendar una cita.")
        if not fecha_cita or not hora_cita:
            raise ValueError("La fecha y la hora de la cita son obligatorias.")
            
        return CitaRepository.create(id_usuario, id_perro, fecha_cita, hora_cita, motivo)

    @staticmethod
    def listar_citas():
        return CitaRepository.get_all_with_details()
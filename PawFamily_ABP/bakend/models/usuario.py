class Usuario:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

    # Esto ayuda a convertir el objeto a un diccionario fácil de transformar en JSON
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email
        }
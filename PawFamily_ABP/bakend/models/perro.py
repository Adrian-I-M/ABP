class Perro:
    def __init__(self, id, nombre, raza, edad, id_usuario):
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.id_usuario = id_usuario  # Esto relaciona al perro con su dueño

    # Esto os vendrá de lujo para convertir el objeto a un diccionario 
    # y poder enviarlo como JSON en las rutas
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "raza": self.raza,
            "edad": self.edad,
            "id_usuario": self.id_usuario
        }
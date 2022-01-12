from persona import Persona


class Firmantes(Persona):
    def __init__(self, nombre, apellido, edad, dni):
        Persona.__init__(self, nombre, apellido, edad, dni)


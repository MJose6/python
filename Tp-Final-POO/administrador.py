from usuarios import Usuario
from persona import Persona
from cliente import  Cliente
from secuencia import Secuencias

class Admin(Persona):
    def __init__(self, nombre, apellido, edad, dni):
        Persona.__init__(self, nombre, apellido, edad, dni)
        self._id = Secuencias.getNroAdm()
        Secuencias.siguienteNroAdm()

    def getId(self):
        return self._id

    def __str__(self):
        return f'Administrador {self._id} : {self._nombre} - {self._apellido} - {self._edad} - {self._dni}'
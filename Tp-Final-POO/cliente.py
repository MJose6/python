from usuarios import Usuario
from persona import Persona
from secuencia import Secuencias

class Cliente():
    def __init__(self, mail, direccion, telefono):
        self._id = Secuencias.getNroCliente()
        Secuencias.siguienteNroCliente()
        self._mail = mail
        self._direccion = direccion
        self._telefono = telefono
        self._cuentasCliente = {}


    def getId(self):
        return self._id

    def getCuentasCli(self):
        return self._cuentasCliente

class Individuo(Cliente, Persona):

    def __init__(self, nombre, apellido, edad, dni, mail, direccion, telefono):
        Persona.__init__(self, nombre, apellido, edad, dni)
        Cliente.__init__(self, mail, direccion, telefono)



    def __str__(self):
        return f'Cliente {self.getId()} : {self._nombre} - {self._apellido} - {self._edad} - {self._dni} - {self._mail} - {self._direccion} - {self._telefono}'



class Pyme(Cliente):

    def __init__(self, razonSocial, cuit, mail, direccion, telefono):
        super().__init__(mail, direccion, telefono)
        self._razonSocial = razonSocial
        self._cuit = cuit


    def __str__(self):
        return f'Cliente {self.getId()} : {self._razonSocial} - {self._cuit} - {self._mail} - {self._direccion} - {self._telefono}'

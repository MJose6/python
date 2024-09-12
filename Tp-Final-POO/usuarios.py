from secuencia import Secuencias

class Usuario:
    def __init__(self, usuario, contraseña, rol):
        self._id = Secuencias.getNroUser()
        Secuencias.siguienteNroUser()
        self._usuario = usuario
        self._contraseña = contraseña
        self._rol = rol


    def getIdUs(self):
        return self._id

    @property
    def usuario(self):
        return  self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def contraseña(self):
        return self._contraseña

    @contraseña.setter
    def contraseña(self, contraseña):
        self._contraseña = contraseña

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol




    def __str__(self):
        return f'{self._usuario} - {self._contraseña} - {self._rol}'



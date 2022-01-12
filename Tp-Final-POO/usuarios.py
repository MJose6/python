from secuencia import Secuencias

class Usuario:
    def __init__(self, usuario, contraseña, rol, pyme, individuo):
        self._id = Secuencias.getNroUser()
        Secuencias.siguienteNroUser()
        self._usuario = usuario
        self._contraseña = contraseña
        self._rol = rol
        self._pyme = pyme
        self._individuo = individuo

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

    @property
    def pyme(self):
        return self._pyme

    @pyme.setter
    def pyme(self, pyme):
        self._pyme = pyme

    @property
    def individuo(self):
        return self._individuo

    @individuo.setter
    def individuo(self, individuo):
        self._individuo = individuo



    def __str__(self):
        return f'{self.getIdUs()} - {self._usuario} - {self._contraseña} - {self._rol} - {self._pyme} - {self._individuo}'



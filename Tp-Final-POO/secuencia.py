class Secuencias():

    nroOperacion = 1
    nroCuenta = 100
    nroCbu = 1000
    nroCliente = 1
    nroAdm = 1
    nroUser = 1

    def __init__(self):
        pass

    @classmethod
    def getNroOperacion(cls):
        return cls.nroOperacion

    @classmethod
    def siguienteNroOperacion(cls):
        cls.nroOperacion += 1

    @classmethod
    def getNroCuenta(cls):
        return cls.nroCuenta

    @classmethod
    def siguienteNroCuenta(cls):
        cls.nroCuenta += 1

    @classmethod
    def getNroCbu(cls):
        return cls.nroCbu

    @classmethod
    def siguienteNroCbu(cls):
        cls.nroCbu += 1

    @classmethod
    def getNroCliente(cls):
        return cls.nroCliente

    @classmethod
    def siguienteNroCliente(cls):
        cls.nroCliente += 1

    @classmethod
    def getNroAdm(cls):
        return cls.nroAdm

    @classmethod
    def siguienteNroAdm(cls):
        cls.nroAdm += 1

    @classmethod
    def getNroUser(cls):
        return cls.nroUser

    @classmethod
    def siguienteNroUser(cls):
        cls.nroUser += 1


from secuencia import Secuencias
from cliente import Cliente, Individuo, Pyme


class Cuenta:
    def __init__(self, sucursal,  fechaApertura, saldo, tipo, saldoRetenido):
        self._sucursal = sucursal
        self._nroCuenta = Secuencias.getNroCuenta()
        Secuencias.siguienteNroCuenta()
        self._cbu = Secuencias.getNroCbu()
        Secuencias.siguienteNroCbu()
        self._fechaApertura = fechaApertura
        self._saldo = saldo
        self._tipo = tipo
        self._saldoRetenido = saldoRetenido



class CajaDeAhorros(Cuenta):
    def __init__(self, sucursal, fechaApertura, saldo, tipo, saldoRetenido):
        super().__init__(sucursal, fechaApertura, saldo, tipo, saldoRetenido)

    def __str__(self):
        return f'{self._nroCuenta} - {self._sucursal} - {self._fechaApertura} - {self._saldo} - {self._tipo} - {self._saldoRetenido}'

class CtaCte(Cuenta):
    def __init__(self, descubierto, sucursal, fechaApertura, saldo, tipo, saldoRetenido):
        self._descubierto = descubierto
        super().__init__( sucursal, fechaApertura, saldo, tipo, saldoRetenido)

    def __str__(self):
        return f'{self._nroCuenta} - {self._descubierto} - {self._sucursal} - {self._fechaApertura} - {self._saldo} - {self._tipo} - {self._saldoRetenido}'


from secuencia import Secuencias
from cliente import Cliente, Individuo, Pyme


class Cuenta:
    def __init__(self, sucursal, cbu, nroCuenta, fechaApertura, saldo, tipo, saldoRetenido):
        self._sucursal = sucursal
        self._cbu = cbu
        self._nroCuenta = nroCuenta
        self._fechaApertura = fechaApertura
        self._saldo = saldo
        self._tipo = tipo
        self._saldoRetenido = saldoRetenido

        self._cbu = Secuencias.getNroCbu()
        Secuencias.siguienteNroCbu()
        self._nroCuenta = Secuencias.getNroCuenta()
        Secuencias.siguienteNroCuenta()

class CajaDeAhorros(Cuenta):
    def __init__(self, sucursal, cbu, nroCuenta, fechaApertura, saldo, tipo, saldoRetenido):
        super().__init__(sucursal, cbu, nroCuenta, fechaApertura, saldo, tipo, saldoRetenido)

    def __str__(self):
        return f' {self._cbu} - {self._nroCuenta} - {self._saldo} - {self._tipo} - {self._saldoRetenido}'

class CtaCte(Cuenta):
    def __init__(self, descubierto, sucursal, cbu, nroCuenta, fechaApertura, saldo, tipo, saldoRetenido):
        self._descubierto = descubierto
        super().__init__(sucursal, cbu, nroCuenta, fechaApertura, saldo, tipo, saldoRetenido)

    def __str__(self):
        return f' {self._cbu} - {self._nroCuenta} - {self._descubierto} - {self._saldo} - {self._tipo} - {self._saldoRetenido}'


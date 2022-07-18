from cliente import  Cliente, Individuo, Pyme
from usuarios import Usuario
from administrador import  Admin
from cuentas import Cuenta, CajaDeAhorros, CtaCte
from datetime import datetime




class Banco():
    def __init__(self, sucursal=None, direccion=None):
        self._sucursal = sucursal
        self._direccion = direccion
        self._admin = {}
        self._clientes = {}
        self._usuarios = {}
        self._cuentas = {}
        self._servicios = {}
        self._operaciones = {}
        self._intentos = 0
        self._usuarioConectado = None
        self.cargarDatosIniciales()

    def getCuentas(self):
        return self._cuentas

    def getUsuarios(self):
        return self._usuarios

    def getClientes(self):
        return self._clientes

    def getAdmin(self):
        return self._admin
    
    def getOperaciones(self):
        return self._operaciones



    def cargarDatosIniciales(self):
        #creando admin
        user = Admin('ricardo', 'pepe', 44, 25343232)
        usUser1 = Usuario('banquero', 'b1234', 'Administrador', None, None)
        self._admin[user.getId()] = user
        self._usuarios[usUser1.usuario] = usUser1

        #creando cliente1
        cliente1 = Individuo('Juan', 'Perez', 33, 33543829, 'jperez@mail.com', 'dinamarca 641', 24940303456)
        usCliente1 = Usuario('jp', 'jp123', 'Cliente Individuo', None, cliente1)
        self._clientes[cliente1.getId()] = cliente1
        self._usuarios[usCliente1.usuario] = usCliente1
        cta = CajaDeAhorros(self._sucursal, datetime.now(), 0, 'Caja de ahorros comun', None)
        self._cuentas[usCliente1] = cta
        usCliente1.individuo.getCuentasCli()[usCliente1] = cta

        #creando cliente2
        cliente2 = Individuo('Raul', 'Gonzales', 38, 27543869, 'rgonzales@mail.com', 'las heras 641', 24944560303)
        usCliente2 = Usuario('rg', 'rg123', 'Cliente Individuo', None, cliente2)
        self._clientes[cliente2.getId()] = cliente2
        self._usuarios[usCliente2.usuario] = usCliente2
        cta = CtaCte(None, self._sucursal, datetime.now(), 0, 'Cta cte de saldo retenido', 3000)
        self._cuentas[usCliente2] = cta
        usCliente2.individuo.getCuentasCli()[usCliente2] = cta

        #creando cliente3
        cliente3 = Pyme('La Super', '30-71495333-5', 'lasuper@mail.com', 'Rauch 1234', 2494219282)
        usCliente3 = Usuario('ls', 'ls123', 'Cliente Pyme', cliente3, None)
        self._clientes[cliente3.getId()] = cliente3
        self._usuarios[usCliente3.usuario] = usCliente3
        cta = CtaCte(10000, self._sucursal, datetime.now(), 0, 'Cta cte comun', None)
        self._cuentas[usCliente3] = cta
        usCliente3.pyme.getCuentasCli()[usCliente3] = cta

        #creando cliente4
        cliente4 = Pyme('La EFE', '30-72436789-5', 'laefe@mail.com', 'Darragueira 525', 2494219282)
        usCliente4 = Usuario('le', 'le123', 'Cliente Pyme', cliente4, None)
        self._clientes[cliente4.getId()] = cliente4
        self._usuarios[usCliente4.usuario] = usCliente4
        cta = CtaCte(10000, self._sucursal, datetime.now(), 0, 'Cta cte de saldo retenido', 3000)
        self._cuentas[usCliente4] = cta
        usCliente4.pyme.getCuentasCli()[usCliente4] = cta




    #metodos utilizado solo por el administrador
    def cargarCostosDeCuentas(self):
        pass



    def registrarCliente(self):
        registro = False
        while registro == False:
            print('1. Registrar Individuo')
            print('2. Registrar Pyme')
            print('3. salir')

            opcion = input('Ingrese el numero de opcion: ')

            if opcion == '1':
                nombre = input('Ingrese su nombre: ')
                apellido = input('Ingrese su apellido: ')
                edad = input('Ingrese su edad: ')
                dni = input('Ingrese su dni: ')
                mail = input('Ingrese su mail: ')
                direccion = input('Ingrese su direccion: ')
                telefono = input('Ingrese su telefono: ')
                cliente = Individuo(nombre, apellido, edad, dni, mail, direccion, telefono)
                self._clientes[cliente.getId()] = cliente
                usuario = input('Ingrese un nombre de usuario: ')
                contraseña = input('Ingrese una contraseña: ')
                rol = 'Cliente Individuo'
                pyme = None
                individuo = cliente
                user = Usuario(usuario, contraseña, rol, pyme, individuo)
                self._usuarios[user.usuario] = user



            if opcion == '2':
                razonSocial = input('Ingrese la razon social: ')
                cuit = input('Ingrese su CUIT: ')
                mail = input('Ingrese su mail: ')
                direccion = input('Ingrese su direccion: ')
                telefono = input('Ingrese su telefono: ')
                cliente = Pyme(razonSocial, cuit, mail, direccion, telefono)
                self._clientes[cliente.getId()] = cliente
                usuario = input('Ingrese un nombre de usuario: ')
                contraseña = input('Ingrese una contraseña: ')
                rol = 'Cliente Pyme'
                pyme = cliente
                individuo = None
                user = Usuario(usuario, contraseña, rol, pyme, individuo)
                self._usuarios[user.usuario] = user

            if opcion == '3':
                self.logOut()
                registro = True
                self.logIn()



    def menuOperacionesCliente(self):
        usuario = self._usuarioConectado

        operaciones = False
        for us in self._cuentas.values():
            operaciones = True
        if operaciones == True and usuario.rol == 'Cliente Individuo':
            opTipoCuenta = input('Presione 1 para operar con CAJA DE AHORROS y 2 para operar con CUENTA CORRIENTE: ')

            if opTipoCuenta == '1':
                if self._usuarioConectado in self._cuentas and self._cuentas[self._usuarioConectado]._tipo == 'Caja de ahorros comun' or self._cuentas[self._usuarioConectado]._tipo == 'Caja de ahorros de saldo retenido':
                    operacion = False
                    while operacion == False:
                        print('1. Depositar')
                        print('2. Transferir')
                        print('3. Consultar saldo')
                        print('4. Pago en linea')
                        print('5. Consultar CBU y Nro Cuenta')
                        print('6. Extraccion')
                        print('7. Salir')
                        opcion = input('Igrese el numero de opcion a realizar: ')
                        if opcion == '1':
                            self.depositar()
                            operacion = False
                        elif opcion == '2':
                            self.transferir()
                            operacion = False
                        elif opcion == '3':
                            self.consultaSaldo()
                            operacion = False
                        elif opcion == '4':
                            self.pagoEnLinea()
                            operacion = False
                        elif opcion == '5':
                            self.consultaCbuCuenta()
                            operacion = False
                        elif opcion == '6':
                            self.extraccion()
                            operacion = False
                        elif opcion == '7':
                            self.logOut()
                            operacion = True
                            self.logIn()
                else:
                    print('-----------------------')
                    print('Usted no posee una caja de ahorros.')
                    self.menuOperacionesCliente()
            else:
                if self._usuarioConectado in self._cuentas and self._cuentas[self._usuarioConectado]._tipo == 'Cta cte comun' or self._cuentas[self._usuarioConectado]._tipo == 'Cta cte de saldo retenido':
                    operacion = False
                    while operacion == False:
                        print('1. Depositar')
                        print('2. Transferir')
                        print('3. Consultar saldo')
                        print('4. Pago en linea')
                        print('5. Consultar CBU y Nro Cuenta')
                        print('6. Extraccion')
                        print('7. Plazo fijo')
                        print('8. Comprar moneda extranjera')
                        print('9. Salir')
                        opcion = input('Igrese el numero de opcion a realizar: ')
                        if opcion == '1':
                            self.depositar()
                            operacion = False
                        elif opcion == '2':
                            self.transferir()
                            operacion = False
                        elif opcion == '3':
                            self.consultaSaldo()
                            operacion = False
                        elif opcion == '4':
                            self.pagoEnLinea()
                            operacion = False
                        elif opcion == '5':
                            self.consultaCbuCuenta()
                            operacion = False
                        elif opcion == '6':
                            self.extraccion()
                            operacion = False
                        elif opcion == '7':
                            operacion = False
                        elif opcion == '8':
                            operacion = False
                        elif opcion == '9':
                            self.logOut()
                            operacion = True
                            self.logIn()


        elif operaciones == True and usuario.rol == 'Cliente Pyme':
            if self._usuarioConectado in self._cuentas:
                operacion = False
                while operacion == False:
                    print('1. Depositar')
                    print('2. Transferir')
                    print('3. Consultar saldo')
                    print('4. Pago en linea')
                    print('5. Plazo fijo')
                    print('6. Comprar moneda extranjera')
                    print('7. Inversion en bonos')
                    print('8. Pago de sueldos')
                    print('9. Consultar CBU y Nro Cuenta')
                    print('10. Extraccion')
                    print('11. Salir')
                    opcion = input('Igrese el numero de opcion a realizar: ')
                    if opcion == '1':
                        self.depositar()
                        operacion = False
                    elif opcion == '2':
                        self.transferir()
                        operacion = False
                    elif opcion == '3':
                        self.consultaSaldo()
                        operacion = False
                    elif opcion == '4':
                        self.pagoEnLinea()
                        operacion = False
                    elif opcion == '5':
                        operacion = False
                    elif opcion == '6':
                        operacion = False
                    elif opcion == '7':
                        operacion = False
                    elif opcion == '8':
                        operacion = False
                    elif opcion == '9':
                        self.consultaCbuCuenta()
                        operacion = False
                    elif opcion == '10':
                        self.extraccion()
                        operacion = False
                    elif opcion == '11':
                        self.logOut()
                        operacion = True
                        self.logIn()



    #Operaciones validas para caja de ahorros y cta cte
    def depositar(self):
        if self._usuarioConectado.rol == 'Cliente Individuo':
            monto = int(input('Ingrese el monto que desea depositar (numeros enteros sin coma): '))
            print('-----------------------')
            print(f' Su saldo actual es de: {self._cuentas[self._usuarioConectado]._saldo} ')
            deposito = self._cuentas[self._usuarioConectado]._saldo + monto
            self._usuarioConectado.individuo.getCuentasCli()[self._usuarioConectado]._saldo = deposito
            print('-----------------------')
            print(f' Acaba de depositar: {monto} ')
        elif self._usuarioConectado.rol == 'Cliente Pyme':
            monto = int(input('Ingrese el monto que desea depositar (numeros enteros sin coma): '))
            print('-----------------------')
            print(f' Su saldo actual es de: {self._cuentas[self._usuarioConectado]._saldo} ')
            deposito = self._cuentas[self._usuarioConectado]._saldo + monto
            self._usuarioConectado.pyme.getCuentasCli()[self._usuarioConectado]._saldo = deposito
            print('-----------------------')
            print(f' Acaba de depositar: {monto} ')



    def extraccion(self):
        extraccion = int(input('Ingrese el monto que desea extraer (numeros enteros sin coma) :'))
        if self._cuentas[self._usuarioConectado]._tipo == 'Caja de ahorros comun':
            if self._cuentas[self._usuarioConectado]._saldo > extraccion:
                print('-----------------------')
                print(f'Se extraera de su cuenta el importe: {extraccion}')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    extraccion = self._cuentas[self._usuarioConectado]._saldo - extraccion
                    self._cuentas[self._usuarioConectado]._saldo = extraccion
                    print('-----------------------')
                    print('Retire el dinero.')
                else:
                    print('-----------------------')
                    print('La extraccion ah sido cancelada.')
            else:
                print('-----------------------')
                print('No posee fondos suficientes para realizar la extraccion.')
        elif self._cuentas[self._usuarioConectado]._tipo == 'Caja de ahorros de saldo retenido' or self._cuentas[self._usuarioConectado]._tipo == 'Cta cte de saldo retenido':
            if self._cuentas[self._usuarioConectado]._saldo > extraccion and (self._cuentas[self._usuarioConectado]._saldo - extraccion) >= 3000:
                if self._cuentas[self._usuarioConectado]._saldo > extraccion:
                    print('-----------------------')
                    print(f'Se extraera de su cuenta el importe: {extraccion}')
                    confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                    confirmacion = confirmacion.upper()
                    if confirmacion == 'SI':
                        extraccion = self._cuentas[self._usuarioConectado]._saldo - extraccion
                        self._cuentas[self._usuarioConectado]._saldo = extraccion
                        print('-----------------------')
                        print('Retire el dinero.')
                    else:
                        print('-----------------------')
                        print('La extraccion ah sido cancelada.')
                else:
                    print('-----------------------')
                    print('No posee fondos suficientes para realizar la extraccion.')
        elif self._cuentas[self._usuarioConectado]._tipo == 'Cta cte comun':
            if self._cuentas[self._usuarioConectado]._saldo > -10000 and (self._cuentas[self._usuarioConectado]._saldo - extraccion) > -10000:
                print('-----------------------')
                print(f'Se extraera de su cuenta el importe: {extraccion}')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    extraccion = self._cuentas[self._usuarioConectado]._saldo - extraccion
                    self._cuentas[self._usuarioConectado]._saldo = extraccion
                    print('-----------------------')
                    print('Retire el dinero.')
                else:
                    print('-----------------------')
                    print('La extraccion ah sido cancelada.')
            else:
                print('-----------------------')
                print('No posee fondos suficientes para realizar la extraccion.')




    def transferir(self):     #No guarda la transferencia en la cuenta destino
        cuentaAtransferir = int(input('Ingrese el numero de la cuenta a donde desea hacer la transferencia: '))
        transferencia = int(input('Ingrese el monto que desea transferir (numeros enteros sin coma): '))
        if self._cuentas[self._usuarioConectado]._tipo == 'Caja de ahorros comun':
            if self._cuentas[self._usuarioConectado]._saldo > transferencia:
                print('-----------------------')
                print(f'Se debitara de su cuenta el importe: {transferencia} destinado a la cuenta n°: {cuentaAtransferir}')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    transferido = self._cuentas[self._usuarioConectado]._saldo - transferencia
                    self._cuentas[self._usuarioConectado]._saldo = transferido
                    print('-----------------------')
                    print('La transferencia se realizo con exito.')
                else:
                    print('-----------------------')
                    print('La transferencia ah sido cancelada.')
            else:
                print('-----------------------')
                print('No posee fondos suficientes para realizar la transferencia.')

        if self._cuentas[self._usuarioConectado]._tipo == 'Cta cte comun':
            if self._cuentas[self._usuarioConectado]._saldo > -10000 and (self._cuentas[self._usuarioConectado]._saldo - transferencia) > -10000:
                print('-----------------------')
                print(f'Se debitara de su cuenta el importe: {transferencia} destinado a la cuenta n°: {cuentaAtransferir}')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    transferido = self._cuentas[self._usuarioConectado]._saldo - transferencia
                    self._cuentas[self._usuarioConectado]._saldo = transferido
                    print('-----------------------')
                    print('La transferencia se realizo con exito.')
                else:
                    print('-----------------------')
                    print('La transferencia ah sido cancelada.')
            else:
                print('-----------------------')
                print('No posee fondos suficientes para realizar la transferencia.')

        elif self._cuentas[self._usuarioConectado]._tipo == 'Caja de ahorros de saldo retenido' or self._cuentas[self._usuarioConectado]._tipo == 'Cta cte de saldo retenido':
            if self._cuentas[self._usuarioConectado]._saldo > transferencia and (self._cuentas[self._usuarioConectado]._saldo - transferencia) >= 3000:
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    transferido = self._cuentas[self._usuarioConectado]._saldo - transferencia
                    self._cuentas[self._usuarioConectado]._saldo = transferido
                    print('-----------------------')
                    print('La transferencia se realizo con exito.')
                else:
                    print('-----------------------')
                    print('La transferencia ah sido cancelada.')
            else:
                print('-----------------------')
                print('No posee fondos suficientes para realizar la transferencia.')




    def consultaSaldo(self):
        print('-----------------------')
        print(f' Su saldo actual es de: {self._cuentas[self._usuarioConectado]._saldo} ')



    def pagoEnLinea(self):
        servicio = input('Ingrese el nombre del servicio que desea pagar: ')
        montoApagar = int(input('Ingrese el monto a pagar (numeros enteros sin coma): '))
        if self._cuentas[self._usuarioConectado]._tipo == 'Caja de ahorros de saldo retenido' or self._cuentas[self._usuarioConectado]._tipo == 'Cta cte de saldo retenido':
            if self._cuentas[self._usuarioConectado]._saldo > montoApagar and (self._cuentas[self._usuarioConectado]._saldo - montoApagar) >= 3000:
                print('-----------------------')
                print(f'Se debitara de su cuenta el importe: {montoApagar} en concepto de pago de: {servicio}')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    pago = self._cuentas[self._usuarioConectado]._saldo - montoApagar
                    self._cuentas[self._usuarioConectado]._saldo = pago
                    print('-----------------------')
                    print('El pago se realizo con exito.')
                else:
                    print('-----------------------')
                    print('El pago de servicio ah sido cancelado.')
            else:
                print('-----------------------')
                print('No posee fondos suficientes para realizar el pago.')
        elif self._cuentas[self._usuarioConectado]._tipo == 'Caja de ahorros comun':
            if self._cuentas[self._usuarioConectado]._saldo > montoApagar:
                print('-----------------------')
                print(f'Se debitara de su cuenta el importe: {montoApagar} en concepto de pago de: {servicio}')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    pago = self._cuentas[self._usuarioConectado]._saldo - montoApagar
                    self._cuentas[self._usuarioConectado]._saldo = pago
                    print('-----------------------')
                    print('El pago se realizo con exito.')
                else:
                    print('-----------------------')
                    print('El pago de servicio ah sido cancelado.')
            else:
                print('-----------------------')
                print('No posee fondos suficientes para realizar el pago.')
        elif self._cuentas[self._usuarioConectado]._tipo == 'Cta cte comun':
            if self._cuentas[self._usuarioConectado]._saldo > montoApagar and (self._cuentas[self._usuarioConectado]._saldo - montoApagar) >= -10000:
                print('-----------------------')
                print(f'Se debitara de su cuenta el importe: {montoApagar} en concepto de pago de: {servicio}')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    pago = self._cuentas[self._usuarioConectado]._saldo - montoApagar
                    self._cuentas[self._usuarioConectado]._saldo = pago
                    print('-----------------------')
                    print('El pago se realizo con exito.')
                else:
                    print('-----------------------')
                    print('El pago de servicio ah sido cancelado.')
            else:
                print('-----------------------')
                print('No posee fondos suficientes para realizar el pago.')




    def consultaCbuCuenta(self):
        print('-----------------------')
        print(f'Su cbu es: \t{self._cuentas[self._usuarioConectado]._cbu} \n Su nro de cuente es: {self._cuentas[self._usuarioConectado]._nroCuenta}')



    #Operacion validas solo para cta cte
    def plazoFijo(self):
        pass
    
    #dfsfgsgf

    # Operacion validas solo para cta cte
    def compraMonedaExtranjera(self):
        pass

    # Operacion validas solo para cta cte
    def inversionBonos(self):
        pass

    # Operacion validas solo para cta cte
    def pagoSueldos(self):
        pass



    def crearCuenta(self):
        if self._usuarioConectado.rol == 'Cliente Individuo':
            cuenta = False
            while cuenta == False:
                print('1. Crear Caja de ahorro')
                print('2. Crear Cuenta corriente')
                opcion = input('Ingrese la opcion deseada: ')
                if opcion == '1':
                    sucursal = self._sucursal
                    fechaApertura = datetime.now()
                    saldo = 0
                    tipo = input('Elija si desea 1 cuenta COMUN o 2 cuenta de SALDO RETENIDO:')
                    if tipo == '1':
                        tipo = 'Caja de ahorros comun'
                        saldoRetenido = None
                        cta = CajaDeAhorros(sucursal, fechaApertura, saldo, tipo, saldoRetenido)
                        self._cuentas[self._usuarioConectado] = cta
                        self._usuarioConectado.individuo._cuentas[self._usuarioConectado] = cta
                        print('-----------------------')
                        print('Su cuenta ah sido creada con exito. Gracias.')
                        self.menuOperacionesCliente()
                        cuenta = True

                    else:
                        tipo = 'Caja de ahorros de saldo retenido'
                        saldoRetenido = 3000
                        cta = CajaDeAhorros(sucursal, fechaApertura, saldo, tipo, saldoRetenido)
                        self._cuentas[self._usuarioConectado] = cta
                        self._usuarioConectado.individuo._cuentas[self._usuarioConectado] = cta
                        print('-----------------------')
                        print('Su cuenta ah sido creada con exito. Gracias.')
                        self.menuOperacionesCliente()
                        cuenta = True

                elif opcion == '2':
                    sucursal = self._sucursal
                    fechaApertura = datetime.now()
                    saldo = 0
                    tipo = input('Elija si desea 1 cuenta COMUN o 2 cuenta de SALDO RETENIDO:')
                    if tipo == '1':
                        tipo = 'Cta cte comun'
                        saldoRetenido = None
                        descubierto = None
                        cta = CtaCte(descubierto, sucursal, fechaApertura, saldo, tipo, saldoRetenido)
                        self._cuentas[self._usuarioConectado] = cta
                        self._usuarioConectado.individuo._cuentas[self._usuarioConectado] = cta
                        print('-----------------------')
                        print('Su cuenta ah sido creada con exito. Gracias.')
                        self.menuOperacionesCliente()
                        cuenta = True

                    else:
                        tipo = 'Cta cte de saldo retenido'
                        saldoRetenido = 3000
                        descubierto = None
                        cta = CtaCte(descubierto, sucursal, fechaApertura, saldo, tipo, saldoRetenido)
                        self._cuentas[self._usuarioConectado] = cta
                        self._usuarioConectado.individuo._cuentas[self._usuarioConectado] = cta
                        print('-----------------------')
                        print('Su cuenta ah sido creada con exito. Gracias.')
                        self.menuOperacionesCliente()
                        cuenta = True

        else:
            print('Crear cuenta corriente')
            sucursal = self._sucursal
            fechaApertura = datetime.now()
            saldo = 0
            tipo = input('Elija si desea 1 cuenta COMUN o 2 cuenta de SALDO RETENIDO:')
            if tipo == '1':
                descubierto = 10000
                tipo = 'Cta cte comun'
                saldoRetenido = None
                cta = CtaCte(descubierto, sucursal, fechaApertura, saldo, tipo, saldoRetenido)
                self._cuentas[self._usuarioConectado] = cta
                self._usuarioConectado.pyme._cuentas[self._usuarioConectado] = cta
                print('-----------------------')
                print('Su cuenta ah sido creada con exito. Gracias.')
                self.menuOperacionesCliente()
                cuenta = True
            else:
                descubierto = None
                tipo = 'Cta cte de saldo retenido'
                saldoRetenido = 3000
                cta = CtaCte(descubierto, sucursal, fechaApertura, saldo, tipo, saldoRetenido)
                self._cuentas[self._usuarioConectado] = cta
                self._usuarioConectado.pyme._cuentas[self._usuarioConectado] = cta
                print('-----------------------')
                print('Su cuenta ah sido creada con exito. Gracias.')
                self.menuOperacionesCliente()
                cuenta = True



    def logIn(self):
        self._conexion = False
        miUsuario = input('Ingrese su nombre de usuario: ')
        miContraseña = input('Ingrese su contraseña: ')
        if miUsuario in self._usuarios and miContraseña == self._usuarios[miUsuario]._contraseña:
            user = self._usuarios.get(miUsuario)
            self._usuarioConectado = user
            self._conexion = True
            if self._conexion == True:
                eleccion = input('Presione 1 para ingresar como administrador, 2 para ingresar como cliente: ')
                if eleccion == '1':
                    if self._usuarioConectado.rol == 'Administrador':
                        operacion = input('Para registrar cliente presione 1, para cargar datos presione 2: ')
                        if operacion == '1':
                            self.registrarCliente()
                        else:
                            self.cargarCostosDeCuentas()
                    elif self._usuarioConectado.rol == 'Cliente Pyme' or self._usuarioConectado.rol == 'Cliente Individuo':
                        print('-----------------------')
                        print('Usted no es administrador, es cliente o no se encuentra registrado')
                        print('El ingreso fallo, intentelo nuevamente.')
                        self.logIn()
                elif eleccion == '2':
                    print('-----------------------')
                    print('Ingreso como cliente')
                    if self._conexion == True:
                        eleccion = input('Si desea crear una cuenta presione 1, si ya posee una cuenta presione 2: ')
                        if eleccion == '1':
                            self.crearCuenta()
                        elif eleccion == '2':
                            for usConectado in self._cuentas:
                                if self._usuarioConectado == usConectado:
                                    self.menuOperacionesCliente()

        else:
            self._intentos += 1
            if self._intentos <= 2:
                print('-----------------------')
                print('Error en el nombre de usuario o contraseña, Intentelo nuevamente: ')
                print(f'Intentos {self._intentos}')
                self.logIn()
            else:
                print('Se acabo el numero de intentos. Adios.')



    def logOut(self):
        if self._conexion:
            print('Se cerro la sesion.')
            self._conexion = False



if __name__ == '__main__':
    print('-----------------------')
    banco1 = Banco()
    print('clave de diccionario usuarios')
    for us in banco1.getUsuarios().keys():
        print(us)

    print('-----------------------')
    print('valores de diccionario usuario')
    for us in banco1.getUsuarios().values():
        print(us)

    print('-----------------------')
    print('clave de diccionario cuentas')
    for us in banco1.getCuentas().keys():
        print(us)

    print('-----------------------')
    print('valor de diccionario cuentas')
    for us in banco1.getCuentas().values():
        print(us)

    print('-----------------------')
    banco1.logIn()

    





from cliente import  Cliente, Individuo, Pyme
from usuarios import Usuario
from administrador import  Admin
from cuentas import Cuenta, CajaDeAhorros, CtaCte
from datetime import datetime
from secuencia import Secuencias



class Banco():
    def __init__(self, sucursal=None, direccion=None):
        self._sucursal = sucursal
        self._direccion = direccion
        self._admin = {}
        self._clientes = {}
        self._usuarios = {}
        self._cuentas = {}
        self._datosCli = {}
        self._costosCjaAhorros = {'mantenimiento' : 200, 'transferencias' : 5, 'depositos' : 5, 'pagosEnLinea' : 3}
        self._costosCjaSR = {'mantenimiento' : 0, 'transferencias' : 0, 'depositos' : 0, 'pagosEnLinea' : 0}
        self._costosCtaCte = {'mantenimiento' : 500, 'transferencias' : 5, 'depositos' : 5, 'pagosEnLinea' : 3}
        self._costosCtaSR = {'mantenimiento' : 0, 'transferencias' : 0, 'depositos' : 0, 'pagosEnLinea' : 0}
        self._tipoCambio = 200
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
        usUser1 = Usuario('ADM', 'ADM123', 'Administrador')
        self._admin[user.getId()] = user
        self._usuarios[usUser1.usuario] = usUser1

        #creando cliente1
        cliente1 = Individuo('Juan', 'Perez', 33, 33543829, 'jperez@mail.com', 'dinamarca 641', 24940303456)
        usCliente1 = Usuario('jp', 'jp123', 'Cliente Individuo')
        self._usuarios[usCliente1.usuario] = usCliente1
        CBU = Secuencias.getNroCbu()
        CTA = Secuencias.getNroCuenta()
        cta = CajaDeAhorros(self._sucursal, CBU, CTA, datetime.now(), 0, 'Caja de ahorros comun', None)
        self._cuentas[usCliente1] = cta
        self._clientes[CBU] = usCliente1
        self._datosCli[CBU] = cliente1


        #creando cliente2
        cliente2 = Individuo('Raul', 'Gonzales', 38, 27543869, 'rgonzales@mail.com', 'las heras 641', 24944560303)
        usCliente2 = Usuario('rg', 'rg123', 'Cliente Individuo')
        self._usuarios[usCliente2.usuario] = usCliente2
        CBU = Secuencias.getNroCbu()
        CTA = Secuencias.getNroCuenta()
        cta = CtaCte(None, self._sucursal, CBU, CTA, datetime.now(), 0, 'Cta cte de saldo retenido', 3000)
        self._cuentas[usCliente2] = cta
        self._clientes[CBU] = usCliente2
        self._datosCli[CBU] = cliente2

        #creando cliente3
        cliente3 = Pyme('La Super', '30-71495333-5', 'lasuper@mail.com', 'Rauch 1234', 2494219282)
        usCliente3 = Usuario('ls', 'ls123', 'Cliente Pyme')
        self._usuarios[usCliente3.usuario] = usCliente3
        CBU = Secuencias.getNroCbu()
        CTA = Secuencias.getNroCuenta()
        cta = CtaCte(10000, self._sucursal, CBU, CTA, datetime.now(), 0, 'Cta cte comun', None)
        self._cuentas[usCliente3] = cta
        self._clientes[CBU] = usCliente3
        self._datosCli[CBU] = cliente3

        #creando cliente4
        cliente4 = Pyme('La EFE', '30-72436789-5', 'laefe@mail.com', 'Darragueira 525', 2494219282)
        usCliente4 = Usuario('le', 'le123', 'Cliente Pyme')
        self._usuarios[usCliente4.usuario] = usCliente4
        CBU = Secuencias.getNroCbu()
        CTA = Secuencias.getNroCuenta()
        cta = CtaCte(None, self._sucursal, CBU, CTA, datetime.now(), 0, 'Cta cte de saldo retenido', 3000)
        self._cuentas[usCliente4] = cta
        self._clientes[CBU] = usCliente4
        self._datosCli[CBU] = cliente4



    #metodos utilizado solo por el administrador
    def cargarCostosDeCuentas(self):
        usuario = self._usuarioConectado
        operacion = False
        if usuario.rol == 'Administrador':
            while operacion == False:
                print('----------------------')
                print('1. Cargar o Modificar costos en Caja de Ahorros')
                print('2. Cargar o Modificar costos en Cuenta Corriente')
                print('3. Registrar un cliente')
                print('4. Registrar una cuenta')
                print('5. Salir')

                eleccion = input('Ingrese el numero de la operacion que desea realizar: ')
                if eleccion == '1':
                    modificacion = True
                    while modificacion == True:
                        print('1. mantenimiento mensual')
                        print('1. transferencias')
                        print('3. depositos')
                        print('4. pagos en linea')
                        print('5. salir')
                        numero = input('Presione el numero de la opcion deseada: ')
                        if numero == '1':
                            self._costosCjaAhorros['mantenimiento'] = int(input('Ingrese el costo: '))
                            modificacion = True
                        elif numero == '2':
                            self._costosCjaAhorros['transferencias'] = int(input('Ingrese el costo: '))
                            modificacion = True
                        elif numero == '3':
                            self._costosCjaAhorros['depositos'] = int(input('Ingrese el costo: '))
                            modificacion = True
                        elif numero == '4':
                            self._costosCjaAhorros['pagosEnLinea'] = int(input('Ingrese el costo: '))
                            modificacion = True
                        elif numero == '5':
                            self.cargarCostosDeCuentas()
                            modificacion = False
                        else:
                            print('El numero ingresado no es valido.')
                            modificacion = True
                elif eleccion == '2':
                    modificacion = True
                    while modificacion == True:
                        print('1. mantenimiento mensual')
                        print('1. transferencias')
                        print('3. depositos')
                        print('4. pagos en linea')
                        print('5. salir')
                        numero = input('Presione el numero de la opcion deseada: ')
                        if numero == '1':
                            self._costosCjaAhorros['mantenimiento'] = int(input('Ingrese el costo: '))
                            modificacion = True
                        elif numero == '2':
                            self._costosCjaAhorros['transferencias'] = int(input('Ingrese el costo: '))
                            modificacion = True
                        elif numero == '3':
                            self._costosCjaAhorros['depositos'] = int(input('Ingrese el costo: '))
                            modificacion = True
                        elif numero == '4':
                            self._costosCjaAhorros['pagosEnLinea'] = int(input('Ingrese el costo: '))
                            modificacion = True
                        elif numero == '5':
                            self.cargarCostosDeCuentas()
                            modificacion = False
                        else:
                            print('El numero ingresado no es valido.')
                            modificacion = True
                elif eleccion == '3':
                    self.registrarCliente()
                elif eleccion == '4':
                    self.crearCuenta()
                elif eleccion == '5':
                    self.logOut()
                    operacion = True
                    self.logIn()
                else:
                    print('El numero elegido es incorrecto, vuelva a intentarlo')
                    operacion = False



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
                usuario = input('Ingrese un nombre de usuario: ')
                contraseña = input('Ingrese una contraseña: ')
                rol = 'Cliente Individuo'
                user = Usuario(usuario, contraseña, rol)
                self._usuarios[user.usuario] = user


            if opcion == '2':
                razonSocial = input('Ingrese la razon social: ')
                cuit = input('Ingrese su CUIT: ')
                mail = input('Ingrese su mail: ')
                direccion = input('Ingrese su direccion: ')
                telefono = input('Ingrese su telefono: ')
                cliente = Pyme(razonSocial, cuit, mail, direccion, telefono)
                usuario = input('Ingrese un nombre de usuario: ')
                contraseña = input('Ingrese una contraseña: ')
                rol = 'Cliente Pyme'
                user = Usuario(usuario, contraseña, rol)
                self._usuarios[user.usuario] = user

            if opcion == '3':
                self.logOut()
                registro = True
                self.logIn()



    def menuOperacionesCliente(self):
        usuario = self._usuarioConectado
        if usuario.rol == 'Cliente Individuo':
            opTipoCuenta = input('Presione 1 para operar con CAJA DE AHORROS y 2 para operar con CUENTA CORRIENTE: ')
            if opTipoCuenta == '1':
                if usuario in self._cuentas and self._cuentas[usuario]._tipo == 'Caja de ahorros comun' or self._cuentas[usuario]._tipo == 'Caja de ahorros de saldo retenido':
                    operacion = False
                    while operacion == False:
                        print('1. Depositar')
                        print('2. Transferir')
                        print('3. Consultar saldo')
                        print('4. Pago en linea')
                        print('5. Consultar CBU y Nro Cuenta')
                        print('6. Extraccion')
                        print('7. Salir')
                        opcion = input('Ingrese el numero de opcion a realizar: ')
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
                            print('El numero ingresado es incorrecto vuelva a intentarlo.')
                            operacion = False
                else:
                    print('-----------------------')
                    print('Usted no posee una caja de ahorros o ingreso un numero incorrecto, por favos vuelva a intentarlo.')
                    self.menuOperacionesCliente()
            elif opTipoCuenta == '2':
                if usuario in self._cuentas and self._cuentas[usuario]._tipo == 'Cta cte comun' or self._cuentas[usuario]._tipo == 'Cta cte de saldo retenido':
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
                        opcion = input('Ingrese el numero de opcion a realizar: ')
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
                            self.plazoFijo()
                            operacion = False
                        elif opcion == '8':
                            self.compraMonedaExtranjera()
                            operacion = False
                        elif opcion == '9':
                            self.logOut()
                            operacion = True
                            self.logIn()
                        else:
                            print('El numero ingresado es incorrecto vuelva a intentarlo.')
                            operacion = False
                else:
                    print('Usted no posee una cuenta corriente.')
                    self.menuOperacionesCliente()
            else:
                print('El numero ingresado no es válido.')
                self.menuOperacionesCliente()

        elif usuario.rol == 'Cliente Pyme':
            if usuario in self._cuentas:
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
                    opcion = input('Ingrese el numero de opcion a realizar: ')
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
                        self.plazoFijo()
                        operacion = False
                    elif opcion == '6':
                        self.compraMonedaExtranjera()
                        operacion = False
                    elif opcion == '7':
                        self.inversionBonos()
                        operacion = False
                    elif opcion == '8':
                        self.pagoSueldos()
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
                    else:
                        print('El numero ingresado es incorrecto vuelva a intentarlo.')
                        operacion = False


    #Operaciones validas para caja de ahorros y cta cte
    def depositar(self):
        usuario = self._usuarioConectado
        if usuario.rol == 'Cliente Individuo':
            if usuario in self._cuentas and self._cuentas[usuario]._tipo == 'Caja de ahorros comun':
                monto = int(input('Ingrese el monto que desea depositar (numeros enteros sin coma): '))
                print('-----------------------')
                costo = self._costosCjaAhorros.get('depositos')
                deposito = (self._cuentas[usuario]._saldo + monto) - costo
                self._cuentas[usuario]._saldo = deposito
                print('-----------------------')
                print(f' Acaba de depositar: {monto} y se le descontaran {costo} por costo de operacion.')
            elif usuario in self._cuentas and self._cuentas[usuario]._tipo == 'Caja de ahorros de saldo retenido':
                monto = int(input('Ingrese el monto que desea depositar (numeros enteros sin coma): '))
                print('-----------------------')
                deposito = (self._cuentas[usuario]._saldo + monto)
                self._cuentas[usuario]._saldo = deposito
                print('-----------------------')
                print(f' Acaba de depositar: {monto}')
            elif usuario in self._cuentas and self._cuentas and self._cuentas[usuario]._tipo == 'Cta cte comun':
                monto = int(input('Ingrese el monto que desea depositar (numeros enteros sin coma): '))
                print('-----------------------')
                costo = self._costosCjaAhorros.get('depositos')
                deposito = (self._cuentas[usuario]._saldo + monto) - costo
                self._cuentas[usuario]._saldo = deposito
                print('-----------------------')
                print(f' Acaba de depositar: {monto} y se le descontaran {costo} por costo de operacion.')
            elif usuario in self._cuentas and self._cuentas[usuario]._tipo == 'Cta cte de saldo retenido':
                monto = int(input('Ingrese el monto que desea depositar (numeros enteros sin coma): '))
                print('-----------------------')
                deposito = (self._cuentas[usuario]._saldo + monto)
                self._cuentas[usuario]._saldo = deposito
                print('-----------------------')
                print(f' Acaba de depositar: {monto}')
        elif usuario.rol == 'Cliente Pyme':
            if usuario in self._cuentas and self._cuentas[usuario]._tipo == 'Cta cte comun':
                monto = int(input('Ingrese el monto que desea depositar (numeros enteros sin coma): '))
                print('-----------------------')
                costo = self._costosCjaAhorros.get('depositos')
                deposito = (self._cuentas[usuario]._saldo + monto) - costo
                self._cuentas[usuario]._saldo = deposito
                print('-----------------------')
                print(f' Acaba de depositar: {monto} y se le descontaran {costo} por costo de operacion.')
            elif usuario in self._cuentas and self._cuentas[usuario]._tipo == 'Cta cte de saldo retenido':
                monto = int(input('Ingrese el monto que desea depositar (numeros enteros sin coma): '))
                print('-----------------------')
                deposito = (self._cuentas[usuario]._saldo + monto)
                self._cuentas[usuario]._saldo = deposito
                print('-----------------------')
                print(f' Acaba de depositar: {monto}')



    def extraccion(self):
        usuario = self._usuarioConectado
        extraccion = int(input('Ingrese el monto que desea extraer (numeros enteros sin coma) :'))
        if self._cuentas[usuario]._tipo == 'Caja de ahorros comun':
            if self._cuentas[usuario]._saldo >= extraccion:
                print('-----------------------')
                print(f'Se extraera de su cuenta el importe: {extraccion}')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    extraccion = self._cuentas[usuario]._saldo - extraccion
                    self._cuentas[usuario]._saldo = extraccion
                    print('-----------------------')
                    print('Retire el dinero.')
                else:
                    print('-----------------------')
                    print('La extraccion ah sido cancelada.')
            else:
                print('-----------------------')
                print('No posee fondos suficientes para realizar la extraccion.')
        elif self._cuentas[usuario]._tipo == 'Caja de ahorros de saldo retenido' or self._cuentas[usuario]._tipo == 'Cta cte de saldo retenido':
            if self._cuentas[usuario]._saldo > extraccion and (self._cuentas[usuario]._saldo - extraccion) >= 3000:
                if self._cuentas[usuario]._saldo > extraccion:
                    print('-----------------------')
                    print(f'Se extraera de su cuenta el importe: {extraccion}')
                    confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                    confirmacion = confirmacion.upper()
                    if confirmacion == 'SI':
                        extraccion = self._cuentas[usuario]._saldo - extraccion
                        self._cuentas[usuario]._saldo = extraccion
                        print('-----------------------')
                        print('Retire el dinero.')
                    else:
                        print('-----------------------')
                        print('La extraccion ah sido cancelada.')
                else:
                    print('-----------------------')
                    print('No posee fondos suficientes para realizar la extraccion.')
        elif self._cuentas[usuario]._tipo == 'Cta cte comun':
            if self._cuentas[usuario]._saldo > -10000 and (self._cuentas[usuario]._saldo - extraccion) > -10000:
                print('-----------------------')
                print(f'Se extraera de su cuenta el importe: {extraccion}')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    extraccion = self._cuentas[usuario]._saldo - extraccion
                    self._cuentas[usuario]._saldo = extraccion
                    print('-----------------------')
                    print('Retire el dinero.')
                else:
                    print('-----------------------')
                    print('La extraccion ah sido cancelada.')
            else:
                print('-----------------------')
                print('No posee fondos suficientes para realizar la extraccion.')




    def transferir(self):
        usuario = self._usuarioConectado
        cbu = int(input('Ingrese el numero de CBU/CVU a donde desea hacer la transferencia: '))
        transferencia = int(input('Ingrese el monto que desea transferir (numeros enteros sin coma): '))
        #se almacenan datos del beneficiario para el usuario
        if cbu in self._datosCli:
            for key, value in self._datosCli.items():
                if cbu == key:
                    destino = value
        #se almacenan datos del beneficiario para el banco
        if cbu in self._clientes:
            for key, value in self._clientes.items():
                if cbu == key:
                    beneficiario = value
            print(f'Esta a punto de transferir: {transferencia} pesos al {destino}')
            if self._cuentas[usuario]._tipo == 'Caja de ahorros comun':
                costo = self._costosCjaAhorros.get('transferencias')
                if self._cuentas[usuario]._saldo > (transferencia + costo):
                    print('-----------------------')
                    confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                    confirmacion = confirmacion.upper()
                    if confirmacion == 'SI':
                        aTransferir = self._cuentas[usuario]._saldo - (transferencia + costo)
                        self._cuentas[usuario]._saldo = aTransferir
                        self._cuentas[beneficiario]._saldo += transferencia
                        print('-----------------------')
                        print('La transferencia se realizo con exito.')
                    else:
                        print('-----------------------')
                        print('La transferencia ah sido cancelada.')
                else:
                    print('-----------------------')
                    print('No posee fondos suficientes para realizar la transferencia.')

        if self._cuentas[usuario]._tipo == 'Cta cte comun':
            costo = self._costosCtaCte.get('transferencias')
            if self._cuentas[usuario]._saldo - (transferencia + costo) > -10000:
                print('-----------------------')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    aTransferir = self._cuentas[usuario]._saldo - (transferencia + costo)
                    self._cuentas[usuario]._saldo = aTransferir
                    self._cuentas[beneficiario]._saldo += transferencia
                    print('-----------------------')
                    print('La transferencia se realizo con exito.')
                else:
                    print('-----------------------')
                    print('La transferencia ah sido cancelada.')
            else:
                print('-----------------------')
                print('No posee fondos suficientes para realizar la transferencia.')

        elif self._cuentas[usuario]._tipo == 'Caja de ahorros de saldo retenido' or self._cuentas[usuario]._tipo == 'Cta cte de saldo retenido':
            if (self._cuentas[usuario]._saldo - transferencia) >= 3000:
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    aTransferir = self._cuentas[usuario]._saldo - transferencia
                    self._cuentas[usuario]._saldo = aTransferir
                    self._cuentas[beneficiario]._saldo += transferencia
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
        costo = self._costosCtaCte.get('pagosEnLinea')
        usuario = self._usuarioConectado
        servicio = input('Ingrese el nombre del servicio que desea pagar: ')
        montoApagar = int(input('Ingrese el monto a pagar (numeros enteros sin coma): '))
        if self._cuentas[usuario]._tipo == 'Caja de ahorros de saldo retenido' or self._cuentas[usuario]._tipo == 'Cta cte de saldo retenido':
            if self._cuentas[usuario]._saldo > montoApagar and (self._cuentas[usuario]._saldo - montoApagar) >= 3000:
                print('-----------------------')
                print(f'Se debitara de su cuenta el importe: {montoApagar} en concepto de pago de: {servicio}')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    pago = self._cuentas[usuario]._saldo - montoApagar
                    self._cuentas[usuario]._saldo = pago
                    print('-----------------------')
                    print('El pago se realizo con exito.')
                else:
                    print('-----------------------')
                    print('El pago de servicio ah sido cancelado.')
            else:
                print('-----------------------')
                print('No posee fondos suficientes para realizar el pago.')
        elif self._cuentas[usuario]._tipo == 'Caja de ahorros comun':
            if self._cuentas[usuario]._saldo > montoApagar:
                print('-----------------------')
                print(f'Se debitara de su cuenta el importe: {montoApagar} mas costos de operacion {costo} en concepto de pago de: {servicio}')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    pago = self._cuentas[usuario]._saldo - (montoApagar + costo)
                    self._cuentas[usuario]._saldo = pago
                    print('-----------------------')
                    print('El pago se realizo con exito.')
                else:
                    print('-----------------------')
                    print('El pago de servicio ah sido cancelado.')
            else:
                print('-----------------------')
                print('No posee fondos suficientes para realizar el pago.')
        elif self._cuentas[usuario]._tipo == 'Cta cte comun':
            if self._cuentas[usuario]._saldo > montoApagar and (self._cuentas[usuario]._saldo - montoApagar) >= -10000:
                print('-----------------------')
                print(f'Se debitara de su cuenta el importe: {montoApagar} mas costos de operacion {costo} en concepto de pago de: {servicio}')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    pago = self._cuentas[usuario]._saldo - (montoApagar + costo)
                    self._cuentas[usuario]._saldo = pago
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
        usuario = self._usuarioConectado
        print('Usted esta por realizar un nuevo plazo fijo')
        montoAplazoFijo = int(input('Ingrese el monto a destinar para el plazo fijo: '))
        duracionPlazoFijo = int(input('Ingrese los dias para realizar el plazo fijo: '))
        ganancia = 0 
        if self._cuentas[usuario]._tipo == 'Cta cte comun':                                                                                      ##
            if self._cuentas[usuario]._saldo >= 1000 and montoAplazoFijo >= 1000 and duracionPlazoFijo == 30:
                print(f'Usted esta por realizar un plazo fijo a 30 dias')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    ganancia = montoAplazoFijo * 0.10
                    saldoRestante = self._cuentas[usuario]._saldo - montoAplazoFijo
                    self._cuentas[usuario]._saldo = saldoRestante
                    print('Felicidades, USTED ha realizado un plazo fijo con exito.')
                    print(f'Obtiene una ganancia de: {ganancia}')
                else:
                    print('-----------------------')
                    print('El plazo fijo a 30 dias ha sido cancelado.')
                    self.menuOperacionesCliente()
            elif self._cuentas[usuario]._saldo >= 1000 and montoAplazoFijo >= 1000 and duracionPlazoFijo == 60:
                print('Usted esta por realizar un plazo fijo a 60 dias')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    ganancia = montoAplazoFijo * 0.20
                    saldoRestante = self._cuentas[usuario]._saldo - montoAplazoFijo
                    self._cuentas[usuario]._saldo = saldoRestante
                    print('Felicidades, USTED ha realizado un plazo fijo con exito.')
                    print(f'Obtiene una ganancia de: {ganancia}')
                else:
                    print('-----------------------')
                    print('El plazo fijo a 60 dias ha sido cancelado.')
                    self.menuOperacionesCliente()
            elif self._cuentas[usuario]._saldo >= 1000 and montoAplazoFijo >= 1000 and duracionPlazoFijo == 90:
                print('Usted esta por realizar un plazo fijo a 90 dias')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    ganancia = montoAplazoFijo * 0.30
                    saldoRestante = self._cuentas[usuario]._saldo - montoAplazoFijo
                    self._cuentas[usuario]._saldo = saldoRestante
                    print('Felicidades, USTED ha realizado un plazo fijo con exito.')
                    print(f'Obtiene una ganancia de: {ganancia}')
                else:
                    print('-----------------------')
                    print('El plazo fijo a 90 dias ha sido cancelado.')
                    self.menuOperacionesCliente()
            else:
                print('Fondos Insuficientes en su cuenta - Recuerde que el monto minimo para realizar un plazo fijo es de $ 1000.')
                self.menuOperacionesCliente()
        else:
            print('Usted debe poseer cta cte para poder realizar un plazo fijo.')
    


    # Operacion validas solo para cta cte
    def compraMonedaExtranjera(self):
        usuario = self._usuarioConectado
        print('Usted va a comprar moneda extranjera - Compra minima 100USD')
        montoAcomprar = int(input('Ingrese el monto que desea comprar en USD: '))
        conversionDia = self._tipoCambio
        montoMinimoUSD = 100
        if self._cuentas[usuario]._tipo == 'Cta cte comun' or self._cuentas[usuario]._tipo == 'Cta cte de saldo retenido':
            conversion = montoAcomprar * conversionDia
            if montoAcomprar >= montoMinimoUSD and self._cuentas[usuario]._saldo >= conversion:
                print(f'Se debitara de su cuenta el importe: {conversion} destinado al cambio de divisas')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    saldoFinal = self._cuentas[usuario]._saldo - conversion
                    self._cuentas[usuario]._saldo = saldoFinal
                    print('-------------')
                    print(f'La conversion se ha realizado con Exito. Compro {montoAcomprar} y se debitaron {conversion} de su cuenta')
                
            else:
                print('-------------')
                print('Usted no dispone del monto minimo equivalente a 100 USD para realizar la operacion')
        else:
            print('Usted debe tener una cta cte para operar con Moneda Extranjera')

    # Operacion validas solo para cta cte
    def inversionBonos(self):
        usuario = self._usuarioConectado
        if usuario.rol == 'Cliente Pyme':
            print('Usted invertira en Bonos Argentinos - tenga en cuenta que 1 bono cotiza a 18 USD')
            cantidadBonos = int(input('Ingrese la cantidad de bonos a comprar para invertir: '))
            pesosAconvertir = cantidadBonos * 18
            if self._cuentas[usuario]._saldo >= pesosAconvertir:
                print(f'Se debitara de su cuenta el importe: {pesosAconvertir} destinado a la compra de bonos para operar.')
                activosLiquidos = self._cuentas[usuario]._saldo - pesosAconvertir
                self._cuentas[usuario]._saldo = activosLiquidos
                print('-------------')
                print(f'La compra de bonos se ha realizado con Exito. Compro {cantidadBonos} y se debitaron {pesosAconvertir} de su cuenta')
            else:
                print('-------------')
                print('Usted no dispone los fondos necesarios para realizar la operacion.')
        else:
            ('Usted debe ser Cliente Pyme para poder operar con bonos.')

    # Operacion validas solo para cta cte
    def pagoSueldos(self):
        usuario = self._usuarioConectado
        if usuario.rol == 'Cliente Pyme':
            print('Usted va a depositar los haberes a un empleado')
            pagoSueldo = int(input('Ingrese el monto a pagar: '))
            cbuCuentaDestino = int(input('Ingrese el cbu de la cuenta destino: '))
            if cbuCuentaDestino in self._datosCli:
                for key, value in self._datosCli.items():
                    if cbuCuentaDestino == key:
                        destino = value
            if self._cuentas[usuario]._saldo >= pagoSueldo:
                print(f'Se debitara de su cuenta el importe: {pagoSueldo} destinado al deposito del sueldo del empleado cbu: {cbuCuentaDestino}')
                confirmacion = input('Ingrese SI para confirmar o NO para cancelar: ')
                confirmacion = confirmacion.upper()
                if confirmacion == 'SI':
                    saldoRestante = self._cuentas[usuario]._saldo - pagoSueldo
                    self._cuentas[usuario]._saldo = saldoRestante
                    self._cuentas[destino]._saldo += pagoSueldo
                    print(f'Usted ha realizado el pago de haberes con exito. Su saldo restante es de {saldoRestante}')
                else:
                    print('La operacion ha sido cancelada.')
            else:
                print('----------')
                print('Usted no dispone de fondos para realizar el pago de sueldos.')
        else:
            print('--------')
            print('Usted no es Cliente Pyme. No puede continuar con la operacion.')


    def crearCuenta(self):
        usuario = self._usuarioConectado
        if usuario.rol == 'Cliente Individuo':
            cuenta = False
            while cuenta == False:
                print('1. Crear Caja de ahorro')
                print('2. Crear Cuenta corriente')
                opcion = input('Ingrese la opcion deseada: ')
                if opcion == '1':
                    sucursal = self._sucursal
                    cbu = Secuencias.siguienteNroCbu()
                    cta = Secuencias.siguienteNroCuenta()
                    fechaApertura = datetime.now()
                    saldo = 0
                    tipo = input('Elija si desea 1 cuenta COMUN o 2 cuenta de SALDO RETENIDO:')
                    if tipo == '1':
                        tipo = 'Caja de ahorros comun'
                        saldoRetenido = None
                        cta = CajaDeAhorros(sucursal, cbu, cta, fechaApertura, saldo, tipo, saldoRetenido)
                        self._cuentas[usuario] = cta
                        print('-----------------------')
                        print('Su cuenta ah sido creada con exito. Gracias.')
                        self.menuOperacionesCliente()
                        cuenta = True

                    elif tipo == '2':
                        tipo = 'Caja de ahorros de saldo retenido'
                        saldoRetenido = 3000
                        cta = CajaDeAhorros(sucursal, cbu, cta, fechaApertura, saldo, tipo, saldoRetenido)
                        self._cuentas[usuario] = cta
                        print('-----------------------')
                        print('Su cuenta ah sido creada con exito. Gracias.')
                        self.menuOperacionesCliente()
                        cuenta = True
                    else:
                        print('El numero ingresado no es válido.')
                        self.logIn()

                elif opcion == '2':
                    sucursal = self._sucursal
                    cbu = Secuencias.siguienteNroCbu()
                    cta = Secuencias.siguienteNroCuenta()
                    fechaApertura = datetime.now()
                    saldo = 0
                    tipo = input('Elija si desea 1 cuenta COMUN o 2 cuenta de SALDO RETENIDO:')
                    if tipo == '1':
                        tipo = 'Cta cte comun'
                        saldoRetenido = None
                        descubierto = None
                        cta = CtaCte(descubierto, sucursal, cbu, cta, fechaApertura, saldo, tipo, saldoRetenido)
                        self._cuentas[usuario] = cta
                        print('-----------------------')
                        print('Su cuenta ah sido creada con exito. Gracias.')
                        self.menuOperacionesCliente()
                        cuenta = True

                    elif tipo == '2':
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
                        print('El numero ingresado no es válido.')
                        self.logIn()

        else:
            print('Crear cuenta corriente')
            sucursal = self._sucursal
            cbu = Secuencias.siguienteNroCbu()
            cta = Secuencias.siguienteNroCuenta()
            fechaApertura = datetime.now()
            saldo = 0
            tipo = input('Elija si desea 1 cuenta COMUN o 2 cuenta de SALDO RETENIDO:')
            if tipo == '1':
                descubierto = 10000
                tipo = 'Cta cte comun'
                saldoRetenido = None
                cta = CtaCte(descubierto, sucursal, cbu, cta, fechaApertura, saldo, tipo, saldoRetenido)
                self._cuentas[usuario] = cta
                print('-----------------------')
                print('Su cuenta ah sido creada con exito. Gracias.')
                self.menuOperacionesCliente()
                cuenta = True
            elif tipo == '2':
                descubierto = None
                tipo = 'Cta cte de saldo retenido'
                saldoRetenido = 3000
                cta = CtaCte(descubierto, sucursal, fechaApertura, saldo, tipo, saldoRetenido)
                self._cuentas[usuario] = cta
                print('-----------------------')
                print('Su cuenta ah sido creada con exito. Gracias.')
                self.menuOperacionesCliente()
                cuenta = True
            else:
                print('El numero ingresado no es válido')
                self.logIn()


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
                        operacion = input('Para registrar cliente presione 1 \n para cargar datos presione 2 \n para crear una cuenta presione 3: ')
                        if operacion == '1':
                            self.registrarCliente()
                        elif operacion == '2':
                            self.cargarCostosDeCuentas()
                        elif operacion == '3':
                            self.crearCuenta()
                        else:
                            print('El numero ingresado no es valido.')
                    elif self._usuarioConectado.rol == 'Cliente Pyme' or self._usuarioConectado.rol == 'Cliente Individuo':
                        print('-----------------------')
                        print('Usted no es administrador, es cliente o no se encuentra registrado')
                        print('El ingreso fallo, intentelo nuevamente.')
                        self.logIn()
                elif eleccion == '2':
                    if self._usuarioConectado.rol == 'Cliente Individuo' or self._usuarioConectado.rol == 'Cliente Pyme':
                        print('-----------------------')
                        print('Ingreso como cliente')
                        if self._conexion == True:
                            opcion = input('Si desea crear una cuenta presione 1, si ya posee una cuenta presione 2: ')
                            if opcion == '1':
                                self.crearCuenta()
                            elif opcion == '2':
                                for key, value in self._clientes.items():
                                    if self._usuarioConectado == value:
                                        self.menuOperacionesCliente()
                            else:
                                print('Ingreso una opcion no válida')
                                self.logIn()
                    else:
                        print('Usted no es cliente, vuelva a intentarlo.')
                        self.logIn()
                else:
                    print('El numero ingresado no es válido.')
                    self.logIn()
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
    print('clave de diccionario clientes')
    for us in banco1.getClientes().keys():
        print(us)

    print('-----------------------')
    print('valor de diccionario clientes')
    for us in banco1.getClientes().values():
        print(us)
    print('-----------------------')

    banco1.logIn()

    





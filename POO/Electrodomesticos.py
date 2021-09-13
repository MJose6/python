'''Modelar la resolución del siguiente problema mediante el paradigma de POO
• Se debe registrar información de los dispositivos electrónicos de un hogar.
• Los dispositivos pueden ser electrodomésticos o maquinarias.
• Los electrodomésticos pueden utilizarse para el trabajo de las personas, que se dedican
al rubro de la gastronomía (por ejemplo batidora, horno eléctrico, etc) o para las tareas
del hogar (por ejemplo lavarropas, aspiradora).
• Las maquinaria puede usarse para el trabajo (por ejemplo envasadora, enbotelladora) o
para las tareas del hogar (por ejemplo máquina de cortar pasto).
• Cada dispositivo tiene un número de serie, una descripción, una marca y un tipo que
determina el consumo de electricidad en kilovatios-hora.
• Las maquinarias tienen un valor y una cantidad de años de amortización, para calcular el
monto de la amortización anual.
• El sistema debe permitir:
  Registrar los electrodomésticos de la casa y sacar el consumo de kilovatios-hora
total en caso que todos operaran juntos y el consumo de kilovatios-hora por tipo de
dispositivo.
  Registrar las maquinarias de la casa y calcular la amortización anual total de las
maquinas.
  Imprimir el listado de dispositivos.'''




class DispositivosElectronicos():
    
    def __init__(self, numeroSerie, descripcion, marca, horasUso, kwatt):
        self._numeroSerie = numeroSerie
        self._descripcion = descripcion
        self._marca = marca
        self._horasUso = horasUso
        self._kwatt = kwatt

    def __str__(self):
        return f'Numero de serie: {self._numeroSerie} - Descripcion: {self._descripcion} - Marca: {self._marca} - Consumo: {self._horasUso * self._kwatt} '


class Electrodomesticos(DispositivosElectronicos):

    def __init__(self, tipo, _numeroSerie, _descripcion, _marca, _horasUso, _kwatt):
        super().__init__(_numeroSerie, _descripcion, _marca, _horasUso, _kwatt)
        self._tipo = tipo

    def __str__(self):
        return f'Tipo: {self._tipo} - {super().__str__()}'


aspiradora = Electrodomesticos("Casero","1549992", "Aspiradora", "Atma", 6, 15)
print(aspiradora)
hidroLavadora = Electrodomesticos('maquinaria', '25482933', 'Lavado industrial', 'Philips', 7, 22)
print(hidroLavadora)

#Posible uso
'''class Maquinarias(DispositivosElectronicos):

    def __init__(self, anioCompra, valor):
        self._anioCompra = anioCompra
        self._valor = valor

'''
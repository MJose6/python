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
    
    def __init__(self, numeroSerie, descripcion, marca, tipo, horasUso, kWatt):
      self._numeroSerie = numeroSerie
      self._descripcion = descripcion
      self._marca = marca
      self._tipo = tipo
      self._horasUso = horasUso
      self._kWatt = kWatt

    @property
    def numeroSerie(self):
      return self._numeroSerie

    @numeroSerie.setter
    def numeroSerie(self, numeroSerie):
      self._numeroSerie = numeroSerie

    @property
    def descripcion(self):
      return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
      self._descripcion = descripcion

    @property
    def marca(self):
      return self._marca 

    @marca.setter
    def marca(self, marca):
      self._marca = marca

    @property
    def tipo(self):
      return self.tipo

    @tipo.setter
    def tipo(self, tipo):
      self._tipo = tipo

    @property
    def horasUso(self):
      return self._horasUso

    @horasUso.setter
    def horasUso(self, horasUso):
      self._horasUso = horasUso

    @property
    def kWatt(self):
      return self._kWatt

    @kWatt.setter
    def kWatt(self, kWatt):
      self._kWatt = kWatt   

    def __str__(self):
        return f'Numero de serie: {self._numeroSerie} | Descripcion: {self._descripcion} | Marca: {self._marca} | Tipo: {self._tipo} | Consumo: {self._horasUso * self._kWatt}\n'
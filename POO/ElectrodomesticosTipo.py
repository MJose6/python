from Electrodomesticos import DispositivosElectronicos


class Artefactos:
    def __init__(self, dispositivos):
        self._dispositivos = list(dispositivos)

    def agregarArtefacto(self, dispositivos):
        self._dispositivos.append(dispositivos)
    
    def __str__(self):
        dispositivos_str = ''
        for dispositivo in self._dispositivos:
            dispositivos_str += dispositivo.__str__()
        return f'{dispositivos_str}'
    
    def consumoTotal(self):
        totalHogar = 0
        totalMaquinaria = 0
        for i in dispositivos:
            if self._tipo == 'Hogar':
                totalHogar = totalHogar + self._tipo
            elif self._tipo == 'Maquinaria':
                totalMaquinaria = totalMaquinaria + self._tipo
        return f'Total consumo Hogar: {totalHogar} - Total consumo Maquinarias: {totalMaquinaria}'
   

if __name__ == '__main__':
    aspiradora = DispositivosElectronicos(54673783, 'Aspiradora', 'Atma', 'Hogar', 24, 10)
    batidora = DispositivosElectronicos(24364758, 'Batidora', 'Atma', 'Hogar', 24, 10)
    hornoElectrico = DispositivosElectronicos(90768392, 'Horno', 'Philip', 'Maquinaria', 24, 22)
    lavarropas = DispositivosElectronicos(12672536, 'Lavarropas', 'Dream', 'Hogar', 24, 10)
    envasadora = DispositivosElectronicos(85749323, 'Envasadora', 'Atma', 'Maquinaria', 24, 22)
    enbotelladora = DispositivosElectronicos(10003454, 'Enbotelladora', 'Atma', 'Maquinaria', 24, 22)
    bordeadora = DispositivosElectronicos(22003496, 'Bordeadora', 'Still', 'Hogar/Maquinaria', 24, 15)
    dispositivos = [aspiradora, batidora, hornoElectrico, lavarropas, envasadora, enbotelladora, bordeadora]
    listaDispositivos = Artefactos(dispositivos)
    print(listaDispositivos)
    print(listaDispositivos.consumoTotal())
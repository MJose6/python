#Ejercicio: 1
'''Escribir un programa que lea la información de vacunación por COVD-19 por provincias y 
almacene en estructuras que permitan dar respuestas a las siguientes consultas:
    1. Dada una provincia informar total de vacunas aplicadas, tipo de vacuna con mayor 
    cantidad de aplicaciones, tipo de vacuna con menor cantidad de aplicaciones.
    2. Listar un ranking de las 10 provincias con mayor porcentaje de segundas dosis 
    totales aplicadas
    3. Listar un ranking de las vacunas por mayor porcentaje de segundas dosis totales 
    aplicadas'''

import csv
from typing import KeysView, ValuesView
archivo = open("Covid19VacunasAgrupadas.csv", "r", encoding='utf8')
leerDatos = csv.DictReader(archivo)
datosVacunas = list(leerDatos)

#1.1
vacuna1 = int()
vacuna2 = int()
vacuna3 = int()
vacuna4 = int()
consulta = str(input("Ingrese la provincia a consultar: "))
consulta = consulta.capitalize()
totalizador = 0
for renglon in datosVacunas:
    if renglon['jurisdiccion_nombre'] == consulta:
        dosis1 = int(renglon['primera_dosis_cantidad'])
        dosis2 = int(renglon['segunda_dosis_cantidad'])
        totalVacunas = dosis2 + dosis1
        totalizador = totalizador + totalVacunas
for marcaVacuna in datosVacunas:
    if marcaVacuna["vacuna_nombre"] == "AstraZeneca ChAdOx1 S recombinante":
        vacuna1 = vacuna1 + int(marcaVacuna["primera_dosis_cantidad"])
        vacuna1 = vacuna1 + int(marcaVacuna["segunda_dosis_cantidad"])
    elif marcaVacuna["vacuna_nombre"] == "COVISHIELD ChAdOx1nCoV COVID 19":
        vacuna2 = vacuna2 + int(marcaVacuna["primera_dosis_cantidad"])
        vacuna2 = vacuna2 + int(marcaVacuna["segunda_dosis_cantidad"])
    elif marcaVacuna["vacuna_nombre"] == "Sinopharm Vacuna SARSCOV 2 inactivada":
        vacuna3 = vacuna3 + int(marcaVacuna["primera_dosis_cantidad"])
        vacuna3 = vacuna3 + int(marcaVacuna["segunda_dosis_cantidad"])
    elif marcaVacuna["vacuna_nombre"] == "Sputnik V COVID19 Instituto Gamaleya":
        vacuna4 = vacuna4 + int(marcaVacuna["primera_dosis_cantidad"])
        vacuna4 = vacuna4 + int(marcaVacuna["segunda_dosis_cantidad"])

print(f"El total de vacunas aplicadas en ",consulta,"es de:" ,totalizador)

if vacuna1 > vacuna2 and vacuna1 > vacuna3 and vacuna1 > vacuna4:
    print("La vacuna con MAYOR cantidad de aplicaciones es AstraZeneca ChAdOx1 S recombinante.")
elif vacuna2 > vacuna1 and vacuna2 > vacuna3 and vacuna2 > vacuna4:
    print("La vacuna con MAYOR cantidad de aplicaciones es COVISHIELD ChAdOx1nCoV COVID 19.")
elif vacuna3 > vacuna1 and vacuna3 > vacuna2 and vacuna3 > vacuna4:
    print("La vacuna con MAYOR cantidad de aplicaciones es Sinopharm Vacuna SARSCOV 2 inactivada.")
elif vacuna4 > vacuna1 and vacuna4 > vacuna2 and vacuna4 > vacuna3:
    print("La vacuna con MAYOR cantidad de aplicaciones es Sputnik V COVID19 Instituto Gamaleya.")

if vacuna1 < vacuna2 and vacuna1 < vacuna3 and vacuna1 < vacuna4:
    print("La vacuna con MENOR cantidad de aplicaciones es AstraZeneca ChAdOx1 S recombinante.")
elif vacuna2 < vacuna1 and vacuna2 < vacuna3 and vacuna2 < vacuna4:
    print("La vacuna con MENOR cantidad de aplicaciones es COVISHIELD ChAdOx1nCoV COVID 19.")
elif vacuna3 < vacuna1 and vacuna3 < vacuna2 and vacuna3 < vacuna4:
    print("La vacuna con MENOR cantidad de aplicaciones es Sinopharm Vacuna SARSCOV 2 inactivada.")
elif vacuna4 < vacuna1 and vacuna4 < vacuna2 and vacuna4 < vacuna3:
    print("La vacuna con MENOR cantidad de aplicaciones es Sputnik V COVID19 Instituto Gamaleya.")

#1.2
import operator
provincias = ["Buenos Aires","CABA","Catamarca","Chaco","Chubut","Corrientes","Córdoba","Entre Ríos","Formosa","Jujuy","La Pampa","La Rioja","Mendoza","Misiones","Neuquén","Río Negro","Salta","San Juan","San Luis","Santa Cruz","Santa Fe","Santiago del Estero","Tierra del Fuego","Tucumán"]
provincias2dosis = {}
total = 0
for nombre in provincias:
    for renglon in datosVacunas:
        if renglon["jurisdiccion_nombre"] == nombre:
            total2dosis = float(renglon['segunda_dosis_cantidad'])
            total += total2dosis   
        provincias2dosis[nombre] = total
    
    total = 0
            
total_dosis2 = sum(provincias2dosis.values())

porcentaje2dosis = {}
porcentaje = float()

for clave, valor in provincias2dosis.items():
    porcentaje = round((valor * 100) / total_dosis2, 2)
    porcentaje2dosis[clave] = porcentaje

    porcentaje = 0

porcentajeOrdenado = sorted(porcentaje2dosis.items(), key=operator.itemgetter(1), reverse=True)

provinciasMayorPorcentaje = {}

contador = 10
for prov, porC in porcentajeOrdenado:
    contador -= 1
    provinciasMayorPorcentaje[prov] = porC
    if contador == 0:
        break

print("El rank 10 de las provincias con mayor porcentaje es: " ,provinciasMayorPorcentaje)

#1.3

AstraZeneca = float()
COVISHIELD = float()
Sinopharm = float()
Sputnik = float()


for renglon in datosVacunas:
    if renglon["vacuna_nombre"] == "AstraZeneca ChAdOx1 S recombinante":
            AstraZeneca = AstraZeneca + float(renglon['segunda_dosis_cantidad'])
    elif renglon["vacuna_nombre"] == "COVISHIELD ChAdOx1nCoV COVID 19":
            COVISHIELD = COVISHIELD + float(renglon['segunda_dosis_cantidad'])
    elif renglon["vacuna_nombre"] == "Sinopharm Vacuna SARSCOV 2 inactivada":
            Sinopharm = Sinopharm + float(renglon['segunda_dosis_cantidad'])
    elif renglon["vacuna_nombre"] == "Sputnik V COVID19 Instituto Gamaleya":
            Sputnik = Sputnik + float(renglon['segunda_dosis_cantidad'])

totalNombreVacunas = AstraZeneca + COVISHIELD + Sinopharm + Sputnik

print("La vacuna AstraZeneca ChAdOx1 S recombinante tiene un" ,round(((AstraZeneca*100)/totalNombreVacunas),2), "% de segundas dosis dadas.")
print("La vacuna COVISHIELD ChAdOx1nCoV COVID 19 tiene un" ,round(((COVISHIELD*100)/totalNombreVacunas),2), "% de segundas dosis dadas.")
print("La vacuna Sinopharm Vacuna SARSCOV 2 inactivada tiene un" ,round(((Sinopharm*100)/totalNombreVacunas),2), "% de segundas dosis dadas.")
print("La vacuna Sputnik V COVID19 Instituto Gamaleya tiene un" ,round(((Sputnik*100)/totalNombreVacunas),2), "% de segundas dosis dadas.")



#Ejercicio: 2
'''Escribir un programa que lea un archivo de texto y escriba en otro archivo, una lista con 
las 10 palabras con mayor ocurrencia ordenadas por cantidad de ocurrencias, tener en 
cuenta una lista de palabras ignoradas en el análisis de ocurrencias'''


import operator

resultado = open("resultado.txt", "w")

archivo = open("texto.txt", "r")
palabrasOut = open("palabrasIgnoradas.txt", "w")
leerArchivo = archivo.read()

losSignos = ",.?!"
saltoRenglos = "\n"

for x in range(len(saltoRenglos)):
    leerArchivo = leerArchivo.replace(saltoRenglos[x], " ")
for x in range(len(losSignos)):
    leerArchivo = leerArchivo.replace(losSignos[x], "")


lista = leerArchivo.split(" ")
lista2 = lista
diccPalabras = {}

contador = 0
for palabra in lista:
    for palabra2 in lista2:
        if palabra == palabra2:
            contador += 1
    diccPalabras[palabra] = contador
    contador = 0


diccPalabras = sorted(diccPalabras.items(), key=operator.itemgetter(1), reverse=True)

resultadoFinal = {}
contadorPalabras = 10
for palabra,cantidad in diccPalabras:
    if contadorPalabras > 0:
       resultadoFinal[palabra] = cantidad
       resultado.write(str(palabra))
       resultado.write(str(" "))
       resultado.write(str(cantidad))
       resultado.write(str("\n"))
       contadorPalabras -= 1
    elif contadorPalabras <= 0:
          palabrasOut.write(str(palabra))
          palabrasOut.write(str("="))
          palabrasOut.write(str(cantidad))
          palabrasOut.write(str("\n"))

print(f"Las 10 palabras con mas ocurrencias son : ",resultadoFinal)
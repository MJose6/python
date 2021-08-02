# Comienzo del codigo: lo primero que hacemos es agregar un import csv para poder traer el archivo con el que vamos a trabajar, 
# mediante la funcion open abrimos el archivo de extension csv y posteriormente mediante el DictReader accedemos a los datos que hay dentro de el.
import csv

archivo = open("historico_temperaturas_TpFinal.csv")
lector_datos_temperatura = csv.DictReader(archivo)
datos_temperatura = list(lector_datos_temperatura)

# Paso 2: Empezamos a trabajar con la temperatura donde calcularemos con bucles el promedio anual para la estación verano e invierno y ambos datos serán guardados en listas.

def armar_lista_temperatura(datos,mes1,mes2,mes3):
    promedio = []
    media = 0
    anio = 1991
    for renglon in datos:
      if renglon['mes'] == mes1:
        media += float(renglon['media'])
      elif renglon['mes'] == mes2:
        media += float(renglon['media'])
      elif renglon['mes'] == mes3:
        media += float(renglon['media'])
        promedio_veranos = round(media / 3, 2)
        promedio.append(promedio_veranos)
        anio += 1
        media = 0
    return promedio

# Calculo de temperatura verano...
promedio_temperatura_verano = []
promedio_temperatura_verano = armar_lista_temperatura(datos_temperatura,'Enero','Febrero','Diciembre')

print('Promedios de temperatura anual en ºC de la estación verano desde 1991 a 2020:',' ',promedio_temperatura_verano)

# Agregamos un comando donde pide al usuario la tecla enter para continuar, dandole una mejor visual a la impresion en pantalla.
# (esta accion se verá repetida en varias ocaciones dentro del codigo)

enter = input("presione enter para continuar:")
print(enter)


ppromedio_temperatura_invierno = []
promedio_temperatura_invierno = armar_lista_temperatura(datos_temperatura,'Junio','Julio','Agosto')

print('Promedios de temperatura anual en ºC de la estación invierno desde 1991 a 2020:', ' ',promedio_temperatura_invierno)

enter = input("presione enter para continuar:")
print(enter)

# Repetimos el procedimiento inicial para continuar con nuestros calculos, donde accedemos al archivo .csv y posteriormente obtenemos los valores, 
# en esta ocasion calcularemos las precipitaciones.



# precipitaciones...

archivo1 = open("historico_precipitaciones_TpFinal.csv")
lector_datos_precipitaciones = csv.DictReader(archivo1)
datos_precipitaciones = list(lector_datos_precipitaciones)

# Paso 3: Al igual que en el paso 2 calculamos con bucles los promedios anuales para las estaciones de verano e invierno, que tambien se guardaran en listas.

def armar_lista_precipitaciones(datos,mes1,mes2,mes3):
  promedio = []
  mm = 0
  anio = 1991
  for renglon in datos_precipitaciones:
    if renglon['mes'] == mes1:
      mm += float(renglon['mm'])
    elif renglon['mes'] == mes2:
      mm += float(renglon['mm'])
    elif renglon['mes'] == mes3:
      mm += float(renglon['mm'])
      promedio_precipitaciones = round(mm / 3, 2)
      promedio.append(promedio_precipitaciones)
      anio += 1
      mm = 0
  return promedio

# Calculo de precipitaciones verano...
promedio_precipitaciones_verano = []
promedio_precipitaciones_verano = armar_lista_precipitaciones(datos_precipitaciones,"Diciembre","Enero","Febrero")

print('Promedios del volumen anual de precipitaciones en mm de la estación verano desde 1991 a 2020:', ' ',promedio_precipitaciones_verano)

enter = input("presione enter para continuar:")
print(enter)

# Calculo de precipitaciones invierno...
promedio_precipitaciones_invierno = []
promedio_precipitaciones_invierno = armar_lista_precipitaciones(datos_precipitaciones,"Junio","Julio","Agosto")

print('Promedios del volumen anual de precipitaciones en mm de la estación invierno desde 1991 a 2020:', ' ',promedio_precipitaciones_invierno)

enter = input("presione enter para continuar:")
print(enter)

# Ingresando en la etapa final del codigo, calculamos promedios totales de temperatura y precipitaciones desde 1991 hasta 2020 para las estaciónes de verano e invierno. 
# Logrando establecer si existe relacion entre variables.


# Promedios en verano de temperatura y precipitaciones...
veranos = 0
contador = 0

for renglon in promedio_temperatura_verano:
    veranos += float(renglon)
    contador += 1
    promedio_verano = round(veranos / contador, 2)
print('Temperatura promedio de verano entre el año 1991 y 2020:', promedio_verano, '°C')

veranos = 0
contador = 0

print("           ""--------------------------------")

for renglon in promedio_precipitaciones_verano:
    veranos += float(renglon)
    contador += 1
    precipitaciones_veranos = round(veranos / contador, 2)
print('Precipitaciones promedio de verano entre 1991 y 2020:', precipitaciones_veranos, 'mm')

print("           ""--------------------------------")

# Promedios en invierno de temperatura y precipitaciones...
inviernos = 0
contador = 0

for renglon in promedio_temperatura_invierno:
    inviernos += float(renglon)
    contador += 1
    promedio = round(inviernos / contador, 2)
print('Temperatura promedio de invierno entre 1991 y 2020:', promedio, '°C')

print("           ""--------------------------------")

inviernos = 0
contador = 0

for renglon in promedio_precipitaciones_invierno:
    inviernos += float(renglon)
    contador += 1
    precipitaciones_inviernos = round(inviernos / contador, 2)
print('Precipitaciones promedio de invierno entre 1991 y 2020:', precipitaciones_inviernos, 'mm')

print("           ""--------------------------------")

# Finalmente, por medio de una condicion lógica logramos visualizar en pantalla el resultado y la relacion establecida entre las variables trabajadas.

if promedio <= 15:
    print('La relacion entre las variables es: A menor temperatura,', promedio,
          'vamos a observar un descenso en las precipitaciones', precipitaciones_inviernos, 'mm'',',
          'por el contrario a mayor temperatura,', promedio_verano, 'observamos el ascenso de las precipitaciones',
          precipitaciones_veranos, 'mm')
else:
    print('La relacion entre las variables es: A menor temperatura,', promedio,
          'vamos a observar un ascenso en las precipitaciones', precipitaciones_inviernos, 'mm'',',
          'por el contrario a mayor temperatura,', promedio_verano, 'observamos un descenso de las precipitaciones',
          precipitaciones_veranos, 'mm')
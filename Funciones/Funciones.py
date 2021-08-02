#Ejercicio: 1
'''Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un 
cilindro usando la primera función.'''

import math
def area_circulo (x):
    area = math.pi * (x * x)
    return area

radio = float(input("Ingrese el radio del circulo: "))
area_a_calcular = area_circulo(radio)
print(area_a_calcular)

def volumen_cilindro(y):
    volumen = (area_circulo(radio)*y)
    return volumen

altura = float(input("Ingrese la altura del cilindro: "))
volumen_a_calcular = volumen_cilindro(altura)
print(volumen_a_calcular)


#Ejercicio: 2
''' Escribir una función que reciba una muestra de números en una lista y devuelva su 
media.'''

def promedio(x):
    y = 0
    c = 0
    for i in x:
        y = y + i
        c += 1
    media = y / c
    return media

lista = []
x = int(input("Ingrese un numero: "))

while len(lista) < 4:
  lista.append(x)
  x = int(input("Ingrese un numero: "))
print("La lista a promediar es: ",lista)
media = promedio(lista)
print("El promedio o la media de los numeros ingresados es: ", media)


#Ejercicio: 3
''' Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario 
generado con la función anterior y devuelva una tupla con la palabra más repetida y su 
frecuencia.'''

import operator

def armar_diccionario(x):
    diccionario = {}
    for i in lista:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1

    return diccionario

def armar_tupla(z):
    for i in z.items():
        resultado = sorted(z.items(), key=operator.itemgetter(1), reverse=True)
    
    return resultado


cadena_caracteres = input("Ingrese un texto sin puntos '.' ni comas ';': ")
cadena_caracteres = cadena_caracteres.lower()
lista = cadena_caracteres.split(" ")

diccionario =  armar_diccionario(cadena_caracteres)
print("La cadena de caracteres ingresadas tiene las siguientes palabras, seguidas por su frecuencia: ",diccionario)
        
tupla = armar_tupla(diccionario)
print("Plabras ordenadas de mayor a menor frecuencia: ",tupla)


#Ejercicio: 4
'''Escribir una función que reciba otra función y una lista, y devuelva otra lista con el 
resultado de aplicar la función dada a cada uno de los elementos de la lista.'''


texto = "Estos son ejercicios para Programacion Orientada a Objetos"

def contarCaracteres(x):
    cont = 0
    for i in x:
        cont += 1
    return cont


def listaFinal(x, z):
    caracteres = []
    for i in z:
        caracteres.append(i)
    cantidadCaracteres = contarCaracteres(z)

    return caracteres, cantidadCaracteres

resultado = listaFinal(contarCaracteres, texto)
print("La texto inicial es: ",texto,'\n',"La lista final es separada caracter a caracter y su longitud es: ", resultado)



#Ejercicio: 5
''' Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con
los elementos de la lista que devuelvan True al aplicarles la función booleana.'''

listaEdad = [15, 20, 7, 10, 25, 33]

def booleana(x):
    edad = True
    if x <= 18:
        edad = False
    return edad

def validacion(x):
    apto = []
    noApto = []

    for i in x:
        mayor = booleana(i)
        if mayor == True:
            apto.append(i)
        else:
            noApto.append(i)
    
    return "Los integrantes son mayores, tienen acceso a la pagina:",apto,"Los integrantes son menores no tienen acceso a la pagina:",noApto

resultado = validacion(listaEdad)
print(resultado)
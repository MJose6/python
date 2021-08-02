#Estructura de datos

#Ejercicio 1:  
'''Escribir una función contar(x,y) que cuente cuántas veces aparece un carácter x dado en 
una cadena y.'''

from typing import KeysView


texto = "Estos son ejercicios para Programacion Orientada a Objetos."
texto = texto.lower()
texto = texto.replace("á", "a")
def contarCaracter(x, y):
    c = 0
    for i in x:
        if i == y:
            c += 1
    return c

caracter = contarCaracter(texto, 'a')
print("el caracter aparece", caracter ,"veces")


#Ejercicio 2:  
'''Escribir un programa que decida si hay más letras “A” o más letras “E” en una cadena.'''


texto = "Estos son ejercicios para Programacion Orientada a Objetos."
texto = texto.lower()
texto = texto.replace("á", "a")
texto = texto.replace("é", "e")
c1 = 0
c2 = 0

for i in texto:
    if i == "a":
        c1 += 1
    elif i == "e":
            c2 += 1
print(c1, c2)
if c1 > c2:
    print("Hay mas letras 'a' que letras 'e'")
elif c2 > c1:
    print("Hay mas letras 'e' que letras 'a'")
else:
    print("la cantidad de letras 'a', es igual a la cantidad de letras 'e'.")


#Ejercicio 3:
'''Escribir un programa que cuente cuantas veces aparecen cada una de las vocales en una 
cadena. No importa si la vocal aparece en mayúscula o en minúscula.'''


texto = "Estos son ejercicios para Programacion Orientada a Objetos."
texto = texto.lower()
vocales = ["a", "e", "i", "o", "u"]

for x in vocales:
    veces = 0
    for y in texto:
        if x == y:
            veces += 1
    print("La vocal", x, "aparece", veces, "veces.")

#ejercicio 4:
''' Escribir una función que reciba como parámetro una cadena de palabras separadas por 
espacios y devuelva, como resultado, cuántas palabras de más de cinco letras tiene la 
cadena dada.'''

def cadena_de_palabras(x):
    palabras = x.split(' ')
    c = 0
    for i in palabras:
        if len(i) >= 5:
            c += 1
    return c

cantidad_de_palabras = cadena_de_palabras('Estos son ejercicios para Programacion Orientada a Objetos')
print(cantidad_de_palabras)


#Ejercicio 5:
'''Procesamiento de telegramas. Un oficial de correos decide optimizar el trabajo de su 
oficina cortando todas las palabras de más de cinco letras a sólo cinco letras (e indicando
que una palabra fue cortada con el agregado de una arroba). Por otro lado cobra un valor 
para las palabras cortas y otro valor para las palabras largas (que deben ser cortadas). 
Escribir una función que reciba un texto, la longitud máxima de las palabras, el costo de 
cada palabra corta, el costo de cada palabra larga, y devuelva como resultado el texto del
telegrama y el costo del mismo.'''

telegrama = "Nuestra hija estudiará Frances. Necesitamos dinero para colegiaturas. Tres mil pesos mensuales. Además dos mil pesos este mes para libros. Te extrañamos. Regresa pronto. Jane"
telegrama = telegrama.split(' ')
telegrama_final = []

for i in telegrama:
    i = i[0:5]
    if len(i) == 5:
        i = i+'@'   
        telegrama_final.append(i)
    else:
        telegrama_final.append(i)
    
    telegrama = " ".join(telegrama_final)
#El costo por palabras cortas es de $25 y palabras largas cortadas $35
palabras_cortas = 0
palabras_largas = 0
for i in telegrama_final:
    if len(i) >= 5:
        palabras_largas += 1
    else:
        palabras_cortas += 1

costo_telegrama = (palabras_cortas * 25) + (palabras_largas * 35)

print(telegrama,'.','\n','El valor del telegrama es de $',costo_telegrama)

#Ejercicio: 6
'''Implementar un diccionario Inglés – Español, permitiendo agregar una palabra en inglés 
y su traducción al español, consultar la traducción de una palabra en ambos sentidos 
(inglés a español y español a inglés) contar la cantidad de palabras y mostrar el 
diccionario ordenado de la Z a la A.'''

ingles_espaniol = {
    'hello' : 'hola',
    'phone' : 'telefono',
    'find' : 'encontrar',
    'bad' : 'malo'
}

consulta = True
numero = True

while numero == consulta:
    print("Menú:")
    print("--------")
    print("1. Consultar palabra en ingles")
    print("2. Consultar palabra en español")
    print("3. Agregar palabra al diccionario")
    print("4. Mostrar largo y contenido del diccionario")
    print("5. Ordenar diccionario")
    print("6. Salir")

    opcion = input("Ingrese el numero de opcion del menu: ")

    if opcion == '1':
      palabra = input("Ingrese la palabra a consultar: ")
      diccionario = ingles_espaniol.get(palabra)
      print("{}:{} ".format(palabra, diccionario))
      if palabra not in ingles_espaniol:
          print("La palabra no se encuentra, si desea agregarla presione la opcion 3.")

    elif opcion == '2':
        palabra = input("Ingrese la palabra a consultar: ")
        if palabra in ingles_espaniol.values():
            for i in ingles_espaniol:
                if ingles_espaniol[i] == palabra:
                    print("{}:{}".format(palabra, i))
        if palabra not in ingles_espaniol:
              print("La palabra no se encuentra, si desea agregarla presione la opcion 3.")

    elif opcion == '3':
        palabra = input("Ingrese la palabra a agregar en ingles: ")
        traduccion = input("Ingrese su traduccion al español: ")
        diccionario = ingles_espaniol.setdefault(palabra, traduccion)
        print(ingles_espaniol.items())

    elif opcion == '4':
        print("El largo del diccionario es de: ", len(ingles_espaniol), "palabras.")
        for palabra in ingles_espaniol.items():
            print(palabra[0], ":", palabra[1])

    elif opcion == '5':
        for palabra in sorted(ingles_espaniol.items(), reverse = True):
            print(palabra[0], ":", palabra[1])

    elif opcion == '6':
      numero = False

print("El programa ah finalizado.")

#Ejercicio: 7
'''Implementar una lista de precios que permita grabar el precio de un producto, consultar 
el precio de un producto, consultar todos los productos cuyo precio sea mayor a un valor 
ingresado y mostrar los productos ordenados del más barato al más caro.'''


lista_precios = {
    'jabon' : 10,
    'shampoo' : 25,
    'acondicionador' : 30,
    'papel higienigo' : 12,
    'pasta dental' : 15
}

consulta = True
numero = True

while consulta == numero:
    print("Menú")
    print("--------")
    print("1. Ver catalogo de productos")
    print("2. Cargar producto")
    print("3. Consultar producto")
    print("4. Ordenar productos")
    print("5. Salir")

    opcion = input("Ingrese la opcion deseada: ")

    if opcion == "1":
        print(lista_precios.keys())

    if opcion == "2":
        grabar = input("Ingrese el producto que desea agregar: ")
        precio = input("Ingrese el precio: ")
        producto = lista_precios.setdefault(grabar, precio)
        print(lista_precios.items())

    elif opcion == "3":
        producto_a_consultar = input("Ingrese el nombre del producto que desea consultar: ")
        producto = lista_precios.get(producto_a_consultar)
        print("{},{}".format(producto_a_consultar, producto))
        if producto_a_consultar not in lista_precios:
            print("EL producto seleccionado no se encuentra, si desea cargarlo elija la opcion 2, gracias.")
    
    elif opcion == "4":
        from operator import itemgetter
        consulta3 = int(input("Para ordenar de menor a mayor, ingrese el precio minimo: "))
        lista_ordenada = {}
        for producto, precio in lista_precios.items():
            if precio >= consulta3:
                lista_ordenada[producto] = precio
        print(sorted(lista_ordenada.items(), key = itemgetter(1)))

    elif opcion == "5":
        numero = False

print("El programa ah finalizado.")






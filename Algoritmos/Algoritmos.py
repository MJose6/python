#Ejercicio: 1
'''Implementar un algoritmo de ordenamiento por burbuja de una lista numérica.'''

listaNumeros = [41, 54, 22, 33, 56, 92, 86, 28, 101, 166]

def ordenamientoBurbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                orden = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = orden
    return lista

print(listaNumeros, "Lista desordenada.")
ordenPorBurbuja = ordenamientoBurbuja(listaNumeros)
print(ordenPorBurbuja, "Lista ordenada por Burbuja.")

#Ejercicio: 2
'''Implementar un algoritmo de ordenamiento por inserción de una lista numérica.'''

def ordenamientoInsercion(lista):
    for i in range(len(lista)):
        valor = lista[i]
        indice = i - 1

        while indice >= 0:
            if valor < lista[indice]:
                lista[indice + 1] = lista[indice]
                lista[indice] = valor
                indice = indice - 1
            else:
                break

    return lista
    
ordenPorInsercion = ordenamientoInsercion(listaNumeros)
print(ordenPorInsercion, "Lista ordenada por insercion.")

#Ejercicio: 3
'''Implementar los algoritmos de búsqueda simple y binaria.
1. Búsqueda simple: busca desde el primer dato hasta el último, uno a uno comparando
sucesivamente todos los datos en memoria hasta localizar el dato que queramos 
localizar. Este algoritmo puede usarse en cualquier situación, pero se recomienda 
usarlo solo en listas que no estén ordenadas
2. Búsqueda binaria: este tipo de búsqueda es usado en listas que estén previamente 
ordenadas, ya que su método de búsqueda es la de dividir los datos en dos grupos, 
eligiendo el grupo en el cual debería estar el dato buscado (supone que está 
ordenado alfabéticamente o numéricamente), volviendo a aplicar la división, y así 
sucesivamente hasta verificar si existe o no existe el dato buscado. Aplicar en este 
caso recursividad.'''

#3.1 busqueda lineal o simple

numero = int(input("Ingrese el numero del cual desea saber la posicion: "))

def busquedaLineal(lista, num):
    for i in range(len(lista)):
        if lista[i] == num:
            return i
    return None

buscar = busquedaLineal(ordenPorInsercion, numero)
print("El numero se encuentra en la posicion: ",buscar)

#3.2 busqueda binaria

numeroBuscado = int(input("Ingrese el numero que desea buscar: "))

def busquedaBinaria(lista, num):
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio] == num:
            return medio
        elif num > lista[medio]:
            inicio = medio + 1
        else:
            final = medio - 1

    return None


indice = busquedaBinaria(ordenPorInsercion, numeroBuscado)
print("El numero", numeroBuscado, "se encuentra en la posicion: ",indice)







#Ejercicio: 4
'''Diseñar e implementar un algoritmo de cifrado de textos.'''

#Cifrado Cesar
from string import ascii_lowercase, ascii_uppercase

texto = input("Ingrese el texto a cifrar: ")
desplazamiento = int(input("Ingrese un numero del 1 al 10 para el desplazamiento: "))

def cifradoCesar(texto, num):
    resultado = []
    for i in texto:
        if i in ascii_lowercase:
            indice = ascii_lowercase.index(i)
            nuevoIndice = (indice + num) % len(ascii_lowercase)
            resultado.append(ascii_lowercase[nuevoIndice])
        elif i in ascii_uppercase:
            indice = ascii_uppercase.index(i)
            nuevoIndice = (indice + num) % len(ascii_uppercase)
            resultado.append(ascii_uppercase[nuevoIndice])
        else:
            resultado.append(i)
    return ''.join(resultado)

textoCifrado = cifradoCesar(texto, desplazamiento)
print(textoCifrado)
    







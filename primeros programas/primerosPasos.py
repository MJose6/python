#Ejercio: 1
'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.'''

edad = int(input("Ingrese su edad:"))
if edad >= 18 :
  print ("Usted es mayor de edad")

else: 
  print ("Usted es menor de edad")

print("Fin del Programa")


#Ejercicio: 2
'''Escribir un programa que pregunte al usuario una contraseña y luego pida que la ingrese de nuevo. Validar que ambas contraseñas son iguales'''

ingresar_contraseña1 = int(input("Ingrese contraseña1:"))
ingresar_contraseña2 = int(input("Ingrese contraseña2:"))

if ingresar_contraseña1 == ingresar_contraseña2 :
  print ("Son Validas")

else: 
  print ("Son invalidas")

print("Fin del Programa")


#Ejercicio: 3
'''Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.'''

numero1 = int(input("Ingrese Numero :"))
numero2 = int(input("Ingrese Divisor:"))

if numero2 == 0: 
  print ("Error")  

else:
  Resultado_division = numero1 / numero2
  print("El resultado de la division es:",Resultado_division)

print("Fin del programa")


#Ejercicio: 4
'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.'''

numero = int(input("Ingrese numero:"))
modulo = numero % 2

if modulo == 0 :
  print ("El numero es par")

else:
  print("El numero es impar")

print("Fin del programa")

 
#Ejercicio: 5
'''Escribir un programa que pida al usuario un número entero y muestre por pantalla la letra del abecedario cuya posición corresponde al valor entero ingresado.'''

numeroEntero = int(input("Ingrese un numero del 1 al 27:"))

cont = 0

for i in "abcdefghijklmnñopkrstuvwxyz":
  cont = cont + 1
  if cont == numeroEntero:
    print ("El numero elegido coincide con la letra", i) 


#Ejercicio: 6
'''Escribir un programa que solicite al usuario una cadena, la almacene en una variable y luego muestre por pantalla el contenido de la variable caracter a caracter.'''
cadena=input("ingrese una palabra: ")
for x in cadena:
  print(x)


#Ejercicio: 7
'''Escribir un programa que solicite al usuario su nombre y un número entero. Luego muestre por pantalla el nombre repetido la cantidad de veces, según el numero ingresado.'''
nombre=input("ingrese su nombre: ")
num=int(input("ingrese un numero: "))
for x in range(num):
  print(nombre)


#Ejercicio: 8
'''Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.'''
num=int(input("ingrese un numero: "))
for x in range(num):
  x=x+1
  print(x)


#Ejercicio: 9
'''Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo muestre por pantalla.'''
peso=float(input("ingrese su peso en kg: "))
altura=float(input("ingrese su altura en mts: "))
imc=peso/altura
print(imc)


#Ejercicio: 10
'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.'''
inversion=int(input("ingrese el monto a invertir: "))
interes=int(input("ingrese el interes anual: "))
interes=(inversion*interes)/100
años=int(input("ingrese la cantidad de años: "))
capital=(inversion+interes)*años
print(capital)


#Ejercicio: 11
'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de la imágen, de altura el número introducido.'''
num=int(input("ingrese un numero: "))
for x in range(num):
  x=x+1
  print("*"*x)


#Ejercicio: 12
'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.'''
num=int(input("ingrese un numero: "))
num=num*2
for x in range(1,num+1,2):
  for j in range(x,0,-2):
    print(j, end=" ")
  print(" ")



#Ejercicio: 13
'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.'''
num=int(input("ingrese un numero: "))
valid_num=False
if num == 2:
  valid_num=True
for x in range(2, num):
  if num%x == 0:
    valid_num=False
    break
  else:
    valid_num=True
if valid_num==True:
  print("es primo")
else:
  print("no es primo")



#Ejercicio: 14
'''Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.'''
frase=input("ingrese una frase: ")
letra=input("ingrese una letra: ")
cont_letra=0
frase.split
for x in frase:
  if x == letra:
    cont_letra +=1
  else:
    cont_letra=cont_letra
print(letra, "=",cont_letra)



#Ejercicio: 15
#Dada una lista de palabras, imprimir las repetidas. Ejemplo: [haciendo,cosas,raras,para,gente,normal,haciendo,cosas,raras,sin,pensar]
lista_palabras=["haciendo","cosas","raras","para","gente","normal","haciendo","cosas","raras","sin","pensar"]
lista=[]
repetidas=[]

for x in lista_palabras:
  if not x in lista:
    lista.append(x)
  else:
    repetidas.append(x)

print(repetidas)



#Ejercicio: 16
#Dada una lista de palabras, imprimir cada una de las palabras junto a la cantidad de letras por palabra
lista_Palabras=["Qué","hay","de","esa","imagen","en","mi","cielo"]
contador=0
palabras=[]

for x in lista_Palabras:
  if not x in palabras:
    palabras.append(x)
  else:
    for j in palabras:
      if j in palabras:
        palabras.split
        contador+=1
print(palabras,contador)




#Ejercicio: 17
#Dadas dos listas con palabras, imprimir las palabras que aparecen en ambas listas
lista1=['hola','que','tal']
lista2=['Qué','hay','de','esa','imagen','en','mi','cielo']

print(lista1)
print(lista2)



#Ejercicio: 18
#Dadas dos listas con palabras, imprimir las palabras que no se repiten entre las listas
lista1=['hola','que','hay','de','bueno']
lista2=['que','hay','de','esa','imagen','en','mi','cielo']

lista=[]

for x in lista1:
  if not x in lista:
    lista.append(x)
    for x in lista2:
      if not x in lista:
        lista.append(x)
print(lista)



#Ejercicio: 19
#Dadas dos listas con palabras, imprimir las palabras que no se repiten entre las listas
lista1=['hola','que','hay','de','bueno']
lista2=['que','hay','de','esa','imagen','en','mi','cielo']

lista=[]

for x in lista1:
  if not x in lista2:
    lista.append(x)
for j in lista2:
  if not j in lista1:
    lista.append(j)
print(lista)



#Ejercicio: 20
#Crear un algoritmo que dado 10 números ingresados por el usuario, los inserte de forma ordenada
print("en este programa van a ingresar 10 numeros a ordenar de menor a mayor.")

num=[]

for x in range(10):
  numeros=int(input("ingrese un numero: "))
  num.append(numeros)
print('lista de numeros desordenados:',num)

def ordenar():
  for x in range(len(num)):
    for j in range(len(num)):
      if num[x] < num[j]:
        orden=num[x]
        num[x]=num[j]
        num[j]=orden
ordenar()
print('lista de numeros ordenados:',num)




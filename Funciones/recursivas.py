#Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas.
def descendente(num):
    if num >= 1:
        print(num)
        descendente(num - 1)

numero = int(input("Ingrese un numero entero: "))
resultado = descendente(numero)
print(resultado)




#función para calcular el total de un pago incluyendo un impuesto aplicado.
def calcularTotal(impuesto, porcentaje):
    porcentaje = (impuesto * porcentaje) / 100
    total = impuesto + porcentaje
    return total


impuesto_a_pagar = float(input("Ingrese el importe del impuesto: "))
porcentaje_a_aplicar = float(input("Ingrese el porcentaje a calcular: "))
total_a_pagar = calcularTotal(impuesto_a_pagar, porcentaje_a_aplicar)
print(f'El total a pagar con el porcentaje aplicado es de: {total_a_pagar}')



# Función que convierte de celsius a fahrenheit y viceversa.
def celsius_fahrenheit(celsius):
        return celsius * 9/5 + 32

def fahrenheit_celsius(fahrenheit):
        return (fahrenheit-32) * 5/9


celsius = float(input('Ingrese la temperatura en grados celsius: '))
resultado = celsius_fahrenheit(celsius)

print(f'{celsius} grados Celsius equivalen a {resultado:.2f} gracos Fahrenheit.')


fahrenheit = float(input('Ingrese la temperatura en grados fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)

print(f'{fahrenheit} grados Fahrenheit equivalen a {resultado:.2f} grados Celsius.')
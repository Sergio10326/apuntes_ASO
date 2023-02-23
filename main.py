#!/usr/bin/env python3
#Ejercicio 1: Crear un script que, dado un valor, calcule si es primo o no

import math
def primos(prm_max_number):
    """
    This function verifies which numbers are prime
    SCOPE: Range indicated between 2 and argument 'prm_max_number'
    """
    prime_numbers_list = []
    numbers_2_to_max_number = range(2, prm_max_number)

    for number in numbers_2_to_max_number:
        # Variable declarations inside for loop
        maximum_posible_divisor = math.ceil(math.sqrt(number))
        isnt_prime = 0
        i = 2

        # 'isnt_prime' will take value '1' if the number being
        # evaluated is not prime, and the loop will end.
        while (isnt_prime < 1) and (i <= maximum_posible_divisor):
            if number % i == 0:
                isnt_prime += 1

            i += 1

        if (isnt_prime < 1):
            prime_numbers_list.append(number)

    return prime_numbers_list
print(primos(101))

# Resolución ejercicio 1

numero_comprobar=13
isNotPrimo=False
auxiliar=2

while not isNotPrimo and auxiliar<numero_comprobar:
    comprobacion = numero_comprobar % auxiliar
    if comprobacion == 0:
        isNotPrimo = True
    auxiliar+=1

if isNotPrimo:
    print(str(numero_comprobar) + " No es primo")
else:
    print(str(numero_comprobar) + " Es primo")

# Ejercicio 2: crear un script que haga la sucesión de fibonacci hasta 50

n=int(input("Veces que se va a ejecutar la sucesión: "))
a=0
b=1
sum=0
count=1
print("Secuencia resultante: ")
while(count<n):
  print(sum)
  count+=1
  a=b
  b=sum
  sum= a + b

# Ejercicio 3: Crea un programa que muertre al usuario un menú con dos opciones: 1- Introducir Datos (y meterlos en una lista) 2- Mostrar datos 3- Salir


x=0
lista_a= list()
while x == 0:
    menu = input(
        "Introduce un valor para acceder a una de las siguientes opciones: \n(1)Actualizar los datos de la lista\n(2)Mostrar los datos de la lista\n(3)Salir del programa\n")
    if menu == "1":
        dato=0
        while dato == 0:
            dato=input("Introduce un valor: ")
            lista_a.append(dato)
            print("Valor introducido")
    elif menu == "2":
            print(lista_a)
    elif menu == "3":
        print("Saliendo del programa...")
        x += 1
    else:
        print("Opción no valida")

#Ejercicio 4: hacer el ejercicio de la sucesion de fibonacci almacenando los valores en una lista

valor=10000
isValor = True
lista_fib = list()
resultado = 0
lista_fib.append(0)
print(lista_fib[len(lista_fib)-1])
lista_fib.append(0)
print(lista_fib[len(lista_fib)-1])
while not isValor:
    if (resultado >= valor):
        isValor = True
    else:
        resultado = lista_fib[len(lista_fib)-1] + lista_fib[len(lista_fib)-2]
        lista_fib.append(resultado)
        print(lista_fib[len(lista_fib) - 1])

# Ejercicio 5: hacer un tres en raya


#Ejercicio 6: hacer un programa que pida al usuario 2 valores y una operación (suma,resta,mult,div). El programa solo parará cuando el usuario lo solicite.
#Debe realizarse una función para cada operación y una para las peticiones del usuario

x=0

def funcion_suma():
    dato=0
    while dato == 0:
        num_1 = input("Introduce el primer valor: ")
        num_2 = input("Introduce el segundo valor: ")
        sum = int(num_1) + int(num_2)
        print("El resultado de la suma es: "+ str(sum))
        dato += 1
def funcion_resta():
    dato=0
    while dato == 0:
        num_1 = input("Introduce el primer valor: ")
        num_2 = input("Introduce el segundo valor: ")
        res = int(num_1) - int(num_2)
        print("El resultado de la resta es: "+ str(res))
        dato += 1
def funcion_mul():
    dato = 0
    while dato == 0:
        num_1 = input("Introduce el primer valor: ")
        num_2 = input("Introduce el segundo valor: ")
        mul = int(num_1) * int(num_2)
        print("El resultado de la multiplicación es: " + str(mul))
        dato += 1
def funcion_div():
    dato = 0
    while dato == 0:
        num_1 = input("Introduce el primer valor: ")
        num_2 = input("Introduce el segundo valor: ")
        div = int(num_1) / int(num_2)
        print("El resultado de la división es: " + str(div))
        dato += 1
while x == 0:
    menu = input(
        "Introduce un valor para acceder a una de las siguientes opciones: \n(1)Sumar\n(2)Restar\n(3)Multiplicar\n(4)Dividir\n(5)Salir del programa\n")
    if menu == "1":
        funcion_suma()
    elif menu == "2":
       funcion_resta()
    elif menu == "3":
        funcion_mul()
    elif menu == "4":
        funcion_div()
    elif menu == "5":
        print("Saliendo del programa...")
        x += 1
    else:
        print("Opción no valida")

#SOLUCIÓN DEL PROFE:

def pedirValor(mensaje):
    valor=input(mensaje)
    return valor

def sumar(valor1,valor2):
    resultado = valor1 + valor2
    return resultado

def restar(valor1,valor2):
    resultado = valor1 - valor2
    return resultado

def multiplicar(valor1,valor2):
    resultado = valor1 * valor2
    return resultado

def dividir(valor1,valor2):
    resultado = valor1 / valor2
    return resultado

isSalir = False
valor1 = 0
valor2 = 0
resultado = 0
while not isSalir:
    valor1 = int(pedirValor("Introduce el primer valor:\n"))
    valor2 = int(pedirValor("Introduce el segundo valor:\n"))
    operacion = pedirValor("Introduce la operacion\n1- Sumar\n2-Restar\n3-Multiplicar\n4- Dividir\n5- Salir\n")
    if(operacion=="1"):
        resultado = sumar(valor1,valor2)
        print("El resultado de "+str(valor1) + " + " + str(valor2) + " es igual a " + str(resultado))
    elif(operacion=="2"):
        resultado = restar(valor1, valor2)
        print("El resultado de " + str(valor1) + " - " + str(valor2) + " es igual a " + str(resultado))
    elif(operacion=="3"):
        resultado = multiplicar(valor1, valor2)
        print("El resultado de " + str(valor1) + " * " + str(valor2) + " es igual a " + str(resultado))
    elif(operacion=="4"):
        resultado = dividir(valor1, valor2)
        print("El resultado de " + str(valor1) + " / " + str(valor2) + " es igual a " + str(resultado))
    elif(operacion=="5"):
        isSalir=True
        print("Hasta luego")
    else:
        print("No existe esa opcion")

# Hacer un programa que emule un cajero. El usuario podrá solicitar una cantidad de dinero y el programa deberá mostrar la combinación de billetes y monedas necesarias para completar esa cantidad
# El programa debe ofrecer el menor número de billetes y monedas posibles.


#??? - Hacer un programa que emule un cajero
# El usuario podrá solicitar una cantidad de dinero
# El programa deberá mostrar la combinación de billetes y monedas
# necesarias para completar esa cantidad. El programa debe
# ofrecer el menor número de billetes y monedas posible.

def cajero(cantidad_pedir):
    # Orden: 500,200,100,50,20,10,5,2,1
    billetes_devolver = [0,0,0,0,0,0,0,0,0]
    while cantidad_pedir>0:
        if (cantidad_pedir > 500):
            #billetes_devolver[0]=billetes_devolver[0]+1
            billetes_devolver[0]+=1
            cantidad_pedir-=500
        elif(cantidad_pedir < 500 and cantidad_pedir > 200):
            billetes_devolver[1]+=1
            cantidad_pedir-=200
        elif (cantidad_pedir < 200 and cantidad_pedir > 100):
            billetes_devolver[2]+=1
            cantidad_pedir-=100
        elif (cantidad_pedir < 100 and cantidad_pedir > 50):
            billetes_devolver[3]+=1
            cantidad_pedir-=50
        elif (cantidad_pedir < 50 and cantidad_pedir > 20):
            billetes_devolver[4]+=1
            cantidad_pedir-=20
        elif (cantidad_pedir < 20 and cantidad_pedir > 10):
            billetes_devolver[5]+=1
            cantidad_pedir-=10
        elif (cantidad_pedir < 10 and cantidad_pedir > 5):
            billetes_devolver[6]+=1
            cantidad_pedir-=5
        elif (cantidad_pedir < 5 and cantidad_pedir > 2):
            billetes_devolver[7]+=1
            cantidad_pedir-=2
        else:
            billetes_devolver[8]+=1
            cantidad_pedir-=1
    return billetes_devolver

# Función para pedir valores al usuario con mensaje personalizado
def pedirValor(mensaje):
    valor = input(mensaje)
    return valor

def mostrar_billetes(lista_billetes):
    mensaje = ""
    valor_billetes = [500,200,100,50,20,10,5,2,1]
    for n_billete in range(0, len(lista_billetes)):
        if lista_billetes[n_billete] > 0:
            mensaje = mensaje + str(lista_billetes[n_billete]) + " billete(s) de " + str(valor_billetes[n_billete])
            mensaje = mensaje + "\n"
    return mensaje

def __main__():
    cantidad_usuario = int(pedirValor("¿Cuánto dinero quieres sacar?\n"))
    billetes = cajero(cantidad_usuario)
    print(mostrar_billetes(billetes))

__main__()

# Con el ejercicio de cajero resuelto, añadir:
# - El cajero funcione hasta que el usuario salga
# - Dinero disponible del usuario, poder visualizarlo
# - El cajero debe evitar que el usuario saque más dinero del que dispone

x=0
while x==0:
    pregunta = int(input("(1) Para meterte en el cajero\n(2) Para salir del programa\n\n"))
    if pregunta == 1:
        def cajero(cantidad_pedir):
            # Orden: 500,200,100,50,20,10,5,2,1
            billetes_devolver = [0,0,0,0,0,0,0,0,0]
            while cantidad_pedir>0:
                if (cantidad_pedir >= 500):
                    #billetes_devolver[0]=billetes_devolver[0]+1
                    billetes_devolver[0]+=1
                    cantidad_pedir-=500
                elif(cantidad_pedir < 500 and cantidad_pedir >= 200):
                    billetes_devolver[1]+=1
                    cantidad_pedir-=200
                elif (cantidad_pedir < 200 and cantidad_pedir >= 100):
                    billetes_devolver[2]+=1
                    cantidad_pedir-=100
                elif (cantidad_pedir < 100 and cantidad_pedir >= 50):
                    billetes_devolver[3]+=1
                    cantidad_pedir-=50
                elif (cantidad_pedir < 50 and cantidad_pedir >= 20):
                    billetes_devolver[4]+=1
                    cantidad_pedir-=20
                elif (cantidad_pedir < 20 and cantidad_pedir >= 10):
                    billetes_devolver[5]+=1
                    cantidad_pedir-=10
                elif (cantidad_pedir < 10 and cantidad_pedir >= 5):
                    billetes_devolver[6]+=1
                    cantidad_pedir-=5
                elif (cantidad_pedir < 5 and cantidad_pedir >= 2):
                    billetes_devolver[7]+=1
                    cantidad_pedir-=2
                else:
                    billetes_devolver[8]+=1
                    cantidad_pedir-=1
            return billetes_devolver

        # Función para pedir valores al usuario con mensaje personalizado
        def pedirValor(mensaje):
            valor = input(mensaje)
            return valor

        def mostrar_billetes(lista_billetes):
            mensaje = ""
            valor_billetes = [500,200,100,50,20,10,5,2,1]
            for n_billete in range(0, len(lista_billetes)):
                if lista_billetes[n_billete] > 0:
                    mensaje = mensaje + str(lista_billetes[n_billete]) + " billete(s) de " + str(valor_billetes[n_billete])
                    mensaje = mensaje + "\n"
            return mensaje

        def __main__():
            din_user = 2000
            cantidad_usuario = int(pedirValor("¿Cuánto dinero quieres sacar?\n"))
            if din_user > cantidad_usuario:
                print("Amigoooo, que tas pobre")
                print(din_user)
            else:
                billetes = cajero(cantidad_usuario)
                print(mostrar_billetes(billetes))
                print(din_user)
        __main__()
    elif pregunta == 2:
            print("Saliendo del programa...")
            x+=1
    else:
            print("Esa opción no es válida. Introduce (1) para accceder al cajero, y (2) para salir del programa")

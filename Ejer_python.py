#!/usr/bin/env python3

#Importación de la librería necesaria para el random

import random

r_1 = random.randint(0,59)
r_2 = random.randint(0,59)
r_3 = random.randint(0,59) #Creación números del boleto ganador
r_4 = random.randint(0,59)
r_5 = random.randint(0,59)
r_6 = random.randint(0,9)

n_1 = random.randint(0,59)
n_2 = random.randint(0,59)
n_3 = random.randint(0,59) #Creación números del boleto random del jugador
n_4 = random.randint(0,59)
n_5 = random.randint(0,59)
n_6 = random.randint(0,9)

boleto_random_win = [r_1, r_2, r_3, r_4, r_5, r_6] #Creación del boleto ganador como lista
boleto_random_jugador = [n_1, n_2, n_3, n_4, n_5, n_6] #Creación del boleto random del jugador como lista

def salida ():
    print("\nSaliendo del programa...") # Mensaje de exit

def comparacion_random (boleto_random_jugador): #función que hace la comparación de todos los elementos de las listas del boleto ganador y del boleto generado de forma aleatoria del jugador
    # a través de un parámetro ya que sino no puede recoger la lista correctamente. Esta también se podría generar dentro de la propia función
    for j in range(0, len(boleto_random_win)):
        sp = 69 #Declaración de la variable. Su valor no influye
        for k in range(0, len(boleto_random_jugador)):
            if boleto_random_win[k] == boleto_random_jugador[j] and k == j: #Bucle de comparación de coincidencia de número y posición
                sp = 0 #Controlador de la comprobación
                break
            elif boleto_random_win[k] == boleto_random_jugador[j] and k != j: #Bucle de comparación de coincidencia de número
                sp = 1 #Controlador de la comprobación
        if sp == 0:
            print("Coinciden número y posición")
        elif sp == 1:
            print("Coincide solo el número")
        else:
            print("No hay coincidencias")


def comparacion_creado (): #Esta función hace la misma tarea que la anterior, con la diferencia de que en este caso la lista es generada de forma manual y dentro de la propia función.
    number_list = []
    for i in range(0, 6):
        print("Introduce el número. El sexto ten en cuenta que es el reintegro, que va del 0 al 9. El resto van del 0 al 59: ", i) #Números que se van a ir añadiendo
        item = int(input())
        number_list.append(item) #Adición de los elementos introducidos al final de la lista
        print("Tus números: ", number_list) #Lista final de los números del boleto
    for j in range(0, len(boleto_random_win)):
        sp = 69 #Declaración de la variable. Su valor no influye
        for k in range(0, len(number_list)):
            if boleto_random_win[k] == number_list[j] and k == j: #Bucle de comparación de coincidencia de número y posición
                sp = 0 #Controlador de la comprobación
                break
            elif boleto_random_win[k] == number_list[j] and k != j: #Bucle de comparación de coincidencia de número
                sp = 1 #Controlador de la comprobación
        if sp == 0:
            print("Coinciden número y posición")
        elif sp == 1:
            print("Coincide solo el número")
        else:
            print("No hay coincidencias")


x=0
while x == 0: #Bucle creado para que se despliegue el menú hasta que el usuario salga por sí mismo cuando quiera del script.
    tipo_boleto = input("Elige si quieres un boleto en específico o uno al azar. \n(1) para crear manualmente la lista\n(2) para generar un boleto de forma aleatoria \n(3) para salir del servicio de lotería ")
    if tipo_boleto == "1":
        comparacion_creado() #Llamada a la función
    elif tipo_boleto == "2":
        comparacion_random(boleto_random_jugador) #Llamada a la función
    elif tipo_boleto == "3":
        salida() #Llamada a la función
        x = 1 #Cambio en la variable para salir del bucle y del programa principal
    else:
        print("\nError, ese valor no es reconocido por el programa, inténtelo de nuevo\n") #Mensaje de error para que el usuario sepa si está haciendo un correcto uso del script.



#!/usr/bin/env python3

import random
import numpy as np

intentos = 0

r_1 = random.randint(0,9)
r_2 = random.randint(0,9)
r_3 = random.randint(0,9)
r_4 = random.randint(0,9)

mylist = [r_1, r_2, r_3, r_4]

print(mylist)
print("Comienza el juego!\n")

x=0
while x == 0:
    number_list = []
    for i in range(0, 4):
        print("Introduce el valor ", i )
        item = int(input())
        number_list.append(item)
        print("Tus números: ", number_list)
    pepe = 4
    for j in range(0,len(mylist)):
        sp = 69
        for k in range(0,len(number_list)):
            if mylist[k] == number_list[j] and k == j:
                pepe -= 1
                sp = 0
                break
            elif mylist[k] == number_list[j] and k != j:
                sp = 1
        if sp == 0:
            print("o")
        elif sp == 1:
            print("+")
        else:
            print("-")
    intentos += 1
    print("\nLlevas " + str(intentos) + " intento(s)\n")
    if pepe == 0:
        x = 1
        print("Enhorabuena! Has ganado")






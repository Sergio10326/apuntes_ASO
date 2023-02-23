# Crear un script que permita al usuario crear o borrar ficheros utilizando los módulos OS y SYS
# Cuando el usuario quiera crear o eliminar un fichero, comprueba que no existe (para crear) o que sí existe (para eliminar)
# Añadir la opción de listar ficheros.
#Permitir al usuario buscar ficheros, incluidas búsquedas parciales.
# Permitir al usuario listar los ficheros con los permisos "ls -l"
#!/usr/bin/env python3
import sys
import os
import subprocess

x = 0
while x == 0:
    y = 0
    resp = int(input("Elige si quieres crear (1), borrar (2) directorios, salir (3) del programa, listar ficheros (4), buscar ficheros (5) o listar ficheros en detalle (6)  \n\n"))
    while y == 0:
        if resp == 1:
            resp_2 = input("Introduce el nombre del fichero que quieres crear\n\n")
            fileExists = True
            for f in os.listdir("."):
                print(f)
                if f == resp_2:
                  fileExists = False
            if fileExists:
                fichero = open(resp_2, "w")
                fichero.close()
                y += 1
            else:
                print("Ese fichero ya existe")
        elif resp == 2:
            resp_2 = input("Introduce el nombre del fichero que quieres borrar. Ten en cuenta que sólo funcionará en caso de que introduzcas el nombre correctamente\n\n")
            fileExists = True
            for f in os.listdir("."):
                print(f)
                if resp_2 == f:
                    fileExists = True
            if fileExists:
                os.remove(resp_2)
                y += 1
            else:
                print("Ese fichero no existe")
        elif resp == 3:
            print("Saliendo del programa...")
            x += 1
            y += 1
        elif resp == 4:
            print(os.getcwd())
            for f in os.listdir("."):
                print(f)
            y += 1
        elif resp == 5:
            busqueda = input("Qué fichero estás buscando?  ")
            for fichero in os.scandir("."):
                if(os.path.isfile(fichero)):
                    if(fichero.name.contains(busqueda)):
                        print(fichero.name)
        elif resp == 6:
            ruta = input("Selecciona la ruta que quieres listar: ")
            subprocess.run("ls -l "+ruta, shell=True)
            y += 1
        else:
            print("El valor introducido no es válido.\n\nElige si quieres crear (1), borrar (2) directorios o salir (3) del programa")
variable = "siuuuuu"
print(variable)
numero=1
numero_2=5
resultado=numero+numero_2
print("Resultado = "+ str(resultado))
#comentario
"""
jaja
pito
jaja
"""
resultado=numero-numero_2
print("Resultado = "+ str(resultado))
resultado=numero*numero_2
print("Resultado = "+ str(resultado))
resultado=numero/numero_2
print("Resultado = "+ str(resultado))
resultado=numero%numero_2 # resto
print("Resultado = "+ str(resultado))
resultado=numero**numero_2 #potencia
print("Resultado = "+ str(resultado))
resultado=numero//numero_2 #división truncada
print("Resultado = "+ str(resultado))
resultado=numero-numero_2
print("Resultado = "+ str(resultado))
resultado += numero_2 # suma con el último valor de la primera variable

# Operadores de comparación

numero_1=5
numero_2=7
numero_3=-4

resultado=numero_1 == numero_2
print("Resultado = "+ str(resultado))
resultado=numero_1 != numero_2
print("Resultado = "+ str(resultado))
resultado=numero_1 > numero_2
print("Resultado = "+ str(resultado))
resultado=numero_1 < numero_2
print("Resultado = "+ str(resultado))
resultado=numero_1 >= numero_2
print("Resultado = "+ str(resultado))
resultado=numero_1 <= numero_2
print("Resultado = "+ str(resultado))

# Comparadores lógicos

resultado=(numero_1 > numero_2 ) & (numero_2 < numero_3) # & comprueba hasta que una de las dos opciones sea falsa
print("Resultado = "+ str(resultado))
resultado=(numero_1 > numero_2 ) and (numero_2 < numero_3)
print("Resultado = "+ str(resultado))
resultado=(numero_1 > numero_2 ) | (numero_2 < numero_3)# or
print("Resultado = "+ str(resultado))
resultado=not (numero_1 > numero_2)
print("Resultado = "+ str(resultado))
resultado=~ (numero_1 > numero_2)
print("Resultado = "+ str(resultado))
resultado=(numero_1 > numero_2) ^ (numero_2 > numero_3) #es un not controlado. Solo 1 puede ser verdad
print("Resultado = "+ str(resultado))
resultado=(numero_1 > numero_2 ) and (numero_2 < numero_3)
print("Resultado = "+ str(resultado))

# Estructuras condicionales

if numero_1 < numero_2:
    print("Asíes")
    print("jaja locooooo")
elif numero_1 > numero_2:
    print("hehehe siuuuuu")
    print("Yo ya no siento; Santi 2k21")
else:
    print("klk manin (Killer Latin King Manin)")
    print("Oye muchacho, ustede escucharon el rempálago")

# Estructuras de repetición

contador=0
while contador < 10:
    print("Contador= " + str(contador))
    contador += 1

for variable in range(7,14):
    print ("Variable: " + str(variable))
for variable in range(7,-7,-1): #el tercer número establece el aumento o decremento del valor
    print("Variable: " + str(variable))

#TUPLAS

conjunto_a =(1, 2, 3, 4, 5)
conjunto_vacio = tuple ()
conjunto_un_miembro = tuple ("uno",)
conjunto_sin_tipo =(1, 2, 3, 4, 5)

contador = 0
while contador < len(conjunto_a): #calcula el número de valores del conjunto
    print(str(conjunto_a[contador]))# los corchetes se usan para indicar el índice a mostrar. Si no hay, se muestran todos
    contador+=1

contador = 0
for contador in conjunto_a:
    print(str(contador))

#LISTAS

lista_a = [0,1,1,2,3,5,8,13]
lista_vacia = []
lista_un_elemento = [1]
lista_vacia_2 = list()

contador = 0
while contador < len(lista_a): #calcula el número de valores del conjunto
    print(str(lista_a[contador]))# los corchetes se usan para indicar el índice a mostrar. Si no hay, se muestran todos
    contador+=1

lista_a[2] = [88,22,33]
lista_a[3] = "sus"

contador = 0
for contador in lista_a:
    print(str(contador))

print("Tamaño de la lista : "+str(len(lista_a)))
print("Rango de la lista 2-4 "+ str(lista_a[2:4])) #No se incluye el último índice
print(lista_a[len(lista_a)-1])
lista_a.append(100) # Introduce el valor puesto al final de la lista
print(lista_a[len(lista_a)-1])
lista_a.remove(5) #Elimina el primer valor que coincida con el indicado
del lista_a[5] #Elimina el índice con este valor
print(lista_a)
print(str(lista_a.pop()))

#INPUT

entrada = input("Introduce un valor: ")
print(entrada)

#DICCIONARIO

diccionario = {'Clave1':'valor1', 'Clave2':'valor2'}
print(diccionario['Clave1'])
diccionario_num = {0:1, 1:2, 2:3}
print(diccionario_num[0])

for clave,valor in diccionario_num.items(): #hace falta poner el "items" para que funcione el diccionario
    print("Clave = "+str(clave))
    print("Valor = " + str(valor))

#FUNCIONES

def funcion_1(mensaje):
    mensaje = mensaje + "\notro hola"
    return mensaje

frase = funcion_1("Hola mundo")

print(frase)


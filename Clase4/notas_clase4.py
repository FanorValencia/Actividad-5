                                                                #Depuracion

#import pdb

def es_primo(n):
    #pdb.set_trace()
    primo = True
    for i in range (2,n):
        if (n%i == 0):
            primo = False
    return primo

def listar_n_primos(n):
    for i in range(2, n+1):
        if (es_primo(i)):
            print (f"{i}, es primo")


listar_n_primos(17)


                                                        #Compresion de Listas

import time
            #Método normal

inicio = time.time()
pares = []
for i in range (200):
    if i%2 == 0:
        pares.append(i)
fin = time.time()
#print ("Los numeros pares son: ", pares)
#print (" El tiempo de ejecución sin compresión es de: ", (fin-inicio), "segundos")

            #Método por compresión de listas

inicio = time.time()
pares_compresion = [i for i in range(200)] #-> imprime una lista de 0 a 100. el 200 no se incluye en el rango 
#Condicionales
pares_compresion2 = [i for i in range(200) if i%2 == 0] #-> imprime una lista con pares de 0 a 200
# un if / else, tiene una sintaxis diferente:
"""pares_compresion3 = [print(i, 'es par') if i%2==0 else print (i, 'es impar') for i in range (11)]"""
fin = time.time()
#print (pares_compresion3)
#print (" El tiempo de ejecución con compresión es de: ", (fin-inicio), "segundos")

#print ('MATRICES')
matriz5x5 = []
for n in range(5):
    matriz5x5.append([])
    for i in range(5):
        matriz5x5[n].append(i)
#print (matriz5x5)

matriz5x5_compresion = [[i for i in range(5)] for n in range(5)]
#print (matriz5x5_compresion)

print ("Cuadrados")
numeros = [2,3,4,5,6]
cuadrados =[]
for e in numeros:
    cuadrados.append(e**2)
print (cuadrados)

def eleva_cuadrados(n):
    return n**2
cuadrados =list(map(eleva_cuadrados,numeros))

print (cuadrados)

numeros = [2,3,4,5,6]
pares2 = []
for e in numeros:
    if n%2 ==0:
        pares2.append(e)
print(pares2)

def es_par(n):
    return n%2 == 0

pares_filtro = list(filter(es_par,numeros))

print (pares_filtro)

total = 0
for e in numeros:
    total += e
print(total)

from functools import reduce
def suma(n,m):
    return n+m

resultado = reduce(suma, numeros)
print(resultado)

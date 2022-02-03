"""Haciendo uso de comprensión de listas realice un programa que, dado una lista de listas de números enteros, 
devuelva el máximo de cada lista. Por ejemplo, suponga la siguiente listas de listas:
[[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
El programa debe devolver el mayor elemento de cada sublista.
Hciendo uso del pdb, inserte puntos de parada justo en la línea donde ha implementado la compresión de listas.
Haga pruebas mostrando el contenido de las variables y continuar con la ejecución línea a línea. ¿Qué conclusiones obtiene?
"""
from numpy import amax
import pdb

l_de_listas = [[3,54,2,5],[7,8,1,3,2],[99,287,54,87],[1,2,3,4,5,6,7]]

print ("Apartado 1. \n ")
# Definimos una función que calcule el máximo de una lista y marcamos el inicio del depurador. 
pdb.set_trace()
def maximo(n):
    return amax(n)

# Método de Compresión de lista
l_maximo2 = [ maximo(e) for e in l_de_listas ]

print ('De la lista inicial: \n', l_de_listas, '\nEl número mayor de cada lista es: \n', l_maximo2, '\n')

"""Haga uso de la función filter para construir un programa que, dado una lista de n números devuelva aquellos que son primos.
Por ejemplo, dada la lista [3, 4, 8, 5, 5, 22, 13], el programa que implemente debe devolver como resultado [3, 5, 5, 13]"""

print ('-------------------------------------------------------------\n')
print ("Apartado 2. \n ")

#Creamos la lista con los valores a analizar
l_numeros = [n for n in range(3,77)]

# Definimos una función que identifique los números primos
def primo(n):
    for i in range (2,n):
        if (n%i == 0):
            return False
    return True

# Utilizamos la función filter para crear una lista con los números primos de la lista inicial
primos = list(filter(primo,l_numeros))

print ('De la lista inicial: \n', l_numeros, '\nLos números primos son: \n', primos, '\n')

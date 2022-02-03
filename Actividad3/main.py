
'''
Actividad 8 Asignatura Programación Avanzada en Python:
1. Desarrolla un script en Python que abra un fichero de texto ‘.txt’.
Escribe unas cuantas líneas en el fichero y finalmente muestra el contenido de dicho fichero por pantalla.
2. Desarrolla un script que cargue el fichero cotizaciones.csv subido a la plataforma y cronstruya un dataframe en pandas. 
Muestra el mínimo, máximo y media de cada columna.
'''

#abrimos el fichero, con método de apertura para escritura al final del fichero existente. -> fichero = open('Act8_ap1.txt', 'w')

datos = ["Primera Línea del apartado 1 de la actividad 8","Segunda Línea del apartado 1 de la actividad 8",
"Tercera Línea del apartado 1 de la actividad 8","Cuarta Línea del apartado 1 de la actividad 8","Quinta Línea del apartado 1 de la actividad 8"
,"Sexta Línea del apartado 1 de la actividad 8"]
try:
    fichero = open('Act8_ap1.txt', 'w')
    for element in datos:
        fichero.write(element + '\n')
        
except Exception as e:
    print (e)

finally:
    fichero = open ('Act8_ap1.txt','r')
    print (fichero.read())
    fichero.close()

'''
Apartado 2.
'''
import pandas as pd

datos = pd.read_csv('cotizacion.csv', delimiter = ';', decimal = ',', thousands = '.')
df = pd.DataFrame(datos)
print ("El fichero cotizaciones.csv es el siguiente:", '\n', df)

#Esta función buscará el valor mínimo de cada columna del dataframe creado a partir del documento csv
def minimo():    
    print ("\n")
    print ("Los Valores mínimos de cada columna son:")
    try:
        m = df.min(numeric_only = True)
        print (m)
    except Exception as e:
        print (e)
    finally:
        print ("\n")

#Esta función buscará el valor máximo de cada columna del dataframe creado a partir del documento csv
def maximo():   
    print ("\n")
    print ("Los Valores máximos de cada columna son:")
    try:
        m = df.max(numeric_only = True)
        print (m)
    except Exception as e:
        print (e)
    finally:
        print ("\n")

#Esta función calculará la  media de cada columna del dataframe creado a partir del documento csv
def media():    
    print ("\n")
    print ("Los Valores medios de cada columna son:")
    try:
        m = df.mean(numeric_only = True)
        print (m)
    except Exception as e:
        print (e)
    finally:
        print ("\n")


minimo()
maximo()
media()




import pandas as pd
import numpy as np
from comprobaciones import*


# 1. Abrimos el fichero .csv, separando los elementos con '\t' y creamos un data frame con el mismo. 
datos = pd.read_csv("finanzas2020[1].csv", sep = '\t')
df = pd.DataFrame(datos)

# 2. Filtramos la información por columnas y creamos una lista para cada elemento a estudiar
#    mes, gastos, ingresos, beneficio
columnas = df.columns
meses =[]
beneficio_mes = []
gasto_mes =[]
ingresos_mes = []

# 3. Para cada lista, generamos un código en el que nos filtre la informacion solicitada y los rellene con dicha informacion
    #3.1. Creamos la lista de los meses
for e in columnas:
    meses.append(e)

    #3.2. Con el objetivo de crear las listas de gastos e ingresos, filtramos la información y llenamos las listas
for mes in meses:
    valores = []                            # De esta lista, extraeremos los gastos y los ingresos
    for element in df[mes]:
        if type(element) == str:
            try:
                element = int(element)
            except:
                element = 0
            finally:
                valores.append(element)
        else:
            valores.append(element)
    #suma_valores = np.sum(valores)
    #beneficio_mes.append(suma_valores)
    gastos = []                           # Añadimos cada gasto del mes, enendiendo gasto como valor negativo
    for element in valores:
        if element < 0:                     
            gastos.append(element)
    
    gasto_total = np.sum(gastos)          # Sumamos los gastos del mes y añadimos dicho valor a la lista general de gastos de cada mes
    #print (gastos)
    gasto_mes.append(gasto_total)

    ingresos = []                         # Repetimos operaciones, esta vez, con los ingresos
    for element in valores:
        if element > 0:
            ingresos.append(element)
    
    ingreso_total = np.sum(ingresos)
    #print (ingresos)
    ingresos_mes.append(ingreso_total)

    #3.3. Rellenamos la lista de los beneficios, calculando, para cada elemento la diferencia entre gasto e ingreso
for i in range(len(gasto_mes)):
    beneficio_mes.append(gasto_mes[i])

for i in range(len(ingresos_mes)):
    beneficio_mes[i] = beneficio_mes[i] + ingresos_mes[i]



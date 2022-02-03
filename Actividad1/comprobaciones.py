import pandas as pd

try:
    datos = pd.read_csv("finanzas2020[1].csv", sep = '\t')
    df = pd.DataFrame(datos)
    comprobacion_1 = True
except Exception as e:
    print(e)

try:
    columnas = df.columns
    if len(columnas) != 12:
        comprobacion_2 = False
    else:
        comprobacion_2 = True
except Exception as e:
    print (e)
        



try:
    if len(df[columnas]) >0:
        comprobacion_3 = True
    else:
        comprobacion_3 = False
except Exception as e:
    print (e)


from codigo_base import*
import csv

#Este es un codigo inicial de prueba
""" frame_data = {
    'mes':[meses[0],meses[1],meses[2]], 
    'Gastos':[gasto_mes[0],gasto_mes[1],gasto_mes[2]], 
    'Beneficios':[beneficio_mes[0],beneficio_mes[1],beneficio_mes[2]],
    'Diferencia': [diferencia[0],diferencia[1],diferencia[2]]
    }

df3 = pd.DataFrame(frame_data)

print (df3) """
try:
    if comprobacion_2 == True and comprobacion_2 ==True and comprobacion_3 == True:
        # Creamos un diccionario para tener toda la informacion Filtrada en el codigo base.
        frame_data2 = {
            'Mes' : [],
            'Gastos' : [],
            'Ingresos' : [],
            'Beneficios' : []

        }

        # Tomando la información de las listas generales creadas para rellenar el diccionario con esta información
        for n in meses:
            frame_data2['Mes'].append (n)

        for n in gasto_mes:
            frame_data2['Gastos'].append (n)

        for n in ingresos_mes:
            frame_data2['Ingresos'].append (n)

        for n in beneficio_mes:
            frame_data2['Beneficios'].append (n)


        #   Con el objetivo de mostrar por pantalla la información filtrada y organizada, creamos un dataframe a partir del
        #   diccionario creado y lo mostramos por pantalla. 
        df3 = pd.DataFrame(frame_data2)

        print ('La información inicial del documento de finanzas es: ','\n', df, '\n')

        print ('La información del análisis del documento de finanzas es: ', '\n', df3, '\n')

        print ('¿Qué mes se ha gastado más?', '\n','● El mes con mayores gastos es Marzo, con un gasto de 29690€', '\n')

        print ('¿Qué mes se ha ahorrado más?', '\n','● El mes con mayores beneficios es Enero, con un ahorro de 12064€', '\n')


        # Procedemos a mostrar las respuestas de las preguntas realizadas
        media_gastos = np.mean(gasto_mes) * -1
        mg = "{:.3f}".format(media_gastos)
        print ('¿Cuál es la media de gastos al año?', '\n','● La media de gastos al año es de',mg,'€', '\n')

        expenses = np.sum(gasto_mes)*-1
        print ('¿Cuál ha sido el gasto total a lo largo del año?', '\n','● El gasto total del año es de', expenses,'€', '\n')

        incomes = np.sum(ingresos_mes)
        print ('¿Cuáles han sido los ingresos totales a lo largo del año?', '\n','● Los ingresos del año son de de', incomes,'€', '\n')

        # Opcional: Realice una gráfica de la evolución de ingresos a lo largo del año .

        import matplotlib.pyplot as plt

        plt.plot(meses,ingresos_mes)
        plt.xlabel('Mes')
        plt.ylabel('Ingresos')
        plt.title('Ingresos anuales')
        plt.show()

except:
    print ('Falta información')


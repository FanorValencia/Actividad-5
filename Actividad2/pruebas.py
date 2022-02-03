import pandas as pd
import main


def test_minimo():
    frame_data = {
    'mes':[1,2,3], 
    'Gastos':[2,3,4], 
    'Beneficios':[4,5,3],
    'Diferencia': [3,4,1]
    }
    df3 = pd.DataFrame(frame_data)
    
    final = {
    'mes':[1], 
    'Gastos':[2], 
    'Beneficios':[3],
    'Diferencia': [1]
    }

    dfinal = pd.DataFrame(final)

    assert main.minimo() == dfinal
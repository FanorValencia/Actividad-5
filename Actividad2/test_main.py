import pytest
import main

#creamos la función de operaciones
def test_sumar_restar_enteros():
    num1 = '7'
    num2 = '3'
    try:
        num1 = float(num1)
        num2 = float(num2)
        if type(num1) or type(num2) == float:
            suma = num1 + num2
            resta = num1 - num2
            print("Suma: ",num1,"+",num2,"=",suma)
            print("Resta: ",num1,"-",num2,"=",resta)
    except ValueError:
        print("Error en la clase del valor ingresado, compruebe que los valores son numéricos")
        print("Para los decimales, utilice el punto (.), no la coma(,)")
    finally:
        print("Fin del Ejercicio")
        print("--------------------------------")

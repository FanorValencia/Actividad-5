#Parte 1 de la Actividad:
#Solicitaremos 2 valores, de los cuales mostraremos sus correspondientes Suma y Resta.
#Para los casos en los que no se introduzca un valor numérico, enviaremos un mensaje
# de error mediante una excepción. 

# 1. Solicitamos la introducción de los números a operar
print("Parte 1 de la actividad")
num1 = input("Introduce un número: ")
num2 = input("Introduce un segundo número: ")

#creamos la función de operaciones
def sumar_restar_enteros(num1,num2):
    #Con la excepción, comprobamos la clase de los valores ingresados
    #A efectos prácticos, las operaciones se harán con decimales.
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
sumar_restar_enteros(num1,num2)


print("Parte 2 de la Actividad:")
#Parte 2 de la Actividad:
#Crearemos una función que por defecto, nos dirá que tenemos 18 años.
nombre = input("introduce un nombre: ")
def predet(nombre,edad=18):
    if edad == 18:
        print(nombre,", tienes 18 años")
   #En caso de que utilicemos la función sobre-escribiendo el valor de la edad 
    else:
        print(nombre, ", tienes",edad, " años")
    
predet(nombre)


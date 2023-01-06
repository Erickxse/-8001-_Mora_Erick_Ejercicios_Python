"""
Descripción:
Ejercicio 5.
Ingresar un valor en dólares y transformar en euros y yen.
Autor:
Erick Sebastian Mora 
"""

def validarNumeros():
    """
    Es un procedimiento generico alternativo para realizar validacion de numeros enteros
    los datos ingresados se leen como string (str) y si son numeros se verifican
    y se transforman en tipo de datos entero (int), en este variante de funcion
    se maneja el uso de una excepcion para el ingreso de datos que no son numericos:
    ------------
        No Recibe parametros de entrada
    
    Retorna:
    ------------
        Retorna un valor entero (numero) que es el dato ingresado transformado a (int)
    """
    while True:
        num = input()
        try:
            num = float(num)
            if num >0:
                return num
            else:
                print("Solo numeros mayores a 0")    
        except ValueError:
            print("Solo se aceptan Reales")   

def ingresarDatos():
    print("Ingrese su valor en Dolares ($): ")
    dolar = validarNumeros()
    transformarEuros(dolar)
    transformarYen(dolar)

def transformarEuros(dolar):
    euro = dolar*0.942
    print(dolar," dolares equivalen a ",round(euro,2)," euros")

def transformarYen(dolar):
    yen = dolar*134.47
    print(dolar," dolares equivalen a ",round(yen,2)," Yenes")

if __name__ == '__main__':
    ingresarDatos()
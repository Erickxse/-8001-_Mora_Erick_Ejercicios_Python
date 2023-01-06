""""
Descripción:
Ejercicio 7.
Transformar una medida ingresada en Libras a Kilogramos y Gramos
Autor:
Erick Sebastian Mora Lara
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
    print("Ingrese su peso en Libras (lb): ")
    peso = validarNumeros()
    transformarKilos(peso)
    transformarGramos(peso)

def transformarKilos(libras):
    kilos = libras/2.2046
    print(libras," libras equivalen a ",round(kilos, 4)," Kilos")

def transformarGramos(libras):
    gramos = libras*453.59
    print(libras," libras equivalen a ",round(gramos,4)," gramos")


if __name__ == '__main__':
    ingresarDatos()
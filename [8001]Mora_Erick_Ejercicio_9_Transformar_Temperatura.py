"""
Descripción:
Ejercicio 9.
Ingresar la temperatura en grados Celsius y convertirla en grados Fahrenheit y viceversa. 
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
            num = int(num)
            return num
        except ValueError:
            print("Solo se aceptan enteros")    

def celsiusFarenheit():
    print("Ingrese la Temperatura en Celsius para Transformar a Farenheit: ")
    celsius = validarNumeros()
    farenheit = (celsius*1.8)+32
    print(celsius,"ºC, equivalen a ",farenheit,"ºF")

def farenheitCelsius():
    print("Ingrese la Temperatura en Farenheit para Transformar a Celsius: ")
    farenheit = validarNumeros()
    celsius = (farenheit-32)/1.8
    print(farenheit,"ºF, equivalen a ",celsius,"ºC")

def salir():
    print("Saliendo")
    exit()

def menuOpciones():
        print("Vamos a Transformar la Temperatura Ingresada")
        print("1.- Transformar de Celsius a Farenheit")
        print("2.- Transformar de Farenheit a Celsius")
        print("3.- Salir")
        print("Ingrese el número de la opción deseada: ")
        opcion = validarMenu()
        return opcion

def validarMenu():
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
            num = int(num)
            if 1<= num <=3:
                return num
            else:
                print("Opcion no valida. Intentelo de Nuevo")    
        except ValueError:
            print("Solo se aceptan Reales") 


def seleccionOpcion(opcion):
        if opcion == 1:
            celsiusFarenheit()
        elif opcion == 2:
            farenheitCelsius()
        elif opcion == 3:
            salir()


if __name__ == '__main__':
    nuevoMenu = menuOpciones()
    seleccionOpcion(nuevoMenu)
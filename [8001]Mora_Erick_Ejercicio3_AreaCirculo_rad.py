""""
Descripción:
Ejercicio 3.
Calcular el Area de un circulo conociendo su Radio
Autor:
Erick Sebastian Mora Lara
"""

def ingresarDatos():
    print("**VAMOS A CALCULAR EL AREA DE UN CIRCULO A PARTIR DE SU RADIO (r)**")
    print("Para empezar Ingrese el valor del radio: ")
    radioC = validarNumeros()
    return radioC

def validarNumeros():
    """
    Es un procedimiento generico alternativo para realizar validacion de numeros se lee un tipo de
    dato ingresado y se intenta su conversion a flotante (float), si es numero se transforman y pasa a la
    validacion para verificar que el numero sea mayor que 0.
    Si la conversion falla, se emplea el uso de Excepciones para imprimir un mensaje de Error
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

def areaCirculo():
    PI = 3.1416
    radioC = ingresarDatos()
    areaC = PI * radioC**2
    print(areaC)

if __name__ == '__main__':
    areaCirculo()

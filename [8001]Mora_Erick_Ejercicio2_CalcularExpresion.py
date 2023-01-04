""""
Descripción:
Ejercicio 2.
Calculo de una expresion matematica
Realizar el calculo de la siguiente expresion y=x^2/2
Autor:
Erick Sebastian Mora Lara
"""
def ingresoDatos():
    """
    Es un procedimiento que solicita el ingreso de datos por teclado,
    se combina con la funcion validarNumeros(), para validar unicamente
    el ingreso de datos numericos positivos y negativos
    ------------
        No Recibe parametros de entrada
    
    Retorna:
    ------------
        Retorna una variable con un valor numerico ingresado por teclado
    """
    print("***VAMOS A CALCULAR EL VALOR DE Y EN LA SIGUIENTE EXPRESION: y=x^2/2 ***")
    print("Para lo cual necesitas Ingresar un valor en X: ")
    xValor=validarNumeros()
    return xValor
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

def calculoMat():
    """
    Es un procedimiento que realiza el calculo de la expresion matematica
    calcula el valor de Y, a partir de un valor X ingresado
    ------------
        No Recibe parametros de entrada
    ------------
    Retorna:
    ------------
        No retorna Ningun Valor
    """
    xValor = ingresoDatos()
    yResultado = ((xValor**2)/2)
    print("x= ",xValor)
    print("y= ",yResultado)


if __name__ == '__main__':
    calculoMat()
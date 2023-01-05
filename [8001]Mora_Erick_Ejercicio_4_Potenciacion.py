"""
Ejercicio 4 
Hallar la potencia n de un numero X ingresado

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
            return num
        except ValueError:
            print("Solo se aceptan Reales")
            
def ingresarDatos(): 
	print("Ingrese el numero base para calcular su potencia: ")
	numBase = validarNumeros()
	print("Ingrese el numero al que desea elevar su base: ")
	numExponente = validarNumeros()
    #Llamado a la operacion para calcular potencia 
	calcularPotencia(numBase, numExponente)
	
	
def calcularPotencia(numBase, numExponente):
	resPotencia = numBase**numExponente
	print("El resultado de ", numBase, " elevado a la ", numExponente, " potencia es: ",round(resPotencia,3))

if __name__ == '__main__':
    ingresarDatos() 
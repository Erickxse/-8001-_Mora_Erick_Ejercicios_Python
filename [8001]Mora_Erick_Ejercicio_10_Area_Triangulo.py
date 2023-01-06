"""
Descripción:
Ejercicio 10.
Ingresar la base y la altura de un triángulo y hallar su área. 
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
    print("Vamos a calcular el Area del Triangulo. Necesitamos el valor de su Base y su Altura: ")
    print("Ingrese el valor de la Base del Triangulo: ")
    baseTr = validarNumeros()
    print("Ingrese el valor de la Altura del Triangulo: ")
    alturaTr = validarNumeros()
    datos = [baseTr, alturaTr]
    return datos

def calcularArea():
    datos = ingresarDatos()
    baseTr = datos[0]
    alturaTr = datos[1]

    areaTr = (baseTr*alturaTr)/2

    print("El area del triangulo es: ",round(areaTr,2))

if __name__ == '__main__':
    calcularArea()
